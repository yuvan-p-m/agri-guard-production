import React, { useState } from 'react';
import { 
  MessageSquareText, 
  Send, 
  RefreshCw, 
  RotateCcw,
  Smartphone, 
  CheckCircle2, 
  AlertCircle, 
  ArrowRight, 
  ShieldCheck,
  Radio
} from 'lucide-react';
import type { UserProfile } from '../types';
import { alertsAPI } from '../services/api';
import { useAppTranslation } from '../i18n';

interface SmsDemoTabProps {
  user: UserProfile;
  onNavigateToProfile: () => void;
}

export const SmsDemoTab: React.FC<SmsDemoTabProps> = ({
  user,
  onNavigateToProfile,
}) => {
  const { t, language } = useAppTranslation();
  const isRtl = language === 'ar' || language === 'ur';

  const [isSending, setIsSending] = useState<boolean>(false);
  const [statusState, setStatusState] = useState<{
    type: 'success' | 'error';
    code: 'SMS_SEND_SUCCESS' | 'SMS_SEND_FAILED' | 'MOBILE_NUMBER_REQUIRED';
    dispatchedMessage?: string;
    errorMessage?: string;
  } | null>(null);

  const rawPhone = user?.phone?.trim() || '';
  const hasPhone = rawPhone.length >= 6;

  // Mask mobile number for privacy (e.g., "+91 ••••••0000" or "••••••4321")
  const maskedPhone = React.useMemo(() => {
    if (!rawPhone) return '';
    const last4 = rawPhone.slice(-4);
    if (rawPhone.startsWith('+')) {
      const spaceIdx = rawPhone.indexOf(' ');
      const prefix = spaceIdx > 0 ? rawPhone.slice(0, spaceIdx + 1) : rawPhone.slice(0, 3) + ' ';
      return `${prefix}••••••${last4}`;
    }
    return `••••••${last4}`;
  }, [rawPhone]);

  const handleSendDemoSms = async () => {
    if (isSending) return;

    if (!hasPhone) {
      setStatusState({
        type: 'error',
        code: 'MOBILE_NUMBER_REQUIRED',
      });
      return;
    }

    setIsSending(true);
    setStatusState(null);

    try {
      const res: any = await alertsAPI.sendTestSms({
        phone: rawPhone,
        uid: user.id,
        name: user.name || 'Farmer Partner',
        location: user.location || user.district || 'Nagpur',
      });

      if (res?.success) {
        setStatusState({
          type: 'success',
          code: 'SMS_SEND_SUCCESS',
          dispatchedMessage: res.message,
        });
      } else {
        setStatusState({
          type: 'error',
          code: 'SMS_SEND_FAILED',
          errorMessage: res?.detail || res?.message || 'Failed to dispatch SMS alert.',
        });
      }
    } catch (err: any) {
      console.warn('SMS Demo send error:', err);
      const detailMsg = err?.response?.data?.detail || err?.message || t('smsDemo.smsError');
      setStatusState({
        type: 'error',
        code: 'SMS_SEND_FAILED',
        errorMessage: detailMsg,
      });
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in pb-12">
      {/* Header Card */}
      <div className="bg-white/95 backdrop-blur-md rounded-3xl p-6 sm:p-8 shadow-xl border border-agri-200/80">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-100">
          <div className="flex items-start gap-4">
            <div className="p-3 rounded-2xl bg-gradient-to-br from-agri-700 to-agri-900 text-white shadow-md shrink-0">
              <MessageSquareText className="w-6 h-6 text-citrus-400" />
            </div>
            <div>
              <div className="flex flex-wrap items-center gap-2.5">
                <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
                  {t('smsDemo.title')}
                </h2>
                <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-sky-100 text-sky-900 border border-sky-300">
                  <Radio className="w-3 h-3 text-sky-600 animate-pulse" />
                  <span>{t('smsDemo.interactiveGateway', 'Interactive Gateway')}</span>
                </span>
              </div>
              <p className="text-xs sm:text-sm text-slate-600 font-medium mt-1">
                {t('smsDemo.subtitle')}
              </p>
            </div>
          </div>
        </div>

        {/* Informational intro */}
        <p className="text-xs sm:text-sm text-slate-600 leading-relaxed mt-5">
          {t('smsDemo.liveDemoNotice')}
        </p>

        {/* State container */}
        <div className="mt-6">
          {hasPhone ? (
            /* CASE A — Mobile number already exists */
            <div className="space-y-6">
              <div className="rounded-2xl border-2 border-emerald-200/80 bg-emerald-50/60 p-5 sm:p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div className="flex items-center gap-3.5">
                  <div className="w-10 h-10 rounded-xl bg-emerald-100 border border-emerald-300 flex items-center justify-center text-emerald-800 shrink-0">
                    <Smartphone className="w-5 h-5" />
                  </div>
                  <div>
                    <span className="text-[10px] font-black uppercase tracking-wider text-emerald-900 block">
                      {t('smsDemo.registeredNumber')}
                    </span>
                    <span 
                      className="text-base sm:text-lg font-mono font-black text-emerald-950 inline-block" 
                      dir="ltr"
                    >
                      {maskedPhone}
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-1.5 self-start sm:self-auto px-3 py-1 rounded-full bg-white border border-emerald-300 text-[11px] font-bold text-emerald-800 shadow-2xs">
                  <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                  <span>{t('smsDemo.privacyProtected', 'Privacy Protected')}</span>
                </div>
              </div>

              {/* Action Trigger Area */}
              <div className="rounded-3xl border border-slate-200 bg-slate-50/80 p-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                <div className="space-y-1 max-w-lg">
                  <h4 className="text-sm sm:text-base font-bold text-slate-900">
                    {t('smsDemo.sendLiveSms')}
                  </h4>
                  <p className="text-xs text-slate-500 leading-relaxed">
                    {t('smsDemo.sendDesc', t('smsDemo.subtitle'))}
                  </p>
                </div>

                <button
                  type="button"
                  onClick={handleSendDemoSms}
                  disabled={isSending}
                  className="w-full sm:w-auto px-6 py-3.5 rounded-2xl bg-gradient-to-r from-agri-700 to-agri-900 hover:from-agri-800 hover:to-agri-950 text-white font-black text-xs sm:text-sm shadow-md shadow-agri-900/20 hover:shadow-lg transition-all flex items-center justify-center gap-2 active:scale-[0.99] disabled:opacity-60 cursor-pointer shrink-0"
                >
                  {isSending ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin" />
                      <span>{t('smsDemo.dispatching')}</span>
                    </>
                  ) : (
                    <>
                      <Send className={`w-4 h-4 text-citrus-400 ${isRtl ? '-scale-x-100' : ''}`} />
                      <span>{t('smsDemo.sendLiveSms')}</span>
                    </>
                  )}
                </button>
              </div>

              {/* Status Message Feedback */}
              {statusState && (
                <div
                  className={`p-4 sm:p-5 rounded-2xl border-2 shadow-sm animate-fade-in flex flex-col sm:flex-row items-start justify-between gap-3.5 ${
                    statusState.type === 'success'
                      ? 'bg-emerald-50 border-emerald-300 text-emerald-950'
                      : 'bg-rose-50 border-rose-300 text-rose-950'
                  }`}
                >
                  <div className="flex items-start gap-3.5">
                    {statusState.type === 'success' ? (
                      <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />
                    ) : (
                      <AlertCircle className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />
                    )}
                    <div className="space-y-1">
                      <p className="text-xs sm:text-sm font-black leading-snug">
                        {statusState.code === 'SMS_SEND_SUCCESS' && t('smsDemo.smsSuccess')}
                        {statusState.code === 'SMS_SEND_FAILED' && t('smsDemo.smsError')}
                        {statusState.code === 'MOBILE_NUMBER_REQUIRED' && t('smsDemo.noNumber')}
                      </p>
                      {statusState.type === 'success' && statusState.dispatchedMessage && (
                        <p className="text-[11px] font-mono text-emerald-800 opacity-90 leading-tight">
                          {t('smsDemo.dispatchedPrefix', 'Dispatched:')} "{statusState.dispatchedMessage}"
                        </p>
                      )}
                      {statusState.type === 'error' && statusState.errorMessage && (
                        <p className="text-[11px] font-medium text-rose-800 leading-tight">
                          {statusState.errorMessage}
                        </p>
                      )}
                    </div>
                  </div>

                  {statusState.type === 'error' && (
                    <button
                      type="button"
                      onClick={handleSendDemoSms}
                      disabled={isSending}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-100 hover:bg-rose-200 text-rose-900 text-xs font-black transition-all active:scale-95 shrink-0 self-start sm:self-auto cursor-pointer"
                    >
                      <RotateCcw className={`w-3.5 h-3.5 ${isRtl ? 'rotate-180' : ''}`} />
                      <span>{t('smsDemo.retryAction', 'Retry Sending')}</span>
                    </button>
                  )}
                </div>
              )}
            </div>
          ) : (
            /* CASE B — Mobile number is missing */
            <div className="rounded-3xl border-2 border-amber-300/90 bg-amber-50/80 p-6 sm:p-8 space-y-5">
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-2xl bg-amber-100 border border-amber-300 flex items-center justify-center text-amber-800 shrink-0 mt-0.5">
                  <Smartphone className="w-6 h-6 text-amber-700" />
                </div>
                <div className="space-y-1.5">
                  <span className="text-[11px] font-black uppercase tracking-wider text-amber-900 block">
                    {t('smsDemo.missingNumberWarning', t('common.warning', 'Notice'))}
                  </span>
                  <p className="text-sm sm:text-base font-extrabold text-amber-950 leading-relaxed">
                    {t('smsDemo.noNumber')}
                  </p>
                  <p className="text-xs text-amber-800 font-medium">
                    {t('smsDemo.enterPhonePrompt')}
                  </p>
                </div>
              </div>

              <div className="pt-2 border-t border-amber-200/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <span className="text-xs font-semibold text-amber-900">
                  {t('smsDemo.updateNumber')}
                </span>
                <button
                  type="button"
                  onClick={onNavigateToProfile}
                  className="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-2xl bg-agri-700 hover:bg-agri-800 text-white text-xs sm:text-sm font-black shadow-md shadow-agri-900/20 transition-all cursor-pointer active:scale-[0.99] self-start sm:self-auto"
                >
                  <span>{t('smsDemo.updateNumber')}</span>
                  <ArrowRight className={`w-4 h-4 ${isRtl ? 'rotate-180' : ''}`} />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
