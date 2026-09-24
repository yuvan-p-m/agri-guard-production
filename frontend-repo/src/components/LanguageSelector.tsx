import React, { useState, useRef, useEffect } from 'react';
import { Globe, Check, ChevronDown } from 'lucide-react';
import { SUPPORTED_LANGUAGES, useAppTranslation } from '../i18n';

interface LanguageSelectorProps {
  className?: string;
  variant?: 'header' | 'modal' | 'pill';
}

export const LanguageSelector: React.FC<LanguageSelectorProps> = ({
  className = '',
  variant = 'header',
}) => {
  const { language, changeLanguage } = useAppTranslation();
  const [isOpen, setIsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const dropdownRef = useRef<HTMLDivElement>(null);

  const currentLang = SUPPORTED_LANGUAGES.find((l) => l.code === language) || SUPPORTED_LANGUAGES[0];

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const filteredLanguages = SUPPORTED_LANGUAGES.filter(
    (l) =>
      l.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      l.native.toLowerCase().includes(searchQuery.toLowerCase()) ||
      l.code.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleSelect = (code: string) => {
    changeLanguage(code);
    setIsOpen(false);
    setSearchQuery('');
  };

  return (
    <div className={`relative inline-block text-left ${className}`} ref={dropdownRef}>
      <button
        type="button"
        onClick={() => setIsOpen((prev) => !prev)}
        aria-haspopup="true"
        aria-expanded={isOpen}
        aria-label="Select Language"
        className={`flex items-center gap-1.5 rounded-xl border font-bold transition-all ${
          variant === 'pill'
            ? 'px-3 py-1.5 bg-white/80 border-agri-200 text-slate-800 shadow-sm hover:bg-white text-xs'
            : 'px-2.5 sm:px-3 py-1.5 bg-white/90 border-slate-200/90 text-slate-700 shadow-xs hover:border-agri-400 hover:text-agri-900 text-xs'
        }`}
      >
        <Globe className="w-3.5 h-3.5 text-agri-700 shrink-0" />
        <span className="max-w-[70px] sm:max-w-[90px] truncate">{currentLang.native}</span>
        <ChevronDown className={`w-3 h-3 text-slate-500 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {isOpen && (
        <div 
          className="absolute ltr:right-0 rtl:left-0 mt-2 w-64 max-h-80 overflow-hidden rounded-2xl border border-slate-200/90 bg-white/95 backdrop-blur-xl shadow-2xl z-[150] animate-fade-in flex flex-col"
        >
          {/* Search bar inside language dropdown */}
          <div className="p-2 border-b border-slate-100 bg-slate-50/70">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search 25 languages..."
              className="w-full px-2.5 py-1 text-xs rounded-lg border border-slate-200 bg-white text-slate-800 focus:outline-none focus:border-agri-600 text-start"
              autoFocus
            />
          </div>

          {/* Languages list */}
          <div className="overflow-y-auto max-h-64 p-1.5 divide-y divide-slate-100/60">
            {filteredLanguages.map((lang) => {
              const isSelected = lang.code === language;
              return (
                <button
                  key={lang.code}
                  type="button"
                  onClick={() => handleSelect(lang.code)}
                  className={`w-full flex items-center justify-between px-3 py-2 text-start rounded-xl text-xs transition-colors ${
                    isSelected
                      ? 'bg-agri-100/90 text-agri-900 font-extrabold'
                      : 'text-slate-700 hover:bg-slate-100/80 font-medium'
                  }`}
                >
                  <div className="flex flex-col">
                    <span className="font-bold text-[13px] leading-tight">{lang.native}</span>
                    <span className="text-[10px] text-slate-500">{lang.name}</span>
                  </div>
                  {isSelected && <Check className="w-3.5 h-3.5 text-agri-700 shrink-0 ms-2" />}
                </button>
              );
            })}
            {filteredLanguages.length === 0 && (
              <div className="p-3 text-center text-xs text-slate-400">No language found</div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
