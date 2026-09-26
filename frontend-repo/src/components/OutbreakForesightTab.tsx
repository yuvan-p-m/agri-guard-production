import React, { useEffect, useState, useCallback } from 'react';
import {
  RefreshCw,
  Activity,
  AlertTriangle,
  CheckCircle2,
  CloudRain,
  Brain,
  ShieldCheck,
  Calendar,
  Users,
  ShieldAlert,
  ArrowRight,
  TrendingUp,
  Sparkles,
} from 'lucide-react';
import type {
  HardwareState,
  UserProfile,
  WeatherInfo,
  OutbreakForesightResponse,
  PredictiveSensorData,
} from '../types';
import {
  subscribeToLiveSensors,
  type InterpretedSensorSnapshot,
} from '../services/sensorService';
import { predictiveAPI } from '../services/api';
import { useAppTranslation } from '../i18n';
import { localizeDiseaseName, localizePreventiveAction } from '../utils/outbreakLocalization';

export interface OutbreakForesightTabProps {
  onNavigateToDiagnosis?: () => void;
  hardwareState?: HardwareState;
  onPairHardware?: () => void;
  user?: UserProfile;
  weather?: WeatherInfo;
}

export const OutbreakForesightTab: React.FC<OutbreakForesightTabProps> = ({
  onNavigateToDiagnosis,
  user,
  weather,
}) => {
  const { t, language } = useAppTranslation();
  const [snapshot, setSnapshot] = useState<InterpretedSensorSnapshot | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Outbreak Foresight State
  const [predictiveResult, setPredictiveResult] = useState<OutbreakForesightResponse | null>(null);
  const [isPredicting, setIsPredicting] = useState<boolean>(false);
  const [predictiveError, setPredictiveError] = useState<string | null>(null);
  const [hasRunInitialPrediction, setHasRunInitialPrediction] = useState<boolean>(false);

  // Live listener to Firebase Realtime Database (`sensors` path)
  useEffect(() => {
    setIsLoading(true);
    const unsubscribe = subscribeToLiveSensors((data) => {
      setSnapshot(data);
      setIsLoading(false);
    });

    return () => {
      unsubscribe();
    };
  }, []);

  // Run Outbreak Foresight Analysis
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
          language: language,
          sensor_data: sensorPayload,
        });

        if (response) {
          setPredictiveResult(response);
        }
      } catch (err: any) {
        console.error('Failed to run outbreak foresight:', err);
        setPredictiveError(
          err?.message || t('outbreakForesight.connectionError', 'Unable to connect to outbreak foresight service.')
        );
      } finally {
        setIsPredicting(false);
      }
    },
    [snapshot, user, weather, language, t]
  );

  // Auto-run once on component mount / when sensor data is ready
  useEffect(() => {
    if (!hasRunInitialPrediction && (snapshot?.available || !isLoading)) {
      setHasRunInitialPrediction(true);
      runPredictiveAnalysis(snapshot);
    }
  }, [snapshot, isLoading, hasRunInitialPrediction, runPredictiveAnalysis]);

  // Re-run when language changes to fetch fresh localized responses
  useEffect(() => {
    if (hasRunInitialPrediction) {
      runPredictiveAnalysis(snapshot);
    }
  }, [language]);

  const getRiskScoreColor = (score: number) => {
    if (score <= 30) {
      return {
        bg: 'bg-emerald-500',
        lightBg: 'bg-emerald-50 dark:bg-emerald-950/40',
        text: 'text-emerald-900 dark:text-emerald-100',
        badgeBg: 'bg-emerald-100 text-emerald-800 border-emerald-300',
        border: 'border-emerald-300 dark:border-emerald-700/60',
        ring: 'ring-emerald-500/20',
        label: t('outbreakForesight.lowRisk', 'LOW RISK'),
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
        label: t('outbreakForesight.mediumRisk', 'MEDIUM RISK'),
      };
    }
    return {
      bg: 'bg-rose-500',
      lightBg: 'bg-rose-50 dark:bg-rose-950/40',
      text: 'text-rose-900 dark:text-rose-100',
      badgeBg: 'bg-rose-100 text-rose-900 border-rose-300 animate-pulse',
      border: 'border-rose-300 dark:border-rose-700/60',
      ring: 'ring-rose-500/20',
      label: score > 80
        ? t('outbreakForesight.criticalRisk', 'CRITICAL RISK')
        : t('outbreakForesight.highRisk', 'HIGH RISK'),
    };
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto animate-fade-in">
      {/* ========================================================================= */}
      {/* OUTBREAK FORESIGHT (DISEASE OUTBREAK FORECASTING)                          */}
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
                  {t('outbreakForesight.title', 'Outbreak Foresight')}
                </h3>
                <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-indigo-50 text-indigo-800 border border-indigo-200">
                  <Sparkles className="w-3 h-3 text-indigo-600" />
                  <span>{t('outbreakForesight.radarBadge', 'AI Outbreak Radar')}</span>
                </span>
              </div>
              <p className="text-xs sm:text-sm text-slate-500 font-medium mt-0.5">
                {t(
                  'outbreakForesight.subtitle',
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
                ? t('outbreakForesight.running', 'Analyzing Multi-Signal Telemetry...')
                : t('outbreakForesight.runPrediction', 'Run Prediction')}
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
              {t('outbreakForesight.retry', 'Retry')}
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

        {/* Outbreak Foresight Content */}
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
                          {t('outbreakForesight.primaryCrop', 'Primary Crop')}:{' '}
                          <strong className="text-slate-800">{user?.primaryCrop || 'Tomato'}</strong>
                        </span>
                      </div>
                      <h4 className="text-base sm:text-lg font-black text-slate-900">
                        {t('outbreakForesight.overallRisk', 'Overall Outbreak Risk Score')}
                      </h4>
                      <p className="text-xs sm:text-sm text-slate-600 font-medium max-w-xl leading-relaxed">
                        {t('outbreakForesight.evaluatedAcross', 'Evaluated across')}{' '}
                        <strong>
                          {predictiveResult.community_threats.report_count}{' '}
                          {t('outbreakForesight.nearbyOutbreaks', 'nearby outbreaks')}
                        </strong>
                        ,{' '}
                        {t(
                          'outbreakForesight.evaluationDesc',
                          'current canopy humidity, soil nutrient stress, and seasonal spore germination conditions.'
                        )}
                      </p>
                    </div>

                    <div className="flex items-center gap-4 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md p-4 rounded-2xl border border-slate-200/80 shadow-sm shrink-0">
                      <div className="text-center">
                        <div className="text-4xl font-black font-mono tracking-tight text-slate-900">
                          {predictiveResult.overall_risk_score}
                          <span className="text-lg font-bold text-slate-500">%</span>
                        </div>
                        <span className="text-[10px] font-black uppercase tracking-wider text-slate-500 block">
                          {t('outbreakForesight.outbreakIndex', 'Outbreak Index')}
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
                      <span>{t('outbreakForesight.safeRange', '0% (Safe)')}</span>
                      <span>{t('outbreakForesight.lowRange', '30% (Low)')}</span>
                      <span>{t('outbreakForesight.moderateRange', '60% (Moderate)')}</span>
                      <span>{t('outbreakForesight.criticalRange', '100% (Critical)')}</span>
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
                    {t('outbreakForesight.soilHealth', 'Soil Health Index')}
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
                    ? t(
                        'outbreakForesight.soilHealthOptimal',
                        'Optimal nutrient balance supports natural disease defense.'
                      )
                    : t(
                        'outbreakForesight.soilHealthDeficient',
                        'Soil stress or deficiency elevates disease susceptibility.'
                      )}
                </p>
              </div>

              {/* Card 2: Weather Risk Score */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-blue-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('outbreakForesight.weatherRisk', 'Weather Risk Score')}
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
                  {t(
                    'outbreakForesight.weatherRiskDesc',
                    'Derived from OpenWeatherMap 5-day humidity & rain forecast.'
                  )}
                </p>
              </div>

              {/* Card 3: Seasonal Risk Level */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-amber-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('outbreakForesight.seasonalRisk', 'Seasonal Risk Level')}
                  </span>
                  <Calendar className="w-4 h-4 text-amber-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.seasonal_risk_level === 'HIGH'
                    ? t('outbreakForesight.highRisk', 'HIGH')
                    : predictiveResult.seasonal_risk_level === 'MEDIUM'
                    ? t('outbreakForesight.mediumRisk', 'MEDIUM')
                    : t('outbreakForesight.lowRisk', 'LOW')}
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
                    ? t(
                        'outbreakForesight.seasonalRiskHigh',
                        'Kharif monsoon period — high fungal spore activity.'
                      )
                    : predictiveResult.seasonal_risk_level === 'MEDIUM'
                    ? t(
                        'outbreakForesight.seasonalRiskMedium',
                        'Rabi season — cool temperature mildew window.'
                      )
                    : t(
                        'outbreakForesight.seasonalRiskLow',
                        'Summer dry window — low seasonal baseline.'
                      )}
                </p>
              </div>

              {/* Card 4: Community Threats (50km radius) */}
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200/90 space-y-2 hover:border-purple-300 transition-all">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-black text-slate-700 uppercase tracking-wider">
                    {t('outbreakForesight.communityThreats', 'Community Threats (50km)')}
                  </span>
                  <Users className="w-4 h-4 text-purple-600" />
                </div>
                <div className="text-2xl font-black text-slate-900 font-mono">
                  {predictiveResult.community_threats.report_count}
                  <span className="text-xs font-bold text-slate-500">
                    {' '}
                    {t('outbreakForesight.reports', 'reports')}
                  </span>
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
                  {t('outbreakForesight.nearestDetection', 'Nearest detection:')}{' '}
                  <strong>{predictiveResult.community_threats.nearest_outbreak_km} km</strong>{' '}
                  {t('outbreakForesight.last7Days', '(last 7 days)')}
                </p>
                {predictiveResult.community_threats.diseases_reported &&
                  predictiveResult.community_threats.diseases_reported.length > 0 && (
                    <div className="flex flex-wrap gap-1 pt-1">
                      {predictiveResult.community_threats.diseases_reported.slice(0, 2).map((d, i) => (
                        <span
                          key={i}
                          className="px-1.5 py-0.5 rounded text-[9px] font-bold bg-purple-100/80 text-purple-900 truncate max-w-[150px]"
                          title={localizeDiseaseName(d, language)}
                        >
                          {localizeDiseaseName(d, language)}
                        </span>
                      ))}
                    </div>
                  )}
              </div>
            </div>

            {/* 3. Top 3 Predicted Disease Outbreaks */}
            {predictiveResult.predicted_outbreaks &&
              predictiveResult.predicted_outbreaks.length > 0 && (
                <div className="space-y-3 pt-2">
                  <div className="flex items-center justify-between">
                    <h4 className="text-sm sm:text-base font-black text-slate-900 flex items-center gap-2">
                      <ShieldAlert className="w-4 h-4 text-rose-600" />
                      <span>
                        {t('outbreakForesight.predictedOutbreaks', 'Top Predicted Disease Outbreaks')}
                      </span>
                    </h4>
                    <span className="text-xs font-bold text-slate-500 font-mono">
                      {t('outbreakForesight.forecastWindow', 'Next 1–5 Days Window')}
                    </span>
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
                              {t('outbreakForesight.windowDays', { days: item.days_until_window })}
                            </span>
                          </div>
                          <h5 className="text-sm font-black text-slate-900 leading-tight">
                            {localizeDiseaseName(item.disease, language)}
                          </h5>
                        </div>

                        <div className="space-y-1">
                          <div className="flex justify-between text-xs font-bold">
                            <span className="text-slate-500">
                              {t('outbreakForesight.outbreakProbability', 'Outbreak Probability')}
                            </span>
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
                            className="mt-1 w-full py-1.5 rounded-xl bg-slate-50 hover:bg-agri-50 text-agri-800 hover:text-agri-900 border border-slate-200 hover:border-agri-300 text-xs font-black transition-all flex items-center justify-center gap-1.5 cursor-pointer"
                          >
                            <span>
                              {t('outbreakForesight.inspectLeaf', 'Inspect & Diagnose Leaf')}
                            </span>
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
                    <span>
                      {t(
                        'outbreakForesight.riskTimeline',
                        '5-Day Risk Progression Timeline'
                      )}
                    </span>
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
                            {idx === 0 ? t('outbreakForesight.today', 'Today') : day.date}
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
                        'outbreakForesight.preventiveActions',
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
                        <span>
                          {localizePreventiveAction(
                            action,
                            user?.primaryCrop || 'Tomato',
                            language,
                            idx
                          )}
                        </span>
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

export default OutbreakForesightTab;
