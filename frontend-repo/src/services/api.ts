// API service for backend integration using native fetch
import { Capacitor } from '@capacitor/core';
import type { UserProfile, PredictiveRiskRequest, PredictiveRiskResponse } from '../types';
import { getCurrentLanguage } from '../i18n';

/**
 * Dynamically resolves the active API base endpoint:
 * 1. Runtime override via localStorage ('api_endpoint_override')
 * 2. Environment variable VITE_API_BASE_URL (with auto-adjustment for native platforms)
 * 3. Native mobile fallback: LAN IP (192.168.1.6:8000/api/v1) or Android Emulator (10.0.2.2:8000/api/v1)
 * 4. Browser web default: 127.0.0.1:8000/api/v1
 */
export function getApiBaseUrl(): string {
  if (typeof window !== 'undefined') {
    const runtimeOverride = localStorage.getItem('api_endpoint_override');
    if (runtimeOverride && runtimeOverride.trim()) {
      return runtimeOverride.trim().replace(/\/+$/, '');
    }
  }

  const envUrl = (import.meta.env.VITE_API_BASE_URL || '').trim();
  if (envUrl) {
    return envUrl.replace(/\/+$/, '');
  }

  // Both browser and Android with ADB reverse connect to 127.0.0.1:8000/api/v1
  return 'http://127.0.0.1:8000/api/v1';
}

export function setCustomApiEndpoint(url: string): void {
  if (typeof window !== 'undefined') {
    if (!url || !url.trim()) {
      localStorage.removeItem('api_endpoint_override');
    } else {
      localStorage.setItem('api_endpoint_override', url.trim().replace(/\/+$/, ''));
    }
  }
}

export const API_BASE_URL = getApiBaseUrl();

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: UserProfile;
}

export interface RegisterPayload {
  full_name: string;
  email: string;
  phone?: string;
  password: string;
  confirm_password: string;
  crop_type?: string;
  location?: string;
  latitude?: number;
  longitude?: number;
  role?: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

async function request<T = any>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const token = localStorage.getItem('access_token');
  const currentLang = getCurrentLanguage();
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    'X-Language': currentLang,
    'Accept-Language': currentLang,
    ...((options.headers as Record<string, string>) || {}),
  };
  
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  const primaryBaseUrl = getApiBaseUrl();
  const isNative = typeof window !== 'undefined' && Capacitor.isNativePlatform();

  // Candidates list for resilient mobile connections (primary, ADB reverse 127.0.0.1, emulator 10.0.2.2, physical LAN 192.168.1.5)
  const candidateUrls = [
    primaryBaseUrl,
    ...(isNative 
      ? ['http://127.0.0.1:8000/api/v1', 'http://10.200.4.112:8000/api/v1', 'http://10.0.2.2:8000/api/v1', 'http://192.168.1.5:8000/api/v1', 'http://192.168.1.6:8000/api/v1'] 
      : ['http://127.0.0.1:8000/api/v1', 'http://10.200.4.112:8000/api/v1', 'http://10.0.2.2:8000/api/v1', 'http://192.168.1.5:8000/api/v1', 'http://192.168.1.6:8000/api/v1'])
  ].filter((url, index, self) => self.indexOf(url) === index);

  let lastError: any = null;

  for (const candidateBase of candidateUrls) {
    try {
      const controller = new AbortController();
      const timeoutMs = isNative ? 3500 : 6000;
      const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

      const response = await fetch(`${candidateBase}${cleanEndpoint}`, {
        ...options,
        headers,
        signal: controller.signal,
      });
      clearTimeout(timeoutId);

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        const error: any = new Error(data?.detail || `HTTP Error ${response.status}`);
        error.response = { status: response.status, data };
        throw error;
      }

      // If a candidate succeeded and it was different from primary, remember it
      if (candidateBase !== primaryBaseUrl) {
        setCustomApiEndpoint(candidateBase);
      }

      return data as T;
    } catch (err: any) {
      // If it's a valid HTTP response with error status (e.g. 400 Bad Request, 401 Unauthorized), don't fallback to other servers
      if (err?.response?.status) {
        throw err;
      }
      lastError = err;
      // Network/connection error -> try next candidate in loop
    }
  }

  const customError: any = new Error(
    `Unable to connect to backend server (${primaryBaseUrl}). Tap 'Server IP' in the top header to configure or check network connection.`
  );
  customError.original = lastError;
  throw customError;
}

// Auth APIs
export const authAPI = {
  register: async (data: RegisterPayload): Promise<AuthResponse> => {
    const resData = await request<AuthResponse>('/auth/register', {
      method: 'POST',
      body: JSON.stringify(data),
    });
    if (resData?.access_token) {
      localStorage.setItem('access_token', resData.access_token);
    }
    return resData;
  },
  login: async (data: LoginPayload): Promise<AuthResponse> => {
    const resData = await request<AuthResponse>('/auth/login', {
      method: 'POST',
      body: JSON.stringify(data),
    });
    if (resData?.access_token) {
      localStorage.setItem('access_token', resData.access_token);
    }
    return resData;
  },
  getMe: async (): Promise<UserProfile> => {
    return request<UserProfile>('/auth/me');
  }
};

// Disease Detection APIs
export const diseaseAPI = {
  predict: async (file: File, lang?: string) => {
    // Guard: reject static sample/placeholder images — only allow real uploaded files
    if (file.name === 'sample_leaf.jpg' || file.size < 2048) {
      throw new Error('Please upload a real photo of a crop leaf, not a sample image.');
    }

    const currentLang = lang || getCurrentLanguage();
    const token = localStorage.getItem('access_token');
    const formData = new FormData();
    formData.append('file', file);
    formData.append('language', currentLang);
    const headers: Record<string, string> = {
      'X-Language': currentLang,
      'Accept-Language': currentLang,
    };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    const bases = [
      getApiBaseUrl(),
      'http://127.0.0.1:8000/api/v1',
      'http://localhost:8000/api/v1',
      'http://10.200.4.112:8000/api/v1',
      'http://10.0.2.2:8000/api/v1',
    ].filter((url, index, self) => self.indexOf(url) === index);

    const candidateUrls: string[] = [];
    for (const b of bases) {
      const root = b.replace(/\/api(\/v1)?$/, '');
      candidateUrls.push(
        `${b}/disease/predict?language=${encodeURIComponent(currentLang)}`,
        `${b}/predict?language=${encodeURIComponent(currentLang)}`,
        `${root}/disease/predict?language=${encodeURIComponent(currentLang)}`,
        `${root}/predict?language=${encodeURIComponent(currentLang)}`
      );
    }

    let lastNetworkError: unknown = null;

    for (const targetUrl of candidateUrls) {
      const controller = new AbortController();
      // 30-second timeout — model inference can be slow on cold start
      const timeoutId = setTimeout(() => controller.abort(), 30000);

      try {
        const res = await fetch(targetUrl, {
          method: 'POST',
          headers,
          body: formData,
          signal: controller.signal,
        });
        clearTimeout(timeoutId);

        // Do NOT fall through to next candidate on HTTP errors (4xx/5xx)
        // — these are real errors from the server, not connectivity issues
        if (!res.ok) {
          const errData = await res.json().catch(() => null);
          const errMsg = errData?.detail || `Server error ${res.status}`;
          throw new Error(errMsg);
        }

        return await res.json();
      } catch (err: unknown) {
        clearTimeout(timeoutId);

        // If it's an HTTP error (we threw it above), propagate immediately
        if (err instanceof Error && !isNetworkError(err)) {
          throw err;
        }

        // Network/timeout/CORS error → try next candidate
        console.warn(`Fetch to ${targetUrl} failed (network):`, err);
        lastNetworkError = err;
      }
    }

    throw new Error(
      `Unable to connect to AI model server. Please ensure the backend is running at ${getApiBaseUrl()}. ` +
      (lastNetworkError instanceof Error ? lastNetworkError.message : String(lastNetworkError))
    );
  },
  getProgressionRisk: (diseaseName: string, confidence: number, language?: string, location?: string) =>
    request('/disease/progression-risk', {
      method: 'POST',
      body: JSON.stringify({
        disease_name: diseaseName,
        confidence,
        language: language || getCurrentLanguage(),
        location: location || '',
      }),
    }),
  history: () => request('/disease/history'),
};

/** Returns true if the error is a network/connectivity issue (not an HTTP-level error) */
function isNetworkError(err: Error): boolean {
  return (
    err.name === 'AbortError' ||
    err.name === 'TypeError' ||
    err.message.includes('Failed to fetch') ||
    err.message.includes('Network request failed') ||
    err.message.includes('abort')
  );
}

// AI Model Status API
export const modelAPI = {
  /** Checks if the backend is reachable and if the AI model is loaded */
  getStatus: async (): Promise<{ model_loaded: boolean; model_id: string; status: string; api_reachable: boolean }> => {
    const bases = [
      getApiBaseUrl(),
      'http://127.0.0.1:8000/api/v1',
      'http://localhost:8000/api/v1',
      'http://10.200.4.112:8000/api/v1',
      'http://10.0.2.2:8000/api/v1',
    ].filter((url, index, self) => self.indexOf(url) === index);

    const candidates: string[] = [];
    for (const b of bases) {
      const root = b.replace(/\/api(\/v1)?$/, '');
      candidates.push(`${b}/model/status`, `${root}/model/status`, `${b}/health`, `${root}/health`);
    }

    for (const url of candidates) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 5000);
        const res = await fetch(url, { signal: controller.signal });
        clearTimeout(timeoutId);
        if (res.ok) {
          const data = await res.json();
          return {
            model_loaded: data.model_loaded ?? false,
            model_id: data.model_id ?? 'unknown',
            status: data.status ?? (data.model_loaded ? 'ready' : 'loading'),
            api_reachable: true,
          };
        }
      } catch {
        // try next
      }
    }

    return { model_loaded: false, model_id: 'unreachable', status: 'offline', api_reachable: false };
  },
};

// Crop Recommendation API
export const cropAPI = {
  getRecommendations: (location: string, lang?: string) => {
    const currentLang = lang || getCurrentLanguage();
    return request(`/crop-recommendations?location=${encodeURIComponent(location)}&language=${encodeURIComponent(currentLang)}`);
  },
};

// Sensor APIs
export const sensorAPI = {
  addReading: (data: any) => request('/sensors/reading', { method: 'POST', body: JSON.stringify(data) }),
  getLatest: () => request('/sensors/latest'),
  getLive: () => request('/sensors/live'),
};

// Weather APIs
export const weatherAPI = {
  getWeatherByCoords: (lat: number, lon: number, lang?: string) =>
    request(`/weather?lat=${lat}&lon=${lon}&language=${encodeURIComponent(lang || getCurrentLanguage())}`),
  getWeatherByCity: (city: string, lang?: string) =>
    request(`/weather?city=${encodeURIComponent(city)}&language=${encodeURIComponent(lang || getCurrentLanguage())}`),
  getForecast: (city?: string, lat?: number, lon?: number, lang?: string) =>
    request(`/weather/forecast?${lat && lon ? `lat=${lat}&lon=${lon}` : `city=${encodeURIComponent(city || 'Nagpur')}`}&language=${encodeURIComponent(lang || getCurrentLanguage())}`),
  getCurrent: (city?: string, lat?: number, lon?: number, lang?: string) =>
    request(`/weather/current?${lat && lon ? `lat=${lat}&lon=${lon}` : `city=${encodeURIComponent(city || 'Nagpur')}`}&language=${encodeURIComponent(lang || getCurrentLanguage())}`),
};

// Alert APIs
export const alertsAPI = {
  subscribe: (data: { phone: string; crop?: string; alert_types?: string[] }) =>
    request('/alerts/subscribe', { method: 'POST', body: JSON.stringify(data) }),
  sendWeatherAlert: (phone: string, alertMessage: string) =>
    request('/alerts/send-weather-alert', { method: 'POST', body: JSON.stringify({ phone, alert_message: alertMessage }) }),
  sendTestSms: (data: { uid?: string; phone?: string; location?: string; name?: string }) =>
    request('/alerts/send-test-sms', { method: 'POST', body: JSON.stringify(data) }),
};

// Risk APIs
export const riskAPI = {
  earlyWarning: () => request('/risk/early-warning'),
};

// Feedback APIs
export const feedbackAPI = {
  submit: (data: any) => request('/feedback/submit', { method: 'POST', body: JSON.stringify(data) }),
  impact: () => request('/feedback/impact'),
};

// Marketplace & Mandi Price APIs
export const marketplaceAPI = {
  getMandiPrices: (crop: string, state: string, lang?: string) =>
    request('/mandi-prices', {
      method: 'POST',
      body: JSON.stringify({ crop, state, language: lang || getCurrentLanguage() }),
    }),
  getPriceForecast: (crop: string, state: string, lang?: string) =>
    request('/price-forecast', {
      method: 'POST',
      body: JSON.stringify({ crop, state, language: lang || getCurrentLanguage() }),
    }),
  getCropAlert: (crop: string, lang?: string) =>
    request(`/crop-alert?crop=${encodeURIComponent(crop)}&language=${encodeURIComponent(lang || getCurrentLanguage())}`),
};

// Predictive Intelligence APIs
export const predictiveAPI = {
  getOutbreakRisk: (data: PredictiveRiskRequest) =>
    request<PredictiveRiskResponse>('/predictive/outbreak-risk', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
};

export default { request };

