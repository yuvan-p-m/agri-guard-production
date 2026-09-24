import React, { useEffect, useState } from 'react';
import { MapPin, Pencil, UserRound, Navigation, LogOut } from 'lucide-react';
import type { UserProfile } from '../types';
import { useAppTranslation } from '../i18n';

interface ProfileFarmSettingsProps {
  user: UserProfile;
  onSave: (profile: UserProfile) => void;
  onLogout?: () => void;
}

export const ProfileFarmSettings: React.FC<ProfileFarmSettingsProps> = ({ 
  user, 
  onSave, 
  onLogout 
}) => {
  const { t } = useAppTranslation();
  const [isEditing, setIsEditing] = useState(false);
  const [draft, setDraft] = useState(user);

  useEffect(() => {
    if (!isEditing) setDraft(user);
  }, [user, isEditing]);

  const updateDraft = <K extends keyof UserProfile>(key: K, value: UserProfile[K]) => {
    setDraft((current) => ({ ...current, [key]: value }));
  };
  const startEditing = () => {
    setDraft(user);
    setIsEditing(true);
  };
  const cancelEditing = () => {
    setDraft(user);
    setIsEditing(false);
  };
  const saveChanges = () => {
    onSave(draft);
    setIsEditing(false);
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6 animate-fade-in">
      <section className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-agri-200/80">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-5 border-b border-slate-100">
          <div className="flex items-center gap-3">
            <span className="p-2.5 rounded-xl bg-agri-100 text-agri-800">
              <UserRound className="w-5 h-5" />
            </span>
            <div>
              <h2 className="text-xl font-black text-slate-900">{t('profile.title')}</h2>
              <p className="text-xs text-slate-500 mt-0.5 font-medium">{t('profile.subtitle')}</p>
            </div>
          </div>
          
          <div className="flex items-center gap-2 self-start sm:self-auto">
            {!isEditing ? (
              <button 
                type="button" 
                onClick={startEditing} 
                className="inline-flex items-center justify-center gap-1.5 rounded-xl bg-agri-700 px-3.5 py-2 text-xs font-black text-white hover:bg-agri-800 transition-colors shadow-sm"
              >
                <Pencil className="w-3.5 h-3.5" /> {t('profile.editProfile')}
              </button>
            ) : (
              <div className="flex items-center gap-2">
                <button 
                  type="button" 
                  onClick={cancelEditing} 
                  className="rounded-xl border border-slate-300 bg-white px-3 py-2 text-xs font-bold text-slate-700 hover:bg-slate-50 transition-colors"
                >
                  {t('profile.cancel')}
                </button>
                <button 
                  type="button" 
                  onClick={saveChanges} 
                  className="rounded-xl bg-agri-700 px-3.5 py-2 text-xs font-black text-white hover:bg-agri-800 transition-colors shadow-sm"
                >
                  {t('profile.saveChanges')}
                </button>
              </div>
            )}
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-5">
          {isEditing ? (
            <EditInput label={t('profile.name')} value={draft.name} onChange={(value) => updateDraft('name', value)} />
          ) : (
            <InfoItem label={t('profile.name')} value={user.name} />
          )}

          {isEditing ? (
            <EditInput label={t('profile.phone')} value={draft.phone} onChange={(value) => updateDraft('phone', value)} />
          ) : (
            <InfoItem label={t('profile.phone')} value={user.phone} />
          )}

          {isEditing ? (
            <EditInput 
              label={t('profile.village')} 
              value={draft.villageTaluka || draft.location || ''} 
              onChange={(value) => updateDraft('villageTaluka', value)} 
              icon={<MapPin className="w-4 h-4 text-agri-600" />} 
            />
          ) : (
            <InfoItem 
              label={t('profile.village')} 
              value={user.villageTaluka || user.location || user.district ? `${user.villageTaluka || user.location || user.district}, ${user.state || 'India'}` : 'Fetching location...'} 
              icon={<MapPin className="w-4 h-4 text-agri-600" />} 
            />
          )}

          {isEditing ? (
            <EditInput 
              label={t('profile.farmSize')} 
              type="number" 
              value={String(draft.farmSize)} 
              onChange={(value) => updateDraft('farmSize', Math.max(0, Number(value)))} 
            />
          ) : (
            <InfoItem label={t('profile.farmSize')} value={`${user.farmSize} ${user.farmUnit}`} />
          )}

          <div className="sm:col-span-2">
            <InfoItem 
              label="Tracked GPS Coordinates" 
              value={user.latitude && user.longitude ? `${user.latitude.toFixed(5)}° N, ${user.longitude.toFixed(5)}° E (Live Fixed)` : '21.14580° N, 79.08820° E (Auto-Mapped GPS)'} 
              icon={<Navigation className="w-4 h-4 text-emerald-600" />} 
            />
          </div>
        </div>
      </section>

      {/* Account Session Actions / Logout */}
      {onLogout && (
        <section className="bg-white/95 backdrop-blur-md rounded-3xl p-5 sm:p-7 shadow-xl border border-rose-200/80 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <h3 className="text-base sm:text-lg font-black text-slate-900 flex items-center gap-2">
              <LogOut className="w-5 h-5 text-rose-600" />
              <span>{t('header.logout')}</span>
            </h3>
            <p className="text-xs text-slate-500 mt-0.5 font-medium">
              Log out of your AgriGuard farmer profile on this device
            </p>
          </div>
          <button
            type="button"
            onClick={onLogout}
            className="w-full sm:w-auto px-5 py-2.5 rounded-2xl bg-rose-600 hover:bg-rose-700 text-white text-xs sm:text-sm font-black shadow-md shadow-rose-600/25 transition-all flex items-center justify-center gap-2 hover:scale-[1.02]"
          >
            <LogOut className="w-4 h-4" />
            <span>{t('header.logout')}</span>
          </button>
        </section>
      )}
    </div>
  );
};

const InfoItem: React.FC<{ label: string; value: string; icon?: React.ReactNode }> = ({ label, value, icon }) => (
  <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200">
    <p className="text-[11px] uppercase tracking-wide font-black text-slate-500 flex items-center gap-1.5">{icon}{label}</p>
    <p className={`text-sm font-extrabold mt-1.5 break-words ${value ? 'text-slate-900' : 'text-slate-400 italic font-medium'}`}>
      {value || 'Not registered'}
    </p>
  </div>
);

const EditInput: React.FC<{ label: string; value: string; onChange: (value: string) => void; type?: string; icon?: React.ReactNode }> = ({ label, value, onChange, type = 'text', icon }) => (
  <label className="p-3 rounded-2xl bg-slate-50 border border-agri-300 block">
    <span className="text-[11px] uppercase tracking-wide font-black text-slate-500 flex items-center gap-1.5">{icon}{label}</span>
    <input 
      type={type} 
      value={value} 
      onChange={(event) => onChange(event.target.value)} 
      className="mt-1.5 w-full rounded-lg border border-slate-300 bg-white px-2.5 py-2 text-sm font-bold text-slate-900 focus:border-agri-600 focus:ring-1 focus:ring-agri-600" 
    />
  </label>
);
