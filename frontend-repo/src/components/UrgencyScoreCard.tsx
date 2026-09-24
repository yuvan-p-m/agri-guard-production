import React from 'react';
import {
  AlertOctagon,
  AlertTriangle,
  TrendingUp,
  ShieldCheck,
  Clock,
  CloudRain,
  Droplets,
  Layers,
  Zap,
  Info
} from 'lucide-react';
import type { UrgencyInfo } from '../types';
import { useAppTranslation } from '../i18n';

interface UrgencyScoreCardProps {
  urgency: UrgencyInfo | null;
  isLoading?: boolean;
  isHealthy?: boolean;
}

export const UrgencyScoreCard: React.FC<UrgencyScoreCardProps> = ({
  urgency,
  isLoading,
  isHealthy,
}) => {
  const { t } = useAppTranslation();

  // Skeleton Loader while diagnosis / urgency calculation is in-flight
  if (isLoading) {
    return (
      <div className="backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-slate-200 bg-white/95 space-y-4 animate-pulse">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-100">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-slate-200" />
            <div className="space-y-1.5">
              <div className="w-28 h-3 bg-slate-200 rounded" />
              <div className="w-48 h-6 bg-slate-200 rounded" />
            </div>
          </div>
          <div className="w-24 h-8 rounded-full bg-slate-200" />
        </div>
        <div className="p-4 rounded-2xl bg-slate-100/80 space-y-2">
          <div className="w-full h-4 bg-slate-200 rounded" />
          <div className="w-3/4 h-4 bg-slate-200 rounded" />
        </div>
      </div>
    );
  }

  if (!urgency) {
    return null;
  }

  const score = urgency.urgency_score || 1;
  const level = (urgency.urgency_level || 'low').toLowerCase();

  // Determine styling theme based on semantic level
  const getTheme = () => {
    switch (level) {
      case 'critical':
        return {
          cardBorder: 'border-red-300 ring-2 ring-red-400/20',
          cardBg: 'bg-gradient-to-br from-white via-red-50/40 to-white',
          badge: 'bg-red-600 text-white shadow-md shadow-red-200 animate-pulse',
          badgeText: t('urgency.levelCritical', 'Critical Urgency'),
          icon: <AlertOctagon className="w-6 h-6 text-red-600" />,
          scoreBg: 'bg-red-600 text-white',
          scoreRing: 'text-red-600',
          instructionBg: 'bg-red-50/90 border border-red-200 text-red-950',
          instructionHeading: 'text-red-900',
          progressColor: 'bg-red-600',
        };
      case 'high':
        return {
          cardBorder: 'border-orange-300 ring-1 ring-orange-300/30',
          cardBg: 'bg-gradient-to-br from-white via-orange-50/40 to-white',
          badge: 'bg-orange-500 text-white shadow-sm shadow-orange-200',
          badgeText: t('urgency.levelHigh', 'High Urgency'),
          icon: <AlertTriangle className="w-6 h-6 text-orange-500" />,
          scoreBg: 'bg-orange-500 text-white',
          scoreRing: 'text-orange-500',
          instructionBg: 'bg-orange-50/90 border border-orange-200 text-orange-950',
          instructionHeading: 'text-orange-900',
          progressColor: 'bg-orange-500',
        };
      case 'moderate':
        return {
          cardBorder: 'border-amber-300',
          cardBg: 'bg-gradient-to-br from-white via-amber-50/30 to-white',
          badge: 'bg-amber-100 text-amber-950 border border-amber-300',
          badgeText: t('urgency.levelModerate', 'Moderate Urgency'),
          icon: <TrendingUp className="w-6 h-6 text-amber-600" />,
          scoreBg: 'bg-amber-500 text-white',
          scoreRing: 'text-amber-500',
          instructionBg: 'bg-amber-50/80 border border-amber-200 text-amber-950',
          instructionHeading: 'text-amber-900',
          progressColor: 'bg-amber-500',
        };
      case 'low':
      default:
        return {
          cardBorder: 'border-emerald-200',
          cardBg: 'bg-gradient-to-br from-white via-emerald-50/30 to-white',
          badge: 'bg-emerald-100 text-emerald-900 border border-emerald-300',
          badgeText: t('urgency.levelLow', 'Low Urgency'),
          icon: <ShieldCheck className="w-6 h-6 text-emerald-600" />,
          scoreBg: 'bg-emerald-600 text-white',
          scoreRing: 'text-emerald-600',
          instructionBg: 'bg-emerald-50/80 border border-emerald-200 text-emerald-950',
          instructionHeading: 'text-emerald-900',
          progressColor: 'bg-emerald-600',
        };
    }
  };

  const theme = getTheme();

  return (
    <div
      id="urgency-score-card"
      className={`rounded-3xl p-5 sm:p-7 shadow-xl backdrop-blur-md transition-all border ${theme.cardBorder} ${theme.cardBg}`}
    >
      {/* ─── Top Header: Title, Level Badge & Score Gauge ────────────────────────── */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-100">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-2xl bg-white shadow-sm border border-slate-100 shrink-0">
            {theme.icon}
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
                {t('urgency.title', 'Action Urgency')}
              </span>
              <span className={`px-2.5 py-0.5 rounded-full text-xs font-black tracking-wide ${theme.badge}`}>
                {theme.badgeText}
              </span>
            </div>
            <h3 className="text-lg sm:text-xl font-black text-slate-900 tracking-tight mt-0.5">
              {t('urgency.scoreLabel', 'Urgency Score')}: <span className="font-black text-slate-950">{score}/10</span>
            </h3>
          </div>
        </div>

        {/* Visual Progress Bar on Mobile / Desktop */}
        <div className="flex items-center gap-3 self-start sm:self-center">
          <div className="w-36 sm:w-44 bg-slate-100 rounded-full h-3.5 p-0.5 border border-slate-200/80 overflow-hidden shadow-inner">
            <div
              className={`h-full rounded-full transition-all duration-700 ${theme.progressColor}`}
              style={{ width: `${Math.max(10, Math.min(100, score * 10))}%` }}
            />
          </div>
          <div className={`px-3 py-1 rounded-xl text-sm font-black shadow-sm ${theme.scoreBg}`}>
            {score}/10
          </div>
        </div>
      </div>

      {/* ─── Primary Farmer Action Instruction ─────────────────────────────────── */}
      <div className="mt-4 space-y-3">
        <div className={`p-4 sm:p-5 rounded-2xl ${theme.instructionBg} shadow-sm`}>
          <div className="flex items-start gap-3">
            <Zap className="w-5 h-5 text-amber-600 shrink-0 mt-0.5" />
            <div className="space-y-1">
              <p className="text-sm sm:text-base font-black tracking-tight leading-snug">
                {urgency.instruction}
              </p>
              {urgency.reason && (
                <p className="text-xs sm:text-sm font-medium text-slate-700 leading-relaxed">
                  {urgency.reason}
                </p>
              )}
            </div>
          </div>
        </div>

        {/* ─── Contextual Signal Badges (Rain, Humidity, Detection Delay) ────────── */}
        <div className="flex flex-wrap items-center gap-2 pt-1">
          {urgency.hours_until_rain !== null && urgency.hours_until_rain !== undefined && (
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-xl bg-blue-50 border border-blue-200 text-blue-900 text-xs font-bold shadow-xs">
              <CloudRain className="w-3.5 h-3.5 text-blue-600" />
              <span>
                {urgency.hours_until_rain === 0
                  ? t('urgency.rainImminent', 'Rain occurring / imminent')
                  : t('urgency.rainApproaching', { hours: Math.round(urgency.hours_until_rain) })}
              </span>
            </div>
          )}

          {urgency.days_since_detection !== null && urgency.days_since_detection !== undefined && urgency.days_since_detection > 0 && (
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs font-bold shadow-xs">
              <Clock className="w-3.5 h-3.5 text-amber-600" />
              <span>
                {t('urgency.daysDelayed', { days: urgency.days_since_detection })}
              </span>
            </div>
          )}

          {/* Factor Breakdown Summary */}
          {urgency.breakdown && (
            <div className="inline-flex items-center gap-1 px-2.5 py-1 rounded-xl bg-slate-100 text-slate-600 text-[11px] font-semibold">
              <Layers className="w-3 h-3 text-slate-500" />
              <span>
                P: +{urgency.breakdown.progression_score} | W: +{urgency.breakdown.weather_score} | S: +{urgency.breakdown.sensor_score} | D: +{urgency.breakdown.delay_score}
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
