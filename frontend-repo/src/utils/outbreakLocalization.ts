/**
 * Outbreak Foresight Localization Utilities (25 Languages)
 * Translates raw disease names, crop names, and recommended prevention actions across all 25 supported locales.
 */

export const CROP_NAMES_25: Record<string, Record<string, string>> = {
  citrus: {
    en: 'Citrus (Orange / Lemon)', ta: 'சிட்ரஸ் (எலுமிச்சை / நாரத்தை)', te: 'సిట్రస్ (నిమ్మ / నారింజ)', ml: 'സിട്രസ് (നാരങ്ങ / ഓറഞ്ച്)', kn: 'ಸಿಟ್ರಸ್ (ನಿಂಬೆ / ಕಿತ್ತಳೆ)',
    hi: 'नींबू वर्गीय (सिट्रस)', bn: 'লেবু জাতীয় (সাইট্রাস)', mr: 'सिट्रस (लिंबू / संत्री)', gu: 'લીંબુ વર્ગ (સાઇટ્રસ)', pa: 'ਨਿੰਬੂ ਜਾਤੀ (ਸਿਟਰਸ)',
    ur: 'سائٹرس (لیموں / مالٹا)', or: 'ଲେମ୍ବୁ ଜାତୀୟ (ସାଇଟ୍ରସ୍)', as: 'টেঙা জাতীয় (ছাইট্ৰাছ)', ne: 'कागती / सुन्तला वर्ग', si: 'පැඟිරි කුලය (දෙහි / දොඩම්)',
    ar: 'الحمضيات (البرتقال / الليمون)', fr: 'Agrumes (Orange / Citron)', es: 'Cítricos (Naranja / Limón)', pt: 'Ccitrinos (Laranja / Limão)', de: 'Zitrusfrüchte (Orange / Zitrone)',
    it: 'Agrumi (Arancia / Limone)', ru: 'Цитрусовые (Апельсин / Лимон)', ja: '柑橘類 (オレンジ / レモン)', ko: '감귤류 (오렌지 / 레몬)', zh: '柑橘类 (柑橘 / 柠檬)',
  },
  vegetables: {
    en: 'Vegetables', ta: 'காய்கறிகள்', te: 'కూరగాయలు', ml: 'പച്ചക്കറികൾ', kn: 'ತರಕಾರಿಗಳು',
    hi: 'सब्जियां', bn: 'শাকসবজি', mr: 'भाज्या', gu: 'શાકભાજી', pa: 'ਸਬਜ਼ੀਆਂ',
    ur: 'سبزیاں', or: 'ପନିପରିବା', as: 'শাক-পাচলি', ne: 'तरकारीहरू', si: 'එළවළු',
    ar: 'الخضروات', fr: 'Légumes', es: 'Verduras', pt: 'Legumes / Verduras', de: 'Gemüse',
    it: 'Verdure / Ortaggi', ru: 'Овощи', ja: '野菜類', ko: '채소류', zh: '蔬菜类',
  },
  tomato: {
    en: 'Tomato', ta: 'தக்காளி', te: 'టమోటా', ml: 'തക്കാളി', kn: 'ಟೊಮೆಟೊ',
    hi: 'टमाटर', bn: 'টমেটো', mr: 'टोमॅटो', gu: 'ટામેટાં', pa: 'ਟਮਾਟਰ',
    ur: 'ٹماٹر', or: 'ବିଲାତି ବାଇଗଣ', as: 'বিলাহী', ne: 'गोलभेंडा', si: 'තක්කාලි',
    ar: 'الطماطم', fr: 'Tomate', es: 'Tomate', pt: 'Tomate', de: 'Tomate',
    it: 'Pomodoro', ru: 'Томат', ja: 'トマト', ko: '토마토', zh: '番茄',
  },
  apple: {
    en: 'Apple', ta: 'ஆப்பிள்', te: 'యాపిల్', ml: 'ആപ്പിൾ', kn: 'ಸೇಬು',
    hi: 'सेब', bn: 'আপেল', mr: 'सफरचंद', gu: 'સફરજન', pa: 'ਸੇਬ',
    ur: 'سیب', or: 'ସେଓ', as: 'আপেল', ne: 'स्याउ', si: 'ඇපල්',
    ar: 'التفاح', fr: 'Pomme', es: 'Manzana', pt: 'Maçã', de: 'Apfel',
    it: 'Mela', ru: 'Яблоко', ja: 'りんご', ko: '사과', zh: '苹果',
  },
  potato: {
    en: 'Potato', ta: 'உருளைக்கிழங்கு', te: 'బంగాళాదుంప', ml: 'ഉരുളക്കിഴങ്ങ്', kn: 'ಆಲೂಗಡ್ಡೆ',
    hi: 'आलू', bn: 'আলু', mr: 'बटाटा', gu: 'બટાકા', pa: 'ਆਲੂ',
    ur: 'آلو', or: 'ଆଳୁ', as: 'আলু', ne: 'आलु', si: 'අර්තාපල්',
    ar: 'البطاطس', fr: 'Pomme de terre', es: 'Patata', pt: 'Batata', de: 'Kartoffel',
    it: 'Patata', ru: 'Картофель', ja: 'ジャガイモ', ko: '감자', zh: '马铃薯',
  },
  corn: {
    en: 'Corn (Maize)', ta: 'மக்காச்சோளம்', te: 'మొక్కజొన్న', ml: 'മക്കച്ചോളം', kn: 'ಮೆಕ್ಕೆಜೋಳ',
    hi: 'मक्का', bn: 'ভুট্টা', mr: 'मका', gu: 'મકાઈ', pa: 'ਮੱਕੀ',
    ur: 'مکئی', or: 'ମକା', as: 'মাকৈ', ne: 'मकै', si: 'ඉරිඟු',
    ar: 'الذرة', fr: 'Maïs', es: 'Maíz', pt: 'Milho', de: 'Mais',
    it: 'Mais', ru: 'Кукуруза', ja: 'トウモロコシ', ko: '옥수수', zh: '玉米',
  },
  grape: {
    en: 'Grapes', ta: 'திராட்சை', te: 'ద్రాక్ష', ml: 'മുന്തിരി', kn: 'ದ್ರಾಕ್ಷಿ',
    hi: 'अंगूर', bn: 'আঙ্গুর', mr: 'द्राक्षे', gu: 'દ્રાક્ષ', pa: 'ਅੰਗੂਰ',
    ur: 'انگور', or: 'ଅଙ୍ଗୁର', as: 'আঙুৰ', ne: 'अंगुर', si: 'මිදි',
    ar: 'العنب', fr: 'Raisin', es: 'Uvas', pt: 'Uvas', de: 'Trauben',
    it: 'Uva', ru: 'Виноград', ja: 'ブドウ', ko: '포도', zh: '葡萄',
  },
  pepper: {
    en: 'Bell Pepper / Capsicum', ta: 'குடைமிளகாய்', te: 'క్యాప్సికం / బెంగళూరు మిరప', ml: 'കാപ്സിക്കം', kn: 'ದಪ್ಪ ಮೆಣಸಿನಕಾಯಿ (ಕ್ಯಾಪ್ಸಿಕಂ)',
    hi: 'शिमला मिर्च', bn: 'ক্যাপসিকাম', mr: 'ढोबळी मिरची', gu: 'કેપ્સીકમ મરચાં', pa: 'ਸ਼ਿਮਲਾ ਮਿਰਚ',
    ur: 'شملہ مرچ', or: 'କ୍ୟାପସିକମ୍', as: 'কেপচিকাম', ne: 'भेडे खुर्सानी', si: 'මාළු මිරිස්',
    ar: 'الفلفل الحلو', fr: 'Poivron', es: 'Pimiento morrón', pt: 'Pimentão', de: 'Paprika',
    it: 'Peperone', ru: 'Болгарский перец', ja: 'ピーマン', ko: '피망', zh: '甜椒',
  },
  orange: {
    en: 'Orange (Citrus)', ta: 'ஆரஞ்சு', te: 'నారింజ', ml: 'ഓറഞ്ച്', kn: 'ಕಿತ್ತಳೆ',
    hi: 'संतरा / नारंगी', bn: 'কমলালেবু', mr: 'संत्रे', gu: 'સંતરાં', pa: 'ਸੰਤਰਾ',
    ur: 'مالٹا', or: 'କମଳା', as: 'কমলা', ne: 'सुन्तला', si: 'දොඩම්',
    ar: 'البرتقال', fr: 'Orange', es: 'Naranja', pt: 'Laranja', de: 'Orange',
    it: 'Arancia', ru: 'Апельсин', ja: 'オレンジ', ko: '오렌지', zh: '柑橘',
  },
  peach: {
    en: 'Peach', ta: 'பீச் பழம்', te: 'పీచ్ పండు', ml: 'പീച്ച്', kn: 'ಪೀಚ್ ಹಣ್ಣು',
    hi: 'आड़ू', bn: 'পীচ ফল', mr: 'सप्ताळू (पीच)', gu: 'પીચ ફળ', pa: 'ਆੜੂ',
    ur: 'آڑو', or: 'ପିଚ୍ ଫଳ', as: 'পীচ ফল', ne: 'आडू', si: 'පීච්',
    ar: 'الخوخ', fr: 'Pêche', es: 'Melocotón', pt: 'Pêssego', de: 'Pfirsich',
    it: 'Pesca', ru: 'Персик', ja: '桃', ko: '복숭아', zh: '桃子',
  },
  strawberry: {
    en: 'Strawberry', ta: 'ஸ்ட்ராபெரி', te: 'స్ట్రాబెర్రీ', ml: 'സ്ട്രോബെറി', kn: 'ಸ್ಟ್ರಾಬೆರಿ',
    hi: 'स्ट्रॉबेरी', bn: 'স্ট্রবেরি', mr: 'स्ट्रॉबेरी', gu: 'સ્ટ્રોબેરી', pa: 'ਸਟ੍ਰਾਬੇਰੀ',
    ur: 'اسٹرابیری', or: 'ଷ୍ଟ୍ରବେରୀ', as: 'ষ্ট্ৰবেৰী', ne: 'स्ट्रबेरी', si: 'ස්ට්‍රෝබෙරි',
    ar: 'الفراولة', fr: 'Fraise', es: 'Fresa', pt: 'Morango', de: 'Erdbeere',
    it: 'Fragola', ru: 'Клубника', ja: 'イチゴ', ko: '딸기', zh: '草莓',
  },
  rice: {
    en: 'Rice / Paddy', ta: 'நெல் / அரிசி', te: 'వరి / ధాన్యం', ml: 'നെല്ല് / അരി', kn: 'ಭತ್ತ / ಅಕ್ಕಿ',
    hi: 'धान / चावल', bn: 'ধান / চাল', mr: 'भात / धान', gu: 'ડાંગર / ચોખા', pa: 'ਝੋਨਾ / ਚੌਲ',
    ur: 'دھان / چاول', or: 'ଧାନ / ଚାଉଳ', as: 'ধান / চাউল', ne: 'धान / चामल', si: 'වී / සහල්',
    ar: 'الأرز', fr: 'Riz', es: 'Arroz', pt: 'Arroz', de: 'Reis',
    it: 'Riso', ru: 'Рис', ja: '水稲 / コメ', ko: '벼 / 쌀', zh: '水稻 / 大米',
  },
  wheat: {
    en: 'Wheat', ta: 'கோதுமை', te: 'గోధుమ', ml: 'ഗോതമ്പ്', kn: 'ಗೋಧಿ',
    hi: 'गेहूं', bn: 'গম', mr: 'गहू', gu: 'ઘઉં', pa: 'ਕਣਕ',
    ur: 'گندم', or: 'ଗହମ', as: 'গম', ne: 'गहुँ', si: 'තිරිඟු',
    ar: 'القمح', fr: 'Blé', es: 'Trigo', pt: 'Trigo', de: 'Weizen',
    it: 'Grano', ru: 'Пшеница', ja: '小麦', ko: '밀', zh: '小麦',
  },
  cotton: {
    en: 'Cotton', ta: 'பருத்தி', te: 'పత్తి', ml: 'പരുത്തി', kn: 'ಹತ್ತಿ',
    hi: 'कपास', bn: 'তুলা', mr: 'कापूस', gu: 'કપાસ', pa: 'ਕਪਾਹ',
    ur: 'کپاس', or: 'କପା', as: 'কপাহ', ne: 'कपास', si: 'කපු',
    ar: 'القطن', fr: 'Coton', es: 'Algodón', pt: 'Algodão', de: 'Baumwolle',
    it: 'Cotone', ru: 'Хлопок', ja: '綿花', ko: '목화', zh: '棉花',
  },
  sugarcane: {
    en: 'Sugarcane', ta: 'கரும்பு', te: 'చెరకు', ml: 'കരിമ്പ്', kn: 'ಕಬ್ಬು',
    hi: 'गन्ना', bn: 'আখ', mr: 'ऊस', gu: 'શેરડી', pa: 'ਗੰਨਾ',
    ur: 'گنا', or: 'ଆଖୁ', as: 'কুঁহিয়াৰ', ne: 'उखु', si: 'උක්',
    ar: 'قصب السكر', fr: 'Canne à sucre', es: 'Caña de azúcar', pt: 'Cana-de-açúcar', de: 'Zuckerrohr',
    it: 'Canna da zucchero', ru: 'Сахарный тростник', ja: 'サトウキビ', ko: '사탕수수', zh: '甘蔗',
  },
  soybean: {
    en: 'Soybean', ta: 'சோயாபீன்', te: 'సోయాబీన్', ml: 'സോയാബീൻ', kn: 'ಸೋಯಾಬೀನ್',
    hi: 'सोयाबीन', bn: 'সয়াবিন', mr: 'सोयाबीन', gu: 'સોયાબીન', pa: 'ਸੋਇਆਬੀਨ',
    ur: 'سویا بین', or: 'ସୋୟାବିନ୍', as: 'ছয়াবিন', ne: 'भटमास', si: 'සෝයා බෝංචි',
    ar: 'فول الصويا', fr: 'Soja', es: 'Soja', pt: 'Soja', de: 'Sojabohne',
    it: 'Soia', ru: 'Соя', ja: '大豆', ko: '대두 (콩)', zh: '大豆',
  },
  onion: {
    en: 'Onion', ta: 'வெங்காயம்', te: 'ఉల్లిపాయ', ml: 'സവാള / ഉള്ളി', kn: 'ಈರುಳ್ಳಿ',
    hi: 'प्याज', bn: 'পেঁয়াজ', mr: 'कांदा', gu: 'ડુંગળી', pa: 'ਪਿਆਜ਼',
    ur: 'پیاز', or: 'ପିଆଜ', as: 'পিয়াঁজ', ne: 'प्याज', si: 'ලූනු',
    ar: 'البصل', fr: 'Oignon', es: 'Cebolla', pt: 'Cebola', de: 'Zwiebel',
    it: 'Cipolla', ru: 'Лук', ja: '玉ねぎ', ko: '양파', zh: '洋葱',
  },
  banana: {
    en: 'Banana', ta: 'வாழை', te: 'అరటి', ml: 'വാഴ', kn: 'ಬಾಳೆ',
    hi: 'केला', bn: 'কলা', mr: 'केळी', gu: 'કેળાં', pa: 'ਕੇਲਾ',
    ur: 'کیلا', or: 'କଦଳୀ', as: 'কল', ne: 'केरा', si: 'කෙසෙල්',
    ar: 'الموز', fr: 'Banane', es: 'Plátano / Banano', pt: 'Banana', de: 'Banane',
    it: 'Banana', ru: 'Банан', ja: 'バナナ', ko: '바나나', zh: '香蕉',
  },
  mango: {
    en: 'Mango', ta: 'மாம்பழம்', te: 'మామిడి', ml: 'മാങ്ങ', kn: 'ಮಾವಿನ ಹಣ್ಣು',
    hi: 'आम', bn: 'আম', mr: 'आंबा', gu: 'કેરી', pa: 'ਅੰਬ',
    ur: 'آم', or: 'ଆମ୍ବ', as: 'আম', ne: 'Category आम', si: 'අඹ',
    ar: 'المانجو', fr: 'Mangue', es: 'Mango', pt: 'Manga', de: 'Mango',
    it: 'Mango', ru: 'Манго', ja: 'マンゴー', ko: '망고', zh: '芒果',
  }
};

export const DISEASE_TRANSLATIONS: Record<string, Record<string, string>> = {
  early_blight: {
    en: 'Early Blight (Alternaria solani)', ta: 'ஆரம்பகால கருகல் நோய் (Early Blight)', te: 'ముందస్తు తెగులు (Early Blight)', ml: 'ആദ്യകാല ബ്ലൈറ്റ് (Early Blight)',
    kn: 'ಮುಂಚಿನ ಕರಗು ರೋಗ (Early Blight)', hi: 'अगेती झुलसा रोग (Early Blight)', bn: 'আগেতি ধসা রোগ', mr: 'लवकर येणारा करपा',
    gu: 'અગેતી સુકારો', pa: 'ਅਗੇਤਾ ਝੁਲਸਾ ਰੋਗ', ur: 'ارلی بلائٹ', or: 'ଆଗୁଆ ପତ୍ରପୋଡ଼ା ରୋଗ',
    as: 'আগতীয়া ব্লাইট ৰোগ', ne: 'अगेती डढुवा', si: 'මුල් අංගමාරය', ar: 'اللفحة المبكرة',
    fr: 'Brûlure alternarienne', es: 'Tizón temprano', pt: 'Pinta-preta', de: 'Dürrfleckenkrankheit',
    it: 'Alternariosi', ru: 'Ранний фитофтороз', ja: '輪紋病 (Early Blight)', ko: '조기 역병', zh: '早疫病'
  },
  late_blight: {
    en: 'Late Blight (Phytophthora infestans)', ta: 'பின்கால கருகல் நோய் (Late Blight)', te: 'ఆలస్యపు తెగులు (Late Blight)', ml: 'പിൽക്കാല ബ്ലൈറ്റ് (Late Blight)',
    kn: 'ತಡವಾದ ಕರಗು ರೋಗ (Late Blight)', hi: 'पछेती झुलसा रोग (Late Blight)', bn: 'নাবী ধসা রোগ', mr: 'उशिरा येणारा करपा',
    gu: 'પાછોતરો સુકારો', pa: 'ਪਛੇਤਾ ਝੁਲਸਾ ਰੋਗ', ur: 'لیٹ بلائٹ', or: 'ପଛୁଆ ପତ୍ରପୋଡ଼ା ରୋଗ',
    as: 'পানী ব্লাইট ৰোগ', ne: 'पछेती डढुवा', si: 'පසු අංගමාරය', ar: 'اللفحة المتأخرة',
    fr: 'Mildiou', es: 'Tizón tardío', pt: 'Requeima', de: 'Kraut- und Knollenfäule',
    it: 'Peronospora', ru: 'Поздний фитофтороз', ja: '疫病 (Late Blight)', ko: '후기 역병', zh: '晚疫病'
  },
  bacterial_spot: {
    en: 'Bacterial Spot', ta: 'பாக்டீரியா இலைப்புள்ளி நோய்', te: 'బాక్టీరియల్ మచ్చల తెగులు', ml: 'ബാക്ടീരിയൽ സ്പോട്ട്',
    kn: 'ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ ರೋಗ', hi: 'जीवाणु धब्बा रोग (Bacterial Spot)', bn: 'ব্যাকটেরিয়াজনিত দাগ', mr: 'जिवाणू ठिपके रोग',
    gu: 'જીવાણુજન્ય ટપકાં', pa: 'ਜੀਵਾਣੂ ਧੱਬਾ ਰੋਗ', ur: 'بیکٹیریل سپاٹ', or: 'ଜୀବାଣୁ ଦାଗ ରୋଗ',
    as: 'বেক্টেৰিয়াজনিত দাগ ৰোগ', ne: 'ब्याक्टेरियल दाग', si: 'බැක්ටීරියා ලප රෝගය', ar: 'التبقع البكتيري',
    fr: 'Gale bactérienne', es: 'Mancha bacteriana', pt: 'Mancha bacteriana', de: 'Bakterienfleckenkrankheit',
    it: 'Maculatura batterica', ru: 'Бактериальная пятнистость', ja: '斑点細菌病', ko: '세균성 점무늬병', zh: '细菌性斑点病'
  },
  cedar_apple_rust: {
    en: 'Cedar Apple Rust', ta: 'சிடார் ஆப்பிள் துரு நோய்', te: 'సీడార్ యాపిల్ తుప్పు తెగులు', ml: 'സിഡാർ ആപ്പിൾ തുരുമ്പ് രോഗം',
    kn: 'ಸಿಡಾರ್ ಆಪಲ್ ತುಕ್ಕು ರೋಗ', hi: 'सीडर एप्पल रतुआ रोग', bn: 'সিডার আপেল মরিচা রোগ', mr: 'सिडार ॲपल तांबेरा रोग',
    gu: 'સીડાર એપલ ગેરુ રોગ', pa: 'ਸੀਡਰ ਸੇਬ ਕੁੰਗੀ ਰੋਗ', ur: 'سیڈار سیب زنگ', or: 'ସିଡାର ଆପଲ କଳଙ୍କି ରୋଗ',
    as: 'চিডাৰ আপেল মামৰ ৰোগ', ne: 'सिडार स्याउ सिन्दुरे रोग', si: 'සීඩාර් ඇපල් මලකඩ රෝගය', ar: 'صدأ أرز التفاح',
    fr: 'Rouille du genévrier et du pommier', es: 'Roya del manzano y cedro', pt: 'Ferrugem do cedro-maçã', de: 'Zedern-Apfel-Rost',
    it: 'Ruggine del melo', ru: 'Ржавчина яблони', ja: '赤星病 (Cedar Apple Rust)', ko: '붉은별무늬병', zh: '苹果雪松锈病'
  },
  root_rot: {
    en: 'Root Rot / Damping-Off (Pythium / Rhizoctonia)', ta: 'வேர் அழுகல் / நாற்று அழுகல் நோய்', te: 'వేరు కుళ్ళు / నారు కుళ్ళు తెగులు', ml: 'വേരുചീയൽ / തൈചീയൽ രോഗം',
    kn: 'ಬೇರು ಕೊಳೆತ / ಸಸಿ ಕೊಳೆತ ರೋಗ', hi: 'जड़ गलन / आद्र गलन रोग', bn: 'শিকড় পচা / চারা ধসা রোগ', mr: 'मूळ कुज / मर रोग',
    gu: 'મૂળનો સડો / સુકારો', pa: 'ਜੜ੍ਹ ਗਲਣ ਰੋਗ', ur: 'جڑ گلن / پودا سڑن بیماری', or: 'ଚେର ପଚା / ଚାରା ପଚା ରୋଗ',
    as: 'শিপা পচা / পুলি পচা ৰোগ', ne: 'जरा कुहिने / डढुवा रोग', si: 'මුල් කුණුවීමේ රෝගය', ar: 'تعفن الجذور وموت البادرات',
    fr: 'Pourriture racinaire / Fonte des semis', es: 'Podredumbre de la raíz / Marchitamiento', pt: 'Podridão radicular / Tombamento', de: 'Wurzelfäule / Umfallkrankheit',
    it: 'Marciume radicale', ru: 'Корневая гниль / Полегание сеянцев', ja: '根腐れ病・苗立枯病', ko: '뿌리썩음병 / 잘록병', zh: '根腐病 / 猝倒病'
  },
  black_rot: {
    en: 'Black Rot', ta: 'கருப்பு அழுகல் நோய்', te: 'నల్ల కుళ్ళు తెగులు', ml: 'കറുത്ത ചീയൽ രോഗം',
    kn: 'ಕಪ್ಪು ಕೊಳೆತ ರೋಗ', hi: 'काला सड़न रोग (Black Rot)', bn: 'কালো পচা রোগ', mr: 'काळा कुजवा रोग',
    gu: 'કાળો સડો', pa: 'ਕਾਲਾ ਗਲਣ ਰੋਗ', ur: 'سیاہ سڑن بیماری', or: 'କଳା ପଚା ରୋଗ',
    as: 'কলা পচা ৰোগ', ne: 'कालो कुहिने रोग', si: 'කළු කුණුවීම', ar: 'العفن الأسود',
    fr: 'Pourriture noire', es: 'Podredumbre negra', pt: 'Podridão-negra', de: 'Schwarzfäule',
    it: 'Marciume nero', ru: 'Черная гниль', ja: '黒腐病 (Black Rot)', ko: '검은썩음병', zh: '黑腐病'
  },
  apple_scab: {
    en: 'Apple Scab', ta: 'ஆப்பிள் செதில் நோய்', te: 'యాపిల్ పొలుசு తెగులు', ml: 'ஆപ്പിൾ സ്കാബ് രോഗം',
    kn: 'ಸೇಬು ಹುರುಪು ರೋಗ (Scab)', hi: 'सेब स्कैब / पपड़ी रोग', bn: 'আপেল স্ক্যাব রোগ', mr: 'सफरचंद खपली रोग',
    gu: 'સફરજન ખસ રોગ', pa: 'ਸੇਬ ਸਕੈਬ ਰੋਗ', ur: 'سیب اسکیب', or: 'ସେଓ ଖାସୁ ରୋଗ',
    as: 'আপেল স্কেব ৰোগ', ne: 'स्याउ काले पोते रोग', si: 'ඇපල් කබොලු රෝගය', ar: 'جرب التفاح',
    fr: 'Tavelure du pommier', es: 'Sarna del manzano', pt: 'Sarna da maçã', de: 'Apfelschorf',
    it: 'Ticchiolatura del melo', ru: 'Парша яблони', ja: '黒星病 (Apple Scab)', ko: '검은별무늬병', zh: '苹果黑星病'
  },
  powdery_mildew: {
    en: 'Powdery Mildew', ta: 'சாம்பல் நோய்', te: 'బూడిద తెగులు', ml: 'പൊടിപ്പൂപ്പ് രോഗം',
    kn: 'ಬೂದಿ ರೋಗ', hi: 'चूर्णिल आसिता (पाउडरी मिल्ड्यू)', bn: 'পাউডারি মিলডিউ', mr: 'भुरी रोग',
    gu: 'છાશિયો રોગ', pa: 'ਪਾਊਡਰੀ ਫ਼ਫ਼ੂੰਦੀ', ur: 'پاؤڈری پھپھوندی', or: 'ପାଉଡରି ମିଲଡ୍ୟୁ',
    as: 'পাউদাৰী মিলডিউ', ne: 'धुलो ढुसी', si: 'පිටි පුස් රෝගය', ar: 'البياض الدقيقي',
    fr: 'Oïdium', es: 'Oídio', pt: 'Oídio', de: 'Echter Mehltau',
    it: 'Oidio', ru: 'Мучнистая роса', ja: 'うどんこ病', ko: '흰가루병', zh: '白粉病'
  },
  yellow_leaf_curl: {
    en: 'Yellow Leaf Curl Virus', ta: 'மஞ்சள் இலை சுருள் வைரஸ்', te: 'పసుపు ఆకు ముడుత వైరస్', ml: 'മഞ്ഞ ഇലച്ചുരുൾ വൈറസ്',
    kn: 'ಹಳದಿ ಎಲೆ ಸುರುಳಿ ವೈರಸ್', hi: 'पीली पत्ती मरोड़ विषाणु', bn: 'হলুদ পাতা কোঁকড়ানো ভাইরাস', mr: 'पिवळा पर्णगुच्छ विषाणू',
    gu: 'પીળા પાન કુકડાઈ વાયરસ', pa: 'ਪੀਲਾ ਪੱਤਾ ਮਰੋੜ ਵਿਸ਼ਾਣੂ', ur: 'پیلا پتا مروڑ وائرس', or: 'ହଳଦିଆ ପତ୍ର କୁଞ୍ଚନ ଭୂତାଣୁ',
    as: 'হালধীয়া পাত কেঁকোৰা ভাইৰাছ', ne: 'पहेंलो पात खुम्चिने भाइरस', si: 'කහ පත්‍ර කොඩවීම් වෛරසය', ar: 'فيروس تجعد أوراق الطماطم الصفراء',
    fr: 'Virus des feuilles jaunes en cuillère', es: 'Virus del rizado amarillo', pt: 'Vírus do enrolamento amarelo', de: 'Gelbblättrigkeit-Virus',
    it: 'Virus dell\'accartocciamento fogliare giallo', ru: 'Вирус желтой курчавости листьев', ja: '黄化葉巻ウイルス', ko: '황화잎말림바이러스', zh: '黄化曲叶病毒'
  },
  haunglongbing: {
    en: 'Huanglongbing (Citrus Greening)', ta: 'சிட்ரஸ் கிரீனிங் நோய் (HLB)', te: 'సిట్రస్ గ్రీనింగ్ తెగులు (HLB)', ml: 'സിട്രസ് ഗ്രീനിംഗ് രോഗം',
    kn: 'ಸಿಟ್ರಸ್ ಹಳದಿ ಗ್ರೀನಿಂಗ್ ರೋಗ (HLB)', hi: 'सिट्रस ग्रीनिंग रोग (HLB)', bn: 'লেবুর গ্রিনিং রোগ', mr: 'सिट्रस ग्रीनिंग रोग',
    gu: 'સિટ્રસ ગ્રીનિંગ રોગ', pa: 'ਸਿਟਰਸ ਗ੍ਰੀਨਿੰਗ ਰੋਗ', ur: 'سٹرس گریننگ بیماری', or: 'ଲେମ୍ବୁ ଗ୍ରୀନିଂ ରୋଗ',
    as: 'টেঙা গ্ৰীনিং ৰোগ', ne: 'कागती ग्रिनिङ रोग', si: 'දෙහි කොළවීම් රෝගය', ar: 'اخضرار الحمضيات (HLB)',
    fr: 'Huanglongbing / Greening des agrumes', es: 'Huanglongbing (Greening)', pt: 'Huanglongbing (Greening)', de: 'Citrus Greening (HLB)',
    it: 'Inverdimento degli agrumi (HLB)', ru: 'Озеленение цитрусовых (Хуанлунбин)', ja: 'カンキツグリーニング病 (HLB)', ko: '감귤 녹화병 (HLB)', zh: '柑橘黄龙病'
  },
  cercospora_leaf_spot: {
    en: 'Cercospora Leaf Spot (Gray Leaf Spot)', ta: 'செர்கோஸ்போரா சாம்பல் இலைப்புள்ளி நோய்', te: 'సెర్కోస్పోరా బూడిద రంగు ఆకు మచ్చ తెగులు', ml: 'സെർക്കോസ്പോറ ചാരനിറ ഇലപ്പുള്ളി',
    kn: 'ಸೆರ್ಕೋಸ್ಪೊರಾ ಬೂದು ಎಲೆ ಕಲೆ ರೋಗ', hi: 'सर्कोस्पोरा धूसर पत्ती धब्बा रोग', bn: 'সারকোস্পোরা ধূসর পাতা দাগ রোগ', mr: 'सर्कोस्पोरा करडा पानावरील ठिपके',
    gu: 'સર્કોસ્પોરા રાખોડી ટપકાં રોગ', pa: 'ਸਰਕੋਸਪੋਰਾ ਸਲੇਟੀ ਪੱਤਾ ਧੱਬਾ ਰੋਗ', ur: 'سرکوسپورا سرمئی پتا دھبہ', or: 'ସରକୋସ୍ପୋରା ଧୂସର ପତ୍ର ଦାଗ ରୋଗ',
    as: 'চাৰ্কোস্পোৰা ধূসৰ পাতৰ দাগ', ne: 'सर्कोस्पोरा खैरो पातको दाग', si: 'සර්කොස්පෝරා අළු පත්‍ර ලප රෝගය', ar: 'تبقع الأوراق السركسبوري',
    fr: 'Cercosporiose / Taches grises', es: 'Mancha gris por Cercospora', pt: 'Cercosporiose', de: 'Cercospora-Blattflecken',
    it: 'Cercosporiosi fogliare', ru: 'Церкоспороз листьев', ja: '褐斑病・灰色斑点病', ko: '점무늬병 (세르코스포라)', zh: '尾孢菌灰叶斑病'
  },
  septoria_leaf_spot: {
    en: 'Septoria Leaf Spot', ta: 'செப்டோரியா இலைப்புள்ளி நோய்', te: 'సెప్టోరియా ఆకు మచ్చ తెగులు', ml: 'സെപ്റ്റോറിയ ഇലപ്പുള്ളി രോഗം',
    kn: 'ಸೆಪ್ಟೋರಿಯಾ ಎಲೆ ಕಲೆ ರೋಗ', hi: 'सेप्टोरिया पत्ती धब्बा रोग', bn: 'সেপ্টোরিয়া পাতা দাগ রোগ', mr: 'सेप्टोरिया पानावरील ठिपके',
    gu: 'સેપ્ટોરિયા પાન ટપકાં રોગ', pa: 'ਸੈਪਟੋਰੀਆ ਪੱਤਾ ਧੱਬਾ ਰੋਗ', ur: 'سیپٹوریا پتا دھبہ', or: 'ସେପ୍ଟୋରିଆ ପତ୍ର ଦାଗ ରୋଗ',
    as: 'চেপ্টোৰিয়া পাতৰ দাগ ৰোগ', ne: 'सेप्टोरिया पातको दाग', si: 'සෙප්ටෝරියා පත්‍ර ලප රෝගය', ar: 'تبقع الأوراق السبتوري',
    fr: 'Septoriose', es: 'Mancha foliar por Septoria', pt: 'Septoriose', de: 'Septoria-Blattflecken',
    it: 'Settoriosi', ru: 'Септориоз листьев', ja: '斑点病 (Septoria)', ko: '점무늬병 (셉토리아)', zh: '壳针孢叶斑病'
  },
  spider_mites: {
    en: 'Spider Mites / Two-Spotted Spider Mite', ta: 'செம்பேன் / சிலந்திப் பூச்சி தாக்குதல்', te: 'ఎర్ర నల్లి / బూడిద పురుగు దాడి', ml: 'ചുവന്ന മണ്ഡരി ബാധ',
    kn: 'ಕೆಂಪು ಜೇಡ ನುಸಿ ಬಾಧೆ', hi: 'लाल मकड़ी / माइट्स का प्रकोप', bn: 'লাল মাকড়সা / স্পাইডার মাইট', mr: 'लाल कोळी / माइट्सचा प्रादुर्भाव',
    gu: 'લાલ કથીરી / સ્પાઈડર માઈટ્સ', pa: 'ਲਾਲ ਮੱਕੜੀ ਦਾ ਹਮਲਾ', ur: 'مکڑی کا جالا / مائٹس', or: 'ନାଲି ବୁଢ଼ିଆଣୀ କୀଟ ଆକ୍ରମଣ',
    as: 'ৰঙা মকৰা পোকৰ আক্ৰমণ', ne: 'रातो सुलसुले', si: 'රතු මයිටාවන්ගේ හානිය', ar: 'العنكبوت الأحمر ذو النقطتين',
    fr: 'Tétranyque tisserand (Araignée rouge)', es: 'Araña roja (Ácaros)', pt: 'Ácaro-rajado', de: 'Spinnmilben (Rote Spinne)',
    it: 'Ragnetto rosso', ru: 'Паутинный клещ', ja: 'ハダニ類・ナミハダニ', ko: '점박이응애', zh: '二斑叶螨 (红蜘蛛)'
  },
  target_spot: {
    en: 'Target Spot (Corynespora)', ta: 'இலக்கு புள்ளி நோய் (Target Spot)', te: 'టార్గెట్ స్పాట్ తెగులు', ml: 'ടാർഗെറ്റ് സ്പോട്ട് രോഗം',
    kn: 'ಟಾರ್ಗೆಟ್ ಸ್ಪಾಟ್ ಎಲೆ ರೋಗ', hi: 'टारगेट स्पॉट रोग', bn: 'টার্গেট স্পট রোগ', mr: 'टार्गेट स्पॉट रोग',
    gu: 'ટાર્ગેટ સ્પોટ રોગ', pa: 'ਟਾਰਗੇਟ ਸਪਾਟ ਰੋਗ', ur: 'ٹارگٹ سپاٹ', or: 'ଟାର୍ଗେଟ୍ ସ୍ପଟ୍ ରୋଗ',
    as: 'টাৰ্গেট স্পট ৰোগ', ne: 'टार्गेट स्पट रोग', si: 'ඉලක්ක ලප රෝගය', ar: 'تبقع الأوراق الهدفي',
    fr: 'Taches cibles (Corynespora)', es: 'Mancha focal (Target spot)', pt: 'Mancha-alvo', de: 'Target-Spot-Krankheit',
    it: 'Maculatura bersaglio', ru: 'Мишеневидная пятнистость', ja: '標的斑点病', ko: '타겟스팟 (과녁무늬병)', zh: '靶斑病'
  },
  leaf_mold: {
    en: 'Leaf Mold (Passalora fulva)', ta: 'இலை பூஞ்சை காளான் நோய்', te: 'ఆకు బూజు తెగులు', ml: 'ഇല പൂപ്പൽ രോഗം',
    kn: 'ಎಲೆ ಬೂజు ರೋಗ (Leaf Mold)', hi: 'पत्ती फफूंद रोग (लीफ मोल्ड)', bn: 'পাতা ছত্রাক রোগ', mr: 'पानावरील बुरशी रोग',
    gu: 'પાન ફૂગ રોગ', pa: 'ਪੱਤਾ ਉੱਲੀ ਰੋਗ', ur: 'پتے کی پھپھوندی', or: 'ପତ୍ର ଫିମ୍ପି ରୋଗ',
    as: 'পাতৰ ভেঁকুৰ ৰোগ', ne: 'पातको ढुसी रोग', si: 'පත්‍ර පුස් රෝගය', ar: 'عفن الأوراق الفطري',
    fr: 'Cladosporiose de la tomate', es: 'Moho de la hoja', pt: 'Mofo-das-folhas', de: 'Samtfleckenkrankheit',
    it: 'Muffa delle foglie', ru: 'Бурая пятнистость (Листовая плесень)', ja: '葉かび病', ko: '잎곰팡이병', zh: '叶霉病'
  },
  rust: {
    en: 'Rust Disease', ta: 'துரு நோய்', te: 'తుప్పు తెగులు', ml: 'തുരുമ്പ് രോഗം',
    kn: 'ತುಕ್ಕು ರೋಗ', hi: 'गेरुआ / रतुआ रोग', bn: 'মরিচা রোগ', mr: 'तांबेरा रोग',
    gu: 'ગેરુ રોગ', pa: 'ਕੁੰਗੀ ਰੋਗ', ur: 'رتوا / کنگی', or: 'କଳଙ୍କି ରୋଗ',
    as: 'মামৰ ৰোগ', ne: 'सिन्दुरे रोग', si: 'මලකඩ රෝගය', ar: 'مرض صدأ النبات',
    fr: 'Maladie de la rouille', es: 'Roya', pt: 'Ferrugem', de: 'Rostkrankheit',
    it: 'Ruggine', ru: 'Ржавчина растений', ja: 'さび病', ko: '녹병', zh: '锈病'
  },
  healthy: {
    en: 'Healthy Foliage', ta: 'ஆரோக்கியமான இலை', te: 'ఆరోగ్యకరమైన ఆకు', ml: 'ആരോഗ്യമുള്ള ഇല',
    kn: 'ಆರೋಗ್ಯಕರ ಎಲೆ', hi: 'स्वस्थ पत्ता', bn: 'সুস্থ পাতা', mr: 'निरोगी पान',
    gu: 'તંદુરસ્ત પાન', pa: 'ਸਿਹਤਮੰਦ ਪੱਤਾ', ur: 'صحت مند پتا', or: 'ସୁସ୍ଥ ପତ୍ର',
    as: 'সুস্থ পাত', ne: 'स्वस्थ पात', si: 'නිරෝගී පත්‍ර', ar: 'أوراق سليمة',
    fr: 'Feuillage sain', es: 'Follaje sano', pt: 'Folhagem saudável', de: 'Gesundes Blattwerk',
    it: 'Fogliame sano', ru: 'Здоровая листва', ja: '健全な葉', ko: '건강한 잎', zh: '健康叶片'
  }
};

export const PREVENTIVE_ACTIONS_TEMPLATES: Record<string, string[]> = {
  en: [
    'Apply prophylactic bio-fungicide (Trichoderma viride @ 5g/L or Pseudomonas fluorescens) before spore settlement on {crop}.',
    'Optimize canopy aeration and prune lower infected foliage to reduce local micro-climate relative humidity.',
    'Avoid overhead sprinkler irrigation during late evening; switch to drip to minimize leaf wetness duration.',
    'Inspect field borders adjacent to recent community disease detections for early necrotic lesions.',
    'Maintain balanced potassium (K) nutrition to strengthen plant epidermal cell walls against fungal penetration.'
  ],
  ta: [
    '{crop} பயிரில் வித்திகள் படிவதற்கு முன் தடுப்பு உயிரியல் பூஞ்சாணக்கொல்லியை (டிரைக்கோடெர்மா விரிடி @ 5g/L அல்லது சூடோமோனாஸ்) தெளிக்கவும்.',
    'நுண்-காலநிலை ஈரப்பதத்தைக் குறைக்க கீழ்மட்ட பாதிக்கப்பட்ட இலைகளை கவாத்து செய்து காற்று சுழற்சியை மேம்படுத்தவும்.',
    'மாலை நேரங்களில் தெளிப்பு நீர்ப்பாசனத்தைத் தவிர்க்கவும்; இலைகள் ஈரமாக இருக்கும் நேரத்தைக் குறைக்க சொட்டு நீர்ப்பாசனத்திற்கு மாறவும்.',
    'சமீபத்தில் நோய் கண்டறியப்பட்ட அருகிலுள்ள எல்லைப் பயிர்களை ஆரம்பகால புள்ளிகளுக்காக கண்காணிக்கவும்.',
    'பூஞ்சாணங்கள் ஊடுருவுவதைத் தடுத்து தாவர செல் சுவர்களை வலுப்படுத்த சீரான பொட்டாசியம் (K) உரமிடுங்கள்.'
  ],
  te: [
    '{crop} పై బీజాంశాలు చేరకముందే నివారణ బయో-ఫంగిసైడ్ (ట్రైకోడెర్మా విరిడే @ 5g/L లేదా సూడోమోనాస్ ఫ్లోరోసెన్స్) పిచికారీ చేయండి.',
    'క్షేత్రంలో తేమను తగ్గించడానికి క్రింది వ్యాధిగ్రస్త ఆకులను తొలగించి గాలి ప్రసరణను మెరుగుపరచండి.',
    'సాయంత్రం వేళల్లో తుంపర సేద్యాన్ని నివారించండి; ఆకులు తడిగా ఉండే సమయాన్ని తగ్గించడానికి బిందు సేద్యం (డ్రిప్) ఉపయోగించండి.',
    'ఇటీవల వ్యాధి సోకిన పొరుగు సరిహద్దు పొలాలను ముందస్తు మచ్చల కోసం నిశితంగా పరిశీలించండి.',
    'శిలీంధ్రాల దాడిని తట్టుకోవడానికి మరియు మొక్కల కణ నిర్మాణాన్ని బలోపేతం చేయడానికి సమతుల్య పొటాషియం (K) అందించండి.'
  ],
  ml: [
    '{crop} വിളകളിൽ രോഗാണുക്കൾ പടരുന്നതിന് മുമ്പ് ജൈവ കുമിൾനാശിനി (ട്രൈക്കോഡെർമ വിരിഡെ @ 5g/L അല്ലെങ്കിൽ സ്യൂഡോമോണസ് ഫ്ലൂറസെൻസ്) തളിക്കുക.',
    'ഈർപ്പം കുറയ്ക്കുന്നതിനായി അടിഭാഗത്തെ രോഗബാധിത ഇലകൾ മുറിച്ചുമാറ്റി വായുസഞ്ചാരം ഉറപ്പാക്കുക.',
    'വൈകുന്നേരങ്ങളിൽ സ്പ്രിംഗ്ലർ നന ഒഴിവാക്കുക; ഇലകളിലെ ഈർപ്പം കുറയ്ക്കാൻ തുള്ളിനന രീതിയിലേക്ക് മാറുക.',
    'സമീപ പ്രദേശങ്ങളിൽ രോഗം റിപ്പോർട്ട് ചെയ്തതിനാൽ പാടത്തിന്റെ അതിരുകൾ പരിശോധിച്ച് ലക്ഷണങ്ങൾ കണ്ടെത്തുക.',
    'കുമിൾ ബാധയെ പ്രതിരോധിക്കാൻ സസ്യങ്ങളുടെ കോശഭിത്തികൾ ശക്തിപ്പെടുത്തുന്നതിന് ആവശ്യമായ പൊട്ടാസ്യം (K) നൽകുക.'
  ],
  kn: [
    '{crop} ಮೇಲೆ ರೋಗಾಣು ಬೀಜಾಣುಗಳು ನೆಲೆಗೊಳ್ಳುವ ಮುನ್ನ ರಕ್ಷಣಾತ್ಮಕ ಜೈವಿಕ ಶಿಲೀಂಧ್ರನಾಶಕ (ಟ್ರೈಕೋಡರ್ಮಾ ವಿರಿಡೆ @ 5g/L ಅಥವಾ ಸ್ಯೂಡೋಮೊನಾಸ್ ಫ್ಲೋರೆಸೆನ್ಸ್) ಸಿಂಪಡಿಸಿ.',
    'ಕ್ಷೇತ್ರದ ಸೂಕ್ಷ್ಮ ಹವಾಮಾನ ತೇವಾಂಶವನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಕೆಳಗಿನ ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ಮತ್ತು ಗಾಳಿಯಾಡುವಿಕೆಯನ್ನು ಸುಧಾರಿಸಿ.',
    'ಸಂಜೆ ವೇಳೆಯಲ್ಲಿ ಮೇಲಿಂದ ತುಂತುರು ನೀರಾವರಿ ನೀಡುವುದನ್ನು ತಪ್ಪಿಸಿ; ಎಲೆಗಳ ತೇವಾಂಶದ ಸಮಯ ತಗ್ಗಿಸಲು ಹನಿ ನೀರಾವರಿಗೆ ಬದಲಾಯಿಸಿ.',
    'ಇತ್ತೀಚಿನ ಸಮುದಾಯ ರೋಗ ಪತ್ತೆಯಾದ ನೆರೆಯ ಜಮೀನಿನ ಗಡಿಗಳನ್ನು ಆರಂಭಿಕ ಕಲೆಗಳಿಗಾಗಿ ಪರಿಶೀಲಿಸಿ.',
    'ಶಿಲೀಂಧ್ರಗಳ ಒಳನುಗ್ಗುವಿಕೆಯನ್ನು ತಡೆಯಲು ಮತ್ತು ಗಿಡದ ಕೋಶಗಳ ಗೋಡೆಯನ್ನು ಬಲಪಡಿಸಲು ಸಮತೋಲಿತ ಪೊಟ್ಯಾಶಿಯಮ್ (K) ಪೋಷಕಾಂಶ ನೀಡಿ.'
  ],
  hi: [
    '{crop} पर बीजाणु बैठने से पहले निवारक जैव-कवकनाशी (ट्राइकोडर्मा विरिडे @ 5g/L या स्यूडोमोनास फ्लोरेसेंस) का छिड़काव करें।',
    'सूक्ष्म जलवायु की आर्द्रता कम करने के लिए निचली संक्रमित पत्तियों की छंटाई करें और वायु संचार में सुधार करें।',
    'देर शाम को ऊपर से फव्वारा सिंचाई से बचें; पत्तियों के गीले रहने की अवधि कम करने के लिए ड्रिप सिंचाई अपनाएं।',
    'हाल के सामुदायिक रोग प्रकोप वाले नजदीकी खेतों की सीमाओं पर शुरुआती धब्बों की निगरानी करें।',
    'कवक के प्रवेश को रोकने और पौधों की कोशिका भित्ति को मजबूत करने के लिए संतुलित पोटेशियम (K) पोषण दें।'
  ],
  bn: [
    '{crop} ফসলে স্পোর জমার আগেই প্রতিরোধমূলক জৈব ছত্রাকনাশক (ট্রাইকোডার্মা ভিরিডি @ ৫ গ্রাম/লিটার বা সিউডোমোনাস) স্প্রে করুন।',
    'ক্ষেতের আর্দ্রতা কমাতে নিচের সংক্রামিত পাতা ছেঁটে ফেলুন এবং বাতাস চলাচলের ব্যবস্থা করুন।',
    'দেরি সন্ধ্যায় ফোয়ারা সেচ এড়িয়ে চলুন; পাতা ভেজা থাকার সময় কমাতে ড্রিপ সেচে চলে যান।',
    'সম্প্রতি রোগ দেখা দেওয়া নিকটবর্তী জমির সীমানায় প্রাথমিক ক্ষতচিহ্ন পরীক্ষা করুন।',
    'ছত্রাকের আক্রমণ প্রতিরোধ করতে এবং উদ্ভিদের কোষ প্রাচীর মজবুত করতে সুষম পটাসিয়াম (K) সরবরাহ করুন।'
  ],
  mr: [
    '{crop} वर बुरशीचे बीजाणू स्थिरावण्यापूर्वी प्रतिबंधात्मक जैविक बुरशीनाशक (ट्रायकोडर्मा विरिडी @ 5g/L किंवा स्यूडोमोनास) फवारा.',
    'सूक्ष्म हवामानातील आर्द्रता कमी करण्यासाठी खालची रोगट पाने छाटा आणि हवा खेळती ठेवा.',
    'संध्याकाळी तुषार सिंचन टाळा; पानांचा ओलावा कमी करण्यासाठी ठिबक सिंचनाचा वापर करा.',
    'अलीकडे रोग आढळलेल्या शेजारील शेतांच्या सीमांवर सुरुवातीच्या डागांची पाहणी करा.',
    'बुरशीचा प्रादुर्भाव रोखण्यासाठी आणि वनस्पतींच्या पेशी मजबूत करण्यासाठी संतुलित पोटॅशियम (K) चे पोषण द्या.'
  ],
  gu: [
    '{crop} પર બીજાણુઓ બેસે તે પહેલાં નિવારક જૈવિક ફૂગનાશક (ટ્રાઇકોડર્મા વિરીડી @ 5g/L અથવા સ્યુડોમોનાસ) છાંટો.',
    'ભેજ ઘટાડવા માટે નીચેના રોગગ્રસ્ત પાંદડાં કાપી નાખો અને હવા-ઉજાસ સુધારો.',
    'સાંજના સમયે સ્પ્રિંકલર પદ્ધતિ ટાળો; પાંદડાં ભીના રહેવાનો સમય ઘટાડવા ટપક પદ્ધતિ અપનાવો.',
    'નજીકના ખેતરોમાં રોગ જોવા મળ્યો હોવાથી ખેતરની સરહદો પર પ્રારંભિક ડાઘાઓની તપાસ કરો.',
    'ફૂગના પ્રવેશને રોકવા અને વનસ્પતિના કોષોને મજબૂત બનાવવા સંતુલિત પોટેશિયમ (K) પોષણ આપો.'
  ],
  pa: [
    '{crop} ਉੱਤੇ ਉੱਲੀ ਦੇ ਬੀਜਾਣੂ ਜੰਮਣ ਤੋਂ ਪਹਿਲਾਂ ਰੋਕਥਾਮ ਵਾਲੀ ਜੈਵਿਕ ਉੱਲੀਨਾਸ਼ਕ (ਟ੍ਰਾਈਕੋਡਰਮਾ ਵਿਰੀਡੇ @ 5g/L ਜਾਂ ਸੂਡੋਮੋਨਾਸ) ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
    'ਨਮੀ ਘਟਾਉਣ ਲਈ ਹੇਠਲੇ ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ ਛਾਂਟੋ ਅਤੇ ਹਵਾ ਦੇ ਗੇੜ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।',
    'ਦੇਰ ਸ਼ਾਮ ਫੁਹਾਰਾ ਸਿੰਚਾਈ ਤੋਂ ਬਚੋ; ਪੱਤੇ ਗਿੱਲੇ ਰਹਿਣ ਦਾ ਸਮਾਂ ਘਟਾਉਣ ਲਈ ਤੁਪਕਾ ਸਿੰਚਾਈ ਅਪਣਾਓ।',
    'ਨੇੜਲੇ ਖੇਤਾਂ ਵਿੱਚ ਰੋਗ ਫੈਲਣ ਦੇ ਮੱਦੇਨਜ਼ਰ ਖੇਤ ਦੀਆਂ ਹੱਦਾਂ \'ਤੇ ਸ਼ੁਰੂਆਤੀ ਨਿਸ਼ਾਨਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।',
    'ਉੱਲੀ ਦੇ ਹਮਲੇ ਨੂੰ ਰੋਕਣ ਅਤੇ ਪੌਦੇ ਦੇ ਸੈੱਲਾਂ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰਨ ਲਈ ਸੰਤੁਲਿਤ ਪੋਟਾਸ਼ੀਅਮ (K) ਖੁਰਾਕ ਦਿਓ।'
  ],
  ur: [
    '{crop} پر بیضانے جمنے سے پہلے حفاظتی بائیو فنگسائڈ (ٹرائیکوڈرما ویریڈی 5 گرام/لیٹر یا سوڈوموناس) کا چھڑکاؤ کریں۔',
    'کھیت میں نمی کم کرنے کے لیے نچلے متاثرہ پتوں کی چھٹائی کریں اور ہوا کی آمدورفت بہتر بنائیں۔',
    'دیر شام فوارہ آبپاشی سے گریز کریں؛ پتوں کی نمی کا دورانیہ کم کرنے کے لیے ڈرپ آبپاشی اپنائیں۔',
    'قریبی علاقوں میں بیماری پھیلنے کے پیش نظر کھیت کی سرحدوں پر ابتدائی دھبوں کی نگرانی کریں۔',
    'پھپھوندی کے حملے سے بچاؤ اور پودوں کی خلیاتی دیواروں کو مضبوط کرنے کے لیے متوازن پوٹاشیم (K) فراہم کریں۔'
  ],
  or: [
    '{crop} ଫସଲରେ କବକ ବୀଜାଣୁ ବସିବା ପୂର୍ବରୁ ପ୍ରତିଷେଧକ ଜୈବ-କବକନାଶକ (ଟ୍ରାଇକୋଡର୍ମା ଭିରିଡି @ ୫ ଗ୍ରାମ/ଲିଟର ବା ସୁଡୋମୋନାସ) ସିଞ୍ଚନ କରନ୍ତୁ।',
    'ଆର୍ଦ୍ରତା କମାଇବା ପାଇଁ ତଳ ଭାଗର ରୋଗାକ୍ରାନ୍ତ ପତ୍ରଗୁଡ଼ିକୁ କାଟି ବାୟୁ ଚଳାଚଳ ବୃଦ୍ଧି କରନ୍ତୁ।',
    'ସନ୍ଧ୍ୟା ସମୟରେ ଫୁଆରା ସିଞ୍ଚନ ଜଳସେଚନରୁ ନିବୃତ୍ତ ରୁହନ୍ତୁ; ପତ୍ର ଓଦା ରହିବା ସମୟ କମାଇବା ପାଇଁ ଡ୍ରିପ୍ ଜଳସେଚନ ବ୍ୟବହାର କରନ୍ତୁ।',
    'ନିକଟସ୍ଥ ଜମିରେ ରୋଗ ଚିହ୍ନଟ ହୋଇଥିବାରୁ ଜମିର ସୀମାନ୍ତ ଅଞ୍ଚଳରେ ପ୍ରାଥମିକ ଦାଗଗୁଡ଼ିକ ଯାଞ୍ଚ କରନ୍ତୁ।',
    'କବକ ସଂକ୍ରମଣ ପ୍ରତିରୋଧ କରିବା ଓ ଉଦ୍ଭିଦ କୋଷିକା ଭିତ୍ତି ସୁଦୃଢ଼ କରିବା ପାଇଁ ସନ୍ତୁଳିତ ପୋଟାସିୟମ୍ (K) ପୋଷକ ତତ୍ତ୍ୱ ପ୍ରଦାନ କରନ୍ତୁ।'
  ],
  as: [
    '{crop} শস্যত ৰেণু বহাৰ আগতেই প্ৰতিৰোধমূলক জৈৱ-ভেঁকুৰনাশক (ট্ৰাইক\'ডাৰ্মা ভিৰিডি @ ৫ গ্ৰাম/লিটাৰ বা চিউড\'ম\'নাছ) স্প্ৰে কৰক।',
    'আৰ্দ্ৰতা হ্ৰাস কৰিবলৈ তলৰ আক্ৰান্ত পাতবোৰ ছাঁটি দিয়ক আৰু বতাহ চলাচলৰ সুবিধা কৰক।',
    'দেৰি সন্ধিয়া পানী ছটিওৱা জলসিঞ্চন পৰিহাৰ কৰক; পাত তিতা হৈ থকা সময় কমাবলৈ টোপাল (ড্ৰিপ) জলসিঞ্চন ব্যৱহাৰ কৰক।',
    'ওচৰ-পাজৰৰ পথাৰত ৰোগ দেখা দিয়াত নিজৰ পথাৰৰ চাৰিওসীমাত প্ৰাৰম্ভিক দাগসমূহ পৰীক্ষা কৰক।',
    'ভেঁকুৰৰ সংক্ৰমণ প্ৰতিৰোধ কৰিবলৈ আৰু গছৰ কোষৰ বেৰ মজবুত কৰিবলৈ সুষম পটাছিয়াম (K) যোগান ধৰক।'
  ],
  ne: [
    '{crop} मा ढुसीका जीवाणु बस्नु अगावै रोकथामकारी जैविक ढुसीनाशक (ट्राइकोडर्मा भिरिडी @ ५ ग्राम/लिटर वा स्युडोमोनास) छर्कनुहोस्।',
    'ओसिलोपना कम गर्न तल्लो संक्रमित पातहरू छाँट्नुहोस् र हावाको बहाव सुधार गर्नुहोस्।',
    'साँझपख स्प्रिंकलर सिँचाइ नगर्नुहोस्; पातहरू भिजेको समय घटाउन थोपा सिँचाइ अपनाउनुहोस्।',
    'नजिकैको क्षेत्रमा रोग देखिएको हुँदा खेतको छेउछाउका बिरुवामा प्रारम्भिक दागहरू निरीक्षण गर्नुहोस्।',
    'ढुसीको आक्रमण रोक्न र बिरुवाको कोष भित्ता मजबुत बनाउन सन्तुलित पोटासियम (K) पोषण दिनुहोस्।'
  ],
  si: [
    '{crop} බෝග මත දිලීර බීජාණු තැන්පත් වීමට පෙර වැළැක්වීමේ ජෛව දිලීර නාශකයක් (ට්‍රයිකොඩර්මා විරිඩේ 5g/L හෝ සියුඩොමොනාස්) යොදන්න.',
    'තෙතමනය අවම කිරීම සඳහා යටි ආසාදිත පත්‍ර කප්පාදු කර වාතාශ්‍රය වැඩි දියුණු කරන්න.',
    'සවස් කාලයේ ඉසින වාරිමාර්ග ක්‍රම භාවිතයෙන් වළකින්න; පත්‍ර තෙත්ව පවතින කාලය අවම කිරීමට බිංදු ජල සම්පාදනයට මාරු වන්න.',
    'මෑතකදී ආසන්න ප්‍රදේශවල රෝග වාර්තා වූ බැවින් ක්ෂේත්‍ර මායිම්වල මුල් ලප නිරීක්ෂණය කරන්න.',
    'දිලීර ආසාදන වැළැක්වීමට හා ශාක සෛල බිත්ති ශක්තිමත් කිරීමට සමබර පොටෑසියම් (K) පෝෂණය ලබා දෙන්න.'
  ],
  ar: [
    'رش مبيداً فطرياً حيوياً وقائياً (تريكوديرما فيريدي 5 جم/لتر أو بسودوموناس) قبل استقرار الأبواغ على {crop}.',
    'حسّن تهوية المجموع الخضري وقلّم الأوراق السفلية المصابة لتقليل الرطوبة النسبية في المناخ المصغر.',
    'تجنب الري بالرشاشات في أواخر المساء؛ وتحول إلى الري بالتنقيط لتقليل مدة بلل الأوراق.',
    'افحص حواف الحقل المجاورة لبؤر الإصابة الحديثة بالمنطقة لاكتشاف البقع النخرية المبكرة.',
    'حافظ على تغذية متوازنة بالبوتاسيوم (K) لتقوية جدران الخلايا النباتية ضد اختراق الفطريات.'
  ],
  fr: [
    'Appliquer un biofongicide prophylactique (Trichoderma viride @ 5g/L ou Pseudomonas fluorescens) avant la fixation des spores sur {crop}.',
    'Optimiser l\'aération de la canopée et tailler le feuillage inférieur infecté pour réduire l\'humidité relative du microclimat.',
    'Éviter l\'irrigation par aspersion en fin de soirée ; privilégier le goutte-à-goutte pour minimiser la durée d\'humectation des feuilles.',
    'Inspecter les bordures de parcelles adjacentes aux détections récentes pour repérer les premières lésions nécrotiques.',
    'Maintenir une fertilisation équilibrée en potassium (K) pour renforcer les parois cellulaires végétales contre la pénétration fongique.'
  ],
  es: [
    'Aplique biofungicida profiláctico (Trichoderma viride @ 5g/L o Pseudomonas fluorescens) antes del asentamiento de esporas en {crop}.',
    'Optimice la aireación del dosel y pode el follaje inferior infectado para reducir la humedad relativa del microclima local.',
    'Evite el riego por aspersión al final de la tarde; cambie a goteo para minimizar la duración de la humedad foliar.',
    'Inspeccione los bordes del campo adyacentes a brotes recientes para detectar lesiones necróticas tempranas.',
    'Mantenga una nutrición equilibrada de potasio (K) para fortalecer las paredes celulares contra la penetración fúngica.'
  ],
  pt: [
    'Aplique biofungicida profilático (Trichoderma viride @ 5g/L ou Pseudomonas fluorescens) antes da fixação de esporos em {crop}.',
    'Otimize o arejamento da copa e desbaste as folhas inferiores infectadas para reduzir a umidade relativa do microclima local.',
    'Evite a irrigação por aspersão no final da tarde; mude para gotejamento para minimizar a duração do molhamento foliar.',
    'Inspecione as bordas do campo próximas a detecções recentes de doenças para identificar lesões necróticas precoces.',
    'Mantenha a nutrição equilibrada com potássio (K) para fortalecer as paredes celulares vegetais contra a penetração fúngica.'
  ],
  de: [
    'Vor der Sporenansiedlung auf {crop} ein vorbeugendes Bio-Fungizid (Trichoderma viride @ 5g/L oder Pseudomonas fluorescens) ausbringen.',
    'Bestandslüftung optimieren und untere befallene Blätter entfernen, um die relative Mikroklima-Luftfeuchtigkeit zu senken.',
    'Überkopfbewässerung am späten Abend vermeiden; auf Tropfbewässerung umstellen, um die Blattnässedauer zu minimieren.',
    'Feldränder neben kürzlich gemeldeten Krankheitsfällen auf frühe nekrotische Flecken kontrollieren.',
    'Ausgewogene Kaliumdüngung (K) sicherstellen, um pflanzliche Zellwände gegen das Eindringen von Pilzen zu stärken.'
  ],
  it: [
    'Applicare un biofungicida preventivo (Trichoderma viride @ 5g/L o Pseudomonas fluorescens) prima dell\'insediamento delle spore su {crop}.',
    'Ottimizzare l\'aerazione della chioma e potare il fogliame inferiore infetto per ridurre l\'umidità relativa del microclima.',
    'Evitare l\'irrigazione a pioggia a tarda sera; passare alla microirrigazione a goccia per ridurre il tempo di bagnatura fogliare.',
    'Ispezionare i bordi del campo adiacenti a recenti focolai della comunità per individuare lesioni necrotiche precoci.',
    'Mantenere un apporto bilanciato di potassio (K) per rinforzare le pareti cellulari vegetali contro la penetrazione fungina.'
  ],
  ru: [
    'Внесите профилактический биофунгицид (Trichoderma viride 5 г/л или Pseudomonas fluorescens) до оседания спор на {crop}.',
    'Улучшите проветривание крон и удалите нижние зараженные листья для снижения влажности микроклимата.',
    'Избегайте дождевания поздним вечером; перейдите на капельный полив для сокращения времени увлажнения листьев.',
    'Осмотрите границы поля рядом с недавними очагами заболеваний на наличие ранних некротических пятен.',
    'Обеспечьте сбалансированное калийное (K) питание для укрепления клеточных стенок растений против грибка.'
  ],
  ja: [
    '{crop} への胞子付着前に、予防的バイオ殺菌剤 (Trichoderma viride 5g/L または Pseudomonas fluorescens) を散布してください。',
    '微気候の湿度を下げるため、樹冠の通気性を改善し、感染した下葉を剪定してください。',
    '夕方遅くの散水灌漑を避け、点滴灌漑に切り替えて葉の湿潤時間を最小限に抑えてください。',
    '最近発生が確認された近隣圃場に隣接する境界部を巡回し、初期の壊死斑点を確認してください。',
    '菌糸の侵入を防ぎ植物の細胞壁を強化するため、バランスの取れたカリウム (K) 施肥を維持してください。'
  ],
  ko: [
    '{crop} 에 포자가 착생하기 전 예방적 생물 살균제 (트리코더마 비리데 5g/L 또는 슈도모나스)를 살포하십시오.',
    '미기후 습도를 낮추기 위해 수관 통풍을 개선하고 하부 감염 잎을 제거하십시오.',
    '늦은 저녁의 살수 관수를 피하고 점적 관수로 전환하여 잎의 젖음 시간을 최소화하십시오.',
    '인근 지역에서 최근 병해가 발생한 경계 구역을 살펴 초기 괴사 병반을 점검하십시오.',
    '곰팡이 침투를 방지하고 식물 세포벽을 강화하기 위해 균형 잡힌 칼륨(K) 영양을 유지하십시오.'
  ],
  zh: [
    '在病菌孢子在 {crop} 上定殖前，喷施预防性生物杀菌剂（哈茨木霉菌 5g/L 或荧光假单胞菌）。',
    '优化冠层通风，剪除下部感病枝叶，以降低田间微气候相对湿度。',
    '避免在傍晚进行高空喷灌；改用滴灌以尽量缩短叶片湿润时间。',
    '巡查邻近近期病害多发区域的地块边界，及早发现初期坏死病斑。',
    '保持均衡的钾肥 (K) 供应，增强植物表皮细胞壁抗真菌穿透能力。'
  ]
};

export function getLocalizedCropName(crop: string, lang: string = 'en'): string {
  if (!crop) return 'Crop';
  const normLang = (lang || 'en').toLowerCase().trim().split('-')[0].split('_')[0];
  const normCrop = crop.toLowerCase().trim();

  // If compound crop string like "Citrus / Vegetables"
  if (normCrop.includes(' / ')) {
    return normCrop
      .split(' / ')
      .map(c => getLocalizedCropName(c, normLang))
      .join(' / ');
  }

  for (const [key, map] of Object.entries(CROP_NAMES_25)) {
    if (normCrop.includes(key)) {
      return map[normLang] || map['en'] || crop;
    }
  }
  return crop;
}

export function localizeDiseaseName(rawName: string, lang: string = 'en'): string {
  if (!rawName) return '';
  const normLang = (lang || 'en').toLowerCase().trim().split('-')[0].split('_')[0];

  const clean = rawName.replace(/___/g, ' - ').replace(/_/g, ' ').trim();
  const lower = clean.toLowerCase();

  let cropPart = '';
  let disPart = clean;
  if (clean.includes(' - ')) {
    const parts = clean.split(' - ');
    cropPart = parts[0].trim();
    disPart = parts[1].trim();
  }

  const locCrop = cropPart ? getLocalizedCropName(cropPart, normLang) : '';
  const searchStr = (cropPart ? disPart : lower).toLowerCase().replace(/[()/\-]/g, ' ');

  const priorityKeys: [string, string][] = [
    ['cedar apple rust', 'cedar_apple_rust'],
    ['root rot', 'root_rot'],
    ['damping off', 'root_rot'],
    ['black rot', 'black_rot'],
    ['apple scab', 'apple_scab'],
    ['scab', 'apple_scab'],
    ['leaf mold', 'leaf_mold'],
    ['septoria', 'septoria_leaf_spot'],
    ['spider mite', 'spider_mites'],
    ['target spot', 'target_spot'],
    ['haunglongbing', 'haunglongbing'],
    ['greening', 'haunglongbing'],
    ['early blight', 'early_blight'],
    ['late blight', 'late_blight'],
    ['bacterial spot', 'bacterial_spot'],
    ['bacterial', 'bacterial_spot'],
    ['cercospora', 'cercospora_leaf_spot'],
    ['gray leaf spot', 'cercospora_leaf_spot'],
    ['powdery mildew', 'powdery_mildew'],
    ['mildew', 'powdery_mildew'],
    ['yellow leaf curl', 'yellow_leaf_curl'],
    ['rust', 'rust'],
    ['healthy', 'healthy'],
  ];

  let matchedDis: string | null = null;
  for (const [needle, key] of priorityKeys) {
    if (searchStr.includes(needle)) {
      matchedDis = DISEASE_TRANSLATIONS[key]?.[normLang] || DISEASE_TRANSLATIONS[key]?.['en'] || null;
      break;
    }
  }

  if (lower.includes('healthy')) {
    const hStr = DISEASE_TRANSLATIONS['healthy']?.[normLang] || 'Healthy Foliage';
    return locCrop ? `${locCrop} — ${hStr}` : hStr;
  }

  if (matchedDis && locCrop) {
    return `${locCrop} — ${matchedDis}`;
  } else if (matchedDis) {
    return matchedDis;
  }

  return clean;
}

export function localizePreventiveAction(
  action: string,
  cropName: string,
  lang: string = 'en',
  index: number = 0
): string {
  const normLang = (lang || 'en').toLowerCase().trim().split('-')[0].split('_')[0];
  const locCrop = getLocalizedCropName(cropName, normLang);

  const templates = PREVENTIVE_ACTIONS_TEMPLATES[normLang] || PREVENTIVE_ACTIONS_TEMPLATES['en'];
  if (!templates) return action;

  // Identify semantic template index based on content or fallback to index
  let targetIdx = index;
  const actLower = (action || '').toLowerCase();
  if (
    actLower.includes('fungicide') ||
    actLower.includes('trichoderma') ||
    actLower.includes('pseudomonas') ||
    actLower.includes('prophylactic') ||
    actLower.includes('spore settlement')
  ) {
    targetIdx = 0;
  } else if (
    actLower.includes('canopy aeration') ||
    actLower.includes('prune lower') ||
    actLower.includes('micro-climate')
  ) {
    targetIdx = 1;
  } else if (
    actLower.includes('sprinkler') ||
    actLower.includes('overhead') ||
    actLower.includes('drip') ||
    actLower.includes('leaf wetness')
  ) {
    targetIdx = 2;
  } else if (
    actLower.includes('field borders') ||
    actLower.includes('community disease') ||
    actLower.includes('necrotic lesions')
  ) {
    targetIdx = 3;
  } else if (
    actLower.includes('potassium') ||
    actLower.includes('epidermal') ||
    actLower.includes('fungal penetration')
  ) {
    targetIdx = 4;
  }

  if (templates[targetIdx] !== undefined) {
    return templates[targetIdx].replace(/{crop}/g, locCrop);
  }

  if (templates[index] !== undefined) {
    return templates[index].replace(/{crop}/g, locCrop);
  }

  return action;
}
