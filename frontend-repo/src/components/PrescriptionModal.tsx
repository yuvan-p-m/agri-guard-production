import React from 'react';
import { 
  FileCheck, 
  Printer, 
  Download, 
  X, 
  Sprout, 
  ShieldCheck, 
  User, 
  Calendar, 
  MapPin,
  CheckCircle2,
  AlertTriangle
} from 'lucide-react';
import type { DiseaseDiagnosis, UserProfile } from '../types';
import { useAppTranslation, getCurrentLanguage } from '../i18n';

interface PrescriptionModalProps {
  isOpen: boolean;
  onClose: () => void;
  diagnosis: DiseaseDiagnosis | null;
  user: UserProfile;
  acreage: number;
}

export const PrescriptionModal: React.FC<PrescriptionModalProps> = ({
  isOpen,
  onClose,
  diagnosis,
  user,
  acreage,
}) => {
  const { t } = useAppTranslation();
  if (!isOpen || !diagnosis) return null;

  const currentLang = getCurrentLanguage();

  const handlePrint = () => {
    window.print();
  };

  const todayStr = new Date().toLocaleDateString(currentLang, {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  });

  const diseaseNameDisplay = (diagnosis.diseaseName as any)?.[currentLang] || diagnosis.diseaseName?.en || 'Identified Plant Condition';
  const organicRemedies = diagnosis.organicProtocol?.remedies || [];
  const chemicalRemedies = diagnosis.chemicalProtocol?.remedies || [];

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6 animate-fade-in">
      <div className="relative w-full max-w-2xl bg-white rounded-3xl shadow-2xl overflow-hidden border border-emerald-200 flex flex-col max-h-[92vh]">
        
        {/* Top Action Bar */}
        <div className="flex items-center justify-between p-4 sm:p-5 bg-agri-900 text-white">
          <div className="flex items-center gap-2">
            <div className="p-1.5 rounded-lg bg-agri-700 text-citrus-300">
              <Sprout className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base sm:text-lg font-black tracking-tight font-sans">
                {t('modals.prescriptionTitle', 'AgriGuard Digital Health Prescription')}
              </h3>
              <p className="text-[11px] text-agri-200 font-mono">
                RX #{Math.floor(100000 + Math.random() * 900000)} • {t('diagnosticHub.modelInference', 'AI Diagnosis Report')}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-agri-700 hover:bg-agri-800 text-white text-xs font-bold transition-colors cursor-pointer"
            >
              <Printer className="w-3.5 h-3.5" />
              <span>{t('common.print', 'Print / PDF')}</span>
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white transition-colors cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Prescription Printable Body */}
        <div id="printable-prescription" className="p-6 sm:p-8 overflow-y-auto space-y-6 text-slate-800">
          
          {/* Header Info Block */}
          <div className="grid grid-cols-2 gap-4 p-4 rounded-2xl bg-slate-50 border border-slate-200/80 text-xs">
            <div>
              <p className="text-slate-500 font-medium">{t('profile.name')}:</p>
              <p className="font-extrabold text-slate-900 text-sm mt-0.5">{user.name || t('common.farmerPartner', 'Farmer Partner')}</p>
              <p className="text-slate-600 font-mono mt-0.5">{user.phone || t('common.na', 'N/A')}</p>
            </div>
            <div>
              <p className="text-slate-500 font-medium">{t('common.date', 'Date')}:</p>
              <p className="font-extrabold text-slate-900 text-sm mt-0.5">{todayStr}</p>
              <p className="text-agri-800 font-bold mt-0.5">{acreage} {t('cropRecommendation.acres')} ({user.district || t('common.district', 'District')}, {user.state || t('common.state', 'State')})</p>
            </div>
          </div>

          {/* Disease Identified */}
          <div className="p-4 rounded-2xl bg-agri-50/80 border border-agri-200">
            <div className="flex items-center justify-between">
              <span className="text-xs font-black text-agri-950 uppercase tracking-wide">
                {t('earlyDetection.title')}
              </span>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-700 text-white">
                {diagnosis.confidence}% {t('earlyDetection.confidence')}
              </span>
            </div>
            <h4 className="text-lg font-black text-slate-900 mt-1">
              {diseaseNameDisplay}
            </h4>
            <p className="text-xs text-agri-800 italic font-mono mt-0.5">
              {t('earlyDetection.pathogen')}: {diagnosis.scientificName || t('earlyDetection.defaultPathogen')} ({diagnosis.pathogenType || t('earlyDetection.pathogenFungus')})
            </p>
          </div>

          {/* Prescribed Dosages Breakdown */}
          <div>
            <h5 className="text-xs font-black uppercase tracking-wider text-slate-500 mb-2.5">
              {t('earlyDetection.prescriptionButton')} ({acreage} {t('cropRecommendation.acres')})
            </h5>
            
            <div className="space-y-3">
              {/* Organic Remedies */}
              <div className="p-3.5 rounded-xl border border-emerald-200 bg-emerald-50/40">
                <div className="text-xs font-bold text-emerald-900 flex items-center gap-1.5 mb-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700" />
                  <span>{t('treatment.protocolA', 'Protocol A: Immediate Steps')}</span>
                </div>
                {organicRemedies.map((rem) => {
                  const calc = typeof rem.dosageFormula === 'function' ? rem.dosageFormula(acreage) : { amount: t('treatment.recommendedDosage', 'Recommended dosage'), waterVolume: '200 L' };
                  return (
                    <div key={rem.id} className="text-xs text-slate-700 mt-1 pl-5">
                      <strong className="text-slate-900">{rem.name}:</strong> {calc.amount} {t('treatment.in', 'in')} {calc.waterVolume} {t('treatment.water', 'water')}.
                      <p className="text-[11px] text-slate-500 mt-0.5">{rem.instructions}</p>
                    </div>
                  );
                })}
              </div>

              {/* Chemical Remedies */}
              <div className="p-3.5 rounded-xl border border-blue-200 bg-blue-50/40">
                <div className="text-xs font-bold text-blue-900 flex items-center gap-1.5 mb-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-blue-700" />
                  <span>{t('treatment.protocolB', 'Protocol B: Approved Chemical Protocol')}</span>
                </div>
                {chemicalRemedies.map((rem) => {
                  const calc = typeof rem.dosageFormula === 'function' ? rem.dosageFormula(acreage) : { amount: t('treatment.recommendedDosage', 'Recommended dosage'), waterVolume: '200 L' };
                  return (
                    <div key={rem.id} className="text-xs text-slate-700 mt-1 pl-5">
                      <strong className="text-slate-900">{rem.name}:</strong> {calc.amount} {t('treatment.in', 'in')} {calc.waterVolume} {t('treatment.water', 'water')}.
                      <p className="text-[11px] text-slate-500 mt-0.5">{rem.instructions} • {t('treatment.sprayTiming')}: {rem.schedule}</p>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Safety & PHI */}
          <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs text-amber-950 flex items-start gap-2">
            <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
            <div>
              <p className="font-bold">{t('treatment.precautions')}:</p>
              <p className="text-[11px] mt-0.5">
                {t('treatment.safetyFirstDesc', 'Always spray during early morning (6:30 AM - 9:30 AM). Wear protective face masks & nitrile gloves. Keep harvest waiting period (PHI) in mind.')}
              </p>
            </div>
          </div>

          {/* Digital Signature & Stamp */}
          <div className="pt-4 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500">
            <div className="flex items-center gap-2">
              <ShieldCheck className="w-6 h-6 text-agri-700" />
              <div>
                <p className="font-bold text-slate-800">{t('treatment.verifiedBadge', 'Verified by AgriGuard AI')}</p>
                <p className="text-[10px]">{t('treatment.cibrcApproved')}</p>
              </div>
            </div>
            <div className="text-right">
              <span className="font-mono text-[10px] text-slate-400">{t('treatment.authenticatedReport', 'AUTHENTICATED DIGITAL REPORT')}</span>
            </div>
          </div>

        </div>

      </div>
    </div>
  );
};
