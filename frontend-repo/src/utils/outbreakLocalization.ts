/**
 * Outbreak Foresight Localization Utilities (25 Languages)
 * Translates raw disease names and recommended prevention actions across all 25 supported locales.
 */

export const CROP_NAMES_25: Record<string, Record<string, string>> = {
  tomato: {
    en: 'Tomato', ta: 'தக்காளி', te: 'టమోటా', ml: 'തക്കാളി', kn: 'ಟೊಮೆಟೊ',
    hi: 'टमाटर', bn: 'টমেটো', mr: 'टोमॅटो', gu: 'ટામેટાં', pa: 'ਟਮਾਟਰ',
    ur: 'ٹماٹر', or: 'ବିଲାତି ବାଇଗଣ', as: 'বিল Vilati', ne: 'गोलभेंडा', si: 'තක්කාලි',
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
    as: 'শিপা পচা / পুলି ପচা ৰোগ', ne: 'जरा कुहिने / डढुवा रोग', si: 'මුල් කුණුවීමේ රෝගය', ar: 'تعفن الجذور وموت البادرات',
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
    en: 'Apple Scab', ta: 'ஆப்பிள் செதில் நோய்', te: 'యాపిల్ పొలుసు తెగులు', ml: 'ആപ്പിൾ സ്കാബ് രോഗം',
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
  mr: [
    '{crop} वर बुरशीचे बीजाणू स्थिरावण्यापूर्वी प्रतिबंधात्मक जैविक बुरशीनाशक (ट्रायकोडर्मा विरिडी @ 5g/L किंवा स्यूडोमोनास) फवारा.',
    'सूक्ष्म हवामानातील आर्द्रता कमी करण्यासाठी खालची रोगट पाने छाटा आणि हवा खेळती ठेवा.',
    'संध्याकाळी तुषार सिंचन टाळा; पानांचा ओलावा कमी करण्यासाठी ठिबक सिंचनाचा वापर करा.',
    'अलीकडे रोग आढळलेल्या शेजारील शेतांच्या सीमांवर सुरुवातीच्या डागांची पाहणी करा.',
    'बुरशीचा प्रादुर्भाव रोखण्यासाठी आणि वनस्पतींच्या पेशी मजबूत करण्यासाठी संतुलित पोटॅशियम (K) चे पोषण द्या.'
  ],
  bn: [
    '{crop} ফসলে স্পোর জমার আগেই প্রতিরোধমূলক জৈব ছত্রাকনাশক (ট্রাইকোডার্মা ভিরিডি @ ৫ গ্রাম/লিটার বা সিউডোমোনাস) স্প্রে করুন।',
    'ক্ষেতের আর্দ্রতা কমাতে নিচের সংক্রামিত পাতা ছেঁটে ফেলুন এবং বাতাস চলাচলের ব্যবস্থা করুন।',
    'দেরি সন্ধ্যায় ফোয়ারা সেচ এড়িয়ে চলুন; পাতা ভেজা থাকার সময় কমাতে ড্রিপ সেচে চলে যান।',
    'সম্প্রতি রোগ দেখা দেওয়া নিকটবর্তী জমির সীমানায় প্রাথমিক ক্ষতচিহ্ন পরীক্ষা করুন।',
    'ছত্রাকের আক্রমণ প্রতিরোধ করতে এবং উদ্ভিদের কোষ প্রাচীর মজবুত করতে সুষম পটাসিয়াম (K) সরবরাহ করুন।'
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
  ]
};

export function getLocalizedCropName(crop: string, lang: string = 'en'): string {
  if (!crop) return 'Crop';
  const normCrop = crop.toLowerCase().trim();
  const normLang = (lang || 'en').toLowerCase().trim();

  for (const [key, map] of Object.entries(CROP_NAMES_25)) {
    if (normCrop.includes(key)) {
      return map[normLang] || map['en'] || crop;
    }
  }
  return crop;
}

export function localizeDiseaseName(rawName: string, lang: string = 'en'): string {
  if (!rawName) return '';
  const normLang = (lang || 'en').toLowerCase().trim();

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
  const normLang = (lang || 'en').toLowerCase().trim();
  const locCrop = getLocalizedCropName(cropName, normLang);

  const templates = PREVENTIVE_ACTIONS_TEMPLATES[normLang] || PREVENTIVE_ACTIONS_TEMPLATES['en'];
  if (templates && templates[index]) {
    return templates[index].replace(/{crop}/g, locCrop);
  }

  return action;
}
