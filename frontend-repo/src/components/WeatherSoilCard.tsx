import React, { useState } from 'react';
import { 
  CloudRain, 
  Sun, 
  Wind, 
  Droplets, 
  AlertTriangle, 
  MapPin, 
  Clock, 
  Activity,
  Layers,
  Thermometer,
  RefreshCw,
  Search,
  AlertCircle,
  Smartphone
} from 'lucide-react';
import type { WeatherInfo, UserProfile } from '../types';
import { useAppTranslation } from '../i18n';

interface WeatherSoilCardProps {
  weather: WeatherInfo;
  user?: UserProfile;
  isLoading?: boolean;
  isGpsDenied?: boolean;
  onRefreshLocation?: () => void;
  onManualCitySubmit?: (city: string) => void;
  onNavigateToSmsDemo?: () => void;
}

export const WeatherSoilCard: React.FC<WeatherSoilCardProps> = ({
  weather,
  user,
  isLoading = false,
  isGpsDenied = false,
  onRefreshLocation,
  onManualCitySubmit,
  onNavigateToSmsDemo,
}) => {
  const { t } = useAppTranslation();
  const [manualInput, setManualInput] = useState('');

  const getLocalizedRisk = (level?: string) => {
    const norm = (level || '').toLowerCase();
    if (norm.includes('low')) return t('risk.low', 'Low Risk');
    if (norm.includes('mod') || norm.includes('med')) return t('risk.moderate', 'Moderate Risk');
    if (norm.includes('high')) return t('risk.high', 'High Risk');
    if (norm.includes('sev') || norm.includes('crit')) return t('risk.severe', 'Severe Risk');
    return `${level || ''} ${t('header.riskSuffix', 'Risk')}`.trim();
  };

  const handleManualSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (manualInput.trim() && onManualCitySubmit) {
      onManualCitySubmit(manualInput.trim());
    }
  };

  return (
    <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-6 shadow-xl border border-agri-200/80 relative">
      
      {/* Header & Location Selector */}
      <div className="flex items-center justify-between gap-2 pb-4 border-b border-slate-100">
        <div className="flex items-center gap-2">
          <div className="p-2 rounded-xl bg-blue-100 text-blue-800">
            <Thermometer className="w-4 h-4 text-blue-700" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm sm:text-base font-extrabold text-slate-900">
                {t('fieldData.weatherHeading')}
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-black bg-emerald-100 text-emerald-800 border border-emerald-300">
                {t('fieldData.liveApi', 'Live API')}
              </span>
            </div>
            <p className="text-[11px] text-slate-500 font-medium">
              {t('fieldData.liveTelemetryDesc', 'Live GPS Field Telemetry & OpenWeatherMap Forecast')}
            </p>
          </div>
        </div>

        {/* GPS Location Indicator & Refresh Button */}
        <div className="flex items-center gap-2">
          {onRefreshLocation && (
            <button
              onClick={onRefreshLocation}
              disabled={isLoading}
              title="Refresh Live GPS Location"
              className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition-colors disabled:opacity-50 flex items-center gap-1 text-xs font-bold"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${isLoading ? 'animate-spin text-agri-600' : 'text-slate-600'}`} />
              <span className="hidden sm:inline">{t('common.retry')}</span>
            </button>
          )}

          <div className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-extrabold ${
            isGpsDenied 
              ? 'bg-amber-50 border-amber-200 text-amber-900'
              : 'bg-emerald-50 border-emerald-200 text-emerald-900'
          }`}>
            <MapPin className={`w-3.5 h-3.5 ${isGpsDenied ? 'text-amber-600' : 'text-emerald-600 animate-bounce'}`} />
            <span>{isGpsDenied ? t('fieldData.gpsDeniedManual', 'GPS Denied (Manual)') : `📍 ${t('fieldData.gpsActive', 'Live GPS Active')}`}</span>
          </div>
        </div>
      </div>

      {/* Conditional Manual City Search Form if GPS Permission is Denied */}
      {isGpsDenied && (
        <form onSubmit={handleManualSubmit} className="mt-3 p-3 rounded-2xl bg-amber-50/80 border border-amber-200/80">
          <div className="flex items-center gap-1.5 text-xs font-bold text-amber-900 mb-2">
            <AlertCircle className="w-3.5 h-3.5 text-amber-600" />
            <span>{t('fieldData.locationBlockedPrompt', 'Location tracking is blocked. Enter your city or village manually:')}</span>
          </div>
          <div className="flex gap-2">
            <input
              type="text"
              value={manualInput}
              onChange={(e) => setManualInput(e.target.value)}
              placeholder={t('fieldData.locationSearchPlaceholder', 'e.g. Nagpur, Amravati, Akola, Wardha...')}
              className="flex-1 px-3 py-1.5 text-xs rounded-xl border border-amber-300 bg-white focus:outline-none focus:ring-1 focus:ring-amber-500 font-medium"
            />
            <button
              type="submit"
              className="px-3 py-1.5 rounded-xl bg-amber-700 text-white text-xs font-bold hover:bg-amber-800 transition-colors flex items-center gap-1 shrink-0"
            >
              <Search className="w-3.5 h-3.5" />
              <span>{t('fieldData.search', 'Search')}</span>
            </button>
          </div>
        </form>
      )}

      {/* Main Weather Overview */}
      <div className="mt-4">
        {isLoading ? (
          <div className="py-8 flex flex-col items-center justify-center gap-2">
            <RefreshCw className="w-6 h-6 text-agri-600 animate-spin" />
            <p className="text-xs text-slate-500 font-semibold">{t('common.loading')}</p>
          </div>
        ) : (
          <div>
            <div className="flex items-center justify-between">
              <div>
                <div className="text-3xl font-black text-slate-900 tracking-tight">
                  {weather.tempC}°C
                </div>
                <p className="text-xs font-bold text-agri-900 mt-0.5">
                  {weather.condition}
                </p>
                <p className="text-[11px] text-slate-600">
                  {weather.city.toLowerCase().includes('fetching')
                    ? t('header.fetchingLocation')
                    : `${weather.city}${weather.state ? `, ${weather.state}` : ''}`}
                </p>
              </div>

              <div className="text-right">
                <span className={`inline-block px-2.5 py-1 rounded-full text-xs font-extrabold ${
                  weather.fungalRiskLevel === 'High' || weather.fungalRiskLevel === 'Severe'
                    ? 'bg-rose-100 text-rose-800 border border-rose-300 animate-pulse'
                    : 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                }`}>
                  {getLocalizedRisk(weather.fungalRiskLevel)}
                </span>
                <p className="text-[11px] text-slate-500 mt-1.5 flex items-center justify-end gap-1 font-medium">
                  <Clock className="w-3 h-3 text-slate-400" />
                  {weather.leafWetnessHours}h {t('fieldData.leafWetness', 'Leaf Wetness')}
                </p>
              </div>
            </div>

            {/* 4-Grid Micro-Climate & Soil Metrics */}
            <div className="grid grid-cols-2 gap-2.5 mt-3.5">
              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200/80">
                <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-500">
                  <Droplets className="w-3.5 h-3.5 text-blue-500" />
                  <span>{t('fieldData.humidity')}</span>
                </div>
                <div className="text-base font-extrabold text-slate-900 mt-1">
                  {weather.humidity}%
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200/80">
                <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-500">
                  <CloudRain className="w-3.5 h-3.5 text-blue-600" />
                  <span>{t('fieldData.rainfallChance')}</span>
                </div>
                <div className="text-base font-extrabold text-slate-900 mt-1">
                  {weather.rainfallChance}%
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200/80">
                <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-500">
                  <Wind className="w-3.5 h-3.5 text-slate-600" />
                  <span>{t('fieldData.wind')}</span>
                </div>
                <div className="text-base font-extrabold text-slate-900 mt-1">
                  {weather.windSpeedKmH} km/h
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200/80">
                <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-500">
                  <Activity className="w-3.5 h-3.5 text-agri-600" />
                  <span>{t('fieldData.soilMoisture')}</span>
                </div>
                <div className="text-xs font-extrabold text-agri-950 mt-1 truncate">
                  {weather.soilMoisture}
                </div>
              </div>
            </div>

            {/* Local Soil Behavior Advisory */}
            <div className="mt-3.5 p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs text-amber-950 flex items-start gap-2">
              <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
              <p className="font-medium leading-relaxed">
                {weather.alertSummary}
              </p>
            </div>
          </div>
        )}
      </div>

          {/* 5-Day Disease & Rain Forecast Breakdown */}
          {weather.forecast && weather.forecast.length > 0 && (
            <div className="mt-4 pt-3 border-t border-slate-100">
              <h4 className="text-xs font-extrabold text-slate-900 mb-2 flex items-center justify-between">
                <span>{t('fieldData.fiveDayForecast', '5-Day Disease Outbreak & Rainfall Forecast')}</span>
                <span className="text-[10px] text-slate-600 font-normal">{t('common.updatedLive', 'Updated Live')}</span>
              </h4>
              <div className="space-y-1.5">
                {weather.forecast.map((item, idx) => (
                  <div key={idx} className="flex items-center justify-between p-2 rounded-xl bg-slate-50 border border-slate-100 text-xs">
                    <div className="flex items-center gap-2">
                      <span className="font-bold text-slate-700 w-20">{item.date}</span>
                      <span className="text-slate-600 font-medium">{item.temp_min}° - {item.temp_max}°C</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-slate-600 text-[11px]">{item.humidity}% {t('fieldData.humidity', 'Humidity')}</span>
                      <span className={`px-2 py-0.5 rounded-md text-[10px] font-black ${
                        item.disease_risk === 'High'
                          ? 'bg-rose-100 text-rose-800'
                          : item.disease_risk === 'Medium'
                          ? 'bg-amber-100 text-amber-800'
                          : 'bg-emerald-100 text-emerald-800'
                      }`}>
                        {getLocalizedRisk(item.disease_risk)}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Live Fast2SMS Dispatcher Test */}
          <div className="mt-4 pt-3 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div className="text-left w-full sm:w-auto">
              <span className="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
                <Smartphone className="w-3.5 h-3.5 text-agri-700" />
                <span>{t('fieldData.smsAdvisoryTitle', 'Fast2SMS Live Weather & Irrigation Advisory')}</span>
              </span>
              <span className="text-[11px] text-slate-500 font-medium">
                {t('fieldData.smsAdvisoryDesc', 'Sends live temperature, humidity, rain status & irrigation time to')} {user?.phone || t('fieldData.registeredPhone', 'registered phone')}
              </span>
            </div>
            <button
              type="button"
              onClick={onNavigateToSmsDemo}
              className="w-full sm:w-auto px-4 py-2 rounded-xl bg-agri-800 hover:bg-agri-900 text-white text-xs font-bold shadow-md shadow-agri-950/20 transition-all flex items-center justify-center gap-1.5 shrink-0 cursor-pointer"
            >
              <Smartphone className="w-3.5 h-3.5 text-citrus-300" />
              <span>{t('fieldData.sendSmsToPhone', 'Send Live SMS to Phone')}</span>
            </button>
          </div>
        </div>
  );
};
