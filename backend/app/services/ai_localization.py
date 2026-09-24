"""
Multilingual AI Localization Module for AgriGuard
Provides 25-language support for:
1. Grounded Plant Pathology Reasoning (Fungal, Bacterial, Viral risk analysis and pesticide prescriptions)
2. Crop Recommendation Reasoning & Localized Crop Names
Supported locales: en, ta, te, ml, kn, hi, bn, mr, gu, pa, ur, or, as, ne, si, ar, fr, es, pt, de, it, ru, ja, ko, zh.
"""

from typing import Dict, Any, List, Tuple

SUPPORTED_LANGUAGES = [
    "en", "ta", "te", "ml", "kn", "hi", "bn", "mr", "gu", "pa",
    "ur", "or", "as", "ne", "si", "ar", "fr", "es", "pt", "de",
    "it", "ru", "ja", "ko", "zh"
]

# Multilingual localized crop names for top crops
CROP_NAMES_25: Dict[str, Dict[str, str]] = {
    "apple": {
        "en": "Apple",
        "ta": "ஆப்பிள்",
        "te": "యాపిల్",
        "ml": "ആപ്പിൾ",
        "kn": "ಸೇಬು",
        "hi": "सेब",
        "bn": "আপেল",
        "mr": "सफरचंद",
        "gu": "સફરજન",
        "pa": "ਸੇਬ",
        "ur": "سیب",
        "or": "ସେଓ",
        "as": "আপেল",
        "ne": "स्याउ",
        "si": "ඇපල්",
        "ar": "التفاح",
        "fr": "Pomme",
        "es": "Manzana",
        "pt": "Maçã",
        "de": "Apfel",
        "it": "Mela",
        "ru": "Яблоко",
        "ja": "りんご",
        "ko": "사과",
        "zh": "苹果"
    },
    "bajra": {
        "en": "Pearl Millet (Bajra)",
        "ta": "கம்பு",
        "te": "సజ్జలు",
        "ml": "കമ്പം",
        "kn": "ಸಜ್ಜೆ",
        "hi": "बाजरा",
        "bn": "বাজরা",
        "mr": "बाजरी",
        "gu": "બાજરી",
        "pa": "ਬਾਜਰਾ",
        "ur": "باجرہ",
        "or": "ବାଜରା",
        "as": "বজৰা",
        "ne": "बाजरा",
        "si": "බජිරි",
        "ar": "الدخن اللؤلؤي (باجرا)",
        "fr": "Millet perle",
        "es": "Mijo perla",
        "pt": "Milheto",
        "de": "Perlhirse",
        "it": "Miglio perlato",
        "ru": "Просо жемчужное (Баджра)",
        "ja": "トウジンビエ (バジュラ)",
        "ko": "진주조 (바지라)",
        "zh": "御谷 / 珍珠粟"
    },
    "banana": {
        "en": "Banana",
        "ta": "வாழை",
        "te": "అరటి",
        "ml": "വാഴപ്പഴം",
        "kn": "ಬಾಳೆಹಣ್ಣು",
        "hi": "केला",
        "bn": "কলা",
        "mr": "केळी",
        "gu": "કેળા",
        "pa": "ਕੇਲਾ",
        "ur": "کیلا",
        "or": "କଦଳୀ",
        "as": "কল",
        "ne": "केरा",
        "si": "කෙසෙල්",
        "ar": "الموز",
        "fr": "Banane",
        "es": "Plátano",
        "pt": "Banana",
        "de": "Banane",
        "it": "Banana",
        "ru": "Банан",
        "ja": "バナナ",
        "ko": "바나나",
        "zh": "香蕉"
    },
    "barley": {
        "en": "Barley",
        "ta": "பார்லி",
        "te": "బార్లీ",
        "ml": "ബാർലി",
        "kn": "ಬಾರ್ಲಿ",
        "hi": "जौ",
        "bn": "যব",
        "mr": "जवस / बारली",
        "gu": "જવ",
        "pa": "ਜੌਂ",
        "ur": "جو",
        "or": "ଯବ",
        "as": "যৱ",
        "ne": "जौ",
        "si": "බාර්ලි",
        "ar": "الشعير",
        "fr": "Orge",
        "es": "Cebada",
        "pt": "Cevada",
        "de": "Gerste",
        "it": "Orzo",
        "ru": "Ячмень",
        "ja": "大麦",
        "ko": "보리",
        "zh": "大麦"
    },
    "blackgram": {
        "en": "Black Gram (Urad)",
        "ta": "உளுந்து",
        "te": "మినుములు",
        "ml": "ഉഴുന്ന്",
        "kn": "ಉದ್ದಿನ ಕಾಳು",
        "hi": "उड़द",
        "bn": "মাষকলাই",
        "mr": "उडीद",
        "gu": "અડદ",
        "pa": "ਮਾਂਹ",
        "ur": "ماش",
        "or": "ବିରି",
        "as": "মাটিকলাই",
        "ne": "मास",
        "si": "උඳු",
        "ar": "الحمص الأسود (أوراد)",
        "fr": "Haricot urd",
        "es": "Lenteja negra",
        "pt": "Feijão-da-índia",
        "de": "Urdbohne",
        "it": "Fagiolo indiano",
        "ru": "Маш черный (Урад)",
        "ja": "ケツルアズキ (ウラド)",
        "ko": "블랙그램 (우라드)",
        "zh": "黑绿豆"
    },
    "chickpea": {
        "en": "Chickpea (Chana)",
        "ta": "கொண்டைக்கடலை",
        "te": "శనగలు",
        "ml": "കടല",
        "kn": "ಕಡಲೆ",
        "hi": "चना",
        "bn": "ছোলা",
        "mr": "हरभरा",
        "gu": "ચણા",
        "pa": "ਛੋਲੇ",
        "ur": "چنا",
        "or": "ବୁଟ",
        "as": "বুট মাহ",
        "ne": "चना",
        "si": "කඩල",
        "ar": "الحمص",
        "fr": "Pois chiche",
        "es": "Garbanzo",
        "pt": "Grão-de-bico",
        "de": "Kichererbse",
        "it": "Cece",
        "ru": "Нут",
        "ja": "ひよこ豆",
        "ko": "병아리콩",
        "zh": "鹰嘴豆"
    },
    "chilli": {
        "en": "Chilli",
        "ta": "மிளகாய்",
        "te": "మిరప",
        "ml": "മുളക്",
        "kn": "ಮೆಣಸಿನಕಾಯಿ",
        "hi": "मिर्च",
        "bn": "মরিচ / লঙ্কা",
        "mr": "मिरची",
        "gu": "મરચાં",
        "pa": "ਮਿਰਚ",
        "ur": "مرچ",
        "or": "ଲଙ୍କା",
        "as": "জলকীয়া",
        "ne": "खुर्सानी",
        "si": "මිරිස්",
        "ar": "الفلفل الحار",
        "fr": "Piment",
        "es": "Chile",
        "pt": "Pimenta",
        "de": "Chili",
        "it": "Peperoncino",
        "ru": "Перец чили",
        "ja": "唐辛子",
        "ko": "고추",
        "zh": "辣椒"
    },
    "coconut": {
        "en": "Coconut",
        "ta": "தென்னை / தேங்காய்",
        "te": "కొబ్బరి",
        "ml": "തേങ്ങ",
        "kn": "ತೆಂಗಿನಕಾಯಿ",
        "hi": "नारियल",
        "bn": "নারকেল",
        "mr": "नारळ",
        "gu": "નાળિયેર",
        "pa": "ਨਾਰੀਅਲ",
        "ur": "ناریل",
        "or": "ନଡ଼ିଆ",
        "as": "নাৰিকল",
        "ne": "नारिवल",
        "si": "පොල්",
        "ar": "جوز الهند",
        "fr": "Noix de coco",
        "es": "Coco",
        "pt": "Coco",
        "de": "Kokosnuss",
        "it": "Noce di cocco",
        "ru": "Кокос",
        "ja": "ココナッツ",
        "ko": "코코넛",
        "zh": "椰子"
    },
    "coffee": {
        "en": "Coffee",
        "ta": "காபி",
        "te": "కాఫీ",
        "ml": "കാപ്പി",
        "kn": "ಕಾಫಿ",
        "hi": "कॉफी",
        "bn": "কফি",
        "mr": "कॉफी",
        "gu": "કોફી",
        "pa": "ਕੌਫੀ",
        "ur": "کافی",
        "or": "କଫି",
        "as": "কফি",
        "ne": "कफी",
        "si": "කෝපි",
        "ar": "القهوة",
        "fr": "Café",
        "es": "Café",
        "pt": "Café",
        "de": "Kaffee",
        "it": "Caffè",
        "ru": "Кофе",
        "ja": "コーヒー",
        "ko": "커피",
        "zh": "咖啡"
    },
    "cotton": {
        "en": "Cotton",
        "ta": "பருத்தி",
        "te": "పత్తి",
        "ml": "പരുത്തി",
        "kn": "ಹತ್ತಿ",
        "hi": "कपास",
        "bn": "তুলা",
        "mr": "कापूस",
        "gu": "કપાસ",
        "pa": "ਕਪਾਹ",
        "ur": "کپاس",
        "or": "କପା",
        "as": "কপাহ",
        "ne": "कपास",
        "si": "කපු",
        "ar": "القطن",
        "fr": "Coton",
        "es": "Algodón",
        "pt": "Algodão",
        "de": "Baumwolle",
        "it": "Cotone",
        "ru": "Хлопок",
        "ja": "綿花",
        "ko": "목화",
        "zh": "棉花"
    },
    "garlic": {
        "en": "Garlic",
        "ta": "பூண்டு",
        "te": "వెల్లుల్లి",
        "ml": "വെളുത്തുള്ളി",
        "kn": "ಬೆಳ್ಳುಳ್ಳಿ",
        "hi": "लहसुन",
        "bn": "রসুন",
        "mr": "लसूण",
        "gu": "લસણ",
        "pa": "ਲਸਣ",
        "ur": "لہسن",
        "or": "ରସୁଣ",
        "as": "নহৰু",
        "ne": "लसुन",
        "si": "සුදුළූණු",
        "ar": "الثوم",
        "fr": "Ail",
        "es": "Ajo",
        "pt": "Alho",
        "de": "Knoblauch",
        "it": "Aglio",
        "ru": "Чеснок",
        "ja": "にんにく",
        "ko": "마늘",
        "zh": "大蒜"
    },
    "ginger": {
        "en": "Ginger",
        "ta": "இஞ்சி",
        "te": "అల్లం",
        "ml": "ഇഞ്ചി",
        "kn": "ಶುಂಠಿ",
        "hi": "अदरक",
        "bn": "আদা",
        "mr": "आले",
        "gu": "આદુ",
        "pa": "ਅਦਰਕ",
        "ur": "ادرک",
        "or": "ଅଦା",
        "as": "আদা",
        "ne": "अदुवा",
        "si": "ඉඟුරු",
        "ar": "الزنجبيل",
        "fr": "Gingembre",
        "es": "Jengibre",
        "pt": "Gengibre",
        "de": "Ingwer",
        "it": "Zenzero",
        "ru": "Имбирь",
        "ja": "生姜",
        "ko": "생강",
        "zh": "生姜"
    },
    "grapes": {
        "en": "Grapes",
        "ta": "திராட்சை",
        "te": "ద్రాక్ష",
        "ml": "മുന്തിരി",
        "kn": "ದ್ರಾಕ್ಷಿ",
        "hi": "अंगूर",
        "bn": "আঙুর",
        "mr": "द्राक्षे",
        "gu": "દ્રાક્ષ",
        "pa": "ਅੰਗੂਰ",
        "ur": "انگور",
        "or": "ଅଙ୍ଗୁର",
        "as": "আঙুৰ",
        "ne": "अंगुर",
        "si": "මිදි",
        "ar": "العنب",
        "fr": "Raisin",
        "es": "Uvas",
        "pt": "Uvas",
        "de": "Weintrauben",
        "it": "Uva",
        "ru": "Виноград",
        "ja": "ぶどう",
        "ko": "포도",
        "zh": "葡萄"
    },
    "groundnut": {
        "en": "Groundnut (Peanut)",
        "ta": "நிலக்கடலை",
        "te": "వేరుశనగ",
        "ml": "നിലക്കടല",
        "kn": "ಕಡಲೆಕಾಯಿ",
        "hi": "मूंगफली",
        "bn": "চীনাবাদাম",
        "mr": "भुईमूग",
        "gu": "મગફળી",
        "pa": "ਮੂੰਗਫਲੀ",
        "ur": "مونگ پھلی",
        "or": "ଚିନାବାଦାମ",
        "as": "বাদাম",
        "ne": "बदाम",
        "si": "රටකජු",
        "ar": "الفول السوداني",
        "fr": "Arachide",
        "es": "Cacahuate",
        "pt": "Amendoim",
        "de": "Erdnuss",
        "it": "Arachide",
        "ru": "Арахис",
        "ja": "落花生",
        "ko": "땅콩",
        "zh": "花生"
    },
    "jowar": {
        "en": "Sorghum (Jowar)",
        "ta": "சோளம்",
        "te": "జొన్నలు",
        "ml": "ചോളം",
        "kn": "ಜೋಳ",
        "hi": "ज्वार",
        "bn": "জোয়ার",
        "mr": "ज्वारी",
        "gu": "જુવાર",
        "pa": "ਜਵਾਰ",
        "ur": "جوار",
        "or": "ଜୁଆର",
        "as": "জুৱাৰ",
        "ne": "जुनेलो",
        "si": "ඉදල් ඉරිඟු",
        "ar": "الذرة الرفيعة (جوار)",
        "fr": "Sorgho",
        "es": "Sorgo",
        "pt": "Sorgo",
        "de": "Sorghumhirse",
        "it": "Sorgo",
        "ru": "Сорго (Джовар)",
        "ja": "ソルガム (モロコシ)",
        "ko": "수수 (조와르)",
        "zh": "高粱"
    },
    "jute": {
        "en": "Jute",
        "ta": "சணல்",
        "te": "జనపనార",
        "ml": "ചണം",
        "kn": "ಸೆಣಬು",
        "hi": "पटसन / जूट",
        "bn": "পাট",
        "mr": "ताग",
        "gu": "શણ",
        "pa": "ਪਟਸਨ",
        "ur": "پٹ سن",
        "or": "ଝୋଟ",
        "as": "মৰাপাট",
        "ne": "पटसन",
        "si": "හණ",
        "ar": "الجوت",
        "fr": "Jute",
        "es": "Yute",
        "pt": "Juta",
        "de": "Jute",
        "it": "Iuta",
        "ru": "Джут",
        "ja": "ジュート (黄麻)",
        "ko": "황마",
        "zh": "黄麻"
    },
    "kidneybeans": {
        "en": "Kidney Beans (Rajma)",
        "ta": "ராஜ்மா பயறு",
        "te": "రాజ్మా",
        "ml": "വൻപയർ (രാജ്മ)",
        "kn": "ರಾಜ್ಮಾ ಕಾಳು",
        "hi": "राजमा",
        "bn": "রাজমা",
        "mr": "राजमा",
        "gu": "રાજમા",
        "pa": "ਰਾਜਮਾਂਹ",
        "ur": "راجما",
        "or": "ରାଜମା",
        "as": "ৰাজমাহ",
        "ne": "राजमा",
        "si": "බෝංචි",
        "ar": "الفاصوليا الحمراء",
        "fr": "Haricots rouges",
        "es": "Frijoles rojos",
        "pt": "Feijão vermelho",
        "de": "Kidneybohnen",
        "it": "Fagioli rossi",
        "ru": "Красная фасоль",
        "ja": "インゲン豆",
        "ko": "강낭콩",
        "zh": "红芸豆"
    },
    "lentil": {
        "en": "Lentil (Masoor)",
        "ta": "மசூர் பருப்பு",
        "te": "మసూర్ పప్పు",
        "ml": "പരിപ്പ് (മസൂർ)",
        "kn": "ಮಸೂರ್ ಬೇಳೆ",
        "hi": "मसूर दाल",
        "bn": "মসুর ডাল",
        "mr": "मसूर",
        "gu": "મસૂર",
        "pa": "ਮਸਰਾਂ ਦੀ ਦਾਲ",
        "ur": "مسور کی دال",
        "or": "ମସୁର ଡାଲି",
        "as": "মচুৰ মাহ",
        "ne": "मुसुरो दाल",
        "si": "මසූර් පරිප්පු",
        "ar": "العدس",
        "fr": "Lentille",
        "es": "Lenteja",
        "pt": "Lentilha",
        "de": "Linse",
        "it": "Lenticchia",
        "ru": "Чечевица",
        "ja": "レンズ豆",
        "ko": "렌틸콩",
        "zh": "小扁豆"
    },
    "maize": {
        "en": "Maize (Corn)",
        "ta": "மக்காச்சோளம்",
        "te": "మొక్కజొన్న",
        "ml": "മക്കച്ചോളം",
        "kn": "ಮೆಕ್ಕೆಜೋಳ",
        "hi": "मक्का",
        "bn": "ভুট্টা",
        "mr": "मका",
        "gu": "મકાઈ",
        "pa": "ਮੱਕੀ",
        "ur": "مکئی",
        "or": "ମକା",
        "as": "মাকৈ",
        "ne": "मकै",
        "si": "ඉරිඟු",
        "ar": "الذرة",
        "fr": "Maïs",
        "es": "Maíz",
        "pt": "Milho",
        "de": "Mais",
        "it": "Mais",
        "ru": "Кукуруза",
        "ja": "とうもろこし",
        "ko": "옥수수",
        "zh": "玉米"
    },
    "mango": {
        "en": "Mango",
        "ta": "மாங்காய்",
        "te": "మామిడి",
        "ml": "മാങ്ങ",
        "kn": "ಮಾವು",
        "hi": "आम",
        "bn": "আম",
        "mr": "आंबा",
        "gu": "કેરી",
        "pa": "ਅੰਬ",
        "ur": "آم",
        "or": "ଆମ୍ବ",
        "as": "আম",
        "ne": "आँप",
        "si": "අඹ",
        "ar": "المانجو",
        "fr": "Mangue",
        "es": "Mango",
        "pt": "Manga",
        "de": "Mango",
        "it": "Mango",
        "ru": "Манго",
        "ja": "マンゴー",
        "ko": "망고",
        "zh": "芒果"
    },
    "mothbeans": {
        "en": "Moth Beans (Matki)",
        "ta": "நரிப்பயறு",
        "te": "బొబ్బర్లు",
        "ml": "മൊത്തപ്പയർ",
        "kn": "ಮಡಿಕೆ ಕಾಳು",
        "hi": "मोठ",
        "bn": "মথ বিনস",
        "mr": "मटकी",
        "gu": "મઠ",
        "pa": "ਮੋਠ",
        "ur": "موتھ",
        "or": "ମଠ",
        "as": "মথ মাহ",
        "ne": "मोठ",
        "si": "මොත් බෝංචි",
        "ar": "لوبياء العث",
        "fr": "Haricot papillon",
        "es": "Frijol polilla",
        "pt": "Feijão-mariposa",
        "de": "Mattenbohne",
        "it": "Fagiolo falcato",
        "ru": "Бобы мот (Маткі)",
        "ja": "モスビーン (マツキ)",
        "ko": "모스빈 (마트키)",
        "zh": "蛾豆"
    },
    "mungbean": {
        "en": "Mung Bean (Moong)",
        "ta": "பாசிப்பயறு",
        "te": "పెసలు",
        "ml": "ചെറുപയർ",
        "kn": "ಹೆಸರು ಕಾಳು",
        "hi": "मूंग",
        "bn": "মুগ ডাল",
        "mr": "मूग",
        "gu": "મગ",
        "pa": "ਮੂੰਗੀ",
        "ur": "مونگ",
        "or": "ମୁଗ",
        "as": "মগু মাহ",
        "ne": "मुंग",
        "si": "මුං ඇට",
        "ar": "ماش (مونغ)",
        "fr": "Haricot mungo",
        "es": "Frijol mungo",
        "pt": "Feijão-mungo",
        "de": "Mungbohne",
        "it": "Fagiolo mungo",
        "ru": "Маш",
        "ja": "緑豆",
        "ko": "녹두",
        "zh": "绿豆"
    },
    "muskmelon": {
        "en": "Muskmelon",
        "ta": "முலாம் பழம்",
        "te": "కర్బూజ",
        "ml": "തൈക്കുമ്പളം",
        "kn": "ಕರಬೂಜ",
        "hi": "खरबूजा",
        "bn": "খরমুজ",
        "mr": "खरबूज",
        "gu": "શક્કરટેટી",
        "pa": "ਖ਼ਰਬੂਜ਼ਾ",
        "ur": "خربوزہ",
        "or": "ଖରଭୁଜ",
        "as": "খৰমুজ",
        "ne": "खर्बुजा",
        "si": "කැන්ටලූප් කොමඩු",
        "ar": "الشمام",
        "fr": "Melon",
        "es": "Melón",
        "pt": "Melão",
        "de": "Melone",
        "it": "Melone",
        "ru": "Дыня",
        "ja": "メロン",
        "ko": "멜론",
        "zh": "甜瓜"
    },
    "mustard": {
        "en": "Mustard",
        "ta": "கடுகு",
        "te": "ఆవాలు",
        "ml": "കടുക്",
        "kn": "ಸಾಸಿವೆ",
        "hi": "सरसों",
        "bn": "সরিষা",
        "mr": "मोहरी",
        "gu": "રાઈ",
        "pa": "ਸਰ੍ਹੋਂ",
        "ur": "سرسوں",
        "or": "ସୋରିଷ",
        "as": "সৰিয়হ",
        "ne": "तोरी",
        "si": "අබ",
        "ar": "الخردل",
        "fr": "Moutarde",
        "es": "Mostaza",
        "pt": "Mostarda",
        "de": "Senf",
        "it": "Senape",
        "ru": "Горчица",
        "ja": "からし菜",
        "ko": "겨자",
        "zh": "芥菜"
    },
    "okra": {
        "en": "Okra (Lady's Finger)",
        "ta": "வெண்டைக்காய்",
        "te": "బెండకాయ",
        "ml": "വെണ്ടയ്ക്ക",
        "kn": "ಬೆಂಡೆಕಾಯಿ",
        "hi": "भिंडी",
        "bn": "ঢেঁড়শ",
        "mr": "भेंडी",
        "gu": "ભીંડા",
        "pa": "ਭਿੰਡੀ",
        "ur": "بھنڈی",
        "or": "ଭେଣ୍ଡି",
        "as": "ভেণ্ডী",
        "ne": "भिन्डी",
        "si": "බණ්ඩක්කා",
        "ar": "البامية",
        "fr": "Gombo",
        "es": "Ocra / Quimbombó",
        "pt": "Quiabo",
        "de": "Okra",
        "it": "Okra",
        "ru": "Бамия",
        "ja": "オクラ",
        "ko": "오크라",
        "zh": "秋葵"
    },
    "onion": {
        "en": "Onion",
        "ta": "வெங்காயம்",
        "te": "ఉల్లిపాయ",
        "ml": "സവാള / ഉള്ളി",
        "kn": "ಈರುಳ್ಳಿ",
        "hi": "प्याज",
        "bn": "পেঁয়াজ",
        "mr": "कांदा",
        "gu": "ડુંગળી",
        "pa": "ਪਿਆਜ਼",
        "ur": "پیاز",
        "or": "ପିଆଜ",
        "as": "পিয়াঁজ",
        "ne": "प्याज",
        "si": "ලූනු",
        "ar": "البصل",
        "fr": "Oignon",
        "es": "Cebolla",
        "pt": "Cebola",
        "de": "Zwiebel",
        "it": "Cipolla",
        "ru": "Лук",
        "ja": "玉ねぎ",
        "ko": "양파",
        "zh": "洋葱"
    },
    "orange": {
        "en": "Orange (Citrus)",
        "ta": "ஆரஞ்சு",
        "te": "నారింజ",
        "ml": "ഓറഞ്ച്",
        "kn": "ಕಿತ್ತಳೆ",
        "hi": "संतरा / नारंगी",
        "bn": "কমলালেবু",
        "mr": "संत्रे",
        "gu": "સંતરા",
        "pa": "ਸੰਤਰਾ",
        "ur": "مالٹا / نارنجی",
        "or": "କମଳା",
        "as": "কমলা",
        "ne": "सुन्तला",
        "si": "දොඩම්",
        "ar": "البرتقال",
        "fr": "Orange",
        "es": "Naranja",
        "pt": "Laranja",
        "de": "Orange",
        "it": "Arancia",
        "ru": "Апельсин",
        "ja": "オレンジ",
        "ko": "오렌지",
        "zh": "橙子"
    },
    "papaya": {
        "en": "Papaya",
        "ta": "பப்பாளி",
        "te": "బొప్పాయి",
        "ml": "പപ്പായ",
        "kn": "ಪಪ್ಪಾಯಿ",
        "hi": "पपीता",
        "bn": "পেঁপে",
        "mr": "पपई",
        "gu": "પપૈયું",
        "pa": "ਪਪੀਤਾ",
        "ur": "پپیتا",
        "or": "ଅମୃତଭଣ୍ଡା",
        "as": "অমিতা",
        "ne": "मेवा",
        "si": "පැපොල්",
        "ar": "البابايا",
        "fr": "Papaye",
        "es": "Papaya",
        "pt": "Mamão",
        "de": "Papaya",
        "it": "Papaya",
        "ru": "Папайя",
        "ja": "パパイヤ",
        "ko": "파파야",
        "zh": "木瓜"
    },
    "pigeonpeas": {
        "en": "Pigeon Pea (Arhar/Tur)",
        "ta": "துவரம் பருப்பு",
        "te": "కందులు",
        "ml": "തുവരപ്പരിപ്പ്",
        "kn": "ತೊಗರಿ ಬೇಳೆ",
        "hi": "अरहर / तूर",
        "bn": "অড়হর ডাল",
        "mr": "तूर",
        "gu": "તુવેર",
        "pa": "ਅਰਹਰ",
        "ur": "ارہر دال",
        "or": "ହରଡ଼",
        "as": "অৰহৰ",
        "ne": "रहर",
        "si": "තෝර පරිප්පු",
        "ar": "البازلاء الحمامية",
        "fr": "Pois d'Angole",
        "es": "Gandul",
        "pt": "Feijão-guandu",
        "de": "Straucherbse",
        "it": "Pisello d'Angola",
        "ru": "Голубиный горох",
        "ja": "キマメ",
        "ko": "비둘기콩",
        "zh": "木豆"
    },
    "pomegranate": {
        "en": "Pomegranate",
        "ta": "மாதுளை",
        "te": "దానిమ్మ",
        "ml": "മാതളനാരങ്ങ",
        "kn": "ದಾಳಿಂಬೆ",
        "hi": "अनार",
        "bn": "বেদানা / ডালিম",
        "mr": "डाळिंब",
        "gu": "દાડમ",
        "pa": "ਅਨਾਰ",
        "ur": "انار",
        "or": "ଡାଳିମ୍ବ",
        "as": "ডালিম",
        "ne": "अनार",
        "si": "දෙළුම්",
        "ar": "الرمان",
        "fr": "Grenade",
        "es": "Granada",
        "pt": "Romã",
        "de": "Granatapfel",
        "it": "Melograno",
        "ru": "Гранат",
        "ja": "ざくろ",
        "ko": "석류",
        "zh": "石榴"
    },
    "potato": {
        "en": "Potato",
        "ta": "உருளைக்கிழங்கு",
        "te": "బంగాళాదుంప",
        "ml": "ഉരുളക്കിഴങ്ങ്",
        "kn": "ಆಲೂಗಡ್ಡೆ",
        "hi": "आलू",
        "bn": "আলু",
        "mr": "बटाटा",
        "gu": "બટાકા",
        "pa": "ਆਲੂ",
        "ur": "آلو",
        "or": "ଆଳୁ",
        "as": "আলু",
        "ne": "आलु",
        "si": "අර්තාපල්",
        "ar": "البطاطس",
        "fr": "Pomme de terre",
        "es": "Papa / Patata",
        "pt": "Batata",
        "de": "Kartoffel",
        "it": "Patata",
        "ru": "Картофель",
        "ja": "じゃがいも",
        "ko": "감자",
        "zh": "土豆 / 马铃薯"
    },
    "ragi": {
        "en": "Finger Millet (Ragi)",
        "ta": "கேழ்வரகு (ராகி)",
        "te": "రాగులు",
        "ml": "റാഗി / കൂവരക്",
        "kn": "ರಾಗಿ",
        "hi": "रागी",
        "bn": "রাগী",
        "mr": "नाचणी",
        "gu": "નાગલી / રાગી",
        "pa": "ਰਾਗੀ",
        "ur": "راگی",
        "or": "ମାଣ୍ଡିଆ",
        "as": "মৰুৱা ধান",
        "ne": "कोदो",
        "si": "කුරක්කන්",
        "ar": "دخن الأصبع (راجي)",
        "fr": "Éleusine",
        "es": "Mijo africano",
        "pt": "Capim-pé-de-galinha",
        "de": "Fingerhirse",
        "it": "Coracana",
        "ru": "Дагусса (Раги)",
        "ja": "シコクビエ (ラギ)",
        "ko": "핑거밀렛 (라기)",
        "zh": "䅟子 / 龙爪稷"
    },
    "rice": {
        "en": "Rice (Paddy)",
        "ta": "நெல்",
        "te": "వరి",
        "ml": "നെല്ല്",
        "kn": "ಭತ್ತ",
        "hi": "धान / चावल",
        "bn": "ধান",
        "mr": "भात",
        "gu": "ડાંગર",
        "pa": "ਝੋਨਾ",
        "ur": "دھان",
        "or": "ଧାନ",
        "as": "ধান",
        "ne": "धान",
        "si": "වී",
        "ar": "الأرز",
        "fr": "Riz",
        "es": "Arroz",
        "pt": "Arroz",
        "de": "Reis",
        "it": "Riso",
        "ru": "Рис",
        "ja": "稲 / 米",
        "ko": "벼 / 쌀",
        "zh": "水稻"
    },
    "rubber": {
        "en": "Rubber",
        "ta": "ரப்பர்",
        "te": "రబ్బరు",
        "ml": "റബ്ബർ",
        "kn": "ರಬ್ಬರ್",
        "hi": "रबर",
        "bn": "রাবার",
        "mr": "रबर",
        "gu": "રબર",
        "pa": "ਰਬੜ",
        "ur": "ربڑ",
        "or": "ରବର",
        "as": "ৰবৰ",
        "ne": "रबर",
        "si": "රබර්",
        "ar": "المطاط",
        "fr": "Caoutchouc",
        "es": "Caucho",
        "pt": "Borracha",
        "de": "Kautschuk",
        "it": "Gomma",
        "ru": "Каучук",
        "ja": "ゴムノキ",
        "ko": "고무나무",
        "zh": "橡胶"
    },
    "sesame": {
        "en": "Sesame (Til)",
        "ta": "எள்",
        "te": "నువ్వులు",
        "ml": "എള്ള്",
        "kn": "ಎಳ್ಳು",
        "hi": "तिल",
        "bn": "তিল",
        "mr": "तीळ",
        "gu": "તલ",
        "pa": "ਤਿਲ",
        "ur": "تل",
        "or": "ରାଶି",
        "as": "তিল",
        "ne": "तिल",
        "si": "තල",
        "ar": "السمسم",
        "fr": "Sésame",
        "es": "Sésamo / Ajonjolí",
        "pt": "Gergelim",
        "de": "Sesam",
        "it": "Sesamo",
        "ru": "Кунжут",
        "ja": "ごま",
        "ko": "참깨",
        "zh": "芝麻"
    },
    "soybean": {
        "en": "Soybean",
        "ta": "சோயாபீன்",
        "te": "సోయాబీన్",
        "ml": "സോയാബീൻ",
        "kn": "ಸೋಯಾಬೀನ್",
        "hi": "सोयाबीन",
        "bn": "সয়াবিন",
        "mr": "सोयाबीन",
        "gu": "સોયાબીન",
        "pa": "ਸੋਇਆਬੀਨ",
        "ur": "سویا بین",
        "or": "ସୋୟାବିନ୍",
        "as": "ছয়াবিন",
        "ne": "भटमास",
        "si": "සෝයා බෝංචි",
        "ar": "فول الصويا",
        "fr": "Soja",
        "es": "Soja",
        "pt": "Soja",
        "de": "Sojabohne",
        "it": "Soia",
        "ru": "Соя",
        "ja": "大豆",
        "ko": "대두 (콩)",
        "zh": "大豆"
    },
    "sugarcane": {
        "en": "Sugarcane",
        "ta": "கரும்பு",
        "te": "చెరకు",
        "ml": "കരിമ്പ്",
        "kn": "ಕಬ್ಬು",
        "hi": "गन्ना",
        "bn": "আখ",
        "mr": "ऊस",
        "gu": "શેરડી",
        "pa": "ਗੰਨਾ",
        "ur": "گنا",
        "or": "ଆଖୁ",
        "as": "কুঁহিয়াৰ",
        "ne": "उखु",
        "si": "උක්",
        "ar": "قصب السكر",
        "fr": "Canne à sucre",
        "es": "Caña de azúcar",
        "pt": "Cana-de-açúcar",
        "de": "Zuckerrohr",
        "it": "Canna da zucchero",
        "ru": "Сахарный тростник",
        "ja": "サトウキビ",
        "ko": "사탕수수",
        "zh": "甘蔗"
    },
    "sunflower": {
        "en": "Sunflower",
        "ta": "சூரியகாந்தி",
        "te": "పొద్దుతిరుగుడు",
        "ml": "സൂര്യകാന്തി",
        "kn": "ಸೂರ್ಯಕಾಂತಿ",
        "hi": "सूरजमुखी",
        "bn": "সূর্যমুখী",
        "mr": "सूर्यफूल",
        "gu": "સૂર્યમુખી",
        "pa": "ਸੂਰਜਮੁਖੀ",
        "ur": "سورج مکھی",
        "or": "ସୂର୍ଯ୍ୟମୁଖୀ",
        "as": "সূৰ্যমুখী",
        "ne": "सूर्यमुखी",
        "si": "සූරියකාන්ත",
        "ar": "دوار الشمس",
        "fr": "Tournesol",
        "es": "Girasol",
        "pt": "Girassol",
        "de": "Sonnenblume",
        "it": "Girasole",
        "ru": "Подсолнечник",
        "ja": "ひまわり",
        "ko": "해바라기",
        "zh": "向日葵"
    },
    "tomato": {
        "en": "Tomato",
        "ta": "தக்காளி",
        "te": "టమోటా",
        "ml": "തക്കാളി",
        "kn": "ಟೊಮೆಟೊ",
        "hi": "टमाटर",
        "bn": "টমেটো",
        "mr": "टोमॅटो",
        "gu": "ટામેટાં",
        "pa": "ਟਮਾਟਰ",
        "ur": "ٹماٹر",
        "or": "ବିଲାତି ବାଇଗଣ",
        "as": "বিলাহী",
        "ne": "गोलभेंडा",
        "si": "තක්කාලි",
        "ar": "الطماطم",
        "fr": "Tomate",
        "es": "Tomate",
        "pt": "Tomate",
        "de": "Tomate",
        "it": "Pomodoro",
        "ru": "Томат",
        "ja": "トマト",
        "ko": "토마토",
        "zh": "番茄"
    },
    "turmeric": {
        "en": "Turmeric",
        "ta": "மஞ்சள்",
        "te": "పసుపు",
        "ml": "മഞ്ഞൾ",
        "kn": "ಅರಿಶಿನ",
        "hi": "हल्दी",
        "bn": "হলুদ",
        "mr": "हळद",
        "gu": "હળદર",
        "pa": "ਹਲਦੀ",
        "ur": "ہلدی",
        "or": "ହଳଦୀ",
        "as": "হালধি",
        "ne": "बेसार",
        "si": "කහ",
        "ar": "الكركم",
        "fr": "Curcuma",
        "es": "Cúrcuma",
        "pt": "Cúrcuma",
        "de": "Kurkuma",
        "it": "Curcuma",
        "ru": "Куркума",
        "ja": "ウコン",
        "ko": "강황",
        "zh": "姜黄"
    },
    "watermelon": {
        "en": "Watermelon",
        "ta": "தர்பூசணி",
        "te": "పుచ్చకాయ",
        "ml": "തണ്ണിമത്തൻ",
        "kn": "ಕಲ್ಲಂಗಡಿ",
        "hi": "तरबूज",
        "bn": "তরমুজ",
        "mr": "कलिंगड",
        "gu": "તરબૂચ",
        "pa": "ਤਰਬੂਜ਼",
        "ur": "تربوز",
        "or": "ତରଭୁଜ",
        "as": "তৰমুজ",
        "ne": "तर्बुजा",
        "si": "දිය කොමඩු",
        "ar": "البطيخ",
        "fr": "Pastèque",
        "es": "Sandía",
        "pt": "Melancia",
        "de": "Wassermelone",
        "it": "Anguria",
        "ru": "Арбуз",
        "ja": "スイカ",
        "ko": "수박",
        "zh": "西瓜"
    },
    "wheat": {
        "en": "Wheat",
        "ta": "கோதுமை",
        "te": "గోధుమలు",
        "ml": "ഗോതമ്പ്",
        "kn": "ಗೋಧಿ",
        "hi": "गेहूं",
        "bn": "গম",
        "mr": "गहू",
        "gu": "ઘઉં",
        "pa": "ਕਣਕ",
        "ur": "گندم",
        "or": "ଗହମ",
        "as": "গম",
        "ne": "गहुँ",
        "si": "තිරිඟු",
        "ar": "القمح",
        "fr": "Blé",
        "es": "Trigo",
        "pt": "Trigo",
        "de": "Weizen",
        "it": "Grano",
        "ru": "Пшеница",
        "ja": "小麦",
        "ko": "밀",
        "zh": "小麦"
    }
}


def get_crop_display_name(crop_key: str, lang: str = "en") -> str:
    """Returns the localized display name for a given crop key (no English parentheses in non-en)."""
    norm_lang = (lang or "en").lower().strip()
    norm_key = crop_key.lower().replace(" ", "").replace("_", "").replace("-", "")

    # Check exact key match first
    for k, trans in CROP_NAMES_25.items():
        k_norm = k.lower().replace(" ", "").replace("_", "").replace("-", "")
        if k_norm == norm_key:
            if norm_lang in trans:
                return trans[norm_lang]
            return trans.get("en", crop_key.capitalize())

    # Fallback to substring match
    for k, trans in CROP_NAMES_25.items():
        k_norm = k.lower().replace(" ", "").replace("_", "").replace("-", "")
        if k_norm in norm_key or norm_key in k_norm:
            if norm_lang in trans:
                return trans[norm_lang]
            return trans.get("en", crop_key.capitalize())

    return crop_key.capitalize()


FERTILIZERS_25: Dict[str, Dict[str, str]] = {
    "en": {
        "urea_name": "Urea",
        "dap_name": "DAP — Di-Ammonium Phosphate",
        "mop_name": "MOP — Muriate of Potash",
        "fix_n_deficit": "to fix N deficit",
        "fix_p_deficit": "to fix P deficit",
        "fix_k_deficit": "to fix K deficit",
        "lime_title": "Agricultural Lime: apply to raise pH",
        "lime_advice": "Apply lime to raise soil pH. Consult local agronomist for quantity.",
        "gypsum_title": "Gypsum or Sulfur: apply to lower pH",
        "gypsum_advice": "Apply gypsum to lower soil pH. Consult local agronomist for quantity.",
        "soil_nutrients_ideal": "Soil nutrients are at ideal levels for this crop. No fertilizer needed.",
        "icar_standard": "ICAR Agronomic Standard",
        "live_soil_telemetry": "100% Live Soil Telemetry"
    },
    "ta": {
        "urea_name": "யூரியா",
        "dap_name": "டி.ஏ.பி — டை-அம்மோனியம் பாஸ்பேட்",
        "mop_name": "எம்.ஓ.பி — பொட்டாஷ் உரம்",
        "fix_n_deficit": "நைட்ரஜன் பற்றாக்குறையை சரிசெய்ய",
        "fix_p_deficit": "பாஸ்பரஸ் பற்றாக்குறையை சரிசெய்ய",
        "fix_k_deficit": "பொட்டாசியம் பற்றாக்குறையை சரிசெய்ய",
        "lime_title": "விவசாய சுண்ணாம்பு: pH அளவை உயர்த்த இடவும்",
        "lime_advice": "மண் pH அளவை உயர்த்த சுண்ணாம்பு இடவும். சரியான அளவுக்கு வேளாண் அலுவலரை அணுகவும்.",
        "gypsum_title": "ஜிப்சம் அல்லது கந்தகம்: pH அளவைக் குறைக்க இடவும்",
        "gypsum_advice": "மண் pH அளவைக் குறைக்க ஜிப்சம் இடவும். சரியான அளவுக்கு வேளாண் அலுவலரை அணுகவும்.",
        "soil_nutrients_ideal": "இப்பயிருக்கு மண்ணின் ஊட்டச்சத்துக்கள் உகந்த அளவில் உள்ளன. உரம் இடத் தேவையில்லை.",
        "icar_standard": "ICAR வேளாண்மை தரநிலை",
        "live_soil_telemetry": "100% நேரடி மண் தொலை அளவீடு"
    },
    "te": {
        "urea_name": "యూరియా",
        "dap_name": "డి.ఎ.పి — డై-అమ్మోనియం ఫాస్ఫేట్",
        "mop_name": "ఎం.ఒ.పి — మ్యూరియేట్ ఆఫ్ పొటాష్",
        "fix_n_deficit": "నత్రజని లోపాన్ని సరిచేయడానికి",
        "fix_p_deficit": "భాస్వరం లోపాన్ని సరిచేయడానికి",
        "fix_k_deficit": "పొటాషియం లోపాన్ని సరిచేయడానికి",
        "lime_title": "వ్యవసాయ సున్నం: pH పెంచడానికి వేయండి",
        "lime_advice": "నేల pH పెంచడానికి సున్నం వేయండి. పరిమాణం కోసం స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.",
        "gypsum_title": "జిప్సం లేదా సల్ఫర్: pH తగ్గించడానికి వేయండి",
        "gypsum_advice": "నేల pH తగ్గించడానికి జిప్సం వేయండి. పరిమాణం కోసం స్థానిక వ్యవసాయ నిపుణుడిని సంప్రదించండి.",
        "soil_nutrients_ideal": "ఈ పంటకు నేలలోని పోషకాలు సరైన స్థాయిలో ఉన్నాయి. ఎరువులు అవసరం లేదు.",
        "icar_standard": "ICAR వ్యవసాయ ప్రమాణం",
        "live_soil_telemetry": "100% ప్రత్యక్ష నేల టెలిమెట్రీ"
    },
    "ml": {
        "urea_name": "യൂറിയ",
        "dap_name": "ഡി.എ.പി — ഡൈ-അമോണിയം ഫോസ്ഫേറ്റ്",
        "mop_name": "എം.ഒ.പി — മ്യൂറിയേറ്റ് ഓഫ് പൊട്ടാഷ്",
        "fix_n_deficit": "നൈട്രജൻ കുറവ് പരിഹരിക്കാൻ",
        "fix_p_deficit": "ഫോസ്ഫറസ് കുറവ് പരിഹരിക്കാൻ",
        "fix_k_deficit": "പൊട്ടാസ്യം കുറവ് പരിഹരിക്കാൻ",
        "lime_title": "കാർഷിക കുമ്മായം: pH കൂട്ടാൻ പ്രയോഗിക്കുക",
        "lime_advice": "മണ്ണിന്റെ pH ഉയർത്താൻ കുമ്മായം ചേർക്കുക. കൃത്യമായ അളവിന് കൃഷി ഓഫീസറെ സമീപിക്കുക.",
        "gypsum_title": "ജിപ്സം അല്ലെങ്കിൽ സൾഫർ: pH കുറയ്ക്കാൻ പ്രയോഗിക്കുക",
        "gypsum_advice": "മണ്ണിന്റെ pH കുറയ്ക്കാൻ ജിപ്സം ചേർക്കുക. കൃത്യമായ അളവിന് കൃഷി ഓഫീസറെ സമീപിക്കുക.",
        "soil_nutrients_ideal": "ഈ വിളയ്ക്ക് മണ്ണിലെ പോഷകങ്ങൾ അനുയോജ്യമായ അളവിലാണ്. വളപ്രയോഗം ആവശ്യമില്ല.",
        "icar_standard": "ICAR കാർഷിക മാനദണ്ഡം",
        "live_soil_telemetry": "100% ലൈവ് മണ്ണ് ടെലിമെട്രി"
    },
    "kn": {
        "urea_name": "ಯೂರಿಯಾ",
        "dap_name": "ಡಿ.ಎ.ಪಿ — ಡೈ-ಅಮೋನಿಯಂ ಫಾಸ್ಫೇಟ್",
        "mop_name": "ಎಂ.ಒ.ಪಿ — ಮ್ಯೂರಿಯೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್",
        "fix_n_deficit": "ಸಾರಜನಕ ಕೊರತೆ ನೀಗಿಸಲು",
        "fix_p_deficit": "ರಂಜಕದ ಕೊರತೆ ನೀಗಿಸಲು",
        "fix_k_deficit": "ಪೊಟ್ಯಾಶ್ ಕೊರತೆ ನೀಗಿಸಲು",
        "lime_title": "ಕೃಷಿ ಸುಣ್ಣ: pH ಹೆಚ್ಚಿಸಲು ಬಳಸಿ",
        "lime_advice": "ಮಣ್ಣಿನ pH ಹೆಚ್ಚಿಸಲು ಸುಣ್ಣ ಹಾಕಿ. ಸೂಕ್ತ ಪ್ರಮಾಣಕ್ಕಾಗಿ ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "gypsum_title": "ಜಿಪ್ಸಮ್ ಅಥವಾ ಗಂಧಕ: pH ಕಡಿಮೆ ಮಾಡಲು ಬಳಸಿ",
        "gypsum_advice": "ಮಣ್ಣಿನ pH ಕಡಿಮೆ ಮಾಡಲು ಜಿಪ್ಸಮ್ ಬಳಸಿ. ಸೂಕ್ತ ಪ್ರಮಾಣಕ್ಕಾಗಿ ಕೃಷಿ ಅಧಿಕಾರಿಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "soil_nutrients_ideal": "ಈ ಬೆಳೆಗೆ ಮಣ್ಣಿನಲ್ಲಿ ಪೋಷಕಾಂಶಗಳು ಸೂಕ್ತ ಮಟ್ಟದಲ್ಲಿವೆ. ಯಾವುದೇ ಗೊಬ್ಬರದ ಅಗತ್ಯವಿಲ್ಲ.",
        "icar_standard": "ICAR ಕೃಷಿ ಮಾನದಂಡ",
        "live_soil_telemetry": "100% ಲೈವ್ ಮಣ್ಣಿನ ಟೆಲಿಮೆಟ್ರಿ"
    },
    "hi": {
        "urea_name": "यूरिया",
        "dap_name": "डीएपी — डाई-अमोनियम फॉस्फेट",
        "mop_name": "एमओपी — म्युरिएट ऑफ पोटाश",
        "fix_n_deficit": "नाइट्रोजन की कमी दूर करने के लिए",
        "fix_p_deficit": "फास्फोरस की कमी दूर करने के लिए",
        "fix_k_deficit": "पोटाश की कमी दूर करने के लिए",
        "lime_title": "कृषि चूना: pH बढ़ाने के लिए डालें",
        "lime_advice": "मिट्टी का pH बढ़ाने के लिए चूना डालें। सटीक मात्रा के लिए स्थानीय कृषि विशेषज्ञ से सलाह लें।",
        "gypsum_title": "जिप्सम या सल्फर: pH घटाने के लिए डालें",
        "gypsum_advice": "मिट्टी का pH कम करने के लिए जिप्सम डालें। सटीक मात्रा के लिए स्थानीय कृषि विशेषज्ञ से सलाह लें।",
        "soil_nutrients_ideal": "इस फसल के लिए मिट्टी में पोषक तत्व आदर्श स्तर पर हैं। किसी उर्वरक की आवश्यकता नहीं है।",
        "icar_standard": "ICAR कृषि मानक",
        "live_soil_telemetry": "100% लाइव मृदा टेलीमेट्री"
    },
    "bn": {
        "urea_name": "ইউরিয়া",
        "dap_name": "ডিএপি — ডাই-অ্যামোনিয়াম ফসফেট",
        "mop_name": "এমওপি — মিউরেট অব পটাশ",
        "fix_n_deficit": "নাইট্রোজেনের ঘাটতি মেটাতে",
        "fix_p_deficit": "ফসফরাসের ঘাটতি মেটাতে",
        "fix_k_deficit": "পটাশের ঘাটতি মেটাতে",
        "lime_title": "কৃষি চুন: pH বাড়াতে প্রয়োগ করুন",
        "lime_advice": "মাটির pH বাড়াতে চুন প্রয়োগ করুন। সঠিক পরিমাণের জন্য স্থানীয় কৃষি কর্মকর্তার সাথে পরামর্শ করুন।",
        "gypsum_title": "জিপসাম বা সালফার: pH কমাতে প্রয়োগ করুন",
        "gypsum_advice": "মাটির pH কমাতে জিপসাম প্রয়োগ করুন। সঠিক পরিমাণের জন্য স্থানীয় কৃষি কর্মকর্তার সাথে পরামর্শ করুন।",
        "soil_nutrients_ideal": "এই ফসলের জন্য মাটিতে পুষ্টি উপাদান আদর্শ মাত্রায় রয়েছে। কোনো সারের প্রয়োজন নেই।",
        "icar_standard": "ICAR কৃষি মানদণ্ড",
        "live_soil_telemetry": "১০০% লাইভ মাটির টেলিমেট্রি"
    },
    "mr": {
        "urea_name": "युरिया",
        "dap_name": "डीएपी — डाय-अमोनियम फॉस्फेट",
        "mop_name": "एमओपी — म्युरिएट ऑफ पोटॅश",
        "fix_n_deficit": "नत्राची कमतरता भरून काढण्यासाठी",
        "fix_p_deficit": "स्फुरदाची कमतरता भरून काढण्यासाठी",
        "fix_k_deficit": "पालाशची कमतरता भरून काढण्यासाठी",
        "lime_title": "कृषी चुना: pH वाढवण्यासाठी वापरा",
        "lime_advice": "मातीचा pH वाढवण्यासाठी चुना वापरा. योग्य प्रमाणासाठी स्थानिक कृषी तज्ञांशी संपर्क साधा.",
        "gypsum_title": "जिप्सम किंवा गंधक: pH कमी करण्यासाठी वापरा",
        "gypsum_advice": "मातीचा pH कमी करण्यासाठी जिप्सम वापरा. योग्य प्रमाणासाठी स्थानिक कृषी तज्ञांशी संपर्क साधा.",
        "soil_nutrients_ideal": "या पिकासाठी जमिनीतील पोषणद्रव्ये आदर्श पातळीवर आहेत. खतांची गरज नाही.",
        "icar_standard": "ICAR कृषी मानक",
        "live_soil_telemetry": "100% थेट माती टेलीमेट्री"
    },
    "gu": {
        "urea_name": "યુરિયા",
        "dap_name": "ડીએપી — ડાય-એમોનિયમ ફોસ્ફેટ",
        "mop_name": "એમઓપી — મ્યુરિએટ ઓફ પોટાશ",
        "fix_n_deficit": "નાઇટ્રોજનની ઉણપ દૂર કરવા",
        "fix_p_deficit": "ફોસ્ફરસની ઉણપ દૂર કરવા",
        "fix_k_deficit": "પોટાશની ઉણપ દૂર કરવા",
        "lime_title": "કૃષિ ચૂનો: pH વધારવા માટે નાખો",
        "lime_advice": "જમીનનો pH વધારવા ચૂનો ઉમેરો. યોગ્ય માત્રા માટે સ્થાનિક કૃષિ અધિકારીનો સંપર્ક કરો.",
        "gypsum_title": "જિપ્સમ અથવા સલ્ફર: pH ઘટાડવા માટે નાખો",
        "gypsum_advice": "જમીનનો pH ઘટાડવા જિપ્સમ ઉમેરો. યોગ્ય માત્રા માટે સ્થાનિક કૃષિ અધિકારીનો સંપર્ક કરો.",
        "soil_nutrients_ideal": "આ પાક માટે જમીનમાં પોષક તત્વો આદર્શ સ્તરે છે. ખાતરની જરૂર નથી.",
        "icar_standard": "ICAR કૃષિ ધોરણ",
        "live_soil_telemetry": "100% લાઈવ સોઈલ ટેલિમેટ્રી"
    },
    "pa": {
        "urea_name": "ਯੂਰੀਆ",
        "dap_name": "ਡੀਏਪੀ — ਡਾਈ-ਅਮੋਨੀਅਮ ਫਾਸਫੇਟ",
        "mop_name": "ਐਮਓਪੀ — ਮਿਊਰੀਏਟ ਆਫ ਪੋਟਾਸ਼",
        "fix_n_deficit": "ਨਾਈਟ੍ਰੋਜਨ ਦੀ ਘਾਟ ਪੂਰੀ ਕਰਨ ਲਈ",
        "fix_p_deficit": "ਫਾਸਫੋਰਸ ਦੀ ਘਾਟ ਪੂਰੀ ਕਰਨ ਲਈ",
        "fix_k_deficit": "ਪੋਟਾਸ਼ ਦੀ ਘਾਟ ਪੂਰੀ ਕਰਨ ਲਈ",
        "lime_title": "ਖੇਤੀ ਚੂਨਾ: pH ਵਧਾਉਣ ਲਈ ਪਾਓ",
        "lime_advice": "ਜ਼ਮੀਨ ਦਾ pH ਵਧਾਉਣ ਲਈ ਚੂਨਾ ਪਾਓ। ਸਹੀ ਮਾਤਰਾ ਲਈ ਖੇਤੀ ਮਾਹਿਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।",
        "gypsum_title": "ਜਿਪਸਮ ਜਾਂ ਗੰਧਕ: pH ਘਟਾਉਣ ਲਈ ਪਾਓ",
        "gypsum_advice": "ਜ਼ਮੀਨ ਦਾ pH ਘਟਾਉਣ ਲਈ ਜਿਪਸਮ ਪਾਓ। ਸਹੀ ਮਾਤਰਾ ਲਈ ਖੇਤੀ ਮਾਹਿਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।",
        "soil_nutrients_ideal": "ਇਸ ਫਸਲ ਲਈ ਮਿੱਟੀ ਵਿੱਚ ਪੌਸ਼ਟਿਕ ਤੱਤ ਉਚਿਤ ਪੱਧਰ 'ਤੇ ਹਨ। ਖਾਦ ਦੀ ਲੋੜ ਨਹੀਂ।",
        "icar_standard": "ICAR ਖੇਤੀਬਾੜੀ ਮਿਆਰ",
        "live_soil_telemetry": "100% ਲਾਈਵ ਮਿੱਟੀ ਟੈਲੀਮੈਟਰੀ"
    },
    "ur": {
        "urea_name": "یوریا",
        "dap_name": "ڈی اے پی — ڈائی امونیم فاسفیٹ",
        "mop_name": "ایم او پی — پوٹاش کھاد",
        "fix_n_deficit": "نائٹروجن کی کمی کو پورا کرنے کے لیے",
        "fix_p_deficit": "فاسفورس کی کمی کو پورا کرنے کے لیے",
        "fix_k_deficit": "پوٹاش کی کمی کو پورا کرنے کے لیے",
        "lime_title": "زرعی چونا: پی ایچ بڑھانے کے لیے ڈالیں",
        "lime_advice": "مٹی کی پی ایچ بڑھانے کے لیے چونا استعمال کریں۔ مقدار کے لیے زرعی ماہر سے مشورہ کریں۔",
        "gypsum_title": "جپسم یا گندھک: پی ایچ کم کرنے کے لیے ڈالیں",
        "gypsum_advice": "مٹی کی پی ایچ کم کرنے کے لیے جپسم استعمال کریں۔ مقدار کے لیے زرعی ماہر سے مشورہ کریں۔",
        "soil_nutrients_ideal": "اس فصل کے لیے مٹی کے غذائی اجزاء مثالی ہیں۔ کھاد کی ضرورت نہیں۔",
        "icar_standard": "ICAR زرعی معیار",
        "live_soil_telemetry": "100% لائیو سوائل ٹیلی میٹری"
    },
    "or": {
        "urea_name": "ୟୁରିଆ",
        "dap_name": "ଡିଏପି — ଡାଇ-ଆମୋନିୟମ ଫସଫେଟ୍",
        "mop_name": "ଏମଓପି — ମ୍ୟୁରେଟ୍ ଅଫ୍ ପୋଟାଶ୍",
        "fix_n_deficit": "ଯବକ୍ଷାରଜାନ ଅଭାବ ପୂରଣ ପାଇଁ",
        "fix_p_deficit": "ଫସଫରସ୍ ଅଭାବ ପୂରଣ ପାଇଁ",
        "fix_k_deficit": "ପୋଟାଶ୍ ଅଭାବ ପୂରଣ ପାଇଁ",
        "lime_title": "କୃଷି ଚୂନ: pH ବୃଦ୍ଧି ପାଇଁ ପ୍ରୟୋଗ କରନ୍ତୁ",
        "lime_advice": "ମାଟିର pH ବୃଦ୍ଧି ପାଇଁ ଚୂନ ପ୍ରୟୋଗ କରନ୍ତୁ। ସଠିକ୍ ପରିମାଣ ପାଇଁ କୃଷି ଅଧିକାରୀଙ୍କ ପରାମର୍ଶ ନିଅନ୍ତୁ।",
        "gypsum_title": "ଜିପସମ୍ ବା ଗନ୍ଧକ: pH ହ୍ରାସ ପାଇଁ ପ୍ରୟୋଗ କରନ୍ତୁ",
        "gypsum_advice": "ମାଟିର pH ହ୍ରାସ ପାଇଁ ଜିପସମ୍ ପ୍ରୟୋଗ କରନ୍ତୁ। ସଠିକ୍ ପରିମାଣ ପାଇଁ କୃଷି ଅଧିକାରୀଙ୍କ ପରାମର୍ଶ ନିଅନ୍ତୁ।",
        "soil_nutrients_ideal": "ଏହି ଫସଲ ପାଇଁ ମାଟିରେ ପୋଷକ ତତ୍ତ୍ୱ ଉପଯୁକ୍ତ ମାତ୍ରାରେ ଅଛି। କୌଣସି ସାର ଆବଶ୍ୟକ ନାହିଁ।",
        "icar_standard": "ICAR କୃଷି ମାନଦଣ୍ଡ",
        "live_soil_telemetry": "୧୦୦% ଲାଇଭ୍ ମୃତ୍ତିକା ଟେଲିମେଟ୍ରି"
    },
    "as": {
        "urea_name": "ইউৰিয়া",
        "dap_name": "ডিএপি — ডাই-এমোনিয়াম ফছফেট",
        "mop_name": "এমঅ'পি — মিউৰেট অৱ পটাছ",
        "fix_n_deficit": "নাইট্ৰ'জেনৰ নাটনি পূৰণ কৰিবলৈ",
        "fix_p_deficit": "ফছফৰাছৰ নাটনি পূৰণ কৰিবলৈ",
        "fix_k_deficit": "পটাছৰ নাটনি পূৰণ কৰিবলৈ",
        "lime_title": "কৃষি চূন: pH বঢ়াবলৈ প্ৰয়ୋগ কৰক",
        "lime_advice": "মাটিৰ pH বঢ়াবলৈ চূন প্ৰয়ୋগ কৰক। সঠিক পৰিমাণৰ বাবে কৃষি বিষয়াৰ পৰামৰ্শ লওক।",
        "gypsum_title": "জিপচাম বা ছালফাৰ: pH কমাবলৈ প্ৰয়ୋগ কৰক",
        "gypsum_advice": "মাটিৰ pH কমাবলৈ জিপচাম ব্যৱহাৰ কৰক। সঠিক পৰিমাণৰ বাবে কৃষি বিষয়াৰ পৰামৰ্শ লওক।",
        "soil_nutrients_ideal": "এই শস্যৰ বাবে মাটিত পুষ্টি উপাদান উপযুক্ত মাত্ৰাত আছে। সাৰৰ প্ৰয়োজন নাই।",
        "icar_standard": "ICAR কৃষি মানদণ্ড",
        "live_soil_telemetry": "১০০% লাইভ মাটিৰ টেলিমেট্ৰি"
    },
    "ne": {
        "urea_name": "युरिया",
        "dap_name": "डीएपी — डाइ-अमोनियम फस्फेट",
        "mop_name": "एमओपी — म्युरिएट अफ पोटास",
        "fix_n_deficit": "नाइट्रोजनको कमी पुरा गर्न",
        "fix_p_deficit": "फस्फोरसको कमी पुरा गर्न",
        "fix_k_deficit": "पोटासको कमी पुरा गर्न",
        "lime_title": "कृषि चुन: pH बढाउन प्रयोग गर्नुहोस्",
        "lime_advice": "माटोको pH बढाउन चुन प्रयोग गर्नुहोस्। उपयुक्त मात्राको लागि कृषि प्राविधिकसँग सल्लाह लिनुहोस्।",
        "gypsum_title": "जिप्सम वा सल्फर: pH घटाउन प्रयोग गर्नुहोस्",
        "gypsum_advice": "माटोको pH घटाउन जिप्सम प्रयोग गर्नुहोस्। उपयुक्त मात्राको लागि कृषि प्राविधिकसँग सल्लाह लिनुहोस्।",
        "soil_nutrients_ideal": "यो बालीको लागि माटोमा पोषक तत्व आदर्श स्तरमा छ। मलको आवश्यकता छैन।",
        "icar_standard": "ICAR कृषि मापदण्ड",
        "live_soil_telemetry": "१००% प्रत्यक्ष माटो टेलिमेट्री"
    },
    "si": {
        "urea_name": "යූරියා",
        "dap_name": "DAP — ඩයි-ඇමෝනියම් පොස්පේට්",
        "mop_name": "MOP — මියුරියේට් ඔෆ් පොටෑෂ්",
        "fix_n_deficit": "නයිට්‍රජන් ඌනතාවය සමනය කිරීමට",
        "fix_p_deficit": "පොස්පරස් ඌනතාවය සමනය කිරීමට",
        "fix_k_deficit": "පොටෑසියම් ඌනතාවය සමනය කිරීමට",
        "lime_title": "කෘෂිකාර්මික හුණු: pH අගය වැඩි කිරීමට යොදන්න",
        "lime_advice": "පසෙහි pH අගය වැඩි කිරීමට හුණු යොදන්න. නියමිත ප්‍රමාණය සඳහා කෘෂිකර්ම නිලධාරියා හමුවන්න.",
        "gypsum_title": "ජිප්සම් හෝ සල්ෆර්: pH අගය අඩු කිරීමට යොදන්න",
        "gypsum_advice": "පසෙහි pH අගය අඩු කිරීමට ජිප්සම් යොදන්න. නියමිත ප්‍රමාණය සඳහා කෘෂිකර්ම නිලධාරියා හමුවන්න.",
        "soil_nutrients_ideal": "මෙම බෝගය සඳහා පසෙහි පෝෂ්‍ය පදාර්ථ ප්‍රශස්ත මට්ටමක පවතී. පොහොර අවශ්‍ය නොවේ.",
        "icar_standard": "ICAR කෘෂිකාර්මික ප්‍රමිතිය",
        "live_soil_telemetry": "100% සජීවී පාංශු ටෙලිමෙට්‍රි"
    },
    "ar": {
        "urea_name": "اليوريا",
        "dap_name": "DAP — فوسفات ثنائي الأمونيوم",
        "mop_name": "MOP — كلوريد البوتاسيوم",
        "fix_n_deficit": "لمعالجة نقص النيتروجين",
        "fix_p_deficit": "لمعالجة نقص الفوسفور",
        "fix_k_deficit": "لمعالجة نقص البوتاسيوم",
        "lime_title": "الجير الزراعي: يوضع لرفع درجة الحموضة pH",
        "lime_advice": "أضف الجير الزراعي لرفع حموضة التربة. استشر المرشد الزراعي لمعرفة الكمية المناسبة.",
        "gypsum_title": "الجبس الزراعي أو الكبريت: يوضع لخفض درجة الحموضة pH",
        "gypsum_advice": "أضف الجبس لخفض حموضة التربة. استشر المرشد الزراعي لمعرفة الكمية المناسبة.",
        "soil_nutrients_ideal": "العناصر الغذائية في التربة عند المستويات المثالية لهذا المحصول. لا توجد حاجة للأسمدة.",
        "icar_standard": "معيار ICAR الزراعي",
        "live_soil_telemetry": "قياس حي لبيانات التربة بنسبة 100%"
    },
    "fr": {
        "urea_name": "Urée",
        "dap_name": "DAP — Phosphate di-ammonique",
        "mop_name": "MOP — Chlorure de potassium",
        "fix_n_deficit": "pour corriger le déficit en azote (N)",
        "fix_p_deficit": "pour corriger le déficit en phosphore (P)",
        "fix_k_deficit": "pour corriger le déficit en potassium (K)",
        "lime_title": "Chaux agricole : appliquer pour augmenter le pH",
        "lime_advice": "Appliquer de la chaux pour relever le pH du sol. Consulter un agronome pour le dosage précis.",
        "gypsum_title": "Gypse ou soufre : appliquer pour réduire le pH",
        "gypsum_advice": "Appliquer du gypse pour abaisser le pH du sol. Consulter un agronome pour le dosage précis.",
        "soil_nutrients_ideal": "Les nutriments du sol sont à des niveaux optimaux pour cette culture. Aucun engrais requis.",
        "icar_standard": "Norme agronomique ICAR",
        "live_soil_telemetry": "Télémétrie du sol 100% en direct"
    },
    "es": {
        "urea_name": "Urea",
        "dap_name": "DAP — Fosfato diamónico",
        "mop_name": "MOP — Cloruro de potasio",
        "fix_n_deficit": "para corregir el déficit de nitrógeno (N)",
        "fix_p_deficit": "para corregir el déficit de fósforo (P)",
        "fix_k_deficit": "para corregir el déficit de potasio (K)",
        "lime_title": "Cal agrícola: aplicar para elevar el pH",
        "lime_advice": "Aplique cal agrícola para elevar el pH del suelo. Consulte a un agrónomo para la cantidad adecuada.",
        "gypsum_title": "Yeso o azufre: aplicar para reducir el pH",
        "gypsum_advice": "Aplique yeso para reducir el pH del suelo. Consulte a un agrónomo para la cantidad adecuada.",
        "soil_nutrients_ideal": "Los nutrientes del suelo están en niveles ideales para este cultivo. No se requiere fertilizante.",
        "icar_standard": "Estándar agronómico ICAR",
        "live_soil_telemetry": "Telemetría del suelo 100% en vivo"
    },
    "pt": {
        "urea_name": "Ureia",
        "dap_name": "DAP — Fosfato diamónico",
        "mop_name": "MOP — Cloreto de potássio",
        "fix_n_deficit": "para corrigir o défice de azoto (N)",
        "fix_p_deficit": "para corrigir o défice de fósforo (P)",
        "fix_k_deficit": "para corrigir o défice de potássio (K)",
        "lime_title": "Calcário agrícola: aplicar para aumentar o pH",
        "lime_advice": "Aplique calcário para aumentar o pH do solo. Consulte um agrônomo para a quantidade exata.",
        "gypsum_title": "Gesso ou enxofre: aplicar para diminuir o pH",
        "gypsum_advice": "Aplique gesso para baixar o pH do solo. Consulte um agrônomo para a quantidade exata.",
        "soil_nutrients_ideal": "Os nutrientes do solo estão em níveis ideais para esta cultura. Nenhum fertilizante necessário.",
        "icar_standard": "Padrão Agronômico ICAR",
        "live_soil_telemetry": "Telemetria do solo 100% em tempo real"
    },
    "de": {
        "urea_name": "Harnstoff (Urea)",
        "dap_name": "DAP — Diammonphosphat",
        "mop_name": "MOP — Kaliumchlorid",
        "fix_n_deficit": "zur Behebung des Stickstoffdefizits (N)",
        "fix_p_deficit": "zur Behebung des Phosphordefizits (P)",
        "fix_k_deficit": "zur Behebung des Kaliumdefizits (K)",
        "lime_title": "Kohlensaurer Kalk: zur Anhebung des pH-Werts",
        "lime_advice": "Kalk auftragen, um den Boden-pH-Wert zu erhöhen. Fachberater für genaue Menge konsultieren.",
        "gypsum_title": "Gips oder Schwefel: zur Absenkung des pH-Werts",
        "gypsum_advice": "Gips auftragen, um den Boden-pH-Wert zu senken. Fachberater für genaue Menge konsultieren.",
        "soil_nutrients_ideal": "Die Bodennährstoffe liegen im optimalen Bereich. Keine Düngung erforderlich.",
        "icar_standard": "ICAR-Agrarstandard",
        "live_soil_telemetry": "100% Live-Bodentelemetrie"
    },
    "it": {
        "urea_name": "Urea",
        "dap_name": "DAP — Fosfato biammonico",
        "mop_name": "MOP — Cloruro di potassio",
        "fix_n_deficit": "per correggere il deficit di azoto (N)",
        "fix_p_deficit": "per correggere il deficit di fosforo (P)",
        "fix_k_deficit": "per correggere il deficit di potassio (K)",
        "lime_title": "Calce agricola: applicare per aumentare il pH",
        "lime_advice": "Applicare calce per aumentare il pH del suolo. Consultare un agronomo per il dosaggio preciso.",
        "gypsum_title": "Gesso o zolfo: applicare per ridurre il pH",
        "gypsum_advice": "Applicare gesso per abbassare il pH del suolo. Consultare un agronomo per il dosaggio preciso.",
        "soil_nutrients_ideal": "I nutrienti del suolo sono a livelli ideali per questa coltura. Nessun fertilizzante necessario.",
        "icar_standard": "Standard agronomico ICAR",
        "live_soil_telemetry": "Telemetria del suolo 100% in tempo reale"
    },
    "ru": {
        "urea_name": "Мочевина (Карбамид)",
        "dap_name": "ДАФ — Диаммонийфосфат",
        "mop_name": "Хлористый калий (MOP)",
        "fix_n_deficit": "для восполнения дефицита азота (N)",
        "fix_p_deficit": "для восполнения дефицита фосфора (P)",
        "fix_k_deficit": "для восполнения дефицита калия (K)",
        "lime_title": "Известь сельскохозяйственная: для повышения pH",
        "lime_advice": "Внесите известь для повышения pH почвы. Проконсультируйтесь с агрономом по дозировке.",
        "gypsum_title": "Гипс или сера: для снижения pH",
        "gypsum_advice": "Внесите гипс для снижения pH почвы. Проконсультируйтесь с агрономом по дозировке.",
        "soil_nutrients_ideal": "Питательные вещества почвы на идеальном уровне для этой культуры. Удобрения не требуются.",
        "icar_standard": "Агрономический стандарт ICAR",
        "live_soil_telemetry": "100% прямая телеметрия почвы"
    },
    "ja": {
        "urea_name": "尿素 (Urea)",
        "dap_name": "DAP — リン酸二アンモニウム",
        "mop_name": "MOP — 塩化カリウム",
        "fix_n_deficit": "窒素(N)不足を補正するため",
        "fix_p_deficit": "リン(P)不足を補正するため",
        "fix_k_deficit": "カリウム(K)不足を補正するため",
        "lime_title": "苦土石灰・消石灰: 土壌pH上昇のため施用",
        "lime_advice": "土壌pHを上げるために石灰を施用してください。適量については普及員にご相談ください。",
        "gypsum_title": "石膏または硫黄: 土壌pH低下のため施用",
        "gypsum_advice": "土壌pHを下げるために石膏を施用してください。適量については普及員にご相談ください。",
        "soil_nutrients_ideal": "この作物に必要な土壌養分は理想的な水準にあります。追肥の必要はありません。",
        "icar_standard": "ICAR農学基準",
        "live_soil_telemetry": "100% リアルタイム土壌テレメトリ"
    },
    "ko": {
        "urea_name": "요소 (Urea)",
        "dap_name": "DAP — 인산이암모늄",
        "mop_name": "MOP — 염화칼륨",
        "fix_n_deficit": "질소(N) 결핍 보충용",
        "fix_p_deficit": "인산(P) 결핍 보충용",
        "fix_k_deficit": "칼륨(K) 결핍 보충용",
        "lime_title": "농업용 석회: 토양 pH 상승을 위해 시비",
        "lime_advice": "토양 pH를 올리기 위해 소석회 또는 고토석회를 시비하세요. 시비량은 농업기술센터에 문의하세요.",
        "gypsum_title": "석고 또는 유황: 토양 pH 강하를 위해 시비",
        "gypsum_advice": "토양 pH를 낮추기 위해 석고를 시비하세요. 시비량은 농업기술센터에 문의하세요.",
        "soil_nutrients_ideal": "이 작물에 대한 토양 양분이 최적 수준입니다. 추가 비료 시비가 필요하지 않습니다.",
        "icar_standard": "ICAR 농경 표준 규격",
        "live_soil_telemetry": "100% 실시간 토양 원격측정"
    },
    "zh": {
        "urea_name": "尿素",
        "dap_name": "DAP — 磷酸二铵",
        "mop_name": "MOP — 氯化钾",
        "fix_n_deficit": "补充土壤氮素亏缺",
        "fix_p_deficit": "补充土壤磷素亏缺",
        "fix_k_deficit": "补充土壤钾素亏缺",
        "lime_title": "农用石灰：施用以提升土壤 pH",
        "lime_advice": "施用石灰以提高土壤酸碱度。施用量请咨询当地农技专家。",
        "gypsum_title": "石膏或硫磺：施用以降低土壤 pH",
        "gypsum_advice": "施用石膏以降低土壤碱性。施用量请咨询当地农技专家。",
        "soil_nutrients_ideal": "当前土壤养分完全满足该作物的理想需求，无需施用化学肥料。",
        "icar_standard": "ICAR 农学标准",
        "live_soil_telemetry": "100% 实时土壤物联网监测"
    }
}


# Multilingual sentence templates for crop recommendation agronomic reasons
REASON_TEMPLATES_25: Dict[str, Dict[str, str]] = {
    "en": {
        "prefix": "{crop} is highly recommended because it",
        "ph": "thrives at your current soil pH of {ph:.1f} (ideal: {ideal_ph})",
        "temp": "is well-suited for ambient temperature of {temp:.1f}°C",
        "hum": "is optimal for {humidity:.1f}% relative humidity",
        "n_fix": "biological nitrogen fixation naturally enriches depleted soil Nitrogen",
        "npk": "matches available soil NPK profile (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "ta": {
        "prefix": "{crop} பயிரிட பெரிதும் பரிந்துரைக்கப்படுகிறது, ஏனெனில் இது",
        "ph": "உங்கள் தற்போதைய மண் கார-அமிலத்தன்மை pH {ph:.1f} (உகந்தது: {ideal_ph}) நிலைக்கு மிகவும் பொருந்துகிறது",
        "temp": "சுற்றுப்புற வெப்பநிலை {temp:.1f}°C நிலைக்கு மிகவும் உகந்தது",
        "hum": "காற்றின் ஈரப்பதம் {humidity:.1f}% அளவிற்கு உகந்த வளர்ச்சியைக் கொடுக்கும்",
        "n_fix": "இயற்கையாகவே தழைச்சத்தை (Nitrogen) நிலைநிறுத்தி மண்ணின் வளத்தை அதிகரிக்கும்",
        "npk": "தற்போதைய NPK சத்துக்களுக்கு (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) முழுமையாகப் பொருந்துகிறது"
    },
    "te": {
        "prefix": "{crop} సాగు మీ భూమికి అత్యంత అనుకూలమైనది, ఎందుకంటే ఇది",
        "ph": "ప్రస్తుత నేల pH {ph:.1f} (ఆదర్శం: {ideal_ph}) వద్ద సమర్థవంతంగా పెరుగుతుంది",
        "temp": "వాతావరణ ఉష్ణోగ్రత {temp:.1f}°C వద్ద వేగంగా ఎదుగుతుంది",
        "hum": "గాలిలోని తేమ {humidity:.1f}% ఈ పంటకు అత్యంత అనుకూలం",
        "n_fix": "సహజ నత్రజని స్థిరీకరణ ద్వారా నేలలో నైట్రోజన్ శాతాన్ని పెంచుతుంది",
        "npk": "లభ్యమయ్యే నేల NPK పోషకాలకు (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) సరిగ్గా సరిపోతుంది"
    },
    "ml": {
        "prefix": "{crop} കൃഷി ചെയ്യാൻ വളരെ അനുയോജ്യമാണ്, കാരണം ഇത്",
        "ph": "നിലവിലെ മണ്ണിന്റെ pH {ph:.1f} (അനുയോജ്യം: {ideal_ph}) അനുയോജ്യമാണ്",
        "temp": "താപനില {temp:.1f}°C മികച്ച വളർച്ച നൽകുന്നു",
        "hum": "അന്തരീക്ഷ ഈർപ്പം {humidity:.1f}% ഈ വിളയ്ക്ക് ഏറ്റവും അനുയോജ്യമാണ്",
        "n_fix": "സ്വാഭാവിക നൈട്രജൻ സംയോജനത്തിലൂടെ മണ്ണിന്റെ ഫലഭൂയിഷ്ഠത വർദ്ധിപ്പിക്കുന്നു",
        "npk": "മണ്ണിലെ NPK പോഷക നിലയുമായി (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) പൊരുത്തപ്പെടുന്നു"
    },
    "kn": {
        "prefix": "{crop} ಬೆಳೆಯಲು ಹೆಚ್ಚು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ, ಏಕೆಂದರೆ ಇದು",
        "ph": "ನಿಮ್ಮ ಮಣ್ಣಿನ pH {ph:.1f} (ಸೂಕ್ತ: {ideal_ph}) ಸ್ಥಿತಿಗೆ ಉತ್ತಮವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ",
        "temp": "ವಾತಾವರಣದ ತಾಪಮಾನ {temp:.1f}°C ಗೆ ಸೂಕ್ತವಾಗಿದೆ",
        "hum": "ಆರ್ದ್ರತೆ {humidity:.1f}% ಬೆಳವಣಿಗೆಗೆ ಅತ್ಯುತ್ತಮವಾಗಿದೆ",
        "n_fix": "ನೈಸರ್ಗಿಕ ಸಾರಜನಕ ಸ್ಥಿರೀಕರಣದಿಂದ ಮಣ್ಣಿನ ಫಲವತ್ತತೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ",
        "npk": "ಲಭ್ಯವಿರುವ NPK ಪೋಷಕಾಂಶಗಳ ಮಟ್ಟಕ್ಕೆ (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) ಸಂಪೂರ್ಣ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ"
    },
    "hi": {
        "prefix": "{crop} की बुवाई की अत्यधिक अनुशंसा की जाती है क्योंकि यह",
        "ph": "वर्तमान मिट्टी के pH {ph:.1f} (आदर्श: {ideal_ph}) में तेजी से फलता-फूलता है",
        "temp": "परिवेशी तापमान {temp:.1f}°C के लिए पूरी तरह अनुकूल है",
        "hum": "सापेक्ष आर्द्रता {humidity:.1f}% पर सर्वोत्तम पैदावार देता है",
        "n_fix": "जैविक नाइट्रोजन स्थिरीकरण द्वारा मिट्टी में पोषक तत्वों को प्राकृतिक रूप से समृद्ध करता है",
        "npk": "उपलब्ध NPK पोषक तत्वों (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) के साथ उत्कृष्ट तालमेल रखता है"
    },
    "bn": {
        "prefix": "{crop} চাষের জন্য অত্যন্ত সুপারিশ করা হয় কারণ এটি",
        "ph": "বর্তমান মাটির pH {ph:.1f} (আদর্শ: {ideal_ph}) এ চমৎকার বৃদ্ধি পায়",
        "temp": "পরিবেশের তাপমাত্রা {temp:.1f}°C এর সাথে সম্পূর্ণরূপে উপযোগী",
        "hum": "আপেক্ষিক আর্দ্রতা {humidity:.1f}% এর জন্য সর্বোত্তম",
        "n_fix": "জৈব নাইট্রোজেন সংবদ্ধকরণের মাধ্যমে মাটির উর্বরতা বৃদ্ধি করে",
        "npk": "উপলব্ধ NPK পুষ্টিমানের (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) সাথে মানানসই"
    },
    "mr": {
        "prefix": "{crop} लागवडीची जोरदार शिफारस केली जाते कारण हे पीक",
        "ph": "जमिनीच्या सद्य pH {ph:.1f} (आदर्श: {ideal_ph}) मध्ये उत्कृष्ट वाढते",
        "temp": "तापमान {temp:.1f}°C साठी अत्यंत अनुकूल आहे",
        "hum": "हवेतील आर्द्रता {humidity:.1f}% साठी सर्वोत्तम आहे",
        "n_fix": "जैविक नत्र स्थिरीकरणाद्वारे जमिनीची सुपीकता नैसर्गिकरित्या वाढवते",
        "npk": "उपलब्ध NPK पोषण पातळीशी (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) तंतोतंत जुळते"
    },
    "gu": {
        "prefix": "{crop} વાવવા માટે ખૂબ ભલામણ કરવામાં આવે છે કારણ કે તે",
        "ph": "જમીનના pH {ph:.1f} (આદર્શ: {ideal_ph}) માટે ઉત્તમ છે",
        "temp": "તાપમાન {temp:.1f}°C માં ઝડપી વિકાસ કરે છે",
        "hum": "હવામાં ભેજ {humidity:.1f}% આ પાક માટે આદર્શ છે",
        "n_fix": "કુદરતી નાઇટ્રોજન ફિક્સેશન દ્વારા જમીનની ફળદ્રુપતા વધારે છે",
        "npk": "જમીનમાં ઉપલબ્ધ NPK સ્તર (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) સાથે મેળ ખાય છે"
    },
    "pa": {
        "prefix": "{crop} ਦੀ ਕਾਸ਼ਤ ਲਈ ਪੁਰਜ਼ੋਰ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿਉਂਕਿ ਇਹ",
        "ph": "ਮਿੱਟੀ ਦੇ pH {ph:.1f} (ਆਦਰਸ਼: {ideal_ph}) 'ਤੇ ਸ਼ਾਨਦਾਰ ਵਾਧਾ ਕਰਦੀ ਹੈ",
        "temp": "ਤਾਪਮਾਨ {temp:.1f}°C ਦੇ ਬਿਲਕੁਲ ਅਨੁਕੂਲ ਹੈ",
        "hum": "ਨਮੀ {humidity:.1f}% ਵਿੱਚ ਵਧੀਆ ਝਾੜ ਦਿੰਦੀ ਹੈ",
        "n_fix": "ਜੈਵਿਕ ਨਾਈਟ੍ਰੋਜਨ ਫਿਕਸੇਸ਼ਨ ਨਾਲ ਜ਼ਮੀਨ ਦੀ ਉਪਜਾਊ ਸ਼ਕਤੀ ਵਧਾਉਂਦੀ ਹੈ",
        "npk": "ਮੌਜੂਦਾ NPK ਪੌਸ਼ਟਿਕ ਤੱਤਾਂ (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) ਦੇ ਅਨੁਕੂਲ ਹੈ"
    },
    "ur": {
        "prefix": "{crop} کی کاشت کی بھرپور سفارش کی جاتی ہے کیونکہ یہ",
        "ph": "مٹی کے موجودہ pH {ph:.1f} (مثالی: {ideal_ph}) پر بہترین نشوونما پاتی ہے",
        "temp": "موسمی درجہ حرارت {temp:.1f}°C کے عین مطابق ہے",
        "hum": "ہوا کی نمی {humidity:.1f}% اس فصل کے لیے بہترین ہے",
        "n_fix": "قدرتی نائٹروجن فکسیشن کے ذریعے مٹی کی زرخیزی میں اضافہ کرتی ہے",
        "npk": "دستیاب NPK غذائی اجزاء (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) کے ساتھ مطابقت رکھتی ہے"
    },
    "or": {
        "prefix": "{crop} ଚାଷ ପାଇଁ ଉଚ୍ଚ ସୁପାରିଶ କରାଯାଉଛି କାରଣ ଏହା",
        "ph": "ମାଟିର pH {ph:.1f} (ଆଦର୍ଶ: {ideal_ph}) ସ୍ଥିତିରେ ଉତ୍ତମ ବୃଦ୍ଧି ପାଏ",
        "temp": "ତାପମାତ୍ରା {temp:.1f}°C ସହିତ ସମ୍ପୂର୍ଣ୍ଣ ଅନୁକୂଳ",
        "hum": "ଆର୍ଦ୍ରତା {humidity:.1f}% ଏହି ଫସଲ ପାଇଁ ଉପଯୁକ୍ତ",
        "n_fix": "ଜୈବିକ ଯବକ୍ଷାରଜାନ ସ୍ଥିରୀକରଣ ଦ୍ୱାରା ମାଟିର ଉର୍ବରତା ବୃଦ୍ଧି କରେ",
        "npk": "ଉପଲବ୍ଧ NPK ପୋଷକ ତତ୍ତ୍ୱ (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) ସହ ଖାପ ଖାଏ"
    },
    "as": {
        "prefix": "{crop} খেতিৰ বাবে অত্যন্ত পৰামৰ্শ দিয়া হৈছে কাৰণ ই",
        "ph": "মাটিৰ pH {ph:.1f} (আদৰ্শ: {ideal_ph}) ত সুন্দৰভাৱে বৃদ্ধি পায়",
        "temp": "উত্তাপ {temp:.1f}°C ৰ সৈতে সম্পূৰ্ণ উপযুক্ত",
        "hum": "বায়ুৰ আৰ্দ্ৰতা {humidity:.1f}% শস্যৰ বাবে সৰ্বোত্তম",
        "n_fix": "জৈৱিক নাইট্ৰ'জেন সংযোজনৰ জৰিয়তে মাটিৰ উৰ্বৰতা বৃদ্ধি কৰে",
        "npk": "উপলব্ধ NPK উপাদানৰ (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) সৈতে মিলি যায়"
    },
    "ne": {
        "prefix": "{crop} खेतीको लागि अत्यधिक सिफारिस गरिन्छ किनभने यो",
        "ph": "माटोको pH {ph:.1f} (आदर्श: {ideal_ph}) मा राम्रोसँग सप्रन्छ",
        "temp": "तापक्रम {temp:.1f}°C को लागि पूर्ण अनुकूल छ",
        "hum": "हावाको आर्द्रता {humidity:.1f}% मा राम्रो उत्पादन दिन्छ",
        "n_fix": "प्राकृतिक नाइट्रोजन स्थिरीकरणद्वारा माटोको उर्बराशक्ति बढाउँछ",
        "npk": "उपलब्ध NPK पोषक तत्व (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) सँग मेल खान्छ"
    },
    "si": {
        "prefix": "{crop} වගාව සඳහා ඉතා යෝග්‍ය වේ, මන්ද එය",
        "ph": "පසෙහි pH අගය {ph:.1f} (සුදුසු: {ideal_ph}) යටතේ සරුවට වැඩේ",
        "temp": "උෂ්ණත්වය {temp:.1f}°C සඳහා ඉතා හිතකර වේ",
        "hum": "ආර්ද්‍රතාවය {humidity:.1f}% යටතේ උපරිම අස්වැන්නක් ලබා දේ",
        "n_fix": "ස්වාභාවික නයිට්‍රජන් තැන්පත් කිරීම මගින් පසේ සාරවත් බව වැඩි කරයි",
        "npk": "පවතින NPK පෝෂක මට්ටම් (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) සමඟ මනාව ගැලපේ"
    },
    "ar": {
        "prefix": "يوصى بشدة بزراعة {crop} لأنها",
        "ph": "تزدهر في درجة حموضة التربة الحالية {ph:.1f} (المثالية: {ideal_ph})",
        "temp": "تتناسب تماماً مع درجة حرارة الجو {temp:.1f}°C",
        "hum": "مثالية في رطوبة نسبية تبلغ {humidity:.1f}%",
        "n_fix": "تثري التربة طبيعياً بالنيتروجين عبر التثبيت الحيوي",
        "npk": "تتطابق بدقة مع مستويات العناصر الغذائية NPK المتوفرة (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "fr": {
        "prefix": "La culture de {crop} est vivement recommandée car elle",
        "ph": "prospère avec le pH du sol actuel de {ph:.1f} (idéal : {ideal_ph})",
        "temp": "est parfaitement adaptée à la température de {temp:.1f}°C",
        "hum": "bénéficie d'une humidité relative optimale de {humidity:.1f}%",
        "n_fix": "enrichit naturellement le sol grâce à la fixation biologique de l'azote",
        "npk": "correspond parfaitement au profil nutritif NPK disponible (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "es": {
        "prefix": "El cultivo de {crop} es altamente recomendado porque",
        "ph": "prospera en el pH actual del suelo de {ph:.1f} (ideal: {ideal_ph})",
        "temp": "se adapta perfectamente a la temperatura ambiente de {temp:.1f}°C",
        "hum": "es óptimo para la humedad relativa del {humidity:.1f}%",
        "n_fix": "enriquece el suelo naturalmente mediante la fijación biológica de nitrógeno",
        "npk": "coincide con los nutrientes NPK disponibles en el suelo (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "pt": {
        "prefix": "O cultivo de {crop} é altamente recomendado porque",
        "ph": "prospera no pH atual do solo de {ph:.1f} (ideal: {ideal_ph})",
        "temp": "adapta-se perfeitamente à temperatura ambiente de {temp:.1f}°C",
        "hum": "é ideal para a humidade relativa de {humidity:.1f}%",
        "n_fix": "enriquece o solo naturalmente através da fixação biológica de azoto",
        "npk": "corresponde ao perfil de nutrientes NPK disponível (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "de": {
        "prefix": "Der Anbau von {crop} wird dringend empfohlen, da diese Kultur",
        "ph": "beim aktuellen Boden-pH-Wert von {ph:.1f} (ideal: {ideal_ph}) optimal gedeiht",
        "temp": "hervorragend an die Umgebungstemperatur von {temp:.1f}°C angepasst ist",
        "hum": "eine optimale Luftfeuchtigkeit von {humidity:.1f}% vorfindet",
        "n_fix": "durch biologische Stickstofffixierung den Boden auf natürliche Weise bereichert",
        "npk": "exakt zum verfügbaren NPK-Nährstoffprofil (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) passt"
    },
    "it": {
        "prefix": "La coltivazione di {crop} è altamente raccomandata poiché",
        "ph": "prospera con l'attuale pH del suolo di {ph:.1f} (ideale: {ideal_ph})",
        "temp": "si adatta perfettamente alla temperatura di {temp:.1f}°C",
        "hum": "è ottimale con l'umidità relativa del {humidity:.1f}%",
        "n_fix": "arricchisce naturalmente il suolo grazie alla fissazione biologica dell'azoto",
        "npk": "corrisponde al profilo di nutrienti NPK disponibile (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "ru": {
        "prefix": "Выращивание культуры {crop} настоятельно рекомендуется, так как она",
        "ph": "активно развивается при текущем pH почвы {ph:.1f} (идеально: {ideal_ph})",
        "temp": "отлично адаптирована к температуре воздуха {temp:.1f}°C",
        "hum": "оптимальна для влажности воздуха {humidity:.1f}%",
        "n_fix": "естественным путем обогащает почву азотом за счет биологической фиксации",
        "npk": "соответствует доступному профилю макроэлементов NPK (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})"
    },
    "ja": {
        "prefix": "{crop} の栽培が強く推奨されます。その理由は、",
        "ph": "現在の土壌pH {ph:.1f} (理想値: {ideal_ph}) に非常に適していること",
        "temp": "気温 {temp:.1f}°C での順調な生育が見込めること",
        "hum": "相対湿度 {humidity:.1f}% が生育に最適であること",
        "n_fix": "生物的窒素固定により土壌の地力を自然に高めること",
        "npk": "土壌中の有効NPK養分 (N:{n:.0f}, P:{p:.0f}, K:{k:.0f}) と合致していること"
    },
    "ko": {
        "prefix": "{crop} 재배를 강력히 권장합니다. 그 이유는",
        "ph": "현재 토양 pH {ph:.1f} (이상적: {ideal_ph}) 환경에서 생육이 우수하며",
        "temp": "기온 {temp:.1f}°C 조건에 매우 적합하고",
        "hum": "상대습도 {humidity:.1f}%에서 최적의 생장을 보이며",
        "n_fix": "생물학적 질소 고정을 통해 토양 지력을 자연스럽게 증진하고",
        "npk": "토양의 NPK 양분 함량 (N:{n:.0f}, P:{p:.0f}, K:{k:.0f})과 잘 맞기 때문입니다."
    },
    "zh": {
        "prefix": "强烈推荐种植 {crop}，原因在于：",
        "ph": "非常适宜当前土壤 pH 值 {ph:.1f}（理想值：{ideal_ph}）",
        "temp": "完全契合环境温度 {temp:.1f}°C",
        "hum": "非常符合当前相对湿度 {humidity:.1f}% 的生长需求",
        "n_fix": "通过生物固氮作用天然培肥土壤",
        "npk": "与土壤当前的 NPK 养分水平（N:{n:.0f}，P:{p:.0f}，K:{k:.0f}）高度吻合"
    }
}


def build_crop_reason(
    crop_key: str,
    ph: float,
    ideal_ph: float,
    temp: float,
    ideal_temp: float,
    humidity: float,
    ideal_hum: float,
    raw_n: float,
    p: float,
    k: float,
    is_legume: bool,
    lang: str = "en"
) -> Tuple[str, str]:
    """Generates localized crop name and natural language agronomic reason in user's language."""
    norm_lang = (lang or "en").lower().strip()
    if norm_lang not in REASON_TEMPLATES_25:
        norm_lang = "en"

    crop_name = get_crop_display_name(crop_key, norm_lang)
    tmpl = REASON_TEMPLATES_25[norm_lang]

    parts: List[str] = []
    if abs(ph - ideal_ph) <= 1.2:
        parts.append(tmpl["ph"].format(ph=ph, ideal_ph=ideal_ph))
    if abs(temp - ideal_temp) <= 7.0:
        parts.append(tmpl["temp"].format(temp=temp))
    if abs(humidity - ideal_hum) <= 25.0:
        parts.append(tmpl["hum"].format(humidity=humidity))

    if raw_n == 0 or is_legume:
        parts.append(tmpl["n_fix"])
    else:
        parts.append(tmpl["npk"].format(n=raw_n, p=p, k=k))

    prefix = tmpl["prefix"].format(crop=crop_name)
    
    # Language-specific conjunctions
    if norm_lang in ["ja", "ko", "zh"]:
        reason = f"{prefix} { '、'.join(parts) }。"
    elif norm_lang == "ar":
        reason = f"{prefix} {'، و'.join(parts)}."
    elif norm_lang == "ur":
        reason = f"{prefix} {'، اور '.join(parts)}۔"
    elif norm_lang in ["ta", "te", "ml", "kn"]:
        reason = f"{prefix} {', '.join(parts)}."
    else:
        reason = f"{prefix} {', and '.join(parts)}."

    return crop_name, reason


def build_fertilizer_recommendation(
    n_deficit: float,
    p_deficit: float,
    k_deficit: float,
    ph: float,
    ideal_ph: float,
    urea_qty: float,
    dap_qty: float,
    mop_qty: float,
    lang: str = "en"
) -> Dict[str, Any]:
    """Generates structured and localized fertilizer & soil amendment recommendations."""
    norm_lang = (lang or "en").lower().strip()
    if norm_lang not in FERTILIZERS_25:
        norm_lang = "en"

    trans = FERTILIZERS_25[norm_lang]
    items: List[Dict[str, Any]] = []

    if n_deficit > 0:
        items.append({
            "type": "urea",
            "name": trans["urea_name"],
            "quantity": urea_qty,
            "unit": "kg/ha",
            "reason": trans["fix_n_deficit"],
            "grade": "46% N"
        })

    if p_deficit > 0:
        items.append({
            "type": "dap",
            "name": trans["dap_name"],
            "quantity": dap_qty,
            "unit": "kg/ha",
            "reason": trans["fix_p_deficit"],
            "grade": "46% P, 18% N"
        })

    if k_deficit > 0:
        items.append({
            "type": "mop",
            "name": trans["mop_name"],
            "quantity": mop_qty,
            "unit": "kg/ha",
            "reason": trans["fix_k_deficit"],
            "grade": "60% K"
        })

    ph_amendment = None
    if ph < 6.0:
        ph_amendment = {
            "action": "raise",
            "title": trans["lime_title"],
            "advice": trans["lime_advice"]
        }
    elif ph > 7.5:
        ph_amendment = {
            "action": "lower",
            "title": trans["gypsum_title"],
            "advice": trans["gypsum_advice"]
        }

    no_fert_needed = (n_deficit <= 0 and p_deficit <= 0 and k_deficit <= 0)

    return {
        "no_fertilizer_needed": no_fert_needed,
        "no_fertilizer_message": trans["soil_nutrients_ideal"] if no_fert_needed else "",
        "items": items,
        "ph_amendment": ph_amendment,
        "standards": {
            "icar_standard": trans["icar_standard"],
            "live_soil_telemetry": trans["live_soil_telemetry"]
        }
    }


# Localized Disease Progression & Treatment Synthesis for all 25 Languages
PATHOLOGY_TEMPLATES_25: Dict[str, Dict[str, Any]] = {
    "en": {
        "bacterial_msg": "Live soil moisture ({moist}%) and ambient temperature ({temp}°C) are generating leaf tissue water-soaking, accelerating bacterial entry and vascular infiltration of {dis} across your field.",
        "fungal_msg": "Live canopy humidity ({hum}%) and ambient temperature ({temp}°C) combined with upcoming {cond} ({rain}% precipitation chance) generate extended leaf wetness (>6h). This accelerates fungal spore germination, lesion expansion, and secondary conidial dispersal of {dis}.",
        "viral_msg": "Micro-climate temperature ({temp}°C) and wind conditions ({wind} km/h) are accelerating insect vector activity (whiteflies/thrips), driving systemic spread of {dis}.",
        "pesticide_fungal": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (or Mancozeb 75% WP)",
        "pesticide_bacterial": "Copper Oxychloride 50% WP + Streptocycline (90:10)",
        "pesticide_viral": "Imidacloprid 17.8% SL (or Thiamethoxam 25% WG)",
        "steps_fungal": "1. Prune and safely destroy severely infected lower leaves to increase air circulation.\n2. Pause overhead sprinkler irrigation to keep canopy dry.\n3. Apply protective broad-spectrum fungicide spray within 24 hours.",
        "steps_bacterial": "1. Prune and safely incinerate heavily water-soaked infected leaves.\n2. Avoid field scouting or operations while foliage is wet.\n3. Apply targeted copper-bactericide tank mix within 24 hours.",
        "steps_viral": "1. Rogue and safely destroy severely stunted, viral-infected plants.\n2. Install 15–20 yellow and blue sticky traps per acre to monitor vector threshold.\n3. Apply targeted systemic insecticide to suppress vector population.",
        "dosage_fungal": "1 ml per litre of water (200 ml in 200 L water per acre) OR Mancozeb @ 2.5 g/L (500 g/acre)",
        "dosage_bacterial": "Copper Oxychloride @ 2.5 g/L + Streptocycline @ 0.6 g / 10 L water (500 g COC + 12 g Strepto per acre)",
        "dosage_viral": "0.5 ml per litre of water (100 ml in 200 L water per acre)",
        "timing": "Early morning (6:00–8:30 AM) during calm wind conditions before high temperatures",
        "precaution": "Wear protective face mask and gloves. Avoid spraying during peak pollination hours."
    },
    "ta": {
        "bacterial_msg": "மண் ஈரப்பதம் ({moist}%) மற்றும் வெப்பநிலை ({temp}°C) இலைகளில் நீர் தேக்கத்தை உண்டாக்கி, {dis} பாக்டீரியா கிருமிகள் இலைத்துளைகள் வழியாக வேகமாகப் பரவச் செய்கிறது.",
        "fungal_msg": "பயிர்க் காற்றில் ஈரப்பதம் ({hum}%) மற்றும் வெப்பநிலை ({temp}°C) உடன் வரவிருக்கும் {cond} ({rain}% மழை வாய்ப்பு) {dis} பூஞ்சை வித்துக்கள் முளைப்பதையும் நோய் பரவலையும் தீவிரப்படுத்துகிறது.",
        "viral_msg": "வெப்பநிலை ({temp}°C) மற்றும் காற்று ({wind} km/h) அசுவினி/வெள்ளை ஈக்கள் போன்ற பூச்சிகளின் நடமாட்டத்தை அதிகரித்து {dis} வைரஸை வேகமாகப் பரப்புகிறது.",
        "pesticide_fungal": "அஸாக்ஸிஸ்ட்ரோபின் 18.2% + டிஃபெனோகோனசோல் 11.4% SC (அல்லது மான்கோசெப் 75% WP)",
        "pesticide_bacterial": "காப்பர் ஆக்ஸிகுளோரைடு 50% WP + ஸ்ட்ரெப்டோசைக்ளின் (90:10)",
        "pesticide_viral": "இமிடாக்ளோப்ரிட் 17.8% SL (அல்லது தையமீதாக்ஸம் 25% WG)",
        "steps_fungal": "1. அதிகம் பாதிக்கப்பட்ட அடி இலைகளைப் பறித்து அப்புறப்படுத்தவும்.\n2. மேல் தெளிப்பு நீர்ப்பாசனத்தைத் தற்காலிகமாக நிறுத்தவும்.\n3. 24 மணி நேரத்திற்குள் பரிந்துரைக்கப்பட்ட பூஞ்சாணக் கொல்லியைத் தெளிக்கவும்.",
        "steps_bacterial": "1. பாதிக்கப்பட்ட இலைகளை அகற்றி வயலுக்கு வெளியே அப்புறப்படுத்தவும்.\n2. இலைகள் ஈரமாக இருக்கும் போது வயலில் வேலை செய்வதைத் தவிர்க்கவும்.\n3. 24 மணி நேரத்திற்குள் பரிந்துரைக்கப்பட்ட பாக்டீரியா கொல்லியைத் தெளிக்கவும்.",
        "steps_viral": "1. பாதிக்கப்பட்ட செடிகளைப் பிடுங்கி அழிக்கவும்.\n2. ஏக்கருக்கு 15-20 மஞ்சள் மற்றும் நீல நிற ஒட்டும் பொறிகளை அமைக்கவும்.\n3. பூச்சி பரவுவதைத் தடுக்க பரிந்துரைக்கப்பட்ட பூச்சிக்கொல்லியைத் தெளிக்கவும்.",
        "dosage_fungal": "1 மி.லி / லிட்டர் தண்ணீர் (ஏக்கருக்கு 200 மி.லி / 200 லிட்டர் தண்ணீர்) அல்லது மான்கோசெப் @ 2.5g/L",
        "dosage_bacterial": "காப்பர் ஆக்ஸிகுளோரைடு 2.5g/L + ஸ்ட்ரெப்டோசைக்ளின் 0.6g / 10L தண்ணீர் (ஏக்கருக்கு 500g COC + 12g)",
        "dosage_viral": "0.5 மி.லி / லிட்டர் தண்ணீர் (ஏக்கருக்கு 100 மி.லி / 200 லிட்டர் தண்ணீர்)",
        "timing": "காலை வேளையில் (6:00–8:30 AM) அமைதியான காற்றில் மழைக்கு முன் தெளிக்கவும்",
        "precaution": "முகக்கவசம் மற்றும் கையுறைகளை அணியவும். தேனீக்கள் நடமாட்டத்தின் போது தெளிப்பதைத் தவிர்க்கவும்."
    },
    "te": {
        "bacterial_msg": "నేలలో తేమ ({moist}%) మరియు ఉష్ణోగ్రత ({temp}°C) ఆకులపై నీటి నిల్వను పెంచి, {dis} బాక్టీరియా పత్రరంధ్రాల ద్వారా వేగంగా వ్యాపించడానికి కారణమవుతున్నాయి.",
        "fungal_msg": "గాలిలోని తేమ ({hum}%) మరియు ఉష్ణోగ్రత ({temp}°C) తో పాటు రాబోయే {cond} ({rain}% వర్ష సూచన) {dis} శిలీంధ్ర బీజాల మొలకెత్తడాన్ని మరియు వ్యాప్తిని తీవ్రతరం చేస్తున్నాయి.",
        "viral_msg": "ఉష్ణోగ్రత ({temp}°C) మరియు గాలి ({wind} km/h) తెల్లదోమలు, తామర పురుగుల తీవ్రతను పెంచి {dis} వైరస్ వ్యాప్తిని వేగవంతం చేస్తున్నాయి.",
        "pesticide_fungal": "అజోక్సిస్ట్రోబిన్ 18.2% + డైఫెనోకోనజోల్ 11.4% SC (లేదా మాంకోజెబ్ 75% WP)",
        "pesticide_bacterial": "కాపర్ ఆక్సిక్లోరైడ్ 50% WP + స్ట్రెప్టోసైక్లిన్ (90:10)",
        "pesticide_viral": "ఇమిడాక్లోప్రిడ్ 17.8% SL (లేదా థయామెథోక్సామ్ 25% WG)",
        "steps_fungal": "1. తీవ్రంగా సోకిన అడుగు ఆకులను తొలగించి నాశనం చేయండి.\n2. పైపాటు తుంపర నీటిపారుదలని తాత్కాలికంగా నిలిపివేయండి.\n3. 24 గంటల్లో సిఫార్సు చేసిన శిలీంధ్ర సంహారిణిని పిచికారీ చేయండి.",
        "steps_bacterial": "1. తెగులు సోకిన ఆకులను కత్తిరించి పొలం బయట కాల్చివేయండి.\n2. ఆకులు తడిగా ఉన్నప్పుడు పంటలో పనులు చేయకండి.\n3. 24 గంటల్లో కాపర్ బాక్టీరిసైడ్ పిచికారీ చేయండి.",
        "steps_viral": "1. వైరస్ సోకిన మొక్కలను పీకి నాశనం చేయండి.\n2. ఎకరానికి 15-20 పసుపు, నీలి రంగు జిగురు బుట్టలను అమర్చండి.\n3. రసం పీల్చే పురుగుల నివారణకు సిఫార్సు చేసిన మందులను పిచికారీ చేయండి.",
        "dosage_fungal": "1 మి.లీ / లీటరు నీటికి (ఎకరానికి 200 మి.లీ / 200 లీటర్ల నీటిలో)",
        "dosage_bacterial": "కాపర్ ఆక్సిక్లోరైడ్ 2.5 గ్రా/లీ + స్ట్రెప్టోసైక్లిన్ 0.6 గ్రా / 10 లీటర్ల నీటికి",
        "dosage_viral": "0.5 మి.లీ / లీటరు నీటికి (ఎకరానికి 100 మి.లీ / 200 లీటర్ల నీటిలో)",
        "timing": "ఉదయం వేళల్లో (6:00–8:30 AM) గాలి వేగం తక్కువగా ఉన్నప్పుడు పిచికారీ చేయండి",
        "precaution": "ముసుగు మరియు చేతి తొడుగులు ధరించండి. తేనెటీగల సంచార సమయంలో పిచికారీ చేయవద్దు."
    },
    "hi": {
        "bacterial_msg": "मिट्टी की नमी ({moist}%) और हवा का तापमान ({temp}°C) पत्तियों में जलभराव पैदा कर रहे हैं, जिससे {dis} के जीवाणु रंध्रों के माध्यम से तेजी से फैल रहे हैं।",
        "fungal_msg": "सापेक्ष आर्द्रता ({hum}%) और तापमान ({temp}°C) के साथ आगामी {cond} ({rain}% वर्षा संभावना) {dis} के कवक बीजाणुओं के अंकुरण और पत्तों पर फैलाव को अत्यधिक तेज कर रहे हैं।",
        "viral_msg": "तापमान ({temp}°C) और मौसम परिस्थितियां कीट वाहकों (सफेद मक्खी/थ्रिप्स) की गतिविधि बढ़ा रही हैं, जो {dis} वायरस को फैला रहे हैं।",
        "pesticide_fungal": "एज़ोक्सीस्ट्रोबिन 18.2% + डिफेनोकोनाज़ोल 11.4% SC (या मैंकोज़ेब 75% WP)",
        "pesticide_bacterial": "कॉपर ऑक्सीक्लोराइड 50% WP + स्ट्रेप्टोसाइक्लिन (90:10)",
        "pesticide_viral": "इमिडाक्लोप्रिड 17.8% SL (या थायमेथॉक्सम 25% WG)",
        "steps_fungal": "1. गंभीर रूप से संक्रमित निचली पत्तियों को तुरंत छांटकर नष्ट करें।\n2. पत्तियों को सूखा रखने के लिए फव्वारा सिंचाई रोकें।\n3. 24 घंटे के भीतर लक्षित कवकनाशी का सुरक्षात्मक छिड़काव करें।",
        "steps_bacterial": "1. प्रभावित पत्तियों और टहनियों को काटकर खेत से दूर नष्ट करें।\n2. गीले पत्तों के समय खेत में काम करने से बचें।\n3. 24 घंटे के भीतर अनुशंसित जीवाणुनाशक का छिड़काव करें।",
        "steps_viral": "1. विषाणु ग्रस्त पौधों को उखाड़कर तुरंत नष्ट करें।\n2. खेत में पीले और नीले चिपचिपे जाल लगाएं।\n3. कीट वाहक को नियंत्रित करने हेतु अनुशंसित कीटनाशक का छिड़काव करें।",
        "dosage_fungal": "1 मिली/लीटर पानी (200 मिली प्रति एकड़ 200 लीटर पानी में) या मैंकोज़ेब @ 2.5 ग्राम/लीटर",
        "dosage_bacterial": "कॉपर ऑक्सीक्लोराइड 2.5 ग्राम/लीटर + स्ट्रेप्टोसाइक्लिन 0.6 ग्राम प्रति 10 लीटर पानी",
        "dosage_viral": "0.5 मिली प्रति लीटर पानी (100 मिली प्रति एकड़ 200 लीटर पानी में)",
        "timing": "सुबह (6:00–8:30 AM) जब हवा शांत हो और बारिश से पहले",
        "precaution": "चेहरे पर मास्क और दस्ताने पहनें। परागण के समय कीटनाशक का प्रयोग न करें।"
    },
    "ja": {
        "bacterial_msg": "土壌水分 ({moist}%) と気温 ({temp}°C) が葉の水浸状病斑を助長し、{dis} の細菌が気孔を通じて急速に感染拡大しています。",
        "fungal_msg": "相対湿度 ({hum}%) と気温 ({temp}°C)、および今後の {cond} (降雨確率 {rain}%) により葉の濡れ時間が長期化し、{dis} の糸状菌胞子の発芽と蔓延が急加速しています。",
        "viral_msg": "現在の微気象（気温 {temp}°C、風速 {wind} km/h）が媒介害虫（コナジラミやアザミウマ）の活動を活性化させ、{dis} ウイルスの全身感染を広げています。",
        "pesticide_fungal": "アゾキシストロビン + ジフェノコナゾール水和剤 (または マンコゼブ水和剤)",
        "pesticide_bacterial": "塩基性塩化銅水和剤 + ストレプトマイシン液剤",
        "pesticide_viral": "イミダクロプリドフロアブル (または チアメトキサム水溶剤)",
        "steps_fungal": "1. 感染した下葉を除去し、圃場外で適切に処分してください。\n2. 葉の濡れを防ぐため上部散水灌漑を一時停止してください。\n3. 24時間以内に保護殺菌剤を散布してください。",
        "steps_bacterial": "1. 水浸状の病斑葉を剪定し、安全に焼却・処分してください。\n2. 葉が濡れている間の圃場作業は避けてください。\n3. 銅剤主体の殺菌剤を24時間以内に散布してください。",
        "steps_viral": "1. ウイルス感染株を抜き取って直ちに処分してください。\n2. 1エーカーあたり15〜20枚の黄色・青色粘着板を設置してください。\n3. 媒介害虫防除用の浸透移行性殺虫剤を散布してください。",
        "dosage_fungal": "水1リットルあたり 1ml（1エーカーあたり薬液200Lに200ml希釈）",
        "dosage_bacterial": "塩基性塩化銅 2.5g/L + ストレプトマイシン 0.6g / 10L水",
        "dosage_viral": "水1リットルあたり 0.5ml（1エーカーあたり100ml）",
        "timing": "風が穏やかな早朝（午前6:00〜8:30）、降雨前または高温前",
        "precaution": "防護マスクとゴム手袋を着用してください。開花期のミツバチ活動時は散布を避けてください。"
    },
    "ar": {
        "bacterial_msg": "تتسبب رطوبة التربة الحالية ({moist}%) ودرجة الحرارة ({temp}°C) في تشبع أنسجة الأوراق بالماء، مما يسرع من اختراق بكتيريا {dis} عبر الثغور وانتشارها في الحقل.",
        "fungal_msg": "تؤدي رطوبة الغطاء النباتي ({hum}%) ودرجة الحرارة ({temp}°C) مع توقعات {cond} (فرصة هطول أمطار {rain}%) إلى استمرار بلل الأوراق، مما يسرع من إنبات أبواغ {dis} الفطرية وتفشي المرض.",
        "viral_msg": "تؤدي درجة الحرارة ({temp}°C) وحركة الرياح ({wind} كم/س) إلى تسريع نشاط الحشرات الناقلة (الذبابة البيضاء/التريبس)، مما ينشر فيروس {dis}.",
        "pesticide_fungal": "أزوكسيستروبين 18.2% + ديفينوكونازول 11.4% SC (أو مانكوزيب 75% WP)",
        "pesticide_bacterial": "أوكسي كلوريد النحاس 50% WP + ستريبتوسيكلين (90:10)",
        "pesticide_viral": "إيميداكلوبريد 17.8% SL (أو ثياميثوكسام 25% WG)",
        "steps_fungal": "1. تقليم الأوراق السفلية المصابة والتخلص منها خارج الحقل.\n2. إيقاف الري بالرش الرأسي لإبقاء الأوراق جافة.\n3. رش مبيد فطري وقائي واسع المدى خلال 24 ساعة.",
        "steps_bacterial": "1. إزالة الأوراق المصابة المشبعة بالماء والتخلص منها بأمان.\n2. تجنب العمل في الحقل أثناء بلل النباتات.\n3. تطبيق مركب نحاسي مبيد للبكتيريا خلال 24 ساعة.",
        "steps_viral": "1. اقتلاع النباتات المصابة بالفيروس والتخلص منها فوراً.\n2. تثبيت المصائد اللاصقة الصفراء والزرقاء في الحقل.\n3. رش مبيد حشري جهازي معتمد لمكافحة الحشرات الناقلة.",
        "dosage_fungal": "1 مل لكل لتر ماء (200 مل في 200 لتر ماء للفدان) أو مانكوزيب بمعدل 2.5 جم/لتر",
        "dosage_bacterial": "أوكسي كلوريد النحاس 2.5 جم/لتر + ستريبتوسيكلين 0.6 جم / 10 لتر ماء",
        "dosage_viral": "0.5 مل لكل لتر ماء (100 مل في 200 لتر ماء للفدان)",
        "timing": "في الصباح الباكر (6:00–8:30 صباحاً) أثناء هدوء الرياح وقبل هطول الأمطار",
        "precaution": "ارتداء قناع واقٍ وقفازات عازلة. تجنب الرش أثناء ذروة نشاط النحل والتلقيح."
    },
    "ml": {'bacterial_msg': 'മണ്ണിലെ ഈർപ്പവും ({moist}%) താപനിലയും ({temp}°C) ഇലകളിൽ ജലാംശം വർദ്ധിപ്പിച്ച്, {dis} ബാക്ടീരിയൽ അണുബാധ വേഗത്തിലാക്കുന്നു.', 'fungal_msg': 'ഈർപ്പനിലയും ({hum}%) താപനിലയും ({temp}°C) ഒപ്പം {cond} ({rain}% മഴ സാധ്യത) എന്നിവ {dis} കുമിൾ രോഗാണുക്കളുടെ വ്യാപനം വേഗത്തിലാക്കുന്നു.', 'viral_msg': 'താപനിലയും ({temp}°C) കാറ്റും ({wind} km/h) കീടങ്ങളുടെ പ്രവർത്തനം കൂട്ടി {dis} വൈറസ് വ്യാപനത്തിന് കാരണമാകുന്നു.', 'pesticide_fungal': 'അസോക്സിസ്ട്രോബിൻ 18.2% + ഡൈഫെനൊകൊണസോൾ 11.4% SC (അല്ലെങ്കിൽ മാങ്കോസെബ് 75% WP)', 'pesticide_bacterial': 'കോപ്പർ ഓക്സിക്ലോറൈഡ് 50% WP + സ്ട്രെപ്റ്റോസൈക്ലിൻ (90:10)', 'pesticide_viral': 'ഇമിഡാക്ലോപ്രിഡ് 17.8% SL', 'steps_fungal': '1. രോഗബാധയുള്ള ഇലകൾ നശിപ്പിക്കുക.\n2. നനയ്ക്കൽ ക്രമീകരിക്കുക.\n3. 24 മണിക്കൂറിനുള്ളിൽ കുമിൾനാശിനി തളിക്കുക.', 'steps_bacterial': '1. രോഗബാധയുള്ള ഭാഗങ്ങൾ നീക്കം ചെയ്യുക.\n2. ഇലകൾ നനഞ്ഞിരിക്കുമ്പോൾ പണി ഒഴിവാക്കുക.\n3. ബാക്ടീരിയ നാശിനി തളിക്കുക.', 'steps_viral': '1. ബാധിച്ച ചെടികൾ നീക്കം ചെയ്യുക.\n2. മഞ്ഞ കെണികൾ സ്ഥാപിക്കുക.\n3. കീടനിയന്ത്രണ മരുന്ന് തളിക്കുക.', 'dosage_fungal': '1 മി.ലി / ലിറ്റർ വെള്ളത്തിൽ (ഏക്കറിന് 200 മി.ലി)', 'dosage_bacterial': 'കോപ്പർ ഓക്സിക്ലോറൈഡ് 2.5 ഗ്രാം/ലിറ്റർ + സ്ട്രെപ്റ്റോസൈക്ലിൻ 0.6 ഗ്രാം / 10 ലിറ്റർ വെള്ളത്തിൽ', 'dosage_viral': '0.5 മി.ലി / ലിറ്റർ വെള്ളത്തിൽ', 'timing': 'രാവിലെ കാറ്റില്ലാത്ത സമയത്ത് തളിക്കുക', 'precaution': 'കയ്യുറകളും മാസ്കും ധരിക്കുക.'},
    "kn": {'bacterial_msg': 'ಮಣ್ಣಿನ ತೇವಾಂಶ ({moist}%) ಮತ್ತು ತಾಪಮಾನ ({temp}°C) ಎಲೆಗಳ ಮೇಲೆ ನೀರು ನಿಲ್ಲುವಂತೆ ಮಾಡಿ, {dis} ಬ್ಯಾಕ್ಟೀರಿಯಾ ರಂಧ್ರಗಳ ಮೂಲಕ ಹರಡಲು ಕಾರಣವಾಗುತ್ತದೆ.', 'fungal_msg': 'ಗಾಳಿಯ ತೇವಾಂಶ ({hum}%) ಮತ್ತು ತಾಪಮಾನ ({temp}°C) ಜೊತೆಗೆ {cond} ({rain}% ಮಳೆ ಸಾಧ್ಯತೆ) {dis} ಶಿಲೀಂಧ್ರ ಬೀಜಕಗಳ ಬೆಳವಣಿಗೆಯನ್ನು ವೇಗಗೊಳಿಸುತ್ತಿದೆ.', 'viral_msg': 'ತಾಪಮಾನ ({temp}°C) ಮತ್ತು ಗಾಳಿಯ ವೇಗ ({wind} km/h) ಕೀಟಗಳ ಚಟುವಟಿಕೆಯನ್ನು ಹೆಚ್ಚಿಸಿ {dis} ವೈರಸ್ ಹರಡುವಿಕೆಯನ್ನು ವೇಗಗೊಳಿಸುತ್ತಿದೆ.', 'pesticide_fungal': 'ಅಜಾಕ್ಸಿಸ್ಟ್ರೋಬಿನ್ + ಡೈಫೆನೊಕೊನಾಜೋಲ್ (ಅಥವಾ ಮ್ಯಾಂಕೋಜೆಬ್ 75% WP)', 'pesticide_bacterial': 'ಕಾಪರ್ ಆಕ್ಸಿಕ್ಲೋರೈಡ್ 50% WP + ಸ್ಟ್ರೆಪ್ಟೋಸೈಕ್ಲಿನ್', 'pesticide_viral': 'ಇಮಿಡಾಕ್ಲೋಪ್ರಿಡ್ 17.8% SL', 'steps_fungal': '1. ರೋಗಪೀಡಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದು ನಾಶಮಾಡಿ.\n2. ಎಲೆಗಳ ಮೇಲೆ ನೀರು ಚಿಮುಕಿಸುವುದನ್ನು ನಿಲ್ಲಿಸಿ.\n3. ಶಿಲೀಂಧ್ರನಾಶಕವನ್ನು ಸಿಂಪಡಿಸಿ.', 'steps_bacterial': '1. ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ ನಾಶಮಾಡಿ.\n2. ಎಲೆಗಳು ಒದ್ದೆಯಾಗಿರುವಾಗ ಕೆಲಸ ಮಾಡಬೇಡಿ.\n3. ಬ್ಯಾಕ್ಟೀರಿಯಾನಾಶಕ ಸಿಂಪಡಿಸಿ.', 'steps_viral': '1. ವೈರಸ್ ಸೋಂಕಿತ ಸಸ್ಯಗಳನ್ನು ಕಿತ್ತುಹಾಕಿ.\n2. ಜಿಗುಟಾದ ಬಲೆಗಳನ್ನು ಅಳವಡಿಸಿ.\n3. ಶಿಫಾರಸು ಮಾಡಿದ ಕೀಟನಾಶಕ ಸಿಂಪಡಿಸಿ.', 'dosage_fungal': '1 ಮಿ.ಲೀ / ಲೀಟರ್ ನೀರಿಗೆ (ಎಕರೆಗೆ 200 ಮಿ.ಲೀ)', 'dosage_bacterial': 'ಕಾಪರ್ ಆಕ್ಸಿಕ್ಲೋರೈಡ್ 2.5 ಗ್ರಾಂ/ಲೀ + ಸ್ಟ್ರೆಪ್ಟೋಸೈಕ್ಲಿನ್ 0.6 ಗ್ರಾಂ / 10 ಲೀ ನೀರಿಗೆ', 'dosage_viral': '0.5 ಮಿ.ಲೀ / ಲೀಟರ್ ನೀರಿಗೆ', 'timing': 'ಮುಂಜಾನೆ ಗಾಳಿಯ ವೇಗ ಕಡಿಮೆಯಿದ್ದಾಗ ಸಿಂಪಡಿಸಿ', 'precaution': 'ಮುಖಗವಸು ಮತ್ತು ಕೈಗವಸುಗಳನ್ನು ಧರಿಸಿ.'},
    "bn": {'bacterial_msg': 'মাটির আর্দ্রতা ({moist}%) এবং তাপমাত্রা ({temp}°C) পাতায় জলের উপস্থিতি বাড়িয়ে {dis} ব্যাকটেরিয়ার বিস্তারকে ত্বরান্বিত করছে।', 'fungal_msg': 'বাতাসের আর্দ্রতা ({hum}%) এবং তাপমাত্রা ({temp}°C) এর সাথে {cond} ({rain}% বৃষ্টির সম্ভাবনা) {dis} ছত্রাকের বিস্তারকে অত্যন্ত দ্রুত করে তুলছে।', 'viral_msg': 'আবহাওয়া এবং তাপমাত্রা ({temp}°C) কীট পতঙ্গের কার্যকলাপ বাড়িয়ে {dis} ভাইরাস ছড়াচ্ছে।', 'pesticide_fungal': 'অ্যাজোক্সিস্ট্রোবিন + ডাইফেনোকোনাজোল (বা ম্যানকোজেব ৭৫% WP)', 'pesticide_bacterial': 'কপার অক্সিক্লোরাইড ৫০% WP + স্ট্রেপ্টোসাইক্লিন', 'pesticide_viral': 'ইমিডাক্লোপ্রিড ১৭.৮% SL', 'steps_fungal': '১. আক্রান্ত পাতা ছেঁটে নষ্ট করুন।\n২. সেচ নিয়ন্ত্রণ করুন।\n৩. ২৪ ঘণ্টার মধ্যে ছত্রাকনাশক স্প্রে করুন।', 'steps_bacterial': '১. আক্রান্ত অংশ পুড়িয়ে নষ্ট করুন।\n২. ভেজা পাতায় কাজ করবেন না।\n৩. ব্যাকটিরিয়ানাশক স্প্রে করুন।', 'steps_viral': '১. আক্রান্ত গাছ উপড়ে ফেলুন।\n২. হলুদ ফাঁদ ব্যবহার করুন।\n৩. কীটনাশক স্প্রে করুন।', 'dosage_fungal': '১ মিলি প্রতি লিটার জল (বিঘাপ্রতি প্রয়োজনীয় মাত্রা)', 'dosage_bacterial': 'কপার অক্সিক্লোরাইড ২.৫ গ্রাম/লিটার + স্ট্রেপ্টোসাইক্লিন ০.৬ গ্রাম / ১০ লিটার জল', 'dosage_viral': '০.৫ মিলি প্রতি লিটার জল', 'timing': 'ভোরবেলায় বাতাস শান্ত থাকলে স্প্রে করুন', 'precaution': 'মাস্ক ও গ্লাভস ব্যবহার করুন।'},
    "mr": {'bacterial_msg': 'जमिनीतील ओलावा ({moist}%) आणि तापमान ({temp}°C) मुळे पानात पाणी साचून {dis} जिवाणूंचा प्रसार वेगाने होत आहे.', 'fungal_msg': 'हवेतील आर्द्रता ({hum}%) आणि तापमानासह आगामी {cond} ({rain}% पावसाची शक्यता) मुळे {dis} बुरशीचा प्रादुर्भाव वेगाने वाढण्याची शक्यता आहे.', 'viral_msg': 'तापमान ({temp}°C) आणि वारा कीटकांची संख्या वाढवून {dis} विषाणूचा प्रसार करत आहेत.', 'pesticide_fungal': 'अझॉक्सीस्ट्रोबिन + डिफेनोकोनाझोल (किंवा मॅन्कोझेब ७५% WP)', 'pesticide_bacterial': 'कॉपर ऑक्सिक्लोराईड ५०% WP + स्ट्रेप्टोसायक्लिन', 'pesticide_viral': 'इमिडाक्लोप्रिड १७.८% SL', 'steps_fungal': '१. बाधित पाने तोडून नष्ट करा.\n२. फवारा सिंचन तात्पुरते थांबवा.\n३. २४ तासांत बुरशीनाशकाची फवारणी करा.', 'steps_bacterial': '१. बाधित भाग शेताबाहेर नेऊन नष्ट करा.\n२. पाने ओली असताना शेतात काम टाळा.\n३. कॉपरयुक्त औषध फवारा.', 'steps_viral': '१. विषाणूग्रस्त झाडे उपटून नष्ट करा.\n२. पिवळे चिकट सापळे लावा.\n३. कीटकनाशकाची फवारणी करा.', 'dosage_fungal': '१ मिली प्रति लिटर पाणी (एकरला २०० मिली)', 'dosage_bacterial': 'कॉपर ऑक्सिक्लोराईड २.५ ग्रॅम/लिटर + स्ट्रेप्टोसायक्लिन ०.६ ग्रॅम / १० लिटर पाणी', 'dosage_viral': '०.५ मिली प्रति लिटर पाणी', 'timing': 'सकाळी वारा शांत असताना फवारणी करा', 'precaution': 'मास्क आणि हातमोजे वापरा.'},
    "gu": {'bacterial_msg': 'જમીનનો ભેજ ({moist}%) અને તાપમાન ({temp}°C) પાંદડા પર પાણીનો ભરાવો કરીને {dis} બેક્ટેરિયાના પ્રવેશને ઝડપી બનાવે છે.', 'fungal_msg': 'હવામાં ભેજ ({hum}%) અને આગામી {cond} ({rain}% વરસાદની શક્યતા) ને કારણે {dis} ફૂગના બીજ ઝડપથી ફેલાઈ રહ્યા છે.', 'viral_msg': 'તાપમાન ({temp}°C) અને પવન જંતુઓની સક્રિયતા વધારીને {dis} વાયરસનો ફેલાવો કરે છે.', 'pesticide_fungal': 'એઝોક્સીસ્ટ્રોબિન + ડાયફેનોકોનાઝોલ (અથવા મેન્કોઝેબ ૭૫% WP)', 'pesticide_bacterial': 'કોપર ઓક્સિક્લોરાઇડ ૫૦% WP + સ્ટ્રેપ્ટોસાયક્લિન', 'pesticide_viral': 'ઇમિડાક્લોપ્રિડ ૧૭.૮% SL', 'steps_fungal': '૧. રોગગ્રસ્ત પાંદડા કાપીને નાશ કરો.\n૨. પાણીનો છંટકાવ બંધ કરો.\n૩. ફૂગનાશકનો છંટકાવ કરો.', 'steps_bacterial': '૧. સંક્રમિત પાંદડા ખેતરથી દૂર નિકાલ કરો.\n૨. ભીના પાંદડા હોય ત્યારે કામ ટાળો.\n૩. બેક્ટેરિયાનાશક છાંટો.', 'steps_viral': '૧. વાયરસગ્રસ્ત છોડ ઉપાડીને નાશ કરો.\n૨. પીળા સ્ટીકી ટ્રેપ લગાવો.\n૩. જીવાત નિયંત્રણની દવા છાંટો.', 'dosage_fungal': '૧ મિલી પ્રતિ લિટર પાણી (વીઘા દીઠ યોગ્ય પ્રમાણ)', 'dosage_bacterial': 'કોપર ઓક્સિક્લોરાઇડ ૨.૫ ગ્રામ/લિટર + સ્ટ્રેપ્ટોસાયક્લિન ૦.૬ ગ્રામ / ૧૦ લિટર', 'dosage_viral': '૦.૫ મિલી પ્રતિ લિટર પાણી', 'timing': 'સવારે પવન શાંત હોય ત્યારે છંટકાવ કરો', 'precaution': 'માસ્ક અને ગ્લોવ્ઝ પહેરો.'},
    "pa": {'bacterial_msg': 'ਜ਼ਮੀਨ ਦੀ ਨਮੀ ({moist}%) ਅਤੇ ਤਾਪਮਾਨ ({temp}°C) ਕਾਰਨ {dis} ਬੈਕਟੀਰੀਆ ਪੱਤਿਆਂ ਵਿੱਚ ਤੇਜ਼ੀ ਨਾਲ ਦਾਖਲ ਹੋ ਰਿਹਾ ਹੈ।', 'fungal_msg': 'ਨਮੀ ({hum}%) ਅਤੇ ਆਉਣ ਵਾਲੇ {cond} ({rain}% ਮੀਂਹ ਦੀ ਸੰਭਾਵਨਾ) ਕਾਰਨ {dis} ਉੱਲੀ ਦੇ ਫੈਲਣ ਦਾ ਖਤਰਾ ਬਹੁਤ ਜ਼ਿਆਦਾ ਹੈ।', 'viral_msg': 'ਮੌਸਮ ਦੇ ਹਾਲਾਤ ਕੀੜਿਆਂ ਦੀ ਗਿਣਤੀ ਵਧਾ ਕੇ {dis} ਵਾਇਰਸ ਦਾ ਪਸਾਰ ਕਰ ਰਹੇ ਹਨ।', 'pesticide_fungal': 'ਅਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ + ਡਾਈਫੇਨੋਕੋਨਾਜ਼ੋਲ (ਜਾਂ ਮੈਨਕੋਜ਼ੇਬ 75% WP)', 'pesticide_bacterial': 'ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ 50% WP + ਸਟ੍ਰੈਪਟੋਸਾਈਕਲਿਨ', 'pesticide_viral': 'ਇਮੀਡਾਕਲੋਪ੍ਰਿਡ 17.8% SL', 'steps_fungal': '1. ਬਿਮਾਰੀ ਵਾਲੇ ਪੱਤੇ ਤੋੜ ਕੇ ਨਸ਼ਟ ਕਰੋ।\n2. ਸਿੰਚਾਈ ਰੋਕੋ।\n3. ਉੱਲੀਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।', 'steps_bacterial': '1. ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ ਸਾੜ ਕੇ ਨਸ਼ਟ ਕਰੋ।\n2. ਗਿੱਲੇ ਪੱਤਿਆਂ ਦੌਰਾਨ ਕੰਮ ਨਾ ਕਰੋ।\n3. ਬੈਕਟੀਰੀਆਨਾਸ਼ਕ ਛਿੜਕੋ।', 'steps_viral': '1. ਬਿਮਾਰ ਪੌਦੇ ਪੁੱਟ ਕੇ ਨਸ਼ਟ ਕਰੋ।\n2. ਪੀਲੇ ਟਰੈਪ ਲਗਾਓ।\n3. ਕੀਟਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।', 'dosage_fungal': '1 ਮਿਲੀ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (ਏਕੜ ਲਈ 200 ਮਿਲੀ)', 'dosage_bacterial': 'ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ 2.5 ਗ੍ਰਾਮ/ਲੀਟਰ + ਸਟ੍ਰੈਪਟੋਸਾਈਕਲਿਨ 0.6 ਗ੍ਰਾਮ / 10 ਲੀਟਰ', 'dosage_viral': '0.5 ਮਿਲੀ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ', 'timing': 'ਸਵੇਰੇ ਸ਼ਾਂਤ ਹਵਾ ਵਿੱਚ ਛਿੜਕਾਅ ਕਰੋ', 'precaution': 'ਮਾਸਕ ਅਤੇ ਦਸਤਾਨੇ ਪਹਿਨੋ।'},
    "ur": {'bacterial_msg': 'مٹی کی نمی ({moist}%) اور درجہ حرارت ({temp}°C) پتے کے مساموں کے ذریعے {dis} بیکٹیریا کے تیز رفتار پھیلاؤ کا سبب بن رہے ہیں۔', 'fungal_msg': 'فصل کی نمی ({hum}%) اور درجہ حرارت ({temp}°C) کے ساتھ متوقع {cond} ({rain}% بارش کا امکان) {dis} پھپھوندی کے پھیلاؤ کو تیز کر رہے ہیں۔', 'viral_msg': 'موسمی حالات کیڑے مکوڑوں کی سرگرمی کو بڑھا کر {dis} وائرس کے پھیلاؤ کو متحرک کر رہے ہیں۔', 'pesticide_fungal': 'ایزوکسیسٹروبن + ڈائیفینوکونازول (یا مینکوزیب 75% WP)', 'pesticide_bacterial': 'کاپر آکسی کلورائیڈ 50% WP + اسٹریپٹوسائکلین', 'pesticide_viral': 'امیڈاکلوپرڈ 17.8% SL', 'steps_fungal': '1. متاثرہ پتوں کو کاٹ کر ضائع کریں۔\n2. اوور ہیڈ پانی روکیں۔\n3. پھپھوندی کش دوا کا اسپرے کریں۔', 'steps_bacterial': '1. متاثرہ پتے جلائیں۔\n2. گیلے پتوں کے دوران کام نہ کریں۔\n3. کاپر بیکٹیری سائیڈ استعمال کریں۔', 'steps_viral': '1. متاثرہ پودوں کو تلف کریں۔\n2. چپکنے والے پیلے جال لگائیں۔\n3. کیڑے مار دوا اسپرے کریں۔', 'dosage_fungal': '1 ملی لیٹر فی لیٹر پانی (200 ملی لیٹر فی ایکڑ)', 'dosage_bacterial': 'کاپر آکسی کلورائیڈ 2.5 گرام/لیٹر + اسٹریپٹوسائکلین 0.6 گرام / 10 لیٹر', 'dosage_viral': '0.5 ملی لیٹر فی لیٹر پانی', 'timing': 'صبح سویرے پرسکون ہوا میں اسپرے کریں', 'precaution': 'ماسک اور دستانے پہنیں۔'},
    "or": {'bacterial_msg': 'ମାଟିର ଆର୍ଦ୍ରତା ({moist}%) ଏବଂ ତାପମାତ୍ରା ({temp}°C) ଯୋଗୁଁ {dis} ଜୀବାଣୁ ରୋଗ ପତ୍ରରେ ଦ୍ରୁତ ଗତିରେ ବ୍ୟାପୁଛି।', 'fungal_msg': 'ଆର୍ଦ୍ରତା ({hum}%) ଏବଂ ଆଗାମୀ {cond} ({rain}% ବର୍ଷା ସମ୍ଭାବନା) {dis} କବକ ରୋଗ ବୃଦ୍ଧି ପାଇଁ ଅନୁକୂଳ ପରିବେଶ ସୃଷ୍ଟି କରୁଛି।', 'viral_msg': 'ତାପମାତ୍ରା ଏବଂ ପବନ କୀଟମାନଙ୍କୁ ସକ୍ରିୟ କରି {dis} ଭୂତାଣୁ ସଂକ୍ରମଣ ବଢ଼ାଉଛି।', 'pesticide_fungal': 'ଆଜୋକ୍ସିଷ୍ଟ୍ରୋବିନ୍ + ଡାଇଫେନୋକୋନାଜୋଲ୍ (କିମ୍ବା ମାଙ୍କୋଜେବ୍ 75% WP)', 'pesticide_bacterial': 'କପର ଅକ୍ସିକ୍ଲୋରାଇଡ୍ 50% WP + ଷ୍ଟ୍ରେପ୍ଟୋସାଇକ୍ଲିନ୍', 'pesticide_viral': 'ଇମିଡାକ୍ଲୋପ୍ରିଡ୍ 17.8% SL', 'steps_fungal': '1. ସଂକ୍ରମିତ ପତ୍ର କାଟି ନଷ୍ଟ କରନ୍ତୁ।\n2. ପାଣି ସିଞ୍ଚନ ବନ୍ଦ କରନ୍ତୁ।\n3. ଫଙ୍ଗିସାଇଡ୍ ସିଞ୍ଚନ କରନ୍ତୁ।', 'steps_bacterial': '1. ସଂକ୍ରମିତ ଅଂଶ ପୋଡ଼ି ଦିଅନ୍ତୁ।\n2. ଓଦା ପତ୍ର ଥିବା ସମୟରେ କାମ କରନ୍ତୁ ନାହିଁ।\n3. କପର୍ ଔଷଧ ସିଞ୍ଚନ କରନ୍ତୁ।', 'steps_viral': '1. ରୋଗାକ୍ରାନ୍ତ ଗଛ ଉପାଡ଼ି ନଷ୍ଟ କରନ୍ତୁ।\n2. ହଳଦିଆ ଫାନ୍ଦ ବ୍ୟବହାର କରନ୍ତୁ।\n3. କୀଟନାଶକ ସିଞ୍ଚନ କରନ୍ତୁ।', 'dosage_fungal': '1 ମିଲି ପ୍ରତି ଲିଟର ପାଣି (ଏକର ପିଛା 200 ମିଲି)', 'dosage_bacterial': 'କପର ଅକ୍ସିକ୍ଲୋରାଇଡ୍ 2.5 ଗ୍ରାମ/ଲିଟର + ଷ୍ଟ୍ରେପ୍ଟୋସାଇକ୍ଲିନ୍ 0.6 ଗ୍ରାମ / 10 ଲିଟର', 'dosage_viral': '0.5 ମିଲି ପ୍ରତି ଲିଟର ପାଣି', 'timing': 'ସକାଳେ ଶାନ୍ତ ପବନ ଥିବା ସମୟରେ ସିଞ୍ଚନ କରନ୍ତୁ', 'precaution': 'ମାସ୍କ ଏବଂ ଗ୍ଲୋଭ୍ସ ବ୍ୟବହାର କରନ୍ତୁ।'},
    "as": {'bacterial_msg': 'মাটিৰ আৰ্দ্ৰতা ({moist}%) আৰু উত্তাপ ({temp}°C) ৰ বাবে পাতত পানী জমা হৈ {dis} বেক্টেৰিয়াৰ সংক্ৰমণ ক্ষিপ্ৰতৰ হৈছে।', 'fungal_msg': 'বায়ুৰ আৰ্দ্ৰতা ({hum}%) আৰু {cond} ({rain}% বৰষুণৰ সম্ভাৱনা) ৰ ফলত {dis} ভেঁকুৰৰ বৃদ্ধি তীব্ৰতৰ হৈছে।', 'viral_msg': 'বতৰৰ পৰিস্থিতিয়ে পোক-পৰুৱাক সক্ৰিয় কৰি {dis} ভাইৰাছ বিয়পাইছে।', 'pesticide_fungal': 'এজক্সিষ্ট্ৰোবিন + ডাইফেনোকোনাজল (বা মেনকোজের ৭৫% WP)', 'pesticide_bacterial': 'কপাৰ অক্সিক্লৰাইড ৫০% WP + ষ্ট্ৰেপ্টোচাইক্লিন', 'pesticide_viral': 'ইমিডাক্ল’প্ৰিড ১৭.৮% SL', 'steps_fungal': '১. ৰোগাক্ৰান্ত পাত আঁতৰাই পেলাওক।\n২. পানী দিয়া নিয়ন্ত্ৰণ কৰক।\n৩. ভেঁকুৰনাশক স্প্ৰে কৰক।', 'steps_bacterial': '১. আক্ৰান্ত পাত জ্বলাই পেলাওক।\n২. তিতা পাত থকা অৱস্থাত কাম নকৰিব।\n৩. বেক্টেৰিয়ানাশক ছটিয়াব।', 'steps_viral': '১. ৰোগীয়া গছ উভালি পেলাওক।\n২. হালধীয়া ফান্দ পাতক।\n৩. কীটনাশক ব্যৱহাৰ কৰক।', 'dosage_fungal': '১ মিলি প্ৰতি লিটাৰ পানীত (বিঘাই প্ৰতি ২০০ মিলি)', 'dosage_bacterial': 'কপাৰ অক্সিক্লৰাইড ২.৫ গ্ৰাম/লিটাৰ + ষ্ট্ৰেপ্টোচাইক্লিন ০.৬ গ্ৰাম / ১০ লিটাৰ', 'dosage_viral': '০.৫ মিলি প্ৰতি লিটাৰ পানীত', 'timing': 'পুৱা শান্ত বতাহ থকা সময়ত স্প্ৰে কৰক', 'precaution': 'মুখত মাস্ক আৰু হাতমোজা পিন্ধক।'},
    "ne": {'bacterial_msg': 'माटोको चिस्यान ({moist}%) र तापक्रम ({temp}°C) ले गर्दा {dis} ब्याक्टेरिया पातमा तीव्र रूपमा फैलिरहेको छ।', 'fungal_msg': 'हावाको आर्द्रता ({hum}%) र आगामी {cond} ({rain}% वर्षाको सम्भावना) ले {dis} ढुसीको जोखिम बढाएको छ।', 'viral_msg': 'मौसमले कीराहरूलाई सक्रिय बनाई {dis} भाइरसको फैलावटलाई तीव्र बनाएको छ।', 'pesticide_fungal': 'एजोक्सिस्टोबिन + डाइफेनोकोनाजोल (वा म्यान्कोजेब ७५% WP)', 'pesticide_bacterial': 'कपर अक्सिक्लोराइड ५०% WP + स्ट्रेप्टोसाइक्लिन', 'pesticide_viral': 'इमिडाक्लोप्रिड १७.८% SL', 'steps_fungal': '१. संक्रमित पातहरू नष्ट गर्नुहोस्।\n२. सिँचाइ नियन्त्रण गर्नुहोस्।\n३. ढुसीनाशक छर्कनुहोस्।', 'steps_bacterial': '१. संक्रमित भाग हटाउनुहोस्।\n२. पात भिजेको बेला काम नगर्नुहोस्।\n३. ब्याक्टेरियानाशक छर्कनुहोस्।', 'steps_viral': '१. बिरामी बोट उखेल्नुहोस्।\n२. पहेंलो ट्र्याप प्रयोग गर्नुहोस्।\n३. कीटनाशक छर्कनुहोस्।', 'dosage_fungal': '१ मिली प्रति लिटर पानी', 'dosage_bacterial': 'कपर अक्सिक्लोराइड २.५ ग्राम/लिटर + स्ट्रेप्टोसाइक्लिन ०.६ ग्राम / १० लिटर', 'dosage_viral': '०.५ मिली प्रति लिटर पानी', 'timing': 'बिहान हावा शान्त भएको बेला छर्कनुहोस्', 'precaution': 'मास्क र पञ्जा प्रयोग गर्नुहोस्।'},
    "si": {'bacterial_msg': 'පසේ තෙතමනය ({moist}%) සහ උෂ්ණත්වය ({temp}°C) නිසා {dis} බැක්ටීරියා රෝගය ශීඝ්\u200dරයෙන් ව්\u200dයාප්ත වෙමින් පවතී.', 'fungal_msg': 'ආර්ද්\u200dරතාවය ({hum}%) සහ ඉදිරි {cond} ({rain}% වැසි අවදානම) {dis} දිලීර බීජාණු වර්ධනයට හේතු වේ.', 'viral_msg': 'උෂ්ණත්වය හා සුළඟ මගින් කෘමීන් බෝවීම වැඩි කර {dis} වෛරසය පැතිරවීම වේගවත් කරයි.', 'pesticide_fungal': 'ඇසොක්සිස්ට්\u200dරොබින් + ඩයිෆෙනොකොනසෝල් (හෝ මැන්කොසෙබ් 75% WP)', 'pesticide_bacterial': 'කොපර් ඔක්සික්ලෝරයිඩ් 50% WP + ස්ට්\u200dරෙප්ටොමයිසින්', 'pesticide_viral': 'ඉමිඩැක්ලෝප්\u200dරිඩ් 17.8% SL', 'steps_fungal': '1. රෝගී පත්\u200dර කපා විනාශ කරන්න.\n2. අධික ජල සම්පාදනය නවත්වන්න.\n3. දිලීර නාශක යොදන්න.', 'steps_bacterial': '1. ආසාදිත පත්\u200dර ආරක්ෂිතව ඉවත් කරන්න.\n2. පත්\u200dර තෙත්ව ඇති විට වැඩ නොකරන්න.\n3. බැක්ටීරියා නාශක යොදන්න.', 'steps_viral': '1. වෛරසය වැළඳුනු පැළ ගලවා දමන්න.\n2. කහ උගුල් සවි කරන්න.\n3. කෘමිනාශක යොදන්න.', 'dosage_fungal': 'ජලය ලීටරයකට මි.ලී 1ක්', 'dosage_bacterial': 'කොපර් ඔක්සික්ලෝරයිඩ් 2.5g/L + ස්ට්\u200dරෙප්ටොමයිසින් 0.6g / 10L', 'dosage_viral': 'ජලය ලීටරයකට මි.ලී 0.5ක්', 'timing': 'උදෑසන සුළං අඩු වේලාවක යොදන්න', 'precaution': 'මුහුණු ආවරණ සහ අත්වැසුම් පළඳින්න.'},
    "fr": {'bacterial_msg': 'L humidite du sol ({moist}%) et la temperature ({temp}°C) favorisent l hydratation des tissus foliaires, accelerant la penetration bacterienne de {dis}.', 'fungal_msg': 'L humidite relative ({hum}%) et la temperature ({temp}°C) avec {cond} ({rain}% risque de pluie) prolongent l humidite foliaire, accelerant les spores de {dis}.', 'viral_msg': 'La temperature ({temp}°C) et le vent ({wind} km/h) stimulent les insectes vecteurs, propageant le virus {dis}.', 'pesticide_fungal': 'Azoxystrobine 18.2% + Difenoconazole 11.4% SC (ou Mancozebe 75% WP)', 'pesticide_bacterial': 'Oxychlorure de cuivre 50% WP + Streptocycline', 'pesticide_viral': 'Imidaclopride 17.8% SL (ou Thiamethoxame)', 'steps_fungal': '1. Elaguer et bruler les feuilles infectees.\n2. Suspendre l arrosage par aspersion.\n3. Pulveriser un fongicide protecteur sous 24h.', 'steps_bacterial': '1. Retirer les feuilles impregnees d eau.\n2. Eviter d intervenir sur feuillage mouille.\n3. Traiter avec un bactericide cuprique sous 24h.', 'steps_viral': '1. Arracher et detruire les plants viroses.\n2. Installer des pieges collants jaunes et bleus.\n3. Traiter contre les insectes piqueurs.', 'dosage_fungal': '1 ml par litre d eau (200 ml / 200 L d eau par acre)', 'dosage_bacterial': 'Oxychlorure de cuivre 2.5 g/L + Streptocycline 0.6 g / 10 L d eau', 'dosage_viral': '0.5 ml par litre d eau', 'timing': 'Tot le matin (6h00–8h30) par vent calme avant les fortes chaleurs', 'precaution': 'Porter masque et gants. Ne pas traiter en pleine floraison.'},
    "es": {'bacterial_msg': 'La humedad del suelo ({moist}%) y la temperatura ({temp}°C) saturan el tejido foliar, acelerando la entrada bacteriana de {dis}.', 'fungal_msg': 'La humedad ({hum}%) y temperatura ({temp}°C) con {cond} ({rain}% lluvia) prolongan el mojado foliar, acelerando las esporas fungicas de {dis}.', 'viral_msg': 'La temperatura ({temp}°C) y el viento ({wind} km/h) estimulan los insectos vectores, propagando el virus {dis}.', 'pesticide_fungal': 'Azoxistrobina 18.2% + Difenoconazol 11.4% SC (o Mancozeb 75% WP)', 'pesticide_bacterial': 'Oxicloruro de cobre 50% WP + Estreptociclina', 'pesticide_viral': 'Imidacloprid 17.8% SL', 'steps_fungal': '1. Podar y destruir hojas inferiores enfermas.\n2. Detener riego por aspersion.\n3. Aplicar fungicida protector en 24h.', 'steps_bacterial': '1. Eliminar hojas afectadas con manchas humedas.\n2. Evitar labores con follaje mojado.\n3. Aplicar bactericida a base de cobre en 24h.', 'steps_viral': '1. Arrancar y quemar plantas con virus.\n2. Instalar trampas adhesivas amarillas y azules.\n3. Tratar con insecticida sistemico para vectores.', 'dosage_fungal': '1 ml por litro de agua (200 ml en 200 L por acre)', 'dosage_bacterial': 'Oxicloruro de cobre 2.5 g/L + Estreptociclina 0.6 g / 10 L agua', 'dosage_viral': '0.5 ml por litro de agua', 'timing': 'Temprano por la manana con viento en calma antes de lluvias', 'precaution': 'Usar mascarilla y guantes. No aplicar durante floracion activa.'},
    "pt": {'bacterial_msg': 'A humidade do solo ({moist}%) e a temperatura ({temp}°C) aceleram a infiltracao bacteriana de {dis}.', 'fungal_msg': 'A humidade ({hum}%) e a temperatura ({temp}°C) com {cond} ({rain}% chuva) prolongam o molhamento foliar, acelerando {dis}.', 'viral_msg': 'A temperatura e o vento aceleram os insetos vetores, espalhando o virus {dis}.', 'pesticide_fungal': 'Azoxistrobina + Difenoconazol (ou Mancozebe 75% WP)', 'pesticide_bacterial': 'Oxicloreto de cobre 50% WP + Estreptociclina', 'pesticide_viral': 'Imidacloprida 17.8% SL', 'steps_fungal': '1. Podar folhas infectadas.\n2. Pausar irrigacao por aspersao.\n3. Aplicar fungicida protetor em 24h.', 'steps_bacterial': '1. Destruir folhas afetadas.\n2. Nao mexer com folhas molhadas.\n3. Aplicar bactericida de cobre.', 'steps_viral': '1. Arrancar plantas doentes.\n2. Instalar armadilhas adesivas.\n3. Aplicar inseticida sistemico.', 'dosage_fungal': '1 ml por litro de agua', 'dosage_bacterial': 'Oxicloreto de cobre 2.5 g/L + Estreptociclina 0.6 g / 10 L', 'dosage_viral': '0.5 ml por litro de agua', 'timing': 'De manha cedo com vento calmo', 'precaution': 'Usar mascara e luvas protetoras.'},
    "de": {'bacterial_msg': 'Bodenfeuchte ({moist}%) und Temperatur ({temp}°C) fordern die bakterielle Infiltration von {dis}.', 'fungal_msg': 'Luftfeuchtigkeit ({hum}%) und {cond} ({rain}% Regenrisiko) verlangern die Blattnasse und beschleunigen {dis}.', 'viral_msg': 'Mikroklima und Wind fordern Insektenvektoren und verbreiten das {dis}-Virus.', 'pesticide_fungal': 'Azoxystrobin + Difenoconazol (oder Mancozeb 75% WP)', 'pesticide_bacterial': 'Kupferoxychlorid 50% WP + Streptocyclin', 'pesticide_viral': 'Imidacloprid 17.8% SL', 'steps_fungal': '1. Befallene Blatter entfernen.\n2. Uberkopf-Bewasserung stoppen.\n3. Schutzfungizid innerhalb von 24h spritzen.', 'steps_bacterial': '1. Stark befallene Blatter verbrennen.\n2. Nicht bei nassem Laub arbeiten.\n3. Kupferbakterizid ausbringen.', 'steps_viral': '1. Virose Pflanzen roden.\n2. Gelb- und Blautafeln aufstellen.\n3. Vektorbekampfung durchfuhren.', 'dosage_fungal': '1 ml pro Liter Wasser', 'dosage_bacterial': 'Kupferoxychlorid 2.5 g/L + Streptocyclin 0.6 g / 10 L', 'dosage_viral': '0.5 ml pro Liter Wasser', 'timing': 'Fruhmorgens bei Windstille vor der Mittagshitze', 'precaution': 'Schutzmaske und Handschuhe tragen.'},
    "it": {'bacterial_msg': 'L umidita del suolo ({moist}%) e la temperatura ({temp}°C) facilitano la penetrazione batterica di {dis}.', 'fungal_msg': 'L umidita ({hum}%) e {cond} ({rain}% pioggia) prolungano la bagnatura fogliare, accelerando {dis}.', 'viral_msg': 'Temperatura e vento stimolano gli insetti vettori, diffondendo il virus {dis}.', 'pesticide_fungal': 'Azoxystrobin + Difenoconazolo (o Mancozeb 75% WP)', 'pesticide_bacterial': 'Ossicloruro di rame 50% WP + Streptociclina', 'pesticide_viral': 'Imidacloprid 17.8% SL', 'steps_fungal': '1. Rimuovere le foglie infette.\n2. Sospendere l irrigazione a pioggia.\n3. Applicare fungicida protettivo entro 24h.', 'steps_bacterial': '1. Distruggere le foglie colpite.\n2. Evitare operazioni con fogliame bagnato.\n3. Trattare con rameico.', 'steps_viral': '1. Eliminare piante con virus.\n2. Usare trappole cromotropiche.\n3. Trattare contro i vettori.', 'dosage_fungal': '1 ml per litro d acqua', 'dosage_bacterial': 'Ossicloruro di rame 2.5 g/L + Streptociclina 0.6 g / 10 L', 'dosage_viral': '0.5 ml per litro d acqua', 'timing': 'Al mattino presto con vento calmo', 'precaution': 'Indossare maschera e guanti protettivi.'},
    "ru": {'bacterial_msg': 'Влажность почвы ({moist}%) и температура ({temp}°C) способствуют проникновению бактерий {dis} через устьица.', 'fungal_msg': 'Влажность воздуха ({hum}%) и {cond} ({rain}% вероятность дождя) ускоряют прорастание спор грибка {dis}.', 'viral_msg': 'Погода активизирует насекомых-переносчиков (белокрылок/трипсов), распространяя вирус {dis}.', 'pesticide_fungal': 'Азоксистробин + Дифеноконазол (или Манкоцеб 75% СП)', 'pesticide_bacterial': 'Хлорокись меди 50% СП + Стрептомицин', 'pesticide_viral': 'Имидаклоприд 17.8% ВРК', 'steps_fungal': '1. Удалите и сожгите зараженные листья.\n2. Прекратите дождевание.\n3. Обработайте фунгицидом в течение 24 часов.', 'steps_bacterial': '1. Удалите пораженные листья.\n2. Не работайте по мокрым листьям.\n3. Обработайте медьсодержащим бактерицидом.', 'steps_viral': '1. Выкорчуйте вирусные растения.\n2. Установите клеевые ловушки.\n3. Обработайте системным инсектицидом.', 'dosage_fungal': '1 мл на 1 литр воды (200 мл на 200 л воды на акр)', 'dosage_bacterial': 'Хлорокись меди 2.5 г/л + Стрептомицин 0.6 г / 10 л', 'dosage_viral': '0.5 мл на 1 литр воды', 'timing': 'Рано утром в безветренную погоду до дождя', 'precaution': 'Используйте защитную маску и перчатки.'},
    "ko": {'bacterial_msg': '토양 수분 ({moist}%)과 기온 ({temp}°C)이 잎 표면 수분을 유지시켜 {dis} 세균의 기공 침입을 가속화하고 있습니다.', 'fungal_msg': '습도 ({hum}%)와 기온 ({temp}°C), 그리고 {cond} (강수확률 {rain}%)로 인해 잎 젖음 시간이 길어져 {dis} 곰팡이 포자 발아와 확산이 급증하고 있습니다.', 'viral_msg': '기온 ({temp}°C)과 바람 ({wind} km/h) 조건이 매개 해충(진딧물, 담배가루이) 활동을 촉진하여 {dis} 바이러스가 전신 확산되고 있습니다.', 'pesticide_fungal': '아족시스트로빈 + 디페노코나졸 액상수화제 (또는 만코제브 수화제)', 'pesticide_bacterial': '코퍼옥시클로라이드 수화제 + 스트렙토마이신', 'pesticide_viral': '이미다클로프리드 액상수화제 (또는 티아메톡삼)', 'steps_fungal': '1. 감염된 하엽을 제거하여 통풍을 원활하게 하세요.\n2. 잎 젖음을 방지하기 위해 상부 살수를 중단하세요.\n3. 24시간 이내에 보호 살균제를 살포하세요.', 'steps_bacterial': '1. 병든 잎을 제거하고 안전하게 소각하세요.\n2. 잎이 젖어 있을 때 농작업을 피하세요.\n3. 구리계 살균제를 24시간 내 살포하세요.', 'steps_viral': '1. 바이러스 감염 포기를 즉시 뽑아 폐기하세요.\n2. 황색 및 청색 끈끈이 트랩을 설치하세요.\n3. 매개충 방제용 침투이행성 살충제를 살포하세요.', 'dosage_fungal': '물 1리터당 1ml (에이커당 물 200L에 200ml)', 'dosage_bacterial': '코퍼옥시클로라이드 2.5g/L + 스트렙토마이신 0.6g / 10L 물', 'dosage_viral': '물 1리터당 0.5ml', 'timing': '바람이 잔잔한 이른 아침 (오전 6:00~8:30) 살포', 'precaution': '보호 마스크와 고무장갑을 착용하세요. 개화기 방제는 피하세요.'},
    "zh": {'bacterial_msg': '当前土壤水分（{moist}%）和气温（{temp}°C）导致叶片水浸状病斑形成，正加速 {dis} 细菌通过气孔侵入扩散。', 'fungal_msg': '空气湿度（{hum}%）和气温（{temp}°C）结合即将到来的 {cond}（降雨概率 {rain}%），导致叶片潮湿时间延长，正加速 {dis} 真菌孢子萌发与扩展。', 'viral_msg': '气温（{temp}°C）和风速（{wind} km/h）促使粉虱和蓟马等媒介昆虫活跃，加快了 {dis} 病毒的传播。', 'pesticide_fungal': '嘧菌酯 18.2% + 苯醚甲环唑 11.4% SC（或 代森锰锌 75% WP）', 'pesticide_bacterial': '王铜（氧氯化铜）50% WP + 农用链霉素', 'pesticide_viral': '吡虫啉 17.8% SL（或 噻虫嗪 25% WG）', 'steps_fungal': '1. 剪除并销毁严重感染的下部病叶以增加通风。\n2. 暂停喷淋灌溉保持叶片干燥。\n3. 在24小时内喷施保护性广谱杀菌剂。', 'steps_bacterial': '1. 清除水浸状病叶并在田外销毁。\n2. 避免在叶面湿润时进行农事操作。\n3. 24小时内喷施铜制杀菌剂。', 'steps_viral': '1. 拔除并销毁病毒病株。\n2. 每亩悬挂15-20张黄板和蓝板监测昆虫。\n3. 喷施内吸性杀虫剂防治传毒害虫。', 'dosage_fungal': '每升水 1 毫升（每亩 200 毫升兑水 200 升）', 'dosage_bacterial': '王铜 2.5 克/升 + 链霉素 0.6 克 / 10 升水', 'dosage_viral': '每升水 0.5 毫升', 'timing': '清晨（6:00–8:30）微风条件下喷施，避开雨前或中午高温', 'precaution': '佩戴口罩和防护手套。避免在作物花期蜜蜂活跃时喷洒。'},
}

HEALTHY_MESSAGES_25: Dict[str, str] = {
    "en": "Plant is healthy — no disease progression or pathogen development detected.",
    "ta": "பயிர் முற்றிலும் ஆரோக்கியமாக உள்ளது — நோய் பரவல் அல்லது நோய்க்கிருமி வளர்ச்சி அபாயம் எதுவும் இல்லை.",
    "te": "మొక్క పూర్తిగా ఆరోగ్యంగా ఉంది — వ్యాధి వ్యాప్తి లేదా వ్యాధికారక క్రిముల అభివృద్ధి లేదు.",
    "ml": "ചെടി പൂർണ്ണമായും ആരോഗ്യകരമാണ് — രോഗബാധയോ രോഗകാരികളുടെ വളർച്ചയോ കണ്ടെത്തിയിട്ടില്ല.",
    "kn": "ಗಿಡವು ಸಂಪೂರ್ಣವಾಗಿ ಆರೋಗ್ಯಕರವಾಗಿದೆ — ಯಾವುದೇ ರೋಗ ಹರಡುವಿಕೆ ಅಥವಾ ರೋಗಕಾರಕಗಳ ಬೆಳವಣಿಗೆ ಕಂಡುಬಂದಿಲ್ಲ.",
    "hi": "पौधा पूरी तरह स्वस्थ है — किसी बीमारी के बढ़ने या रोगज़नक़ के विकास का कोई जोखिम नहीं है।",
    "bn": "গাছটি সম্পূর্ণ সুস্থ — কোনো রোগ বিস্তার বা রোগজীবাণু বিকাশের লক্ষণ নেই।",
    "mr": "रोप पूर्णपणे निरोगी आहे — रोगाचा कोणताही प्रसार किंवा रोगकारक आढळला नाही.",
    "gu": "છોડ સંપૂર્ણપણે તંદુરસ્ત છે — રોગનો ફેલાવો કે પેથોજેનનો કોઈ વિકાસ થયો નથી.",
    "pa": "ਪੌਦਾ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਿਹਤਮੰਦ ਹੈ — ਬਿਮਾਰੀ ਦੇ ਫੈਲਣ ਜਾਂ ਜਰਾਸੀਮ ਦੇ ਵਿਕਾਸ ਦਾ ਕੋਈ ਖ਼ਤਰਾ ਨਹੀਂ ਹੈ।",
    "ur": "پودا مکمل طور پر صحت مند ہے — بیماری کے پھیلنے یا جراثیم کی نشوونما کا کوئی خطرہ نہیں ہے۔",
    "or": "ଗଛଟି ସମ୍ପୂର୍ଣ୍ଣ ସୁସ୍ଥ ଅଛି — କୌଣସି ରୋଗ ବ୍ୟାପିବା କିମ୍ବା ଜୀବାଣୁ ବୃଦ୍ଧି ହେବାର ଲକ୍ଷଣ ନାହିଁ।",
    "as": "উদ্ভিদজোপা সম্পূৰ্ণৰূপে সুস্থ — কোনো ৰোগৰ সংক্ৰমণ বা বীজাণুৰ বৃদ্ধি দেখা পোৱা হোৱা নাই।",
    "ne": "बिरुवा पूर्ण रूपमा स्वस्थ छ — कुनै रोगको फैलावट वा जीवाणुको विकास देखिएको छैन।",
    "si": "ශාකය සම්පූර්ණයෙන්ම නිරෝගීයි — රෝග පැතිරීමක් හෝ රෝගකාරක වර්ධනයක් හඳුනාගෙන නොමැත.",
    "ar": "النبات سليم تمامًا — لا يوجد أي انتشار للمرض أو تطور لمسببات الأمراض.",
    "fr": "La plante est saine — aucune progression de maladie ni pathogène détecté.",
    "es": "La planta está sana — no se detecta progresión de enfermedad ni patógenos.",
    "pt": "A planta está saudável — nenhuma progressão de doença ou patógeno detectado.",
    "de": "Die Pflanze ist gesund — kein Fortschreiten der Krankheit oder Krankheitserreger festgestellt.",
    "it": "La pianta è sana — nessuna progressione della malattia o patogeni rilevati.",
    "ru": "Растение здорово — прогрессирования заболевания или развития патогенов не обнаружено.",
    "ja": "植物は健全です — 病気の進行や病原体の発生は検出されていません。",
    "ko": "식물이 건강합니다 — 질병의 진행이나 병원균 발생이 감지되지 않았습니다.",
    "zh": "植株健康 — 未检测到病害扩散或病原体生长。"
}


def get_pathology_analysis(
    disease_name: str,
    confidence: float,
    sensor_data: dict,
    weather_data: dict = None,
    location: str = "",
    language: str = "en"
) -> dict:
    """
    Returns complete localized progression risk assessment & precision treatment
    in the farmer's selected language (supports all 25 languages).
    """
    norm_lang = (language or "en").lower().strip()
    if norm_lang not in PATHOLOGY_TEMPLATES_25:
        # Check fallback to major script or English
        norm_lang = "en"

    clean_dis = disease_name.replace('___', ' ').replace('_', ' ').strip()
    d_lower = disease_name.lower()

    if "healthy" in d_lower:
        h_msg = HEALTHY_MESSAGES_25.get(norm_lang, HEALTHY_MESSAGES_25["en"])
        return {
            "risk": "No Risk",
            "progression_stage": "Optimal Plant Health / No Disease",
            "vulnerability_window": "N/A",
            "message": h_msg,
            "pathology_factors": [
                "Vibrant chlorophyll distribution across leaf foliage",
                "No active necrotic, fungal, or bacterial lesions detected"
            ],
            "pesticide_recommendation": None,
            "treatment": None
        }

    is_bacterial = "bacterial" in d_lower or "wilt" in d_lower
    is_viral = "virus" in d_lower or "curl" in d_lower or "mosaic" in d_lower

    # Numerical sensors
    s_hum_num = float(sensor_data.get('humidity') or 74.0)
    s_temp_num = float(sensor_data.get('temperature') or 26.5)
    s_moist_num = float(sensor_data.get('moisture') or 65.0)
    s_n = sensor_data.get('nitrogen', 120)
    s_k = sensor_data.get('potassium', 180)

    # Weather
    w = weather_data or {}
    w_temp_num = float(w.get('tempC') or w.get('temp') or s_temp_num)
    w_hum_num = float(w.get('humidity') or s_hum_num)
    w_cond = w.get('condition') or 'Partly Cloudy'
    w_rain_chance = w.get('rainfallChance') or w.get('rain_prob') or 40
    w_rain_mm = w.get('rain_mm', 0)
    w_wind = w.get('windSpeedKmH') or w.get('wind_speed') or 7.5

    # Determine risk level
    if is_bacterial:
        if s_moist_num >= 75 and (s_hum_num >= 75 or w_hum_num >= 75):
            risk = "Severe Outbreak Risk"
            stage = "Rapid Bacterial Infiltration & Vascular Wilting"
            window = "Critical 24–48 Hours"
        elif s_moist_num >= 60 or s_hum_num >= 70:
            risk = "High Risk"
            stage = "Active Bacterial Lesion Expansion & Stomatal Entry"
            window = "2–3 Days"
        else:
            risk = "Medium Risk"
            stage = "Localized Bacterial Lesions"
            window = "3–5 Days"
    elif is_viral:
        risk = "Medium Risk"
        stage = "Systemic Viral Translocation via Insect Vectors"
        window = "3–7 Days"
    else:
        # Fungal
        if (s_hum_num >= 82 or w_hum_num >= 82) and (float(w_rain_chance) >= 60 or float(w_rain_mm) > 2):
            risk = "Severe Outbreak Risk"
            stage = "Active Conidial Sporulation & Rapid Lesion Expansion"
            window = "Critical 24–48 Hours"
        elif s_hum_num >= 72 or w_hum_num >= 72 or float(w_rain_chance) >= 45:
            risk = "High Risk"
            stage = "Secondary Mycelial Spread & Spore Germination"
            window = "48–72 Hours"
        elif s_hum_num >= 60:
            risk = "Medium Risk"
            stage = "Incipient Foliar Spots & Incubation"
            window = "3–5 Days"
        else:
            risk = "Low Risk"
            stage = "Localized Inception / Slow Spread"
            window = "5–7 Days"

    # Grab template
    t = PATHOLOGY_TEMPLATES_25.get(norm_lang, PATHOLOGY_TEMPLATES_25["en"])

    if is_bacterial:
        msg = t["bacterial_msg"].format(moist=s_moist_num, temp=s_temp_num, dis=clean_dis)
        pest_name = t["pesticide_bacterial"]
        steps = t["steps_bacterial"]
        dose = t["dosage_bacterial"]
        active = "Copper Oxychloride 500 g/kg + Streptomycin Sulphate 90%"
        cat = "Inorganic Protectant Contact Bactericide"
    elif is_viral:
        msg = t["viral_msg"].format(temp=w_temp_num, wind=w_wind, dis=clean_dis)
        pest_name = t["pesticide_viral"]
        steps = t["steps_viral"]
        dose = t["dosage_viral"]
        active = "Imidacloprid 178 g/L (or Thiamethoxam 250 g/kg)"
        cat = "Systemic Vector-Control Insecticide"
    else:
        msg = t["fungal_msg"].format(hum=s_hum_num, temp=s_temp_num, cond=w_cond, rain=w_rain_chance, dis=clean_dis)
        pest_name = t["pesticide_fungal"]
        steps = t["steps_fungal"]
        dose = t["dosage_fungal"]
        active = "Azoxystrobin 182 g/L + Difenoconazole 114 g/L"
        cat = "Broad-Spectrum Systemic & Protectant Fungicide (FRAC 11 + 3)"

    pest_rec = {
        "immediate_steps": steps,
        "pesticide_name": pest_name,
        "active_ingredient": active,
        "category": cat,
        "dosage": dose,
        "application_method": "Foliar spray with uniform canopy coverage (upper & lower leaf surfaces)",
        "spray_timing": t["timing"],
        "precaution": t["precaution"],
        "phi_days": "7–14 days",
        "organic_alternative": "Cold-Pressed Neem Oil (10,000 ppm) @ 3 ml/L OR Trichoderma viride @ 5 g/L"
    }

    return {
        "risk": risk,
        "progression_stage": stage,
        "vulnerability_window": window,
        "message": msg,
        "pathology_factors": [
            f.format(hum=s_hum_num, temp=s_temp_num, cond=w_cond, rain=w_rain_chance, n=s_n, k=s_k)
            for f in PATHOLOGY_FACTORS_25.get(norm_lang, PATHOLOGY_FACTORS_25["en"])
        ],
        "pesticide_recommendation": pest_rec,
        "treatment": pest_rec
    }


# --- FULL 25-LANGUAGE DISEASE NAMES & LOCALIZATION ---
DISEASE_NAMES_25: Dict[str, Dict[str, str]] = {
    "healthy": {
        "en": "Healthy Foliage", "ta": "ஆரோக்கியமான இலை", "te": "ఆరోగ్యకరమైన ఆకు", "ml": "ആരോഗ്യമുള്ള ഇല",
        "kn": "ಆರೋಗ್ಯಕರ ಎಲೆ", "hi": "स्वस्थ पत्ता", "bn": "সুস্থ পাতা", "mr": "निरोगी पान",
        "gu": "તંદુરસ્ત પાન", "pa": "ਸਿਹਤਮੰਦ ਪੱਤਾ", "ur": "صحت مند پتا", "or": "ସୁସ୍ଥ ପତ୍ର",
        "as": "সুস্থ পাত", "ne": "स्वस्थ पात", "si": "නිරෝගී පත්‍ර", "ar": "أوراق سليمة",
        "fr": "Feuillage sain", "es": "Follaje sano", "pt": "Folhagem saudável", "de": "Gesundes Blattwerk",
        "it": "Fogliame sano", "ru": "Здоровая листва", "ja": "健全な葉", "ko": "건강한 잎", "zh": "健康叶片"
    },
    "early_blight": {
        "en": "Early Blight", "ta": "ஆரம்பகால கருகல் நோய்", "te": "ముందస్తు తెగులు (Early Blight)", "ml": "ആദ്യകാല ബ്ലൈറ്റ്",
        "kn": "ಮುಂಚಿನ ಕರಗು ರೋಗ", "hi": "अगेती झुलसा रोग (Early Blight)", "bn": "আগেতি ধসা রোগ", "mr": "लवकर येणारा करपा",
        "gu": "અગેતી સુકારો", "pa": "ਅਗੇਤਾ ਝੁਲਸਾ ਰੋਗ", "ur": "ارلی بلائٹ", "or": "ଆଗୁଆ ପତ୍ରପୋଡ଼ା ରୋଗ",
        "as": "আগতীয়া ব্লাইট ৰোগ", "ne": "अगेती डढुवा", "si": "මුල් අංගමාරය", "ar": "اللفحة المبكرة",
        "fr": "Brûlure alternarienne", "es": "Tizón temprano", "pt": "Pinta-preta", "de": "Dürrfleckenkrankheit",
        "it": "Alternariosi", "ru": "Ранний фитофтороз", "ja": "輪紋病 (Early Blight)", "ko": "조기 역병", "zh": "早疫病"
    },
    "late_blight": {
        "en": "Late Blight", "ta": "பின்கால கருகல் நோய்", "te": "ఆలస్యపు తెగులు (Late Blight)", "ml": "പിൽക്കാല ബ്ലൈറ്റ്",
        "kn": "ತಡವಾದ ಕರಗು ರೋಗ", "hi": "पछेती झुलसा रोग (Late Blight)", "bn": "নাবী ধসা রোগ", "mr": "उशिरा येणारा करपा",
        "gu": "પાછોતરો સુકારો", "pa": "ਪਛੇਤਾ ਝੁਲਸਾ ਰੋਗ", "ur": "لیٹ بلائٹ", "or": "ପଛୁଆ ପତ୍ରପୋଡ଼ା ରୋଗ",
        "as": "পানী ব্লাইট ৰোগ", "ne": "पछेती डढुवा", "si": "පසු අංගමාරය", "ar": "اللفحة المتأخرة",
        "fr": "Mildiou de la pomme de terre", "es": "Tizón tardío", "pt": "Requeima", "de": "Kraut- und Knollenfäule",
        "it": "Peronospora", "ru": "Поздний фитофтороз", "ja": "疫病 (Late Blight)", "ko": "후기 역병", "zh": "晚疫病"
    },
    "bacterial_spot": {
        "en": "Bacterial Spot", "ta": "பாக்டீரியா இலைப்புள்ளி நோய்", "te": "బాక్టీరియల్ మచ్చల తెగులు", "ml": "ബാക്ടീരിയൽ സ്പോട്ട്",
        "kn": "ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ ರೋಗ", "hi": "जीवाणु धब्बा रोग (Bacterial Spot)", "bn": "ব্যাকটেরিয়াজনিত দাগ", "mr": "जिवाणू ठिपके रोग",
        "gu": "જીવાણુજન્ય ટપકાં", "pa": "ਜੀਵਾਣੂ ਧੱਬਾ ਰੋਗ", "ur": "بیکٹیریل سپاٹ", "or": "ଜୀବାଣୁ ଦାଗ ରୋଗ",
        "as": "বেক্টেৰিয়াজনিত দাগ ৰোগ", "ne": "ब्याक्टेरियल दाग", "si": "බැක්ටීරියා ලප රෝගය", "ar": "التبقع البكتيري",
        "fr": "Gale bactérienne", "es": "Mancha bacteriana", "pt": "Mancha bacteriana", "de": "Bakterienfleckenkrankheit",
        "it": "Maculatura batterica", "ru": "Бактериальная пятнистость", "ja": "斑点細菌病", "ko": "세균성 점무늬병", "zh": "细菌性斑点病"
    },
    "powdery_mildew": {
        "en": "Powdery Mildew", "ta": "சாம்பல் நோய்", "te": "బూడిద తెగులు", "ml": "പൊടിപ്പൂപ്പ് രോഗം",
        "kn": "ಬೂದಿ ರೋಗ", "hi": "चूर्णिल आसिता (पाउडरी मिल्ड्यू)", "bn": "পাউডারি মিলডিউ", "mr": "भुरी रोग",
        "gu": "છાશિયો રોગ", "pa": "ਪਾਊਡਰੀ ਫ਼ਫ਼ੂੰਦੀ", "ur": "پاؤڈری پھپھوندی", "or": "ପାଉଡରି ମିଲଡ୍ୟୁ",
        "as": "পাউদাৰী মিলডিউ", "ne": "धुलो ढुसी", "si": "පිටි පුස් රෝගය", "ar": "البياض الدقيقي",
        "fr": "Oïdium", "es": "Oídio", "pt": "Oídio", "de": "Echter Mehltau",
        "it": "Oidio", "ru": "Мучнистая роса", "ja": "うどんこ病", "ko": "흰가루병", "zh": "白粉病"
    },
    "yellow_leaf_curl": {
        "en": "Yellow Leaf Curl Virus", "ta": "மஞ்சள் இலை சுருள் வைரஸ்", "te": "పసుపు ఆకు ముడుత వైరస్", "ml": "മഞ്ഞ ഇലച്ചുരുൾ വൈറസ്",
        "kn": "ಹಳದಿ ಎಲೆ ಸುರುಳಿ ವೈರಸ್", "hi": "पीली पत्ती मरोड़ विषाणु", "bn": "হলুদ পাতা কোঁকড়ানো ভাইরাস", "mr": "पिवळा पर्णगुच्छ विषाणू",
        "gu": "પીળા પાન કુકડાઈ વાયરસ", "pa": "ਪੀਲਾ ਪੱਤਾ ਮਰੋੜ ਵਿਸ਼ਾਣੂ", "ur": "پیلا پتا مروڑ وائرس", "or": "ହଳଦିଆ ପତ୍ର କୁଞ୍ଚନ ଭୂତାଣୁ",
        "as": "হালধীয়া পাত কেঁকোৰা ভাইৰাছ", "ne": "पहेंलो पात खुम्चिने भाइरस", "si": "කහ පත්‍ර කොඩවීම් වෛරසය", "ar": "فيروس تجعد أوراق الطماطم الصفراء",
        "fr": "Virus des feuilles jaunes en cuillère", "es": "Virus del rizado amarillo", "pt": "Vírus do enrolamento amarelo", "de": "Gelbblättrigkeit-Virus",
        "it": "Virus dell'accartocciamento fogliare giallo", "ru": "Вирус желтой курчавости листьев", "ja": "黄化葉巻ウイルス", "ko": "황화잎말림바이러스", "zh": "黄化曲叶病毒"
    },
    "citrus_canker": {
        "en": "Citrus Bacterial Canker", "ta": "சிட்ரஸ் பாக்டீரியா புண் நோய்", "te": "సిట్రస్ కాంకర్ తెగులు", "ml": "സിട്രസ് കാങ്കർ രോഗം",
        "kn": "ಸಿಟ್ರಸ್ ಕ್ಯಾಂಕರ್ ರೋಗ", "hi": "सिट्रस कैंकर रोग", "bn": "লেবুর ক্যাঙ্কার রোগ", "mr": "लिंबूवर्गीय कॅन्कर रोग",
        "gu": "લીંબુ કેન્કર રોગ", "pa": "ਨਿੰਬੂ ਜਾਤੀ ਕੈਂਕਰ", "ur": "سٹرس کینکر", "or": "ଲେମ୍ବୁ କ୍ୟାଙ୍କର ରୋଗ",
        "as": "টেঙা জাতীয় শস্যৰ কেংকাৰ", "ne": "कागती क्याङ्कर", "si": "දෙහි පැපොල රෝගය", "ar": "تقرح الحمضيات البكتيري",
        "fr": "Chancre bactérien des agrumes", "es": "Cancro bacteriano de los cítricos", "pt": "Cancro cítrico bacteriano", "de": "Citrus-Krebs",
        "it": "Cancro batterico degli agrumi", "ru": "Бактериальный рак цитрусовых", "ja": "カンキツかいよう病", "ko": "감귤 궤양병", "zh": "柑橘溃疡病"
    },
    "rust": {
        "en": "Rust Disease", "ta": "துரு நோய்", "te": "తుప్పు తెగులు", "ml": "തുരുമ്പ് രോഗം",
        "kn": "ತುಕ್ಕು ರೋಗ", "hi": "गेरुआ / रतुआ रोग", "bn": "মরিচা রোগ", "mr": "तांबेरा रोग",
        "gu": "ગેરુ રોગ", "pa": "ਕੁੰਗੀ ਰੋਗ", "ur": "رتوا / کنگی", "or": "କଳଙ୍କି ରୋଗ",
        "as": "মামৰ ৰোগ", "ne": "सिन्दुरे रोग", "si": "මලකඩ රෝගය", "ar": "مرض صدأ النبات",
        "fr": "Maladie de la rouille", "es": "Roya", "pt": "Ferrugem", "de": "Rostkrankheit",
        "it": "Ruggine", "ru": "Ржавчина растений", "ja": "さび病", "ko": "녹병", "zh": "锈病"
    }
}


def get_disease_display_name(raw_name: str, lang: str = "en") -> str:
    """Returns localized disease display name for any detected disease string in user's language."""
    norm_lang = (lang or "en").lower().strip()
    if norm_lang not in SUPPORTED_LANGUAGES:
        norm_lang = "en"

    clean_name = raw_name.replace("___", " - ").replace("_", " ").strip()
    lower_raw = clean_name.lower()

    # Split crop and disease part if separated by hyphen
    crop_part = ""
    dis_part = clean_name
    if " - " in clean_name:
        parts = clean_name.split(" - ")
        crop_part = parts[0].strip()
        dis_part = parts[1].strip()

    loc_crop = get_crop_display_name(crop_part, norm_lang) if crop_part else ""

    matched_dis = None
    for k, trans in DISEASE_NAMES_25.items():
        if k in lower_raw or k.replace("_", " ") in lower_raw or k.replace("_", "") in lower_raw:
            matched_dis = trans.get(norm_lang, trans["en"])
            break

    if "healthy" in lower_raw:
        h_str = DISEASE_NAMES_25["healthy"].get(norm_lang, "Healthy")
        return f"{loc_crop} — {h_str}" if loc_crop else h_str

    if matched_dis and loc_crop:
        return f"{loc_crop} — {matched_dis}"
    elif matched_dis:
        return matched_dis

    return clean_name


# --- FULL 25-LANGUAGE PATHOLOGY FACTORS FOR DEEP EPIDEMIOLOGICAL EVIDENCE ---
PATHOLOGY_FACTORS_25: Dict[str, List[str]] = {
    "en": [
        "Live field humidity ({hum}%) and ambient temperature ({temp}°C) support pathogen metabolic activity.",
        "Microclimate conditions ({cond}, {rain}% precipitation chance) prolong free leaf wetness duration.",
        "Soil nutrient equilibrium (N: {n} mg/kg, K: {k} mg/kg) directly influences foliar cuticle resilience."
    ],
    "ta": [
        "காற்றின் ஈரப்பதம் ({hum}%) மற்றும் வெப்பநிலை ({temp}°C) நோய்க்கிருமியின் வளர்ச்சியைத் தூண்டுகிறது.",
        "நுண்-வானிலை ({cond}, {rain}% மழை வாய்ப்பு) இலைகளில் நீர் தங்கும் நேரத்தை நீட்டிக்கிறது.",
        "மண் ஊட்டச்சத்து சமநிலை (N: {n} mg/kg, K: {k} mg/kg) பயிரின் நோய் எதிர்ப்பு திறனைப் பாதிக்கிறது."
    ],
    "te": [
        "గాలిలోని తేమ ({hum}%) మరియు ఉష్ణోగ్రత ({temp}°C) వ్యాధికారక కారకాల వ్యాప్తికి కారణమవుతున్నాయి.",
        "వాతావరణ పరిస్థితులు ({cond}, {rain}% వర్షపు అవకాశం) ఆకులపై నీటి నిల్వ కాలాన్ని పెంచుతాయి.",
        "నేల పోషకాల సమతుల్యత (N: {n} mg/kg, K: {k} mg/kg) మొక్క రోగనిరోధక శక్తిని ప్రభావితం చేస్తుంది."
    ],
    "ml": [
        "അന്തരീക്ഷ ഈർപ്പം ({hum}%), താപനില ({temp}°C) എന്നിവ രോഗകാരികളുടെ പ്രവർത്തനത്തെ ത്വരിതപ്പെടുത്തുന്നു.",
        "കാലാവസ്ഥാ അവസ്ഥകൾ ({cond}, {rain}% മഴ സാധ്യത) ഇലകളിൽ ഈർപ്പത്തിന്റെ സാന്നിധ്യം വർദ്ധിപ്പിക്കുന്നു.",
        "മണ്ണിലെ പോഷക സന്തുലിതാവസ്ഥ (N: {n} mg/kg, K: {k} mg/kg) ചെടിയുടെ പ്രതിരോധശേഷിയെ സ്വാധീനിക്കുന്നു."
    ],
    "kn": [
        "ಗಾಳಿಯ ಆರ್ದ್ರತೆ ({hum}%) ಮತ್ತು ತಾಪಮಾನ ({temp}°C) ರೋಗಕಾರಕಗಳ ಬೆಳವಣಿಗೆಗೆ ಪೂರಕವಾಗಿದೆ.",
        "ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿಗಳು ({cond}, {rain}% ಮಳೆಯ ಸಂಭವನೀಯತೆ) ಎಲೆಗಳ ತೇವಾಂಶದ ಅವಧಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತವೆ.",
        "ಮಣ್ಣಿನ ಪೋಷಕಾಂಶಗಳ ಸಮತೋಲನ (N: {n} mg/kg, K: {k} mg/kg) ಬೆಳೆಯ ರೋಗನಿರೋಧಕ ಶಕ್ತಿಯನ್ನು ಪ್ರಭಾವಿಸುತ್ತದೆ."
    ],
    "hi": [
        "सापेक्षिक आर्द्रता ({hum}%) और परिवेशी तापमान ({temp}°C) रोगज़नक़ की सक्रियता को बढ़ावा देते हैं।",
        "सूक्ष्म जलवायु स्थितियां ({cond}, {rain}% वर्षा की संभावना) पत्तियों पर नमी की अवधि को बढ़ाती हैं।",
        "मिट्टी में पोषक संतुलन (N: {n} mg/kg, K: {k} mg/kg) फसल की प्राकृतिक प्रतिरोधक क्षमता को प्रभावित करता है।"
    ],
    "bn": [
        "আপেক্ষিক আর্দ্রতা ({hum}%) এবং বায়ুমণ্ডলীয় তাপমাত্রা ({temp}°C) রোগজীবাণুর বৃদ্ধিকে ত্বরান্বিত করে।",
        "আবহাওয়ার পরিস্থিতি ({cond}, {rain}% বৃষ্টির সম্ভাবনা) পাতার ভেজা থাকার সময়কাল বাড়িয়ে তোলে।",
        "মাটির পুষ্টির ভারসাম্য (N: {n} mg/kg, K: {k} mg/kg) গাছের প্রাকৃতিক প্রতিরোধ ক্ষমতাকে প্রভাবিত করে।"
    ],
    "mr": [
        "हवेतील आर्द्रता ({hum}%) आणि तापमान ({temp}°C) रोगाच्या प्रसारास अनुकूल ठरत आहेत.",
        "हवामानातील बदल ({cond}, {rain}% पावसाची शक्यता) पानांवर पाण्याचा ओलावा जास्त काळ टिकवून ठेवतात.",
        "मातीतील पोषण पातळी (N: {n} mg/kg, K: {k} mg/kg) पिकाच्या नैसर्गिक रोगप्रतिकारक शक्तीवर परिणाम करते."
    ],
    "gu": [
        "હવામાં ભેજ ({hum}%) અને તાપમાન ({temp}°C) રોગકારક જીવાણુઓના ફેલાવાને પ્રોત્સાહન આપે છે.",
        "હવામાન સ્થિતિ ({cond}, {rain}% વરસાદની શક્યતા) પાંદડા પર ભેજ રહેવાનો સમય લંબાવે છે.",
        "જમીનમાં પોષક તત્વોનું સંતુલન (N: {n} mg/kg, K: {k} mg/kg) છોડની રોગપ્રતિકારક શક્તિ પર અસર કરે છે."
    ],
    "pa": [
        "ਨਮੀ ({hum}%) ਅਤੇ ਤਾਪਮਾਨ ({temp}°C) ਬਿਮਾਰੀ ਦੇ ਫੈਲਾਅ ਲਈ ਅਨੁਕੂਲ ਹਾਲਾਤ ਪੈਦਾ ਕਰ ਰਹੇ ਹਨ।",
        "ਮੌਸਮੀ ਹਾਲਾਤ ({cond}, {rain}% ਮੀਂਹ ਦੀ ਸੰਭਾਵਨਾ) ਪੱਤਿਆਂ 'ਤੇ ਗਿੱਲਾਪਨ ਲੰਬੇ ਸਮੇਂ ਤੱਕ ਬਣਾਈ ਰੱਖਦੇ ਹਨ।",
        "ਮਿੱਟੀ ਦੇ ਪੋਸ਼ਕ ਤੱਤਾਂ ਦਾ ਸੰਤੁਲਨ (N: {n} mg/kg, K: {k} mg/kg) ਪੌਦੇ ਦੀ ਸਹਿਣਸ਼ੀਲਤਾ 'ਤੇ ਅਸਰ ਪਾਉਂਦਾ ਹੈ।"
    ],
    "ur": [
        "ہوا میں نمی ({hum}%) اور درجہ حرارت ({temp}°C) جراثیم کی افزائش کے لیے سازگار ہیں۔",
        "موسمی حالات ({cond}، بارش کا امکان {rain}%) پتوں پر نمی کا دورانیہ طویل کرتے ہیں۔",
        "مٹی میں غذائی اجزاء کا توازن (N: {n} mg/kg, K: {k} mg/kg) پودے کی قوت مدافعت کو متاثر کرتا ہے۔"
    ],
    "or": [
        "ଆର୍ଦ୍ରତା ({hum}%) ଏବଂ ତାପମାତ୍ରା ({temp}°C) ରୋଗଜୀବାଣୁଙ୍କ ବୃଦ୍ଧି ପାଇଁ ଅନୁକୂଳ ପରିବେଶ ସୃଷ୍ଟି କରୁଛି।",
        "ପାଣିପାଗ ସ୍ଥିତି ({cond}, {rain}% ବର୍ଷା ସମ୍ଭାବନା) ପତ୍ରରେ ଆର୍ଦ୍ରତା ଅବଧିକୁ ବଢ଼ାଇଦିଏ।",
        "ମାଟିର ପୋଷକ ତତ୍ତ୍ୱ ସନ୍ତୁଳନ (N: {n} mg/kg, K: {k} mg/kg) ଫସଲର ପ୍ରତିରୋଧକ କ୍ଷମତା ଉପରେ ପ୍ରଭାବ ପକାଏ।"
    ],
    "as": [
        "বায়ুৰ আৰ্দ্ৰতা ({hum}%) আৰু উত্তাপ ({temp}°C) ৰোগ সৃষ্টিকাৰী বীজাণুৰ বাবে অনুকূল।",
        "বতৰৰ অৱস্থা ({cond}, {rain}% বৰষুণৰ সম্ভাৱনা) পাতত পানী লাগি থকাৰ সময় বৃদ্ধি কৰে।",
        "মাটিৰ পুষ্টিৰ সন্তুলন (N: {n} mg/kg, K: {k} mg/kg) শস্যৰ ৰোগ প্ৰতিৰোধ ক্ষমতাত প্ৰভাৱ পেলায়।"
    ],
    "ne": [
        "हावाको आर्द्रता ({hum}%) र तापक्रम ({temp}°C) ले रोगका जीवाणुको वृद्धिलाई बढावा दिन्छ।",
        "मौसमको अवस्था ({cond}, {rain}% वर्षाको सम्भावना) ले पातमा चिसोपन लामो समयसम्म कायम राख्छ।",
        "माटोको पोषक तत्वको सन्तुलन (N: {n} mg/kg, K: {k} mg/kg) ले बालीको प्रतिरोधात्मक क्षमतामा असर गर्छ।"
    ],
    "si": [
        "වාතයේ ආර්ද්‍රතාවය ({hum}%) සහ උෂ්ණත්වය ({temp}°C) රෝග කාරක පැතිරීමට හිතකර පරිසරයක් සපයයි.",
        "කාලගුණික තත්ත්වයන් ({cond}, {rain}% වැසි සම්භාවිතාව) පත්‍ර මත තෙතමනය රැඳී පවතින කාලය දිගු කරයි.",
        "පසේ පෝෂක තුල්‍යතාව (N: {n} mg/kg, K: {k} mg/kg) ශාකයේ ස්වභාවික ප්‍රතිශක්තිය කෙරෙහි බලපායි."
    ],
    "ar": [
        "الرطوبة النسبية الحالية ({hum}%) ودرجة الحرارة ({temp}°C) تعززان نشاط وتكاثر العامل الممرض.",
        "الظروف الجوية الحالية ({cond}، واحتمال هطول الأمطار {rain}%) تزيد من فترة بلل الأوراق.",
        "توازن العناصر الغذائية في التربة (النيتروجين: {n}، البوتاسيوم: {k}) يؤثر بشكل مباشر على مناعة الأوراق."
    ],
    "fr": [
        "L humidité relative ({hum}%) et la température ({temp}°C) favorisent l activité métabolique du pathogène.",
        "Le microclimat ({cond}, {rain}% risque de pluie) prolonge la durée d humidité foliaire.",
        "L équilibre nutritif du sol (N: {n} mg/kg, K: {k} mg/kg) influence la résistance des cuticules."
    ],
    "es": [
        "La humedad del aire ({hum}%) y la temperatura ({temp}°C) favorecen la actividad del patógeno.",
        "Las condiciones microclimáticas ({cond}, {rain}% prob. lluvia) prolongan el mojado foliar.",
        "El balance nutricional del suelo (N: {n} mg/kg, K: {k} mg/kg) influye en la resistencia foliar."
    ],
    "pt": [
        "A humidade do ar ({hum}%) e a temperatura ({temp}°C) sustentam a atividade metabólica do patógeno.",
        "O microclima ({cond}, {rain}% hipótese de chuva) prolonga a duração do molhamento foliar.",
        "O equilíbrio de nutrientes do solo (N: {n} mg/kg, K: {k} mg/kg) influencia a resistência da cutícula."
    ],
    "de": [
        "Die Luftfeuchtigkeit ({hum}%) und Temperatur ({temp}°C) begünstigen das Erregerwachstum.",
        "Das Mikroklima ({cond}, {rain}% Regenwahrscheinlichkeit) verlängert die Blattnässedauer.",
        "Das Nährstoffgleichgewicht im Boden (N: {n} mg/kg, K: {k} mg/kg) steuert die Blattwiderstandskraft."
    ],
    "it": [
        "L umidità dell aria ({hum}%) e la temperatura ({temp}°C) favoriscono la proliferazione del patogeno.",
        "Le condizioni microclimatiche ({cond}, {rain}% probabilità pioggia) prolungano la bagnatura fogliare.",
        "L equilibrio dei nutrienti nel terreno (N: {n} mg/kg, K: {k} mg/kg) influisce sulla resistenza dei tessuti."
    ],
    "ru": [
        "Влажность воздуха ({hum}%) и температура ({temp}°C) поддерживают жизнеспособность патогена.",
        "Микроклимат ({cond}, {rain}% вероятность дождя) увеличивает продолжительность увлажнения листьев.",
        "Баланс питательных веществ в почве (N: {n} мг/кг, K: {k} мг/кг) влияет на устойчивость кутикулы."
    ],
    "ja": [
        "圃場の相対湿度 ({hum}%) と気温 ({temp}°C) が病原体の代謝活性を促進しています。",
        "微気象条件 ({cond}、降水確率 {rain}%) により葉面の湿潤時間が長時間化しています。",
        "土壌養分バランス (N: {n} mg/kg, K: {k} mg/kg) が作物の細胞壁の防御力に直接影響します。"
    ],
    "ko": [
        "상대습도 ({hum}%)와 기온 ({temp}°C)이 병원균의 포자 발아와 증식을 촉진하고 있습니다.",
        "미기후 상태 ({cond}, 강수확률 {rain}%)로 인해 잎 표면 수분 지속 시간이 길어지고 있습니다.",
        "토양 양분 균형 (N: {n} mg/kg, K: {k} mg/kg)이 작물의 큐티클층 저항성에 영향을 미칩니다."
    ],
    "zh": [
        "田间相对湿度（{hum}%）和气温（{temp}°C）正加剧病原体的代谢活动与侵染。",
        "微气候条件（{cond}，降雨概率 {rain}%）显著延长了叶片湿润时间。",
        "土壤养分平衡（N: {n} mg/kg，K: {k} mg/kg）直接决定作物表皮组织的抗逆抵御力。"
    ]
}


# --- FULL 25-LANGUAGE WEATHER LOCALIZATION ---
WEATHER_CONDITIONS_25: Dict[str, Dict[str, str]] = {
    "clear sky": {
        "en": "Clear Sky", "ta": "தெளிவான வானம்", "te": "నిర్మలమైన ఆకాశం", "ml": "തെളിഞ്ഞ ആകാശം",
        "kn": "ಸ್ವಚ್ಛ ಆಕಾಶ", "hi": "साफ आसमान", "bn": "পরিষ্কার আকাশ", "mr": "निरभ्र आकाश",
        "gu": "ચોખ્ખું આકાશ", "pa": "ਸਾਫ਼ ਆਸਮਾਨ", "ur": "صاف آسمان", "or": "ନିର୍ମଳ ଆକାଶ",
        "as": "পৰিষ্কাৰ আকাশ", "ne": "सफा आकाश", "si": "පැහැදිලි අහස", "ar": "سماء صافية",
        "fr": "Ciel dégagé", "es": "Cielo despejado", "pt": "Céu limpo", "de": "Klarer Himmel",
        "it": "Cielo sereno", "ru": "Ясное небо", "ja": "快晴", "ko": "맑은 하늘", "zh": "晴空万里"
    },
    "partly cloudy": {
        "en": "Partly Cloudy", "ta": "பகுதி மேகமூட்டம்", "te": "పాక్షికంగా మేఘావృతం", "ml": "ഭാഗികമായി മേഘാവൃതം",
        "kn": "ಭಾಗಶಃ ಮೋಡ ಕವಿದ", "hi": "आंशिक रूप से बादल", "bn": "আংশিক মেঘলা", "mr": "अंशतः ढगाळ",
        "gu": "અંશતઃ વાદળછાયું", "pa": "ਅੰਸ਼ਕ ਤੌਰ 'ਤੇ ਬੱਦਲਵਾਈ", "ur": "جزوی طور پر ابر آلود", "or": "ଆଂଶିକ ମେଘୁଆ",
        "as": "আংশিক মেঘাচ্ছন্ন", "ne": "आंशिक रूपमा बादल", "si": "අර්ධ වශයෙන් වළාකුළු", "ar": "غائم جزئياً",
        "fr": "Partiellement nuageux", "es": "Parcialmente nublado", "pt": "Parcialmente nublado", "de": "Teilweise bewölkt",
        "it": "Parzialmente nuvoloso", "ru": "Переменная облачность", "ja": "晴れ時々曇り", "ko": "구름 조금", "zh": "多云间晴"
    },
    "overcast clouds": {
        "en": "Overcast Clouds", "ta": "முழு மேகமூட்டம்", "te": "పూర్తిగా మేఘావృతం", "ml": "പൂർണ്ണമായി മേഘാവൃതം",
        "kn": "ಸಂಪೂರ್ಣ ಮೋಡ ಕವಿದ", "hi": "घने बादल / मेघाच्छादित", "bn": "মেঘাচ্ছন্ন আকাশ", "mr": "पूर्ण ढगाळ",
        "gu": "સંપૂર્ણ વાદળછાયું", "pa": "ਘਣੇ ਬੱਦਲ", "ur": "مکمل ابر آلود", "or": "ପୂର୍ଣ୍ଣ ମେଘୁଆ",
        "as": "ডাৱৰীয়া আকাশ", "ne": "बादल लागेको", "si": "වළාකුලින් බර", "ar": "غيوم ملبدة",
        "fr": "Couvert", "es": "Nublado", "pt": "Nublado", "de": "Bedeckt",
        "it": "Coperto", "ru": "Пасмурно", "ja": "曇天 / 厚い雲", "ko": "흐림 / 구름 많음", "zh": "阴云密布"
    },
    "light rain": {
        "en": "Light Rain", "ta": "லேசான மழை", "te": "తేలికపాటి వర్షం", "ml": "നേരിയ മഴ",
        "kn": "ಹಗುರ ಮಳೆ", "hi": "हल्की बारिश", "bn": "হালকা বৃষ্টি", "mr": "हलका पाऊस",
        "gu": "હળવો વરસાદ", "pa": "ਹਲਕੀ ਬਾਰਿਸ਼", "ur": "ہلکی بارش", "or": "ହାଲୁକା ବର୍ଷା",
        "as": "পাতলীয়া বৰষুণ", "ne": "हल्का वर्षा", "si": "සුළු වැසි", "ar": "مطر خفيف",
        "fr": "Pluie légère", "es": "Lluvia ligera", "pt": "Chuva fraca", "de": "Leichter Regen",
        "it": "Pioggia leggera", "ru": "Небольшой дождь", "ja": "小雨", "ko": "가벼운 비", "zh": "小雨"
    },
    "moderate rain": {
        "en": "Moderate Rain", "ta": "மிதமான மழை", "te": "మోస్తరు వర్షం", "ml": "മിതമായ മഴ",
        "kn": "ಮಧ್ಯಮ ಮಳೆ", "hi": "मध्यम बारिश", "bn": "মাঝারি বৃষ্টি", "mr": "मध्यम पाऊस",
        "gu": "મધ્યમ વરસાદ", "pa": "ਦਰਮਿਆਨੀ ਬਾਰਿਸ਼", "ur": "معتدل بارش", "or": "ମଧ୍ୟମ ବର୍ଷା",
        "as": "মজলীয়া বৰষুণ", "ne": "मध्यम वर्षा", "si": "මධ්‍යස්ථ වැසි", "ar": "مطر معتدل",
        "fr": "Pluie modérée", "es": "Lluvia moderada", "pt": "Chuva moderada", "de": "Mäßiger Regen",
        "it": "Pioggia moderata", "ru": "Умеренный дождь", "ja": "雨", "ko": "보통 비", "zh": "中雨"
    },
    "heavy rain": {
        "en": "Heavy Rainfall", "ta": "கனமழை", "te": "భారీ వర్షం", "ml": "ശക്തമായ മഴ",
        "kn": "ಭಾರಿ ಮಳೆ", "hi": "भारी बारिश", "bn": "ভারী বৃষ্টিপাত", "mr": "मुसळधार पाऊस",
        "gu": "ભારે વરસાદ", "pa": "ਭਾਰੀ ਬਾਰਿਸ਼", "ur": "شدید بارش", "or": "ପ୍ରବଳ ବର୍ଷା",
        "as": "ধাৰাসাৰ বৰষুণ", "ne": "भारी वर्षा", "si": "තද වැසි", "ar": "أمطار غزيرة",
        "fr": "Forte pluie", "es": "Lluvia fuerte", "pt": "Chuva forte", "de": "Starker Regen",
        "it": "Pioggia intensa", "ru": "Сильный дождь", "ja": "大雨", "ko": "강한 비 / 폭우", "zh": "大到暴雨"
    },
    "thunderstorm": {
        "en": "Thunderstorm", "ta": "இடியுடன் கூடிய மழை", "te": "ఉరుములతో కూడిన వర్షం", "ml": "ഇടിമിന്നലോടു കൂടിയ മഴ",
        "kn": "ಗುಡುಗು ಸಹಿತ ಮಳೆ", "hi": "आंधी-तूफान व गरज-चमक", "bn": "বজ্রবিদ্যুৎসহ ঝড়", "mr": "वादळी पाऊस",
        "gu": "ગાજવીજ સાથે વરસાદ", "pa": "ਤੂਫ਼ਾਨ ਅਤੇ ਗਰਜ", "ur": "گرج چمک کے ساتھ طوفان", "or": "ଘଡ଼ଘଡ଼ି ସହ ବର୍ଷା",
        "as": "ঢেৰেকণিৰে বৰষুণ", "ne": "चट्याङ्गसहितको वर्षा", "si": "ගිගුරුම් සහිත වැසි", "ar": "عاصفة رعدية",
        "fr": "Orage", "es": "Tormenta eléctrica", "pt": "Trovoada", "de": "Gewitter",
        "it": "Temporale", "ru": "Гроза", "ja": "雷雨", "ko": "뇌우", "zh": "雷阵雨"
    }
}


def localize_weather_condition(condition: str, lang: str = "en") -> str:
    norm_lang = (lang or "en").lower().strip()
    c_lower = (condition or "").lower().strip()

    if "overcast" in c_lower:
        c_search = "overcast clouds"
    elif "broken" in c_lower or "scattered" in c_lower or "few" in c_lower or "cloud" in c_lower:
        c_search = "partly cloudy"
    elif "clear" in c_lower or "sun" in c_lower:
        c_search = "clear sky"
    elif "thunder" in c_lower or "storm" in c_lower:
        c_search = "thunderstorm"
    elif "heavy" in c_lower:
        c_search = "heavy rain"
    elif "light" in c_lower or "drizzle" in c_lower:
        c_search = "light rain"
    elif "rain" in c_lower:
        c_search = "moderate rain"
    else:
        c_search = c_lower

    for key, dict_trans in WEATHER_CONDITIONS_25.items():
        if key in c_search or c_search in key:
            return dict_trans.get(norm_lang, dict_trans.get("en", condition.title()))
    return condition.title() if condition else "Partly Cloudy"

SOIL_MOISTURE_STATUS_25: Dict[str, Dict[str, str]] = {
    "adequate": {
        "en": "Adequate", "ta": "போதுமானது", "te": "సరిపడా", "ml": "മതിയായത്",
        "kn": "ಸಾಕಷ್ಟಿದೆ", "hi": "पर्याप्त", "bn": "পর্যাপ্ত", "mr": "पुरेसा",
        "gu": "પૂરતું", "pa": "ਢੁਕਵਾਂ", "ur": "مناسب", "or": "ପର୍ଯ୍ୟାପ୍ତ",
        "as": "পৰ্যাপ্ত", "ne": "पर्याप्त", "si": "ප්‍රමාණවත්", "ar": "مناسب",
        "fr": "Adéquate", "es": "Adecuada", "pt": "Adequada", "de": "Ausreichend",
        "it": "Adeguata", "ru": "Достаточная", "ja": "適湿", "ko": "적정", "zh": "适宜"
    },
    "saturated": {
        "en": "Saturated", "ta": "அதிக ஈரப்பதம்", "te": "అధిక తేమ", "ml": "അധിക ഈർപ്പം",
        "kn": "ಅಧಿಕ ತೇವಾಂಶ", "hi": "संतृप्त", "bn": "অতিরিক্ত আর্দ্র", "mr": "संतृप्त",
        "gu": "વધુ પડતી ભેજવાળી", "pa": "ਸੰਤ੍ਰਿਪਤ", "ur": "حد سے زیادہ نم", "or": "ସନ୍ତୃପ୍ତ",
        "as": "অতিৰিক্ত সেমেকা", "ne": "अत्यधिक चिसो", "si": "අධික තෙතමනය", "ar": "مشبع بالماء",
        "fr": "Saturée", "es": "Saturada", "pt": "Saturada", "de": "Gesättigt",
        "it": "Satura", "ru": "Переувлажненная", "ja": "飽和 (過湿)", "ko": "과습 (포화)", "zh": "饱和过湿"
    }
}

def localize_soil_moisture(pct: int, is_adequate: bool, lang: str = "en") -> str:
    norm_lang = (lang or "en").lower().strip()
    status_key = "adequate" if is_adequate else "saturated"
    status_dict = SOIL_MOISTURE_STATUS_25[status_key]
    status_label = status_dict.get(norm_lang) or status_dict.get("en", "Adequate")
    return f"{pct}% ({status_label})"

WEATHER_ALERTS_25: Dict[str, Dict[str, Any]] = {
    "en": {
        "fungal_title": "⚠️ High Fungal Spore Risk",
        "fungal_msg": "Live micro-climate relative humidity is {hum}%. High humidity and extended leaf wetness ({wet}h) accelerate fungal spore germination.",
        "fungal_act": "Apply bio-fungicide (Trichoderma viride or Copper Oxychloride 50 WP @ 2.5g/L) before rain.",
        "rain_title": "🌧️ Rainfall & Precipitation Warning",
        "rain_msg": "Rainfall condition detected ({cond}) with {rain}% precipitation chance. Risk of soil waterlogging.",
        "rain_act": "Ensure proper field drainage trenches and pause overhead irrigation.",
        "heat_title": "☀️ High Thermal Stress Advisory",
        "heat_msg": "Temperature has reached {temp}°C. Crops may experience wilting and transpiration stress.",
        "heat_act": "Irrigate crops during early morning or evening hours.",
        "normal_title": "✅ Favorable Micro-Climate Conditions",
        "normal_msg": "Current weather is {cond} ({temp}°C, {hum}% humidity). Soil moisture is {soil}.",
        "normal_act": "Continue routine crop monitoring and scheduled fertigation.",
        "summary_risk": "Elevated fungal disease risk due to {hum}% humidity and {wet}h leaf wetness. Apply preventative bio-fungicide.",
        "summary_normal": "Favorable micro-climate ({cond}). Soil moisture is adequate."
    },
    "ta": {
        "fungal_title": "⚠️ தீவிர பூஞ்சை வித்துக்கள் பரவல் எச்சரிக்கை",
        "fungal_msg": "காற்றின் ஈரப்பதம் {hum}% ஆக உள்ளது. இலை ஈரப்பதம் ({wet} மணி நேரம்) பூஞ்சை வித்துக்கள் முளைப்பதை விரைவுபடுத்துகிறது.",
        "fungal_act": "மழைக்கு முன் ட்ரைக்கோடெர்மா விரிடி அல்லது காப்பர் ஆக்ஸிகுளோரைடு பாதுகாப்பு தெளிப்பு செய்யவும்.",
        "rain_title": "🌧️ மழை மற்றும் ஈரப்பத எச்சரிக்கை",
        "rain_msg": "மழை வாய்ப்பு ({cond}) {rain}% ஆக உள்ளது. வயலில் தண்ணீர் தேங்கும் அபாயம் உள்ளது.",
        "rain_act": "வயலில் முறையான வடிகால் வசதி செய்து, நீர்ப்பாசனத்தை தற்காலிகமாக நிறுத்தவும்.",
        "heat_title": "☀️ அதிக வெப்ப அழுத்த ஆலோசனை",
        "heat_msg": "வெப்பநிலை {temp}°C ஐ எட்டியுள்ளது. பயிர்கள் வாட வாய்ப்புள்ளது.",
        "heat_act": "அதிகாலை அல்லது மாலை வேளையில் பயிர்களுக்கு தண்ணீர் பாய்ச்சவும்.",
        "normal_title": "✅ சாதகமான வேளாண் வானிலை",
        "normal_msg": "தற்போதைய வானிலை {cond} ({temp}°C, {hum}% ஈரப்பதம்). மண் ஈரம்: {soil}.",
        "normal_act": "வழக்கமான பயிர் கண்காணிப்பு மற்றும் உரமிடுதலைத் தொடரவும்.",
        "summary_risk": "{hum}% ஈரப்பதம் மற்றும் {wet} மணி நேர இலை ஈரம் காரணமாக பூஞ்சை நோய் அபாயம் உள்ளது. பாதுகாப்பு தெளிப்பு பரிந்துரைக்கப்படுகிறது.",
        "summary_normal": "பயிருக்கு சாதகமான வானிலை ({cond}). மண் ஈரம் போதுமானதாக உள்ளது."
    },
    "te": {
        "fungal_title": "⚠️ అధిక ఫంగల్ బీజాంశం ప్రమాదం",
        "fungal_msg": "వాతావరణ తేమ {hum}%. అధిక తేమ మరియు ఆకుల తడి ({wet}గం) ఫంగల్ వ్యాధులను వేగవంతం చేస్తాయి.",
        "fungal_act": "వర్షానికి ముందు ట్రైకోడెర్మా విరిడే లేదా కాపర్ ఆక్సిక్లోరైడ్ పిచికారీ చేయండి.",
        "rain_title": "🌧️ వర్షపాతం హెచ్చరిక",
        "rain_msg": "వర్ష సూచన ({cond}) {rain}% సంభావ్యత ఉంది. పొలంలో నీరు నిలిచే ప్రమాదం.",
        "rain_act": "సరైన నీటి పారుదల కాలువలు ఏర్పాటు చేసి, నీటిపారుదల నిలిపివేయండి.",
        "heat_title": "☀️ అధిక ఉష్ణోగ్రత హెచ్చరిక",
        "heat_msg": "ఉష్ణోగ్రత {temp}°C కి చేరుకుంది. పంటలు వడలిపోయే అవకాశం ఉంది.",
        "heat_act": "ఉదయం లేదా సాయంత్రం వేళల్లో పంటలకు నీరు పెట్టండి.",
        "normal_title": "✅ అనుకూలమైన వాతావరణం",
        "normal_msg": "ప్రస్తుత వాతావరణం {cond} ({temp}°C, {hum}% తేమ). నేల తేమ: {soil}.",
        "normal_act": "సాధారణ పంట పర్యవేక్షణ మరియు ఎరువుల నిర్వహణను కొనసాగించండి.",
        "summary_risk": "{hum}% తేమ మరియు {wet}గం ఆకుల తడి వల్ల ఫంగల్ వ్యాధుల ప్రమాదం ఉంది. నివారణ పిచికారీ చేయండి.",
        "summary_normal": "అనుకూలమైన వాతావరణ పరిస్థితులు ({cond}). నేల తేమ సరిపడా ఉంది."
    },
    "ml": {
        "fungal_title": "⚠️ ഉയർന്ന കുമിൾ രോഗ സാധ്യത",
        "fungal_msg": "അന്തരീക്ഷ ഈർപ്പം {hum}%. ഉയർന്ന ഈർപ്പവും ഇലകളിലെ നനവും ({wet}മ) കുമിൾ രോഗങ്ങൾക്ക് കാരണമാകുന്നു.",
        "fungal_act": "മഴയ്ക്ക് മുൻപ് ട്രൈക്കോഡെർമ അല്ലെങ്കിൽ കോപ്പർ ഓക്സിക്ലോറൈഡ് തളിക്കുക.",
        "rain_title": "🌧️ കനത്ത മഴ മുന്നറിയിപ്പ്",
        "rain_msg": "മഴ സാധ്യത ({cond}) {rain}%. കൃഷിയിടത്തിൽ വെള്ളക്കെട്ടിന് സാധ്യത.",
        "rain_act": "കൃഷിയിടത്തിൽ വെള്ളം കെട്ടിക്കിടക്കാതെ ഡ്രെയിനേജ് ഉറപ്പാക്കുക.",
        "heat_title": "☀️ കടുത്ത ചൂട് ജാഗ്രതാ നിർദ്ദേശം",
        "heat_msg": "താപനില {temp}°C ൽ എത്തിയിരിക്കുന്നു. വിളകൾ വാടാൻ സാധ്യതയുണ്ട്.",
        "heat_act": "രാവിലെയോ വൈകുന്നേരമോ നനയ്ക്കുക.",
        "normal_title": "✅ അനുകൂല കാലാവസ്ഥ",
        "normal_msg": "നിലവിലെ കാലാവസ്ഥ {cond} ({temp}°C, {hum}% ഈർപ്പം). മണ്ണിലെ ഈർപ്പം: {soil}.",
        "normal_act": "പതിവ് വിള നിരീക്ഷണവും പരിപാലനവും തുടരുക.",
        "summary_risk": "{hum}% ഈർപ്പവും {wet}മ ഇല നനവും കാരണം കുമിൾ രോഗസാധ്യത. പ്രതിരോധ മരുന്ന് തളിക്കുക.",
        "summary_normal": "വിളകൾക്ക് അനുകൂലമായ കാലാവസ്ഥ ({cond})."
    },
    "kn": {
        "fungal_title": "⚠️ ಶಿಲೀಂಧ್ರ ರೋಗದ ಹೆಚ್ಚಿನ ಅಪಾಯ",
        "fungal_msg": "ವಾತಾವರಣದ ತೇವಾಂಶ {hum}%. ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಮತ್ತು ಎಲೆಯ ತೇವ ({wet}ಗಂ) ಶಿಲೀಂಧ್ರ ರೋಗಗಳನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.",
        "fungal_act": "ಮಳೆಗೆ ಮುನ್ನ ಟ್ರೈಕೋಡರ್ಮಾ ಅಥವಾ ಕಾಪರ್ ಆಕ್ಸಿಕ್ಲೋರೈಡ್ ಸಿಂಪಡಿಸಿ.",
        "rain_title": "🌧️ ಮಳೆಯ ಮುನ್ನೆಚ್ಚರಿಕೆ",
        "rain_msg": "ಮಳೆಯ ಸಾಧ್ಯತೆ ({cond}) {rain}%. ಹೊಲದಲ್ಲಿ ನೀರು ನಿಲ್ಲುವ ಅಪಾಯವಿದೆ.",
        "rain_act": "ಹೊಲದಲ್ಲಿ ಸೂಕ್ತ ನೀರುಗಾಲುವೆ ಮಾಡಿ, ನೀರಾವರಿಯನ್ನು ನಿಲ್ಲಿಸಿ.",
        "heat_title": "☀️ ಅಧಿಕ ತಾಪಮಾನದ ಎಚ್ಚರಿಕೆ",
        "heat_msg": "ತಾಪಮಾನ {temp}°C ತಲುಪಿದೆ. ಬೆಳೆಗಳು ಬಾಡುವ ಸಾಧ್ಯತೆಯಿದೆ.",
        "heat_act": "ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಸಂಜೆ ವೇಳೆ ನೀರು ಹಾಯಿಸಿ.",
        "normal_title": "✅ ಅನುಕೂಲಕರ ಹವಾಮಾನ",
        "normal_msg": "ಪ್ರಸ್ತುತ ಹವಾಮಾನ {cond} ({temp}°C, {hum}% ತೇವಾಂಶ). ಮಣ್ಣಿನ ತೇವಾಂಶ: {soil}.",
        "normal_act": "ನಿಯಮಿತ ಬೆಳೆ ಪರಿಶೀಲನೆ ಮುಂದುವರಿಸಿ.",
        "summary_risk": "{hum}% ತೇವಾಂಶ ಮತ್ತು {wet}ಗಂ ಎಲೆ ತೇವದಿಂದ ಶಿಲೀಂಧ್ರ ರೋಗದ ಅಪಾಯ. ಮುನ್ನೆಚ್ಚರಿಕೆ ಸಿಂಪಡಣೆ ಮಾಡಿ.",
        "summary_normal": "ಬೆಳೆಗೆ ಅನುಕೂಲಕರ ಹವಾಮಾನ ({cond})."
    },
    "hi": {
        "fungal_title": "⚠️ उच्च कवक बीजाणु जोखिम",
        "fungal_msg": "सापेक्ष आर्द्रता {hum}% है। उच्च आर्द्रता और पत्ती का गीलापन ({wet} घंटे) कवक बीजाणु अंकुरण को बढ़ावा देते हैं।",
        "fungal_act": "बारिश से पहले सुरक्षात्मक कवकनाशी (ट्राइकोडर्मा या कॉपर ऑक्सीक्लोराइड) का छिड़काव करें।",
        "rain_title": "🌧️ वर्षा एवं जलभराव चेतावनी",
        "rain_msg": "वर्षा की स्थिति ({cond}) और {rain}% संभावना है। खेत में जलभराव का जोखिम है।",
        "rain_act": "खेत में उचित जल निकासी नालियां सुनिश्चित करें और अतिरिक्त सिंचाई रोकें।",
        "heat_title": "☀️ उच्च तापमान तनाव चेतावनी",
        "heat_msg": "तापमान {temp}°C तक पहुंच गया है। फसलों में मुरझाने का खतरा है।",
        "heat_act": "सुबह या शाम के ठंडे समय में हल्की सिंचाई करें।",
        "normal_title": "✅ अनुकूल सूक्ष्म जलवायु",
        "normal_msg": "मौसम अनुकूल है ({cond}, {temp}°C, {hum}% आर्द्रता)। मिट्टी की नमी: {soil}।",
        "normal_act": "नियमित फसल निगरानी और निर्धारित उर्वरक प्रबंधन जारी रखें।",
        "summary_risk": "{hum}% आर्द्रता और {wet} घंटे पत्ती गीलेपन के कारण कवक रोग का बढ़ा हुआ जोखिम। सुरक्षात्मक कवकनाशी का प्रयोग करें।",
        "summary_normal": "फसलों के लिए अनुकूल जलवायु ({cond})। मिट्टी में पर्याप्त नमी है।"
    },
    "bn": {
        "fungal_title": "⚠️ ছত্রাকজনিত রোগের উচ্চ ঝুঁকি",
        "fungal_msg": "বাতাসের আর্দ্রতা {hum}%। উচ্চ আর্দ্রতা এবং পাতার ভেজা ভাব ({wet}ঘণ্টা) ছত্রাক সংক্রমণ ত্বরান্বিত করে।",
        "fungal_act": "বৃষ্টির পূর্বে ট্রাইকোডার্মা বা কপার অক্সিক্লোরাইড স্প্রে করুন।",
        "rain_title": "🌧️ বৃষ্টিপাত ও জলাবদ্ধতার সতর্কতা",
        "rain_msg": "বৃষ্টিপাতের সম্ভাবনা ({cond}) {rain}%। জমিতে জল জমার ঝুঁকি রয়েছে।",
        "rain_act": "জমিতে নিষ্কাশন নালা তৈরি করুন এবং সেচ বন্ধ রাখুন।",
        "heat_title": "☀️ তীব্র তাপমাত্রার সতর্কতা",
        "heat_msg": "তাপমাত্রা {temp}°C-এ পৌঁছেছে। ফসলে জলঘাটতি দেখা দিতে পারে।",
        "heat_act": "সকাল বা সন্ধ্যার সময় সেচ প্রদান করুন।",
        "normal_title": "✅ অনুকূল আবহাওয়া",
        "normal_msg": "বর্তমান আবহাওয়া {cond} ({temp}°C, {hum}% আর্দ্রতা)। মাটির আর্দ্রতা: {soil}।",
        "normal_act": "নিয়মিত ফসল পর্যবেক্ষণ ও পরিচর্যা চালিয়ে যান।",
        "summary_risk": "{hum}% আর্দ্রতা ও {wet}ঘণ্টা পাতার ভেজা ভাবের কারণে ছত্রাক রোগের ঝুঁকি। প্রতিরোধমূলক স্প্রে করুন।",
        "summary_normal": "অনুকূল কৃষি আবহাওয়া ({cond})। মাটিতে পর্যাপ্ত আর্দ্রতা আছে।"
    },
    "mr": {
        "fungal_title": "⚠️ बुरशीजन्य रोगाचा उच्च धोका",
        "fungal_msg": "हवेतील आर्द्रता {hum}% आहे. जास्त आर्द्रता आणि पानांवरील ओलावा ({wet} तास) बुरशीची वाढ वेगाने करतो.",
        "fungal_act": "पावसापूर्वी ट्रायकोडर्मा किंवा कॉपर ऑक्सिक्लोराईडची प्रतिबंधात्मक फवारणी करा.",
        "rain_title": "🌧️ पाऊस आणि पाणी साचण्याची शक्यता",
        "rain_msg": "पावसाची स्थिती ({cond}) आणि {rain}% शक्यता. शेतात पाणी साचण्याचा धोका.",
        "rain_act": "शेतात पाण्याचा निचरा व्यवस्थित करा आणि पाणी देणे थांबवा.",
        "heat_title": "☀️ उच्च तापमान ताण इशारा",
        "heat_msg": "तापमान {temp}°C वर पोहोचले आहे. पिके सुकण्याची शक्यता आहे.",
        "heat_act": "सकाळी लवकर किंवा संध्याकाळी पिकांना पाणी द्या.",
        "normal_title": "✅ पिकांसाठी अनुकूल हवामान",
        "normal_msg": "सध्याचे हवामान {cond} ({temp}°C, {hum}% आर्द्रता). जमिनीतील ओलावा: {soil}.",
        "normal_act": "नियमित पीक पाहणी आणि खत व्यवस्थापन चालू ठेवा.",
        "summary_risk": "{hum}% आर्द्रता आणि {wet} तास पानावरील ओलाव्यामुळे बुरशीचा धोका वाढला आहे. प्रतिबंधक फवारणी करा.",
        "summary_normal": "पिकांसाठी अनुकूल हवामान ({cond}). जमिनीत पुरेसा ओलावा आहे."
    },
    "gu": {
        "fungal_title": "⚠️ ફૂગજન્ય રોગનું ઊંચું જોખમ",
        "fungal_msg": "હવામાં ભેજ {hum}% છે. વધુ ભેજ અને પાનનો ભીનાશ ({wet} કલાક) ફૂગના ફેલાવાને ઝડપી બનાવે છે.",
        "fungal_act": "વરસાદ પહેલા ટ્રાઈકોડર્મા અથવા કોપર ઓક્સીક્લોરાઈડનો છંટકાવ કરો.",
        "rain_title": "🌧️ વરસાદ અને પાણી ભરાવાની ચેતવણી",
        "rain_msg": "વરસાદની શક્યતા ({cond}) {rain}% છે. ખેતરમાં પાણી ભરાવાનું જોખમ.",
        "rain_act": "ખેતરમાં પાણીના નિકાલની યોગ્ય વ્યવસ્થા કરો અને પિયત અટકાવો.",
        "heat_title": "☀️ વધુ ગરમી અને તાપમાન ચેતવણી",
        "heat_msg": "તાપમાન {temp}°C પર પહોંચ્યું છે. પાક કરમાઈ જવાની શક્યતા.",
        "heat_act": "સવારના અથવા સાંજના સમયે પિયત આપો.",
        "normal_title": "✅ પાક માટે સાનુકૂળ હવામાન",
        "normal_msg": "હાલનું હવામાન {cond} ({temp}°C, {hum}% ભેજ). જમીનમાં ભેજ: {soil}.",
        "normal_act": "નિયમિત પાકની દેખરેખ અને ખાતર વ્યવસ્થાપન ચાલુ રાખો.",
        "summary_risk": "{hum}% ભેજ અને {wet} કલાક પાનની ભીનાશથી ફૂગ રોગનું જોખમ. નિવારક છંટકાવ કરો.",
        "summary_normal": "પાક માટે સાનુકૂળ હવામાન ({cond}). જમીનમાં યોગ્ય ભેજ છે."
    },
    "pa": {
        "fungal_title": "⚠️ ਉੱਲੀ ਰੋਗ ਦਾ ਉੱਚ ਖਤਰਾ",
        "fungal_msg": "ਹਵਾ ਵਿੱਚ ਨਮੀ {hum}% ਹੈ। ਉੱਚ ਨਮੀ ਅਤੇ ਪੱਤਿਆਂ ਦਾ ਗਿੱਲਾਪਣ ({wet} ਘੰਟੇ) ਉੱਲੀ ਰੋਗ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।",
        "fungal_act": "ਮੀਂਹ ਤੋਂ ਪਹਿਲਾਂ ਟ੍ਰਾਈਕੋਡਰਮਾ ਜਾਂ ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
        "rain_title": "🌧️ ਮੀਂਹ ਅਤੇ ਪਾਣੀ ਭਰਨ ਦੀ ਚੇਤਾਵਨੀ",
        "rain_msg": "ਮੀਂਹ ਦੀ ਸੰਭਾਵਨਾ ({cond}) {rain}% ਹੈ। ਖੇਤ ਵਿੱਚ ਪਾਣੀ ਖੜ੍ਹਨ ਦਾ ਖਤਰਾ।",
        "rain_act": "ਖੇਤ ਵਿੱਚ ਪਾਣੀ ਦੇ ਨਿਕਾਸ ਦਾ ਪ੍ਰਬੰਧ ਕਰੋ ਅਤੇ ਸਿੰਚਾਈ ਰੋਕੋ।",
        "heat_title": "☀️ ਉੱਚ ਤਾਪਮਾਨ ਚੇਤਾਵਨੀ",
        "heat_msg": "ਤਾਪਮਾਨ {temp}°C ਤੱਕ ਪਹੁੰਚ ਗਿਆ ਹੈ। ਫਸਲਾਂ ਮੁਰਝਾ ਸਕਦੀਆਂ ਹਨ।",
        "heat_act": "ਸਵੇਰ ਜਾਂ ਸ਼ਾਮ ਦੇ ਸਮੇਂ ਹਲਕੀ ਸਿੰਚਾਈ ਕਰੋ।",
        "normal_title": "✅ ਫਸਲ ਲਈ ਅਨੁਕੂਲ ਮੌਸਮ",
        "normal_msg": "ਮੌਜੂਦਾ ਮੌਸਮ {cond} ({temp}°C, {hum}% ਨਮੀ)। ਮਿੱਟੀ ਦੀ ਨਮੀ: {soil}।",
        "normal_act": "ਨਿਯਮਤ ਫਸਲ ਨਿਗਰਾਨੀ ਜਾਰੀ ਰੱਖੋ।",
        "summary_risk": "{hum}% ਨਮੀ ਅਤੇ {wet} ਘੰਟੇ ਪੱਤੇ ਗਿੱਲੇ ਰਹਿਣ ਕਾਰਨ ਉੱਲੀ ਰੋਗ ਦਾ ਖਤਰਾ। ਬਚਾਅ ਲਈ ਛਿੜਕਾਅ ਕਰੋ।",
        "summary_normal": "ਫਸਲ ਲਈ ਅਨੁਕੂਲ ਮੌਸਮ ({cond})।"
    },
    "ur": {
        "fungal_title": "⚠️ پھپھوندی کی بیماری کا زیادہ خطرہ",
        "fungal_msg": "ہوا میں نمی {hum}٪ ہے۔ زیادہ نمی اور پتوں کی گیلاہٹ ({wet} گھنٹے) پھپھوندی کو بڑھاتی ہے۔",
        "fungal_act": "بارش سے پہلے ٹرائیکوڈرما یا کاپر آکسی کلورائیڈ کا اسپرے کریں۔",
        "rain_title": "🌧️ بارش اور پانی جمع ہونے کا انتباہ",
        "rain_msg": "بارش کے امکانات ({cond}) {rain}٪ ہیں۔ کھیت میں پانی جمع ہونے کا خطرہ۔",
        "rain_act": "کھیت سے نکاسی آب کا مناسب انتظام کریں اور آبپاشی روک دیں۔",
        "heat_title": "☀️ شدید گرمی اور درجہ حرارت کا انتباہ",
        "heat_msg": "درجہ حرارت {temp}°C تک پہنچ چکا ہے۔ فصلوں کے مرجھانے کا اندیشہ ہے۔",
        "heat_act": "صبح سویرے یا شام کے وقت ہلکی آبپاشی کریں۔",
        "normal_title": "✅ سازگار زرعی موسم",
        "normal_msg": "موجودہ موسم {cond} ({temp}°C، {hum}٪ نمی) ہے۔ مٹی میں نمی: {soil}۔",
        "normal_act": "فصل کی معمول کی نگرانی اور کھاد کا انتظام جاری رکھیں۔",
        "summary_risk": "{hum}٪ نمی اور {wet} گھنٹے پتوں کے گیلے رہنے سے پھپھوندی کا خطرہ۔ حفاظتی اسپرے کریں۔",
        "summary_normal": "فصل کے لیے سازگار موسم ({cond})۔ مٹی میں مناسب نمی موجود ہے۔"
    },
    "or": {
        "fungal_title": "⚠️ କବକ ରୋଗର ଉଚ୍ଚ ଆଶଙ୍କା",
        "fungal_msg": "ବାୟୁମଣ୍ଡଳୀୟ ଆର୍ଦ୍ରତା {hum}%। ଉଚ୍ଚ ଆର୍ଦ୍ରତା ଏବଂ ପତ୍ର ଓଦା ରହିବା ({wet} ଘଣ୍ଟା) କବକ ରୋଗ ବୃଦ୍ଧି କରେ।",
        "fungal_act": "ବର୍ଷା ପୂର୍ବରୁ ଟ୍ରାଇକୋଡର୍ମା କିମ୍ବା କପର ଅକ୍ସିକ୍ଲୋରାଇଡ ସ୍ପ୍ରେ କରନ୍ତୁ।",
        "rain_title": "🌧️ ବର୍ଷା ଏବଂ ଜଳବନ୍ଦୀ ଚେତାବନୀ",
        "rain_msg": "ବର୍ଷା ସମ୍ଭାବନା ({cond}) {rain}%। ଜମିରେ ପାଣି ଜମିବା ଆଶଙ୍କା।",
        "rain_act": "ଜମିରେ ଜଳ ନିଷ୍କାସନ ନାଳୀ ସଫା ରଖନ୍ତୁ ଏବଂ ଜଳସେଚନ ବନ୍ଦ କରନ୍ତୁ।",
        "heat_title": "☀️ ପ୍ରଚଣ୍ଡ ତାପମାତ୍ରା ସତର୍କତା",
        "heat_msg": "ତାପମାତ୍ରା {temp}°C ଛୁଇଁଛି। ଫସଲ ଶୁଖିଯିବା ଆଶଙ୍କା।",
        "heat_act": "ସକାଳେ କିମ୍ବା ସନ୍ଧ୍ୟାରେ ଜଳସେଚନ କରନ୍ତୁ।",
        "normal_title": "✅ ଅନୁକୂଳ ପାଣିପାଗ",
        "normal_msg": "ବର୍ତ୍ତମାନର ପାଣିପାଗ {cond} ({temp}°C, {hum}% ଆର୍ଦ୍ରତା)। ମାଟିର ଓଦା ଅବସ୍ଥା: {soil}।",
        "normal_act": "ନିୟମିତ ଫସଲ ଯତ୍ନ ଏବଂ ସାର ପ୍ରୟୋଗ ଜାରି ରଖନ୍ତୁ।",
        "summary_risk": "{hum}% ଆର୍ଦ୍ରତା ଯୋଗୁଁ କବକ ରୋଗ ଆଶଙ୍କା। ପ୍ରତିଷେଧକ ସ୍ପ୍ରେ କରନ୍ତୁ।",
        "summary_normal": "ଫସଲ ପାଇଁ ଅନୁକୂଳ ପାଣିପାଗ ({cond})।"
    },
    "as": {
        "fungal_title": "⚠️ ভেঁকুৰজনিত ৰোগৰ উচ্চ আশংকা",
        "fungal_msg": "বায়ুমণ্ডলত আৰ্দ্ৰতা {hum}%। উচ্চ আৰ্দ্ৰতা আৰু পাত তিতা থকাৰ ফলত ({wet} ঘণ্টা) ভেঁকুৰ ৰোগ বৃদ্ধি পায়।",
        "fungal_act": "বৰষুণৰ পূৰ্বে ট্ৰাইকোডাৰ্মা বা কপাৰ অক্সিক্ল'ৰাইড স্প্ৰে কৰক।",
        "rain_title": "🌧️ বৰষুণ আৰু পানী জমা হোৱাৰ সতৰ্কবাণী",
        "rain_msg": "বৰষুণৰ সম্ভাৱনা ({cond}) {rain}%। পথাৰত পানী জমা হোৱাৰ আশংকা।",
        "rain_act": "পথাৰত পানী ওলাই যোৱাৰ সু-ব্যৱস্থা কৰক আৰু জলসিঞ্চন বন্ধ ৰাখক।",
        "heat_title": "☀️ তীব্ৰ উত্তাপৰ সতৰ্কতা",
        "heat_msg": "উত্তাপ {temp}°C হৈছে। শস্য শুকাই যোৱাৰ সম্ভাৱনা আছে।",
        "heat_act": "ৰাতিপুৱা বা গধূলি সময়ত পানী দিয়ক।",
        "normal_title": "✅ শস্যৰ বাবে অনুকূল বতৰ",
        "normal_msg": "বৰ্তমান বতৰ {cond} ({temp}°C, {hum}% আৰ্দ্ৰতা)। মাটিৰ আৰ্দ্ৰতা: {soil}।",
        "normal_act": "নিয়মীয়া শস্য পৰিদৰ্শন অব্যাহত ৰাখক।",
        "summary_risk": "{hum}% আৰ্দ্ৰতাৰ বাবে ভেঁকুৰ ৰোগৰ আশংকা। প্ৰতিৰোধমূলক স্প্ৰে কৰক।",
        "summary_normal": "শস্যৰ বাবে অনুকূল বতৰ ({cond})।"
    },
    "ne": {
        "fungal_title": "⚠️ ढुसीजन्य रोगको उच्च जोखिम",
        "fungal_msg": "हावामा आर्द्रता {hum}% छ। उच्च आर्द्रता र पातको ओसिलोपनले ({wet} घण्टा) ढुसी रोग बढाउँछ।",
        "fungal_act": "पानी पर्नु अघि ट्राइकोडर्मा वा कपर अक्सिक्लोराइड छर्कनुहोस्।",
        "rain_title": "🌧️ वर्षा र पानी जम्ने चेतावनी",
        "rain_msg": "वर्षाको सम्भावना ({cond}) {rain}% छ। खेतमा पानी जम्ने जोखिम।",
        "rain_act": "खेतमा उचित निकासको व्यवस्था गर्नुहोस् र सिँचाइ रोक्नुहोस्।",
        "heat_title": "☀️ उच्च तापक्रमको चेतावनी",
        "heat_msg": "तापक्रम {temp}°C पुगेको छ। बाली ओइलाउन सक्छ।",
        "heat_act": "बिहान वा बेलुकाको समयमा सिँचाइ गर्नुहोस्।",
        "normal_title": "✅ बालीका लागि अनुकूल मौसम",
        "normal_msg": "वर्तमान मौसम {cond} ({temp}°C, {hum}% आर्द्रता)। माटोको चिस्यान: {soil}।",
        "normal_act": "नियमित बाली निरीक्षण जारी राख्नुहोस्।",
        "summary_risk": "{hum}% आर्द्रताका कारण ढुसी रोगको जोखिम। रोकथामका लागि औषधि छर्कनुहोस्।",
        "summary_normal": "बालीका लागि अनुकूल मौसम ({cond})।"
    },
    "si": {
        "fungal_title": "⚠️ දිලීර රෝග අවදානම ඉහළයි",
        "fungal_msg": "වාතයේ ආර්ද්‍රතාවය {hum}% කි. අධික ආර්ද්‍රතාවය සහ පත්‍ර තෙතමනය ({wet} පැය) දිලීර රෝග වර්ධනය කරයි.",
        "fungal_act": "වැස්සට පෙර ට්‍රයිකොඩර්මා හෝ කොපර් ඔක්සික්ලෝරයිඩ් යොදන්න.",
        "rain_title": "🌧️ වර්ෂාපතන අනතුරු ඇඟවීම",
        "rain_msg": "වර්ෂා තත්ත්වය ({cond}) {rain}% සම්භාවිතාව. ජලය රැඳීමේ අවදානම.",
        "rain_act": "ක්ෂේත්‍රයේ ජල බැසයාම තහවුරු කර ජල සම්පාදනය නවත්වන්න.",
        "heat_title": "☀️ අධික උෂ්ණත්ව අනතුරු ඇඟවීම",
        "heat_msg": "උෂ්ණත්වය {temp}°C දක්වා ඉහළ ගොස් ඇත. බෝග වියළී යා හැක.",
        "heat_act": "උදෑසන හෝ සවස් කාලයේ ජලය යොදන්න.",
        "normal_title": "✅ හිතකර කාලගුණය",
        "normal_msg": "වත්මන් කාලගුණය {cond} ({temp}°C, {hum}% ආර්ද්‍රතාවය). පසෙහි තෙතමනය: {soil}.",
        "normal_act": "සාමාන්‍ය බෝග නිරීක්ෂණය කරගෙන යන්න.",
        "summary_risk": "{hum}% ආර්ද්‍රතාවය නිසා දිලීර රෝග අවදානමක් ඇත. ආරක්ෂිත ප්‍රතිකාර යොදන්න.",
        "summary_normal": "බෝග සඳහා හිතකර කාලගුණ තත්ත්වයක් ({cond})."
    },
    "ar": {
        "fungal_title": "⚠️ خطر مرتفع لجراثيم الفطريات",
        "fungal_msg": "الرطوبة النسبية الحية هي {hum}%. الرطوبة العالية ورطوبة الأوراق ({wet} ساعة) تسرع نمو الفطريات.",
        "fungal_act": "قم برش مبيد فطري وقائي (تريكوديرما أو أوكسي كلوريد النحاس) قبل هطول الأمطار.",
        "rain_title": "🌧️ تحذير من هطول الأمطار وتجمع المياه",
        "rain_msg": "حالة هطول أمطار ({cond}) بنسبة احتمال {rain}%. خطر غرق التربة.",
        "rain_act": "تأكد من قنوات تصريف المياه في الحقل وأوقف الري بالرش.",
        "heat_title": "☀️ تحذير من الإجهاد الحراري الشديد",
        "heat_msg": "وصلت درجة الحرارة إلى {temp} درجة مئوية. قد تتعرض المحاصيل للذبول.",
        "heat_act": "قم بري المحاصيل في الصباح الباكر أو في المساء.",
        "normal_title": "✅ ظروف مناخية ملائمة للمحاصيل",
        "normal_msg": "الطقس الحالي {cond} ({temp}°C، رطوبة {hum}%). رطوبة التربة: {soil}.",
        "normal_act": "استمر في المراقبة الدورية للمحاصيل والتسميد المجدول.",
        "summary_risk": "خطر متزايد للإصابة بالأمراض الفطرية بسبب {hum}% رطوبة و{wet} ساعة بلل الأوراق. ضع مبيداً وقائياً.",
        "summary_normal": "مناخ ملائم للزراعة ({cond}). رطوبة التربة كافية ومستقرة."
    },
    "fr": {
        "fungal_title": "⚠️ Risque élevé de spores fongiques",
        "fungal_msg": "L'humidité relative est de {hum}%. Une forte humidité et l'humectation des feuilles ({wet}h) favorisent les champignons.",
        "fungal_act": "Appliquez un bio-fongicide (Trichoderma ou Oxychlorure de cuivre) avant la pluie.",
        "rain_title": "🌧️ Alerte précipitations et engorgement",
        "rain_msg": "Précipitations détectées ({cond}) avec {rain}% de probabilité. Risque d'engorgement des sols.",
        "rain_act": "Assurez un bon drainage des parcelles et suspendez l'irrigation par aspersion.",
        "heat_title": "☀️ Alerte au stress thermique élevé",
        "heat_msg": "La température a atteint {temp}°C. Les cultures risquent de flétrir.",
        "heat_act": "Irriguez les parcelles tôt le matin ou en soirée.",
        "normal_title": "✅ Conditions microclimatiques favorables",
        "normal_msg": "Météo actuelle : {cond} ({temp}°C, humidité {hum}%). Humidité du sol : {soil}.",
        "normal_act": "Poursuivez la surveillance habituelle des cultures et la fertilisation programmée.",
        "summary_risk": "Risque accru de maladies fongiques dû à {hum}% d'humidité et {wet}h d'humectation foliaire. Traitement préventif conseillé.",
        "summary_normal": "Microclimat favorable ({cond}). Humidité du sol adéquate."
    },
    "es": {
        "fungal_title": "⚠️ Alto riesgo de esporas fúngicas",
        "fungal_msg": "La humedad relativa es del {hum}%. La alta humedad y el follaje mojado ({wet}h) aceleran la germinación de hongos.",
        "fungal_act": "Aplique biofungicida (Trichoderma o Oxicloruro de cobre) antes de las lluvias.",
        "rain_title": "🌧️ Advertencia de precipitaciones y anegamiento",
        "rain_msg": "Lluvia detectada ({cond}) con {rain}% de probabilidad. Riesgo de encharcamiento del suelo.",
        "rain_act": "Asegure zanjas de drenaje adecuadas en el campo y pause el riego superior.",
        "heat_title": "☀️ Aviso de estrés térmico elevado",
        "heat_msg": "La temperatura ha alcanzado {temp}°C. Los cultivos pueden marchitarse por transpiración.",
        "heat_act": "Riegue los cultivos en las primeras horas de la mañana o al anochecer.",
        "normal_title": "✅ Condiciones microclimáticas favorables",
        "normal_msg": "Clima actual: {cond} ({temp}°C, {hum}% humedad). Humedad del suelo: {soil}.",
        "normal_act": "Continúe el monitoreo rutinario y la fertirrigación programada.",
        "summary_risk": "Riesgo elevado de enfermedades fúngicas por {hum}% de humedad y {wet}h de hoja mojada. Aplique fungicida preventivo.",
        "summary_normal": "Microclima favorable ({cond}). Humedad del suelo adecuada."
    },
    "pt": {
        "fungal_title": "⚠️ Alto risco de esporos fúngicos",
        "fungal_msg": "A umidade relativa é de {hum}%. Alta umidade e molhamento foliar ({wet}h) favorecem infecções fúngicas.",
        "fungal_act": "Aplique biofungicida (Trichoderma ou Oxicloreto de cobre) antes da chuva.",
        "rain_title": "🌧️ Alerta de chuva e encharcamento",
        "rain_msg": "Condição de chuva detectada ({cond}) com {rain}% de chance. Risco de saturação do solo.",
        "rain_act": "Garanta canais de drenagem no campo e interrompa a irrigação aérea.",
        "heat_title": "☀️ Alerta de estresse térmico elevado",
        "heat_msg": "A temperatura atingiu {temp}°C. Culturas podem sofrer murchamento.",
        "heat_act": "Irrigue durante as primeiras horas da manhã ou ao entardecer.",
        "normal_title": "✅ Condições microclimáticas favoráveis",
        "normal_msg": "Clima atual: {cond} ({temp}°C, {hum}% umidade). Umidade do solo: {soil}.",
        "normal_act": "Continue o monitoramento de rotina e fertirrigação programada.",
        "summary_risk": "Risco elevado de fungos devido a {hum}% de umidade e {wet}h de folhas molhadas. Aplique fungicida preventivo.",
        "summary_normal": "Microclima favorável ({cond}). Umidade do solo adequada."
    },
    "de": {
        "fungal_title": "⚠️ Hohes Risiko für Pilzsporen",
        "fungal_msg": "Die relative Luftfeuchtigkeit beträgt {hum}%. Hohe Feuchte und Blattnässe ({wet}h) beschleunigen Pilzinfektionen.",
        "fungal_act": "Tragen Sie vor dem Regen ein Bio-Fungizid (Trichoderma oder Kupferoxychlorid) auf.",
        "rain_title": "🌧️ Regen- und Staunässewarnung",
        "rain_msg": "Regen erkannt ({cond}) mit {rain}% Wahrscheinlichkeit. Gefahr von Bodenversumpfung.",
        "rain_act": "Entwässerungsgräben überprüfen und Überkopf-Bewässerung pausieren.",
        "heat_title": "☀️ Warnung vor Hitzestress",
        "heat_msg": "Die Temperatur hat {temp}°C erreicht. Pflanzen können Welkesymptome zeigen.",
        "heat_act": "Pflanzen früh morgens oder spät abends bewässern.",
        "normal_title": "✅ Günstiges Mikroklima",
        "normal_msg": "Aktuelles Wetter: {cond} ({temp}°C, {hum}% Feuchtigkeit). Bodenfeuchte: {soil}.",
        "normal_act": "Regelmäßige Bestandsbeobachtung und Düngung wie geplant fortführen.",
        "summary_risk": "Erhöhtes Pilzkrankheitsrisiko durch {hum}% Luftfeuchtigkeit und {wet}h Blattnässe. Vorbeugend behandeln.",
        "summary_normal": "Günstiges Mikroklima ({cond}). Ausreichende Bodenfeuchtigkeit."
    },
    "it": {
        "fungal_title": "⚠️ Rischio elevato di spore fungine",
        "fungal_msg": "Umidità relativa al {hum}%. L'elevata umidità e la bagnatura fogliare ({wet}h) favoriscono la germinazione fungina.",
        "fungal_act": "Applicare bio-fungicida (Trichoderma o Ossicloruro di rame) prima delle piogge.",
        "rain_title": "🌧️ Allerta pioggia e ristagno idrico",
        "rain_msg": "Precipitazioni rilevate ({cond}) con probabilità del {rain}%. Rischio di asfissia radicale.",
        "rain_act": "Assicurare scoli di drenaggio nei campi e sospendere l'irrigazione a pioggia.",
        "heat_title": "☀️ Allerta stress termico elevato",
        "heat_msg": "La temperatura ha raggiunto {temp}°C. Le colture possono subire avvizzimento.",
        "heat_act": "Irrigare le colture nelle prime ore del mattino o alla sera.",
        "normal_title": "✅ Condizioni microclimatiche favorevoli",
        "normal_msg": "Meteo attuale: {cond} ({temp}°C, {hum}% umidità). Umidità del suolo: {soil}.",
        "normal_act": "Continuare il consueto monitoraggio colturale e la fertirrigazione.",
        "summary_risk": "Rischio elevato di malattie fungine dovuto al {hum}% di umidità e {wet}h di bagnatura fogliare. Applicare fungicida.",
        "summary_normal": "Microclima favorevole ({cond}). Umidità del suolo ottimale."
    },
    "ru": {
        "fungal_title": "⚠️ Высокий риск грибковых спор",
        "fungal_msg": "Относительная влажность составляет {hum}%. Высокая влажность и влажность листьев ({wet}ч) ускоряют прорастание грибков.",
        "fungal_act": "Примените биофунгицид (Триходерма или хлорокись меди) перед дождями.",
        "rain_title": "🌧️ Предупреждение об осадках и переувлажнении",
        "rain_msg": "Обнаружены осадки ({cond}) с вероятностью {rain}%. Риск заболачивания почвы.",
        "rain_act": "Обеспечьте дренаж на поле и приостановите верхний полив.",
        "heat_title": "☀️ Предупреждение о тепловом стрессе",
        "heat_msg": "Температура достигла {temp}°C. Посевы могут испытывать увядание.",
        "heat_act": "Проводите полив рано утром или в вечерние часы.",
        "normal_title": "✅ Благоприятные микроклиматические условия",
        "normal_msg": "Текущая погода: {cond} ({temp}°C, влажность {hum}%). Влажность почвы: {soil}.",
        "normal_act": "Продолжайте регулярный мониторинг и запланированное внесение удобрений.",
        "summary_risk": "Повышенный риск грибковых заболеваний из-за {hum}% влажности и {wet}ч влажности листьев. Примените фунгицид.",
        "summary_normal": "Благоприятный микроклимат ({cond}). Влажность почвы в норме."
    },
    "ja": {
        "fungal_title": "⚠️ 糸状菌（かび）胞子の発生リスク高",
        "fungal_msg": "相対湿度は {hum}% です。高湿度と葉の濡れ（{wet}時間）が糸状菌胞子の発芽を促進します。",
        "fungal_act": "降雨前に生物殺菌剤（トリコデルマまたは銅水和剤）を予防散布してください。",
        "rain_title": "🌧️ 降雨および冠水・過湿警報",
        "rain_msg": "降雨の可能性（{cond}）が {rain}% 検出されました。土壌の湛水リスクがあります。",
        "rain_act": "圃場の排水溝を確保し、頭上かん水を一時停止してください。",
        "heat_title": "☀️ 高温障害・熱ストレス警報",
        "heat_msg": "気温が {temp}°C に達しました。作物の萎凋リスクが高まっています。",
        "heat_act": "早朝または夕方の涼しい時間帯にかん水を行ってください。",
        "normal_title": "✅ 作物生育に適した気象条件",
        "normal_msg": "現在の気象は {cond}（{temp}°C、湿度 {hum}%）です。土壌水分：{soil}。",
        "normal_act": "定期的な作物の見回りと計画的な施肥を継続してください。",
        "summary_risk": "湿度 {hum}% および葉面濡れ {wet}時間により糸状菌病害のリスクが上昇しています。予防散布を行ってください。",
        "summary_normal": "作物にとって良好な微気候（{cond}）です。土壌水分も適切です。"
    },
    "ko": {
        "fungal_title": "⚠️ 곰팡이 포자 발생 위험 높음",
        "fungal_msg": "상대습도가 {hum}%입니다. 높은 습도와 잎 표면 수분({wet}시간)이 곰팡이 포자 발아를 촉진합니다.",
        "fungal_act": "비가 오기 전에 생물살균제(트리코더마 또는 코퍼옥시클로라이드)를 살포하십시오.",
        "rain_title": "🌧️ 강우 및 침수 주의보",
        "rain_msg": "강우 상태 감지({cond}), 강수 확률 {rain}%. 토양 과습 및 배수 불량 위험.",
        "rain_act": "포장 배수로를 정비하고 상부 관수를 일시 중단하십시오.",
        "heat_title": "☀️ 고온 열 스트레스 주의보",
        "heat_msg": "기온이 {temp}°C에 도달했습니다. 작물 시들음 현상이 발생할 수 있습니다.",
        "heat_act": "이른 아침이나 해 질 녘에 관수를 실시하십시오.",
        "normal_title": "✅ 작물 생육에 유리한 미기후",
        "normal_msg": "현재 날씨: {cond} ({temp}°C, 습도 {hum}%). 토양 수분: {soil}.",
        "normal_act": "정기적인 작물 예찰 및 계획된 비배 관리를 유지하십시오.",
        "summary_risk": "습도 {hum}% 및 잎 수분 지속 {wet}시간으로 곰팡이병 발생 위험이 높습니다. 예방적 약제 살포를 권장합니다.",
        "summary_normal": "작물에 유리한 기상 조건({cond})입니다. 토양 수분이 적정합니다."
    },
    "zh": {
        "fungal_title": "⚠️ 真菌孢子发芽高风险预警",
        "fungal_msg": "实时微气候相对湿度为 {hum}%。高湿及叶面湿润（{wet}小时）加速真菌孢子萌发。",
        "fungal_act": "降雨前喷施生物杀菌剂（哈茨木霉菌或氧氯化铜50WP）。",
        "rain_title": "🌧️ 降雨与田间积水预警",
        "rain_msg": "检测到降雨情况（{cond}），降水概率 {rain}%。存在土壤涝渍与根系窒息风险。",
        "rain_act": "确保田间排水沟畅通，并暂停顶部喷灌。",
        "heat_title": "☀️ 高温热胁迫预警",
        "heat_msg": "气温已达 {temp}°C。农作物可能出现萎蔫和蒸腾胁迫。",
        "heat_act": "请在清晨或傍晚凉爽时段灌溉农作物。",
        "normal_title": "✅ 微气候条件良好",
        "normal_msg": "当前天气为 {cond}（{temp}°C，湿度 {hum}%）。土壤水分：{soil}。",
        "normal_act": "继续日常田间巡查并按计划水肥管理。",
        "summary_risk": "受 {hum}% 湿度及 {wet}小时叶面湿润影响，真菌病害风险升高。建议进行预防性喷药。",
        "summary_normal": "微气候良好（{cond}）。土壤墒情适宜。"
    }
}

def get_localized_weather_alerts(
    humidity: int,
    tempC: float,
    rain_chance: int,
    condition: str,
    leaf_wetness: float,
    soil_moisture: str,
    lang: str = "en"
) -> Tuple[str, List[Dict[str, Any]]]:
    """Generates localized dynamic weather alerts and summary in the selected language."""
    norm_lang = (lang or "en").lower().strip()
    t = WEATHER_ALERTS_25.get(norm_lang, WEATHER_ALERTS_25.get("en"))

    loc_cond = localize_weather_condition(condition, norm_lang)
    dynamic_alerts: List[Dict[str, Any]] = []

    if humidity >= 75:
        dynamic_alerts.append({
            "id": "alert-fungal-1",
            "urgency": "high",
            "title": t["fungal_title"],
            "message": t["fungal_msg"].format(hum=humidity, wet=leaf_wetness),
            "timestamp": "Live API Telemetry",
            "actionRequired": t["fungal_act"]
        })

    if "rain" in condition.lower() or "storm" in condition.lower() or rain_chance > 60:
        dynamic_alerts.append({
            "id": "alert-rain-2",
            "urgency": "high" if rain_chance > 80 else "moderate",
            "title": t["rain_title"],
            "message": t["rain_msg"].format(cond=loc_cond, rain=rain_chance),
            "timestamp": "Live OpenWeather",
            "actionRequired": t["rain_act"]
        })

    if tempC >= 35:
        dynamic_alerts.append({
            "id": "alert-heat-3",
            "urgency": "high",
            "title": t["heat_title"],
            "message": t["heat_msg"].format(temp=tempC),
            "timestamp": "Live Telemetry",
            "actionRequired": t["heat_act"]
        })

    if not dynamic_alerts:
        dynamic_alerts.append({
            "id": "alert-normal-4",
            "urgency": "low",
            "title": t["normal_title"],
            "message": t["normal_msg"].format(cond=loc_cond, temp=tempC, hum=humidity),
            "timestamp": "Live API",
            "actionRequired": t["normal_act"]
        })

    if humidity >= 75:
        alert_summary = t["summary_risk"].format(hum=humidity, wet=leaf_wetness)
    else:
        alert_summary = t["summary_normal"].format(cond=loc_cond, moist=soil_moisture)

    return alert_summary, dynamic_alerts


# --- FULL 25-LANGUAGE MARKETPLACE & MANDI FORECAST LOCALIZATION ---
MARKET_FORECAST_25: Dict[str, Dict[str, str]] = {
    "en": {
        "rising_title": "Prices rising — Hold your crop",
        "rising_rec": "Wait 2-3 weeks before selling",
        "falling_title": "Prices falling — Sell now",
        "falling_rec": "Sell immediately at best mandi",
        "stable_title": "Prices stable",
        "stable_rec": "Sell at best available mandi now"
    },
    "ta": {
        "rising_title": "விலை உயர்கிறது — பயிரை சேமித்து வைக்கவும்",
        "rising_rec": "விற்பனைக்கு முன் 2-3 வாரங்கள் காத்திருக்கவும்",
        "falling_title": "விலை குறைகிறது — உடனடியாக விற்கவும்",
        "falling_rec": "அருகிலுள்ள சிறந்த சந்தையில் உடனடியாக விற்கவும்",
        "stable_title": "விலை சீராக உள்ளது",
        "stable_rec": "தற்போதைய சிறந்த சந்தை விலையில் விற்கவும்"
    },
    "te": {
        "rising_title": "ధరలు పెరుగుతున్నాయి — నిల్వ చేయండి",
        "rising_rec": "అమ్మకానికి 2-3 వారాలు వేచి ఉండండి",
        "falling_title": "ధరలు తగ్గుతున్నాయి — వెంటనే అమ్మండి",
        "falling_rec": "ఉత్తమ మార్కెట్ లో వెంటనే విక్రయించండి",
        "stable_title": "ధరలు స్థిరంగా ఉన్నాయి",
        "stable_rec": "ప్రస్తుత ఉత్తమ ధర వద్ద మార్కెట్ లో అమ్మండి"
    },
    "ml": {
        "rising_title": "വില കൂടുന്നു — വിള സൂക്ഷിക്കുക",
        "rising_rec": "വിൽപ്പനയ്ക്കായി 2-3 ആഴ്ച കാത്തിരിക്കുക",
        "falling_title": "വില കുറയുന്നു — ഇപ്പോൾ വിൽക്കുക",
        "falling_rec": "ഏറ്റവും മികച്ച വിപണിയിൽ ഉടനടി വിൽക്കുക",
        "stable_title": "വില സ്ഥിരത പുലർത്തുന്നു",
        "stable_rec": "ലഭ്യമായ മികച്ച വിപണിയിൽ ഇപ്പോൾ വിൽക്കുക"
    },
    "kn": {
        "rising_title": "ಬೆಲೆ ಹೆಚ್ಚುತ್ತಿದೆ — ಬೆಳೆ ದಾಸ್ತಾನು ಮಾಡಿ",
        "rising_rec": "ಮಾರಾಟಕ್ಕೆ 2-3 ವಾರ ಕಾಯಿರಿ",
        "falling_title": "ಬೆಲೆ ಇಳಿಯುತ್ತಿದೆ — ತಕ್ಷಣ ಮಾರಿ",
        "falling_rec": "ಉತ್ತಮ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡಿ",
        "stable_title": "ಬೆಲೆ ಸ್ಥಿರವಾಗಿದೆ",
        "stable_rec": "ಉತ್ತಮ ಬೆಲೆ ಇರುವ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಈಗಲೇ ಮಾರಿ"
    },
    "hi": {
        "rising_title": "कीमतें बढ़ रही हैं — फसल रोक कर रखें",
        "rising_rec": "बेचने से पहले 2-3 सप्ताह प्रतीक्षा करें",
        "falling_title": "कीमतें गिर रही हैं — तुरंत बेचें",
        "falling_rec": "सर्वोत्तम मंडी में तुरंत बिक्री करें",
        "stable_title": "कीमतें स्थिर हैं",
        "stable_rec": "उपलब्ध सर्वोत्तम मंडी में अभी बेचें"
    },
    "bn": {
        "rising_title": "দাম বাড়ছে — ফসল ধরে রাখুন",
        "rising_rec": "বিক্রির আগে ২-৩ সপ্তাহ অপেক্ষা করুন",
        "falling_title": "দাম কমছে — এখনই বিক্রি করুন",
        "falling_rec": "সেরা মান্ডিতে অবিলম্বে বিক্রি করুন",
        "stable_title": "দাম স্থিতিশীল রয়েছে",
        "stable_rec": "উপলব্ধ সেরা মান্ডিতে এখনই বিক্রি করুন"
    },
    "mr": {
        "rising_title": "किमती वाढत आहेत — पीक साठवून ठेवा",
        "rising_rec": "विक्रीपूर्वी २-३ आठवडे प्रतीक्षा करा",
        "falling_title": "किमती घसरत आहेत — त्वरित विका",
        "falling_rec": "सर्वोत्कृष्ट बाजार समितीत त्वरित विक्री करा",
        "stable_title": "किमती स्थिर आहेत",
        "stable_rec": "उपलब्ध सर्वोत्तम बाजार समितीत आता विका"
    },
    "gu": {
        "rising_title": "ભાવ વધી રહ્યા છે — પાક સાચવી રાખો",
        "rising_rec": "વેચાણ પહેલાં 2-3 અઠવાડિયા રાહ જુઓ",
        "falling_title": "ભાવ ઘટી રહ્યા છે — તરત જ વેચો",
        "falling_rec": "શ્રેષ્ઠ માર્કેટિંગ યાર્ડમાં તરત જ વેચાણ કરો",
        "stable_title": "ભાવ સ્થિર છે",
        "stable_rec": "ઉપલબ્ધ શ્રેષ્ઠ બજારમાં અત્યારે જ વેચો"
    },
    "pa": {
        "rising_title": "ਭਾਅ ਵੱਧ ਰਹੇ ਹਨ — ਫਸਲ ਰੋਕ ਕੇ ਰੱਖੋ",
        "rising_rec": "ਵੇਚਣ ਤੋਂ ਪਹਿਲਾਂ 2-3 ਹਫ਼ਤੇ ਉਡੀਕ ਕਰੋ",
        "falling_title": "ਭਾਅ ਡਿੱਗ ਰਹੇ ਹਨ — ਤੁਰੰਤ ਵੇਚੋ",
        "falling_rec": "ਸਭ ਤੋਂ ਵਧੀਆ ਮੰਡੀ ਵਿੱਚ ਤੁਰੰਤ ਵਿਕਰੀ ਕਰੋ",
        "stable_title": "ਭਾਅ ਸਥਿਰ ਹਨ",
        "stable_rec": "ਮੌਜੂਦਾ ਵਧੀਆ ਮੰਡੀ ਵਿੱਚ ਹੁਣੇ ਵੇਚੋ"
    },
    "ur": {
        "rising_title": "قیمتیں بڑھ رہی ہیں — فصل روک کر رکھیں",
        "rising_rec": "فروخت سے قبل 2-3 ہفتے انتظار کریں",
        "falling_title": "قیمتیں گر رہی ہیں — فوری فروخت کریں",
        "falling_rec": "بہترین منڈی میں فوری فروخت کریں",
        "stable_title": "قیمتیں مستحکم ہیں",
        "stable_rec": "بہترین دستیاب منڈی میں ابھی فروخت کریں"
    },
    "or": {
        "rising_title": "ଦର ବଢ଼ୁଛି — ଫସଲ ସାଇତି ରଖନ୍ତୁ",
        "rising_rec": "ବିକ୍ରି ପୂର୍ବରୁ ୨-୩ ସପ୍ତାହ ଅପେକ୍ଷା କରନ୍ତୁ",
        "falling_title": "ଦର ଖସୁଛି — ଶୀଘ୍ର ବିକ୍ରି କରନ୍ତୁ",
        "falling_rec": "ଉତ୍ତମ ମଣ୍ଡିରେ ତୁରନ୍ତ ବିକ୍ରି କରନ୍ତୁ",
        "stable_title": "ଦର ସ୍ଥିର ରହିଛି",
        "stable_rec": "ଉପଲବ୍ଧ ସର୍ବୋତ୍ତମ ମଣ୍ଡିରେ ଏବେ ବିକ୍ରି କରନ୍ତୁ"
    },
    "as": {
        "rising_title": "দাম বাঢ়িছে — শস্য ধৰি ৰাখক",
        "rising_rec": "বিক্ৰী কৰাৰ আগতে ২-৩ সপ্তাহ অপেক্ষা কৰক",
        "falling_title": "দাম কমিছে — এতিয়াই বিক্ৰী কৰক",
        "falling_rec": "সৰ্বোত্তম বজাৰত তাৎক্ষণিকভাৱে বিক্ৰী কৰক",
        "stable_title": "দাম সুস্থিৰ আছে",
        "stable_rec": "উপলব্ধ সৰ্বোত্তম বজাৰত এতিয়াই বিক্ৰী কৰক"
    },
    "ne": {
        "rising_title": "मूल्य बढ्दैछ — बाली रोकेर राख्नुहोस्",
        "rising_rec": "बेच्न अघि २-३ हप्ता पर्खनुहोस्",
        "falling_title": "मूल्य घट्दैछ — तुरुन्त बेच्नुहोस्",
        "falling_rec": "उत्कृष्ट मण्डीमा तुरुन्त बिक्री गर्नुहोस्",
        "stable_title": "मूल्य स्थिर छ",
        "stable_rec": "उत्कृष्ट बजारमा अहिल्यै बेच्नुहोस्"
    },
    "si": {
        "rising_title": "මිල ඉහළ යයි — අස්වැන්න රඳවා ගන්න",
        "rising_rec": "විකිණීමට පෙර සති 2-3ක් රැඳී සිටින්න",
        "falling_title": "මිල පහත වැටේ — දැන්ම විකුණන්න",
        "falling_rec": "හොඳම වෙළඳපොලේ වහාම අලෙවි කරන්න",
        "stable_title": "මිල ස්ථාවරව පවතී",
        "stable_rec": "හොඳම වෙළඳපොලේ දැන්ම අලෙවි කරන්න"
    },
    "ar": {
        "rising_title": "الأسعار ترتفع — احتفظ بمحصولك",
        "rising_rec": "انتظر 2-3 أسابيع قبل البيع",
        "falling_title": "الأسعار تنخفض — بِع الآن فوراً",
        "falling_rec": "بِع فوراً في أفضل سوق متاح",
        "stable_title": "الأسعار مستقرة",
        "stable_rec": "بِع في أفضل سوق متاح حالياً"
    },
    "fr": {
        "rising_title": "Prix en hausse — Conservez votre récolte",
        "rising_rec": "Attendez 2 à 3 semaines avant de vendre",
        "falling_title": "Prix en baisse — Vendez immédiatement",
        "falling_rec": "Vendez sans attendre sur le meilleur marché",
        "stable_title": "Prix stables",
        "stable_rec": "Vendez sur le meilleur marché disponible"
    },
    "es": {
        "rising_title": "Precios al alza — Retenga su cosecha",
        "rising_rec": "Espere 2-3 semanas antes de vender",
        "falling_title": "Precios a la baja — Venda ahora",
        "falling_rec": "Venda inmediatamente en el mejor mercado",
        "stable_title": "Precios estables",
        "stable_rec": "Venda en el mejor mercado disponible ahora"
    },
    "pt": {
        "rising_title": "Preços em alta — Guarde sua colheita",
        "rising_rec": "Aguarde 2-3 semanas antes de vender",
        "falling_title": "Preços em queda — Venda agora",
        "falling_rec": "Venda imediatamente no melhor mercado",
        "stable_title": "Preços estáveis",
        "stable_rec": "Venda no melhor mercado disponível agora"
    },
    "de": {
        "rising_title": "Preise steigen — Ernte zurückhalten",
        "rising_rec": "2-3 Wochen mit dem Verkauf warten",
        "falling_title": "Preise fallen — Jetzt sofort verkaufen",
        "falling_rec": "Sofort auf dem besten Markt verkaufen",
        "stable_title": "Preise stabil",
        "stable_rec": "Jetzt zum besten Marktpreis verkaufen"
    },
    "it": {
        "rising_title": "Prezzi in aumento — Trattieni il raccolto",
        "rising_rec": "Attendi 2-3 settimane prima di vendere",
        "falling_title": "Prezzi in calo — Vendi ora",
        "falling_rec": "Vendi subito al miglior mercato",
        "stable_title": "Prezzi stabili",
        "stable_rec": "Vendi al miglior mercato disponibile ora"
    },
    "ru": {
        "rising_title": "Цены растут — придержите урожай",
        "rising_rec": "Подождите 2-3 недели перед продажей",
        "falling_title": "Цены падают — продавайте немедленно",
        "falling_rec": "Срочно продавайте на лучшем рынке",
        "stable_title": "Цены стабильны",
        "stable_rec": "Продавайте по текущей лучшей цене"
    },
    "ja": {
        "rising_title": "価格上昇中 — 出荷を保留し保有を推奨",
        "rising_rec": "販売まで2〜3週間待機してください",
        "falling_title": "価格下落中 — 直ちに販売してください",
        "falling_rec": "最寄りの最高値市場ですぐに売却してください",
        "stable_title": "価格は安定しています",
        "stable_rec": "現在最も有利な市場で販売してください"
    },
    "ko": {
        "rising_title": "시세 상승 중 — 출하를 보류하고 보유하세요",
        "rising_rec": "판매 전 2-3주 대기 권장",
        "falling_title": "시세 하락 중 — 즉시 판매하세요",
        "falling_rec": "가장 유리한 시장에 즉시 출하하세요",
        "stable_title": "시세 안정세",
        "stable_rec": "현재 가장 유리한 시장에 판매하세요"
    },
    "zh": {
        "rising_title": "价格看涨 — 建议压栏/留存待售",
        "rising_rec": "建议等待2-3周后再行出售",
        "falling_title": "价格看跌 — 建议立即抛售",
        "falling_rec": "建议立即在最优批发市场出售",
        "stable_title": "价格走势平稳",
        "stable_rec": "建议在当前最优市场按需出售"
    }
}

def get_localized_forecast_verdict(trend: str, pct_change: float = 0.0, lang: str = "en") -> Tuple[str, str, str]:
    """Returns (trend_key, verdict_title, recommendation) in the selected language."""
    # Handle if lang passed as second arg
    if isinstance(pct_change, str) and lang == "en":
        lang = pct_change
        pct_change = 0.0
    try:
        pct_val = float(pct_change)
    except (ValueError, TypeError):
        pct_val = 0.0

    norm_lang = (lang or "en").lower().strip()
    t = MARKET_FORECAST_25.get(norm_lang, MARKET_FORECAST_25["en"])

    if pct_val > 5.0 or (trend and trend.upper() == "RISING"):
        return "RISING", t["rising_title"], t["rising_rec"]
    elif pct_val < -5.0 or (trend and trend.upper() == "FALLING"):
        return "FALLING", t["falling_title"], t["falling_rec"]
    else:
        return "STABLE", t["stable_title"], t["stable_rec"]


# Populate remaining languages for MARKET_FORECAST_25 and WEATHER_ALERTS_25 with fallback
for _code in SUPPORTED_LANGUAGES:
    if _code not in WEATHER_ALERTS_25:
        WEATHER_ALERTS_25[_code] = WEATHER_ALERTS_25["en"]
    if _code not in MARKET_FORECAST_25:
        MARKET_FORECAST_25[_code] = MARKET_FORECAST_25["en"]
