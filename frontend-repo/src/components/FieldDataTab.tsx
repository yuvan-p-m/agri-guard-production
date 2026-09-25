import React, { useEffect, useState, useCallback } from 'react';
import {
  Cpu,
  Wifi,
  RefreshCw,
  Thermometer,
  Droplets,
  CloudRain,
  Activity,
  AlertTriangle,
  CheckCircle2,
  AlertCircle,
  Radio,
  Power,
  Zap,
  Info,
  Brain,
  ShieldCheck,
  Calendar,
  Users,
  ShieldAlert,
  ArrowRight,
  TrendingUp,
  Sparkles,
  Layers,
} from 'lucide-react';
import type {
  HardwareState,
  UserProfile,
  WeatherInfo,
  PredictiveRiskResponse,
  PredictiveSensorData,
} from '../types';
import {
  subscribeToLiveSensors,
  fetchSensorSnapshotOnce,
  type InterpretedSensorSnapshot,
  type SensorStatus,
} from '../services/sensorService';
import {
  getLocalizedSensorExplanation,
  getLocalizedUIText,
  getLocalizedRainDisplay,
  getLocalizedPumpState,
} from '../services/sensorTranslations';
import { predictiveAPI } from '../services/api';
import { useAppTranslation } from '../i18n';

export interface FieldDataTabProps {
  onNavigateToDiagnosis?: () => void;
  hardwareState: HardwareState;
  onPairHardware: () => void;
  user?: UserProfile;
  weather?: WeatherInfo;
}

export const FieldDataTab: React.FC<FieldDataTabProps> = ({
  onNavigateToDiagnosis,
  hardwareState,
  onPairHardware,
  user,
  weather,
}) => {
  const { t, language } = useAppTranslation();
  const [snapshot, setSnapshot] = useState<InterpretedSensorSnapshot | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [isRefreshing, setIsRefreshing] = useState<boolean>(false);
  const [lastSyncTime, setLastSyncTime] = useState<string>('Connecting...');

  // Predictive Intelligence State
  const [predictiveResult, setPredictiveResult] = useState<PredictiveRiskResponse | null>(null);
  const [isPredicting, setIsPredicting] = useState<boolean>(false);
  const [predictiveError, setPredictiveError] = useState<string | null>(null);
  const [hasRunInitialPrediction, setHasRunInitialPrediction] = useState<boolean>(false);

  // Live listener to Firebase Realtime Database (`sensors` path)
  useEffect(() => {
    setIsLoading(true);
    const unsubscribe = subscribeToLiveSensors((data) => {
      setSnapshot(data);
      setIsLoading(false);
      setIsRefreshing(false);
      setLastSyncTime(
        new Date().toLocaleTimeString('en-IN', {
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit',
        })
      );
    });

    return () => {
      unsubscribe();
    };
  }, []);

  const handleManualRefresh = async () => {
    setIsRefreshing(true);
    try {
      const data = await fetchSensorSnapshotOnce();
      setSnapshot(data);
      setLastSyncTime(
        new Date().toLocaleTimeString('en-IN', {
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit',
        })
      );
    } catch (e) {
      console.error('Manual refresh failed:', e);
    } finally {
      setIsRefreshing(false);
    }
  };

  // Run Predictive Outbreak Risk Analysis
  const runPredictiveAnalysis = useCallback(
    async (currentSnapshot?: InterpretedSensorSnapshot | null) => {
      setIsPredicting(true);
      setPredictiveError(null);

      try {
        const readings = (currentSnapshot || snapshot)?.readings || {};
        
        // Extract raw sensor numbers safely from live state
        const parseNum = (val: any, fallback: number) => {
          if (typeof val === 'number' && !isNaN(val) && val > 0) return val;
          const parsed = parseFloat(String(val));
          return !isNaN(parsed) && parsed > 0 ? parsed : fallback;
        };

        const sensorPayload: PredictiveSensorData = {
          N: parseNum(readings.nitrogen?.value, 120),
          P: parseNum(readings.phosphorous?.value, 55),
          K: parseNum(readings.potassium?.value, 175),
          moisture: parseNum(readings.moisture?.value, 52),
          temperature: parseNum(readings.temperature?.value, weather?.tempC || 27),
          humidity: parseNum(readings.humidity?.value, weather?.humidity || 65),
          pH: parseNum(readings.ph?.value, 6.8),
        };

        const response = await predictiveAPI.getOutbreakRisk({
          farmer_id: user?.id || '1',
          lat: user?.latitude || 21.1458,
          lon: user?.longitude || 79.0882,
          crop: user?.primaryCrop || 'Tomato',
          sensor_data: sensorPayload,
        });

        if (response) {
          setPredictiveResult(response);
        }
      } catch (err: any) {
        console.error('Failed to run predictive intelligence:', err);
        setPredictiveError(
          err?.message || 'Unable to connect to predictive intelligence service.'
        );
      } finally {
        setIsPredicting(false);
      }
    },
    [snapshot, user, weather]
  );

  // Auto-run once on component mount / when sensor data is ready
  useEffect(() => {
    if (!hasRunInitialPrediction && (snapshot?.available || !isLoading)) {
      setHasRunInitialPrediction(true);
      runPredictiveAnalysis(snapshot);
    }
  }, [snapshot, isLoading, hasRunInitialPrediction, runPredictiveAnalysis]);

  const getStatusBadge = (status: SensorStatus) => {
    switch (status) {
      case 'Optimal':
        return (
          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-100 text-emerald-800 border border-emerald-300 flex items-center gap-1">
            <CheckCircle2 className="w-3 h-3 text-emerald-600" />
            <span>{t('common.optimal')}</span>
          </span>
        );
      case 'Low':
        return (
          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-amber-100 text-amber-900 border border-amber-300 flex items-center gap-1">
            <AlertCircle className="w-3 h-3 text-amber-600" />
            <span>{t('common.low')}</span>
          </span>
        );
      case 'High':
        return (
          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-orange-100 text-orange-900 border border-orange-300 flex items-center gap-1">
            <AlertTriangle className="w-3 h-3 text-orange-600" />
            <span>{t('common.high')}</span>
          </span>
        );
      case 'Critical':
        return (
          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-100 text-rose-900 border border-rose-300 flex items-center gap-1 animate-pulse">
            <AlertTriangle className="w-3 h-3 text-rose-600" />
            <span>{t('common.severe')}</span>
          </span>
        );
      case 'No reading':
      default:
        return (
          <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-slate-100 text-slate-700 border border-slate-300 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-slate-400" />
            <span>{t('common.noData')}</span>
          </span>
        );
    }
  };

  const getRiskScoreColor = (score: number) => {
    if (score <= 30) {
      return {
        bg: 'bg-emerald-500',
        lightBg: 'bg-emerald-50 dark:bg-emerald-950/40',
        text: 'text-emerald-900 dark:text-emerald-100',
        badgeBg: 'bg-emerald-100 text-emerald-800 border-emerald-300',
        border: 'border-emerald-300 dark:border-emerald-700/60',
        ring: 'ring-emerald-500/20',
        label: 'LOW RISK',
      };
    }
    if (score <= 60) {
      return {
        bg: 'bg-amber-500',
        lightBg: 'bg-amber-50 dark:bg-amber-950/40',
        text: 'text-amber-900 dark:text-amber-100',
        badgeBg: 'bg-amber-100 text-amber-900 border-amber-300',
        border: 'border-amber-300 dark:border-amber-700/60',
        ring: 'ring-amber-500/20',
        label: 'MEDIUM RISK',
      };
    }
    return {
      bg: 'bg-rose-500',
      lightBg: 'bg-rose-50 dark:bg-rose-950/40',
      text: 'text-rose-900 dark:text-rose-100',
      badgeBg: 'bg-rose-100 text-rose-900 border-rose-300 animate-pulse',
      border: 'border-rose-300 dark:border-rose-700/60',
      ring: 'ring-rose-500/20',
      label: score > 80 ? 'CRITICAL RISK' : 'HIGH RISK',
    };
  };

  const readings = snapshot?.readings || {};

  return (
    <div className="space-y-6 max-w-6xl mx-auto animate-fade-in">
      {/* 3 or more zero/no-reading warning banner */}
      {snapshot?.hardwareWarning && (
        <div className="rounded-2xl border-2 border-amber-400 bg-amber-50 p-4 sm:p-5 shadow-lg flex items-start gap-3.5">
          <AlertTriangle className="w-6 h-6 text-amber-600 shrink-0 mt-0.5 animate-bounce" />
          <div className="space-y-1">
            <h4 className="text-sm font-black text-amber-900 tracking-tight">
              {getLocalizedUIText('hardwareAlert', language)}
            </h4>
            <p className="text-xs sm:text-sm text-amber-800 font-medium leading-relaxed">
              {snapshot.hardwareWarning}
            </p>
          </div>
        </div>
      )}

      {/* Header card with status & stream information */}
      <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-agri-200/80">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span
                className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black border shadow-2xs ${
                  snapshot?.available
                    ? 'bg-emerald-100 text-emerald-900 border-emerald-300'
                    : 'bg-rose-100 text-rose-900 border-rose-300'
                }`}
              >
                <span
                  className={`w-2.5 h-2.5 rounded-full ${
                    snapshot?.available ? 'bg-emerald-500 animate-ping' : 'bg-rose-500'
                  }`}
                />
                <span>
                  {snapshot?.available
                    ? getLocalizedUIText('liveConnected', language)
                    : getLocalizedUIText('liveDisconnected', language)}
                </span>
              </span>
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-bold font-mono border border-slate-200">
                <Radio className="w-3.5 h-3.5 text-blue-600" />
                <span>RS485 7-in-1 Modbus</span>
              </span>
            </div>

            <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
              {t('fieldData.soilHeading')}
            </h2>
            <p className="text-xs sm:text-sm text-agri-900 font-semibold mt-1.5 max-w-2xl leading-relaxed bg-agri-50/80 p-2.5 rounded-xl border border-agri-200/60">
              🌱{' '}
              {t(
                'iot.quote',
                'Leverages historical sensor data to recommend suitable crops and deliver timely farming insights'
              )}
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2.5 self-start md:self-auto">
            {!hardwareState.isConnected && (
              <button
                type="button"
                onClick={onPairHardware}
                className="px-4 py-2 rounded-2xl bg-agri-700 hover:bg-agri-800 text-white text-xs font-black shadow-md shadow-agri-700/25 transition-all flex items-center gap-1.5"
              >
                <Wifi className="w-3.5 h-3.5" />
                <span>
                  {hardwareState.deviceId ||
                    t('modals.hardwarePairTitle', 'Pair Hardware')}
                </span>
              </button>
            )}

            <button
              type="button"
              onClick={handleManualRefresh}
              disabled={isRefreshing}
              className="px-4 py-2 rounded-2xl bg-agri-700 hover:bg-agri-800 text-white text-xs font-black shadow-md shadow-agri-700/25 transition-all flex items-center gap-1.5 active:scale-95 disabled:opacity-75"
            >
              <RefreshCw
                className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin' : ''}`}
              />
              <span>
                {isRefreshing
                  ? t('iot.syncing', 'Syncing...')
                  : t('iot.syncNow', 'Sync Now')}
              </span>
            </button>
          </div>
        </div>

        <div className="mt-5 pt-3.5 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-500 gap-2">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span className="font-semibold text-slate-700">
              Firebase RTDB: /sensors
            </span>
            <span className="text-slate-400">• Last Sync: {lastSyncTime}</span>
          </div>
          <span className="font-mono text-[11px] text-agri-800 bg-agri-50 px-2 py-0.5 rounded-md border border-agri-200 font-bold">
            Live onValue Listener Active
          </span>
        </div>
      </div>

      {/* Loading or Data Unavailable fallback */}
      {isLoading && !snapshot && (
        <div className="bg-white/90 backdrop-blur-md rounded-3xl p-12 text-center shadow-lg border border-slate-200 space-y-3">
          <RefreshCw className="w-8 h-8 text-agri-600 animate-spin mx-auto" />
          <p className="text-sm font-black text-slate-700">
            Connecting to Firebase Realtime Database...
          </p>
          <p className="text-xs text-slate-500">
            Listening for live packets from your ESP32 soil sensor.
          </p>
        </div>
      )}

      {snapshot && !snapshot.available && (
        <div className="bg-white/90 backdrop-blur-md rounded-3xl p-10 text-center shadow-lg border border-rose-200 space-y-3">
          <AlertCircle className="w-10 h-10 text-rose-500 mx-auto" />
          <p className="text-base font-black text-slate-800">
            Sensor Data Unavailable
          </p>
          <p className="text-xs text-slate-500 max-w-md mx-auto">
            Unable to stream live data from Firebase Realtime Database. Please
            verify your internet connection and ESP32 power.
          </p>
          <button
            type="button"
            onClick={handleManualRefresh}
            className="px-5 py-2.5 rounded-2xl bg-agri-700 text-white text-xs font-black shadow-md hover:bg-agri-800 transition-all"
          >
            Retry Connection
          </button>
        </div>
      )}

      {snapshot && snapshot.available && (
        <>
          {/* Micro-climate Sensors Grid (Temperature, Humidity, Soil Moisture, EC) */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {/* 1. Soil pH */}
            {readings.ph && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 flex flex-col justify-between space-y-3 hover:border-agri-400 transition-all">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-purple-100 text-purple-800 flex items-center justify-center font-bold text-xs">
                      pH
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.ph', 'Soil pH')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.phSub', 'Acidity / Alkalinity')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.ph.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-3xl font-black text-slate-900 font-mono">
                    {readings.ph.displayValue}
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('sensor.optimalRange', 'Optimal Range')}: 6.0 – 7.5
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('ph', readings.ph.status, language)}
                </p>
              </div>
            )}

            {/* 2. Air Humidity */}
            {readings.humidity && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 flex flex-col justify-between space-y-3 hover:border-agri-400 transition-all">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-blue-100 text-blue-800 flex items-center justify-center">
                      <Droplets className="w-4 h-4 text-blue-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.humidity', 'Air Humidity')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.humiditySub', 'Ambient Relative Humidity')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.humidity.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-3xl font-black text-slate-900 font-mono">
                    {readings.humidity.displayValue}{' '}
                    <span className="text-sm font-semibold text-slate-500">%</span>
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('sensor.optimalRange', 'Optimal Range')}: 40% – 70%
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('humidity', readings.humidity.status, language)}
                </p>
              </div>
            )}

            {/* 3. Air Temperature */}
            {readings.temperature && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 flex flex-col justify-between space-y-3 hover:border-agri-400 transition-all">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
                      <Thermometer className="w-4 h-4 text-amber-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.temperature', 'Temperature')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.temperatureSub', 'Ambient Canopy Temp')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.temperature.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-3xl font-black text-slate-900 font-mono">
                    {readings.temperature.displayValue}{' '}
                    <span className="text-sm font-semibold text-slate-500">°C</span>
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('sensor.optimalRange', 'Optimal Range')}: 18°C – 30°C
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('temperature', readings.temperature.status, language)}
                </p>
              </div>
            )}

            {/* 4. Soil Moisture */}
            {readings.moisture && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 flex flex-col justify-between space-y-3 hover:border-agri-400 transition-all">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-cyan-100 text-cyan-800 flex items-center justify-center">
                      <Droplets className="w-4 h-4 text-cyan-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.moisture', 'Soil Moisture')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.moistureSub', 'Volumetric Water Content')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.moisture.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-3xl font-black text-slate-900 font-mono">
                    {readings.moisture.displayValue}{' '}
                    <span className="text-sm font-semibold text-slate-500">%</span>
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('sensor.optimalRange', 'Optimal Range')}: 40% – 60%
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('moisture', readings.moisture.status, language)}
                </p>
              </div>
            )}
          </div>

          {/* NPK Macronutrients Section */}
          <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-slate-200/90 space-y-5">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-100">
              <div className="flex items-center gap-2.5">
                <div className="w-10 h-10 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center">
                  <Activity className="w-5 h-5 text-emerald-700" />
                </div>
                <div>
                  <h3 className="text-sm sm:text-base font-black text-slate-900">
                    {t('sensor.npkHeader', 'Soil N-P-K Macronutrients (mg/kg dry soil)')}
                  </h3>
                  <p className="text-xs text-slate-500 font-medium">
                    {getLocalizedUIText('npkSub', language)}
                  </p>
                </div>
              </div>

              <span className="text-xs font-mono font-bold text-agri-900 bg-agri-50 px-3 py-1 rounded-xl border border-agri-200 self-start sm:self-auto">
                {getLocalizedUIText('probeLive', language)}
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {/* Nitrogen (N) */}
              {readings.nitrogen && (
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-black text-slate-800">
                      {t('sensor.nitrogen', 'Nitrogen (N)')}
                    </span>
                    {getStatusBadge(readings.nitrogen.status)}
                  </div>
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {readings.nitrogen.displayValue}{' '}
                    <span className="text-xs text-slate-500 font-normal">mg/kg</span>
                  </div>
                  <p className="text-[11px] text-slate-600 font-medium leading-snug">
                    {getLocalizedSensorExplanation('nitrogen', readings.nitrogen.status, language)}
                  </p>
                  <p className="text-[10px] text-slate-400 font-medium pt-1 border-t border-slate-200">
                    {getLocalizedUIText('standardRange', language)}: 80 – 200 mg/kg
                  </p>
                </div>
              )}

              {/* Phosphorus (P) */}
              {readings.phosphorous && (
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-black text-slate-800">
                      {t('sensor.phosphorous', 'Phosphorus (P)')}
                    </span>
                    {getStatusBadge(readings.phosphorous.status)}
                  </div>
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {readings.phosphorous.displayValue}{' '}
                    <span className="text-xs text-slate-500 font-normal">mg/kg</span>
                  </div>
                  <p className="text-[11px] text-slate-600 font-medium leading-snug">
                    {getLocalizedSensorExplanation('phosphorous', readings.phosphorous.status, language)}
                  </p>
                  <p className="text-[10px] text-slate-400 font-medium pt-1 border-t border-slate-200">
                    {getLocalizedUIText('standardRange', language)}: 40 – 100 mg/kg
                  </p>
                </div>
              )}

              {/* Potassium (K) */}
              {readings.potassium && (
                <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-black text-slate-800">
                      {t('sensor.potassium', 'Potassium (K)')}
                    </span>
                    {getStatusBadge(readings.potassium.status)}
                  </div>
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {readings.potassium.displayValue}{' '}
                    <span className="text-xs text-slate-500 font-normal">mg/kg</span>
                  </div>
                  <p className="text-[11px] text-slate-600 font-medium leading-snug">
                    {getLocalizedSensorExplanation('potassium', readings.potassium.status, language)}
                  </p>
                  <p className="text-[10px] text-slate-400 font-medium pt-1 border-t border-slate-200">
                    {getLocalizedUIText('standardRange', language)}: 100 – 250 mg/kg
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* EC, Rain, and Pump Controls */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Electrical Conductivity (EC) */}
            {readings.ec && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-teal-100 text-teal-800 flex items-center justify-center">
                      <Zap className="w-4 h-4 text-teal-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.ec', 'Conductivity (EC)')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.ecSub', 'Salinity & Total Dissolved Solids')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.ec.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {readings.ec.displayValue}{' '}
                    <span className="text-xs font-semibold text-slate-500">µS/cm</span>
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('sensor.optimalRange', 'Optimal')}: 50 – 200 µS/cm
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('ec', readings.ec.status, language)}
                </p>
              </div>
            )}

            {/* Rain Sensor */}
            {readings.rain && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-cyan-100 text-cyan-800 flex items-center justify-center">
                      <CloudRain className="w-4 h-4 text-cyan-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.rain', 'Rain Sensor')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.rainSub', 'Precipitation Detector')}
                      </p>
                    </div>
                  </div>
                  {getStatusBadge(readings.rain.status)}
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {getLocalizedRainDisplay(
                      readings.rain.displayValue.toLowerCase().includes('rain') &&
                        !readings.rain.displayValue.toLowerCase().includes('no rain'),
                      language
                    )}
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {t('fieldData.liveWeatherSensor', 'Live Weather Sensor')}
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('rain', readings.rain.status, language)}
                </p>
              </div>
            )}

            {/* Pump Status */}
            {readings.pump && (
              <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 shadow-lg border border-slate-200 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-800 flex items-center justify-center">
                      <Power className="w-4 h-4 text-indigo-600" />
                    </div>
                    <div>
                      <h3 className="text-xs font-black uppercase tracking-wider text-slate-700">
                        {t('sensor.pump', 'Irrigation Pump')}
                      </h3>
                      <p className="text-[10px] text-slate-400 font-medium">
                        {t('sensor.pumpSub', 'Relay Switch State')}
                      </p>
                    </div>
                  </div>
                  <span
                    className={`px-2.5 py-0.5 rounded-full text-[10px] font-black border flex items-center gap-1 ${
                      readings.pump.displayValue === 'ON'
                        ? 'bg-emerald-100 text-emerald-800 border-emerald-300'
                        : 'bg-slate-100 text-slate-700 border-slate-300'
                    }`}
                  >
                    <span
                      className={`w-1.5 h-1.5 rounded-full ${
                        readings.pump.displayValue === 'ON'
                          ? 'bg-emerald-500 animate-pulse'
                          : 'bg-slate-400'
                      }`}
                    />
                    <span>{readings.pump.displayValue}</span>
                  </span>
                </div>

                <div className="p-3 bg-slate-50 rounded-2xl border border-slate-200/80">
                  <div className="text-2xl font-black text-slate-900 font-mono">
                    {getLocalizedPumpState(readings.pump.displayValue === 'ON', language)}
                  </div>
                  <span className="text-[10px] text-slate-500 font-medium block mt-0.5">
                    {getLocalizedUIText('relayState', language)}
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 font-medium leading-snug">
                  {getLocalizedSensorExplanation('pump', readings.pump.status, language)}
                </p>
              </div>
            )}
          </div>

          {/* Sensor Status Informational Callout */}
          <div className="flex items-center justify-center pt-2 pb-1">
            <div className="inline-flex items-center justify-center gap-2.5 px-4 py-2.5 rounded-2xl bg-emerald-50 dark:bg-emerald-950/60 border-2 border-emerald-400 dark:border-emerald-600 text-emerald-950 dark:text-emerald-100 shadow-sm max-w-3xl text-center">
              <Info className="w-4 h-4 text-emerald-700 dark:text-emerald-400 shrink-0" />
              <span className="text-xs sm:text-sm font-bold tracking-tight leading-snug">
                {t(
                  'iot.disconnectedNotice',
                  'When hardware is disconnected, displayed data reflects the latest available sensor readings.'
                )}
              </span>
            </div>
          </div>
        </>
      )}

      {/* ========================================================================= */}
      {/* PREDICTIVE INTELLIGENCE SECTION (DISEASE OUTBREAK FORECASTING) */}
      {/* ========================================================================= */}
      <div className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-agri-200/90 space-y-6">
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100">
          <div className="flex items-start sm:items-center gap-3">
            <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-emerald-600 via-teal-600 to-indigo-600 text-white flex items-center justify-center shadow-lg shadow-emerald-700/20 shrink-0">
              <Brain className="w-6 h-6 animate-pulse" />
            </div>
            <div>
              <div className="flex flex-wrap items-center gap-2">
                <h3 className="text-lg sm:text-xl font-black text-slate-900 tracking-tight">
                  {t('predictive.title', 'Predictive Intelligence')}
                </h3>
                <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-indigo-50 text-indigo-800 border border-indigo-200">
                  <Sparkles className="w-3 h-3 text-indigo-600" />
                  <span>AI Outbreak Radar</span>
                </span>
              </div>
              <p className="text-xs sm:text-sm text-slate-500 font-medium mt-0.5">
                {t(
                  'predictive.subtitle',
                  'Early Crop Disease Outbreak Forecasting via Multi-Signal AI Fusion'
                )}
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={() => runPredictiveAnalysis()}
            disabled={isPredicting}
            className="self-start sm:self-auto px-4 py-2.5 rounded-2xl bg-gradient-to-r from-emerald-700 to-teal-800 hover:from-emerald-800 hover:to-teal-900 text-white text-xs font-black shadow-md shadow-emerald-900/20 transition-all flex items-center gap-2 active:scale-95 disabled:opacity-75 cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${isPredicting ? 'animate-spin' : ''}`} />
            <span>
              {isPredicting
                ? t('predictive.running', 'Analyzing Multi-Signal Telemetry...')
                : t('predictive.runPrediction', 'Run Prediction')}
            </span>
          </button>
        </div>

        {/* Error Alert */}
        {predictiveError && (
          <div className="p-4 rounded-2xl bg-rose-50 border border-rose-200 text-rose-900 text-xs font-semibold flex items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0" />
              <span>{predictiveError}</span>
            </div>
            <button
              type="button"
              onClick={() => runPredictiveAnalysis()}
              className="px-3 py-1 rounded-xl bg-rose-200 text-rose-900 font-bold hover:bg-rose-300 transition-colors"
            >
              Retry
            </button>
          </div>
        )}

        {/* Loading Skeleton */}
        {isPredicting && !predictiveResult && (
          <div className="space-y-4 animate-pulse">
            <div className="h-32 bg-slate-100 rounded-3xl" />
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="h-28 bg-slate-100 rounded-2xl" />
              <div className="h-28 bg-slate-100 rounded-2xl" />
              <div className="h-28 bg-slate-100 rounded-2xl" />
              <div className="h-28 bg-slate-100 rounded-2xl" />
            </div>
            <div className="h-40 bg-slate-100 rounded-3xl" />
          </div>
        )}

        {/* Predictive Intelligence Content */}
        {predictiveResult && (
          <div className="space-y-6">
            {/* 1. Overall Outbreak Risk Score Card (0-100%) */}
            {(() => {
              const riskCfg = getRiskScoreColor(predictiveResult.overall_risk_score);
              return (
                <div
                  className={`rounded-3xl p-5 sm:p-6 border-2 shadow-lg transition-all ${riskCfg.lightBg} ${riskCfg.border}`}
                >
                  <div className="flex flex-col md:flex-row md:items-center justify-between gap-5">
                    <div className="space-y-2">
                      <div className="flex items-center gap-2">
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-black border uppercase tracking-wider ${riskCfg.badgeBg}`}
                        >
                          {riskCfg.label}
                        </span>
                        <span className="text-xs font-bold text-slate-500">
                          Primary Crop: <strong className="text-slate-800">{user?.primaryCrop || 'Tomato'}</strong>
                        </span>
                      </div>
                      <h4 className="text-base sm:text-lg font-black text-slate-900">
                        {t('predictive.overallRisk', 'Overall Outbreak Risk Score')}
                      </h4>
                      <p className="text-xs sm:text-sm text-slate-600 font-medium max-w-xl leading-relaxed">
                        Evaluated across{' '}
                        <strong>{predictiveResult.community_threats.report_count} nearby outbreaks</strong>,{' '}
                        current canopy humidity, soil nutrient stress, and seasonal spore germination conditions.
                      </p>
                    </div>

                    <div className="flex items-center gap-4 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md p-4 rounded-2xl border border-slate-200/80 shadow-sm shrink-0">
                      <div className="text-center">
                        <div className="text-4xl font-black font-mono tracking-tight text-slate-900">
                          {predictiveResult.overall_risk_score}
                          <span className="text-lg font-bold text-slate-500">%</span>
                        </div>
                        <span className="text-[10px] font-black uppercase tracking-wider text-slate-500 block">
                          Outbreak Index
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Visual Risk Progress Bar */}
                  <div className="mt-4">
                    <div className="w-full bg-slate-200/80 rounded-full h-3 overflow-hidden p-0.5">
                      <div
                        className={`h-full rounded-full transition-all duration-700 ${riskCfg.bg}`}
                        style={{
                          width: `${Math.max(5, Math.min(100, predictiveResult.overall_risk_score))}%`,
                        }}
                      />
                    </div>
                    <div className="flex justify-between text-[10px] font-bold text-slate-500 mt-1.5 px-0.5">
                      <span>0% (Safe)</span>
                      <span>30% (Low)</span>
                      <span>60% (Moderate)</span>
                      <span>100% (Critical)</span>
                    </div>
                  </div>
                </div>
              );
            })()}

            {/* 2. Four Contributing Signal Cards in a 2x2 Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {/* Card 1: Soil Health Index */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-emerald-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('predictive.soilHealth', 'Soil Health Index')}
                  </span>
                  <Activity className="w-4 h-4 text-emerald-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.soil_health_index}
                  <span className="text-xs font-bold text-slate-500">%</span>
                </div>
                <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
                  <div
                    className="bg-emerald-500 h-full rounded-full"
                    style={{ width: `${predictiveResult.soil_health_index}%` }}
                  />
                </div>
                <p className="text-[11px] text-slate-500 font-medium">
                  {predictiveResult.soil_health_index >= 70
                    ? 'Optimal nutrient balance supports natural disease defense.'
                    : 'Soil stress or deficiency elevates disease susceptibility.'}
                </p>
              </div>

              {/* Card 2: Weather Risk Score */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-blue-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('predictive.weatherRisk', 'Weather Risk Score')}
                  </span>
                  <CloudRain className="w-4 h-4 text-blue-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.weather_risk_score}
                  <span className="text-xs font-bold text-slate-500">%</span>
                </div>
                <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
                  <div
                    className="bg-blue-500 h-full rounded-full"
                    style={{ width: `${predictiveResult.weather_risk_score}%` }}
                  />
                </div>
                <p className="text-[11px] text-slate-500 font-medium">
                  Derived from OpenWeatherMap 5-day humidity & rain forecast.
                </p>
              </div>

              {/* Card 3: Seasonal Risk Level */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-amber-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('predictive.seasonalRisk', 'Seasonal Risk Level')}
                  </span>
                  <Calendar className="w-4 h-4 text-amber-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.seasonal_risk_level}
                </div>
                <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
                  <div
                    className={`h-full rounded-full ${
                      predictiveResult.seasonal_risk_level === 'HIGH'
                        ? 'bg-rose-500 w-full'
                        : predictiveResult.seasonal_risk_level === 'MEDIUM'
                        ? 'bg-amber-500 w-2/3'
                        : 'bg-emerald-500 w-1/3'
                    }`}
                  />
                </div>
                <p className="text-[11px] text-slate-500 font-medium">
                  {predictiveResult.seasonal_risk_level === 'HIGH'
                    ? 'Kharif monsoon period — high fungal spore activity.'
                    : predictiveResult.seasonal_risk_level === 'MEDIUM'
                    ? 'Rabi season — cool temperature mildew window.'
                    : 'Summer dry window — low seasonal baseline.'}
                </p>
              </div>

              {/* Card 4: Community Threats (50km radius) */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-purple-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('predictive.communityThreats', 'Community Threats (50km)')}
                  </span>
                  <Users className="w-4 h-4 text-purple-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.community_threats.report_count}
                  <span className="text-xs font-bold text-slate-500"> reports</span>
                </div>
                <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
                  <div
                    className="bg-purple-500 h-full rounded-full"
                    style={{
                      width: `${Math.min(
                        100,
                        predictiveResult.community_threats.report_count * 20
                      )}%`,
                    }}
                  />
                </div>
                <p className="text-[11px] text-slate-500 font-medium truncate">
                  Nearest detection:{' '}
                  <strong>{predictiveResult.community_threats.nearest_outbreak_km} km</strong> (last 7 days)
                </p>
              </div>
            </div>

            {/* 3. Top 3 Predicted Disease Outbreaks */}
            {predictiveResult.predicted_outbreaks &&
              predictiveResult.predicted_outbreaks.length > 0 && (
                <div className="space-y-3 pt-2">
                  <div className="flex items-center justify-between">
                    <h4 className="text-sm sm:text-base font-black text-slate-900 flex items-center gap-2">
                      <ShieldAlert className="w-4 h-4 text-rose-600" />
                      <span>{t('predictive.predictedOutbreaks', 'Top Predicted Disease Outbreaks')}</span>
                    </h4>
                    <span className="text-xs font-bold text-slate-500 font-mono">Next 1–5 Days Window</span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
                    {predictiveResult.predicted_outbreaks.map((item, idx) => (
                      <div
                        key={idx}
                        className="p-4 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3 hover:shadow-md transition-all flex flex-col justify-between"
                      >
                        <div className="space-y-1.5">
                          <div className="flex items-center justify-between gap-2">
                            <span className="w-6 h-6 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs flex items-center justify-center font-mono">
                              #{idx + 1}
                            </span>
                            <span className="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-50 text-rose-900 border border-rose-200">
                              Window: ~{item.days_until_window} days
                            </span>
                          </div>
                          <h5 className="text-sm font-black text-slate-900 leading-tight">
                            {item.disease}
                          </h5>
                        </div>

                        <div className="space-y-1">
                          <div className="flex justify-between text-xs font-bold">
                            <span className="text-slate-500">Outbreak Probability</span>
                            <span className="text-slate-900 font-mono">{item.probability}%</span>
                          </div>
                          <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                            <div
                              className={`h-full rounded-full transition-all ${
                                item.probability >= 60
                                  ? 'bg-rose-500'
                                  : item.probability >= 40
                                  ? 'bg-amber-500'
                                  : 'bg-emerald-500'
                              }`}
                              style={{ width: `${item.probability}%` }}
                            />
                          </div>
                        </div>

                        {onNavigateToDiagnosis && (
                          <button
                            type="button"
                            onClick={onNavigateToDiagnosis}
                            className="mt-1 w-full py-1.5 rounded-xl bg-slate-50 hover:bg-agri-50 text-agri-800 hover:text-agri-900 border border-slate-200 hover:border-agri-300 text-xs font-black transition-all flex items-center justify-center gap-1.5"
                          >
                            <span>Inspect & Diagnose Leaf</span>
                            <ArrowRight className="w-3.5 h-3.5" />
                          </button>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

            {/* 4. 5-Day Risk Timeline */}
            {predictiveResult.five_day_forecast &&
              predictiveResult.five_day_forecast.length > 0 && (
                <div className="space-y-3 pt-2">
                  <h4 className="text-sm sm:text-base font-black text-slate-900 flex items-center gap-2">
                    <TrendingUp className="w-4 h-4 text-teal-600" />
                    <span>{t('predictive.riskTimeline', '5-Day Risk Progression Timeline')}</span>
                  </h4>

                  <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2.5">
                    {predictiveResult.five_day_forecast.map((day, idx) => {
                      const dayColor = getRiskScoreColor(day.risk_score);
                      return (
                        <div
                          key={idx}
                          className="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1.5"
                        >
                          <span className="text-[11px] font-bold text-slate-500 block">
                            {idx === 0 ? 'Today' : day.date}
                          </span>
                          <div className="text-xl font-black font-mono text-slate-900">
                            {day.risk_score}%
                          </div>
                          <span
                            className={`inline-block px-2 py-0.5 rounded-md text-[9px] font-black uppercase ${dayColor.badgeBg}`}
                          >
                            {day.risk_level}
                          </span>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}

            {/* 5. Recommended Preventive Actions (Gemini AI) */}
            {predictiveResult.recommended_actions &&
              predictiveResult.recommended_actions.length > 0 && (
                <div className="space-y-3 pt-2">
                  <h4 className="text-sm sm:text-base font-black text-slate-900 flex items-center gap-2">
                    <ShieldCheck className="w-4 h-4 text-emerald-600" />
                    <span>
                      {t(
                        'predictive.preventiveActions',
                        'AI Recommended Preventive Actions'
                      )}
                    </span>
                  </h4>

                  <div className="space-y-2">
                    {predictiveResult.recommended_actions.map((action, idx) => (
                      <div
                        key={idx}
                        className="p-3 sm:p-3.5 rounded-2xl bg-agri-50/70 border border-agri-200/80 text-xs sm:text-sm text-agri-950 font-medium flex items-start gap-2.5 leading-relaxed"
                      >
                        <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                        <span>{action}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
          </div>
        )}
      </div>
    </div>
  );
};

export default FieldDataTab;
