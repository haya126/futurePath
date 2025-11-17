# -*- coding: utf-8 -*-
from collections import OrderedDict
import streamlit as st

# ------------------ HIDE DEFAULT STREAMLIT MENU ------------------
st.markdown("""
    <style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="تخصصي", layout="centered")

# ------------------ GLOBAL STYLE ------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

        body {
            direction: rtl;
            text-align: right;
            background-color: #F9F7F1;
        }

        * {
            font-family: 'Tajawal', sans-serif !important;
        }

        h1, h2 {
            text-align: center !important;
            font-weight: 700;
            color: #2C2C2C;
        }

        label {
            font-size: 16px;
            font-weight: 500;
        }

        .result-card {
            background-color: #fff;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-right: 4px solid #4CAF50;
        }
        .path {
            padding: 6px;
            border-radius: 6px;
            margin-bottom: 5px;
            font-weight: 500;
        }
        .path.green {
            background-color: #eaf7e9;
            color: #218838;
            border-right: 4px solid #28a745;
        }
        .path.red {
            background-color: #fbeaea;
            color: #b21f2d;
            border-right: 4px solid #dc3545;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<h1>تخصصي</h1>", unsafe_allow_html=True)
st.markdown("<h2>ابحث عن التخصص المناسب لك</h2>", unsafe_allow_html=True)

# ------------------ INPUT FIELDS ------------------
st.subheader("أدخل درجاتك:")
gpa = st.number_input("معدل الثانوية العامة ٪", 0.0, 100.0, step=0.01, format="%g")
math = st.number_input("درجة القدرات – رياضيات ٪ (إن وجدت)", 0.0, 100.0, step=0.01, format="%g")
english = st.number_input("درجة القدرات – إنجليزي ٪ (إن وجدت)", 0.0, 100.0, step=0.01, format="%g")
arabic = st.number_input("درجة القدرات – عربي ٪ (إن وجدت)", 0.0, 100.0, step=0.01, format="%g")
french = st.number_input("درجة القدرات – فرنسي ٪ (إن وجدت)", 0.0, 100.0, step=0.01, format="%g")

stream = st.radio("المسار:", ["علمي", "أدبي"])
kuwait_university_colleges = OrderedDict({
    "كلية الطب": {
      "stream": "علمي",
      "weights": {"gpa": 75, "english": 15, "math": 10},
      "min_score": 95.68,
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 7
    },

    "كلية طب الأسنان": {
      "stream": "علمي",
      "weights": {"gpa": 75, "english": 15, "math": 10},
      "min_score": 95.09,
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 6
    },
    "كلية الصيدلة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 93,
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 6
    },

    "كلية العلوم الطبية المساعدة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 20, "math": 10},
      "min_score": 85.68,  # أقل مسار: إدارة المعلومات الصحية
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 4,
      "paths": [
        {"name": "العلاج المهني", "min_score": 90.06},
        {"name": "علوم المختبرات الطبية", "min_score": 87.83},
        {"name": "العلاج الطبيعي", "min_score": 91.28},
        {"name": "تكنولوجيا الأشعة التشخيصية", "min_score": 88.57},
        {"name": " المعلوماتيه إدارة المعلومات الصحية", "min_score": 85.68},
        {"name": "التمريض", "min_score": 85.68}
      ]
    },

    "كلية الصحة العامة": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 83.82,
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 4
},

   "كلية العمارة": {
    "stream": "علمي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 66.29,
    "interests": ["الفنون والتصميم 🎨"],
    "years": 5,
    "paths": [
        {"name": "التصميم المرئي", "min_score": 66.29},
        {"name": "العمارة الداخلية", "min_score": 72.71},
        {"name": "العمارة", "min_score": 80.02}
    ]
},


    "كلية الهندسة والبترول": {
      "stream": "علمي",
      "weights": {"gpa": 65, "english": 10, "math": 20},
      "min_score": 63.17,  # أقل حد لأي مسار داخل الكلية
      "interests": ["الهندسة والتقنية ⚙️", "التحليل والرياضيات 📊"],
      "years": 5,
      "paths": [
        {"name": "هندسة البترول", "min_score": 77.42},
        {"name": "هندسة كمبيوتر", "min_score": 76.48},
        {"name": "الهندسة الصناعية والنظم الإدارية", "min_score": 65.07},
        {"name": "الهندسة الكهربائية", "min_score": 70.1},
        {"name": "الهندسة الكيميائية", "min_score": 66.42},
        {"name": "الهندسة المدنية", "min_score": 72.5},
        {"name": "الهندسة الميكانيكية", "min_score": 63.17}
        ]
    },

    "كلية العلوم (علوم رياضية وطبيعية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 70.0,  # أقل تخصص
      "interests": ["العلوم الطبيعية 🧪", "التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "الرياضيات", "min_score": 73.72},
        {"name": "الفيزياء الاساسية", "min_score": 79.63},
        {"name": "الفيزياء الهندسية", "min_score": 74.33},
        {"name": "الليزر والاتصالات البصرية", "min_score": 74.33},
        {"name": "الإحصاء وبحوث العمليات", "min_score": 70.0},
        {"name": "علوم في الامن السبراني", "min_score": 86.18},
        {"name": "الكيمياء", "min_score": 78.43},
        {"name": "الجيولوجيا", "min_score": 82.61},
        {"name": "الإحصاء التطبيقي", "min_score": 73.41},
        {"name": "الكيمياء التطبيقية", "min_score": 76.82},
        {"name": "الفيزياء الهندسية", "min_score": 74.8},
        {"name": "الاستشعار عن بعد", "min_score": 74.8},
        {"name": "علوم الحاسوب", "min_score": 79.69},
        {"name": "الرياضيات المالية والاكتوارية", "min_score": 71.88},
        {"name": "علوم البحار", "min_score": 78.8}
      ]
    },
        "كلية العلوم (علوم بيولوجية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 82.08,  # أقل تخصص
      "interests": ["العلوم الطبيعية 🧪", "التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "بيولوجيا الحيوان", "min_score": 84.4},
        {"name": "بيولوجيا النبات", "min_score": 82.08},
        {"name": "علم الميكرو بيولوجيا", "min_score": 93.2},
        {"name": "علم الكيمياء الحيوية", "min_score": 91.28},
        {"name": "علم البيولوجيا الجزيئية", "min_score": 90.21}
      ]
    },

    "كلية العلوم الحياتية": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 57.4,  # أقل مسار: علوم المعلومات
      "interests": ["العلوم الطبيعية 🧪", "الفنون والتصميم 🎨", "التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "علم التغذية", "min_score": 81.1},
        {"name": "اضطرابات التواصل", "min_score": 81.84},
        {"name": "علوم البيئية", "min_score": 58.46},
        {"name": "علوم المعلومات", "min_score": 57.4},
        {"name": "علوم الأغذية", "min_score": 74.1},
        {"name": "علم البيانات والذكاء الاصطناعي", "min_score": 72.24}
        ]
      },

    "كلية العلوم الإدارية (علمي)": {
    "stream": "علمي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 57.3,  # أقل معدل (الإدارة العامة – علمي)
    "interests": ["التحليل والرياضيات 📊"],
    "years": 4,
    "paths": [
        {"name": "التسويق", "min_score": 57.27},
        {"name": "الإدارة العامة", "min_score": 61.32},
        {"name": "نظم المعلومات الإدارية", "min_score": 56.48},
        {"name": "التمويل والمنشآت المالية", "min_score": 60.6},
        {"name": "الاقتصاد", "min_score": 60.15},
        {"name": "المحاسبة", "min_score": 73.18},
        {"name": "إدارة العمليات والإمدادات", "min_score": 64.68},
        {"name": "الادارة", "min_score": 63.03}
    ]
},
    "كلية العلوم الإدارية (ادبي)": {
    "stream": "أدبي",
    "weights": {"gpa": 70, "english": 15, "math": 15},
    "min_score": 57.3,  # أقل معدل (الإدارة العامة – علمي)
    "interests": ["التحليل والرياضيات 📊"],
    "years": 4,
    "paths": [
        {"name": "التسويق", "min_score": 64.64},
        {"name": "الإدارة العامة", "min_score": 63.44},
        {"name": "نظم المعلومات الإدارية", "min_score": 61.64},
        {"name": "التمويل والمنشآت المالية", "min_score": 61.59},
        {"name": "الاقتصاد", "min_score": 69.4},
        {"name": "المحاسبة", "min_score": 70.58},
        {"name": "إدارة العمليات والإمدادات", "min_score": 67.75},
        {"name": "الادارة", "min_score": 62.55}
    ]
},


    "كلية الآداب": {
    "weights": {
      "stream": "أدبي",
        "default": {"gpa": 85, "arabic": 15},
        "اللغة الإنجليزية": {"gpa": 85, "english": 15},
        "اللغة الفرنسية وثقافتها": {"gpa": 85, "french": 15}  # Assuming you add a field for French aptitude
    },
    "min_score": 66.35,  # Minimum for "الإعلام"
    "interests": ["القانون والقراءة 📚"],
    "years": 4,
    "paths": [
        {"name": "اللغة العربية", "min_score": 66.35},
        {"name": "اللغة الإنجليزية", "min_score": 66.79},
        {"name": "اللغة الفرنسية وثقافتها", "min_score": 66.59},
        {"name": "التاريخ", "min_score": 66.78},
        {"name": "الفلسفة", "min_score": 69.4},
        {"name": "الإعلام", "min_score": 66.37}
    ]
},

    "كلية الحقوق": {
      "stream": "أدبي",
      "weights": {"gpa": 100},
      "min_score": 85.14,
      "interests": ["القانون والقراءة 📚"],
      "years": 4
    },

    "كلية الشريعة": {
      "stream": "أدبي",
      "weights": {"gpa": 85, "arabic": 15},
      "min_score": 66.33,  # أقل درجة بين المسارات
      "interests": ["القانون والقراءة 📚", "التربية والتعليم 👩‍🏫"],
      "years": 4,
      "paths": [
        {"name": "الفقه وأصول الفقه", "min_score": 66.66},
        {"name": "الفقه المقارن والسياسة الشرعية", "min_score": 66.53},
        {"name": "التفسير والحديث", "min_score": 66.33},
        {"name": "العقيدة والدعوة", "min_score": 68.1}
      ]
   },
    "كلية التربية(ادبي)": {
    "stream": "أدبي",
    "weights": {"gpa": 80, "english": 10, "arabic": 10},
    "min_score": 77.95,  # Minimum is for علمي رياضيات ابتدائي
    "interests": ["التربية والتعليم 👩‍🏫"],
    "years": 4,
    "paths": [
        {"name": "برنامج متوسط/ثانوي – اللغة الإنجليزية ", "min_score": 79.88},
        {"name": "برنامج متوسط/ثانوي – اللغة العربية ", "min_score": 77.95},
        {"name": "برنامج متوسط/ثانوي –الدراسات الاسلامية ", "min_score": 81.85},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/الجغرافيا ", "min_score": 83.17},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/التاريخ ", "min_score": 84.02},
        {"name": "برنامج متوسط/ثانوي – الاجتماعيات/الفلسفة ", "min_score": 81.85},
        {"name": "برنامج متوسط/ثانوي – علم النفس/علوم اجتماعية ", "min_score": 84.96},
        {"name": "برنامج رياض الأطفال", "min_score": 84.63},
        {"name": "برنامج الابتدائي – الدراسات الإسلامية ", "min_score": 82.61},
        {"name": "برنامج الابتدائي – اجتماعيات ", "min_score": 84.74},
        {"name": "برنامج الابتدائي – اللغة العربية ", "min_score": 79.36},
        {"name": "برنامج متوسط– اللغة الإنجليزية ", "min_score": 80.41}
        
    ]
},
    "كلية التربية(علمي)": {
    "stream": "علمي",
    "weights": {"gpa": 80, "english": 7.5, "math": 7.5, "arabic": 5},
    "min_score": 71.37,  # Minimum is for علمي رياضيات ابتدائي
    "interests": ["التربية والتعليم 👩‍🏫"],
    "years": 4,
    "paths": [
    
        {"name": "برنامج متوسط/ثانوي – البيولوجيا ", "min_score": 80.23},
        {"name": "برنامج متوسط/ثانوي – الرياضيات ", "min_score": 71.37},
        {"name": "برنامج متوسط/ثانوي – الفيزياء ", "min_score": 76.15},
        {"name": "برنامج متوسط/ثانوي – الجيولوجيا ", "min_score": 79.8},
        {"name": "برنامج متوسط/ثانوي – الكيمياء ", "min_score": 76.78},
        {"name": "برنامج الابتدائي – العلوم ", "min_score": 79.3},
        {"name": "برنامج الابتدائي – الرياضيات ", "min_score": 74.78}
    ]
},


    "كلية العلوم الاجتماعية": {
      "stream": "أدبي",
      "weights": {"gpa": 90, "arabic": 10},
      "min_score": 70.2,  # أقل مسار = علم المعلومات الجغرافية
      "interests": ["القانون والقراءة 📚"],
      "years": 4,
      "paths": [
        {"name": "علم الاجتماع", "min_score": 70.21},
        {"name": "علم النفس", "min_score": 72.24},
        {"name": "علم المعلومات الجغرافية", "min_score": 70.28},
        {"name": "العلوم السياسية", "min_score": 70.23},
        {"name": "الجغرافيا التطبيقية", "min_score": 70.2},
        {"name": "الخدمة الاجتماعية", "min_score": 70.35}
       ]
    }
})

# --- الجامعة الأمريكية في الشرق الأوسط (AUM) ---
aum_colleges = {
    "College of Engineering and Technology": {
        "weights": {"gpa": 80, "english": 20},
        "min_score": 70.0,
        "interests": ["الهندسة والتقنية ⚙️", "التحليل والرياضيات 📊"],
        "years": 4,
        "paths": ["Mechanical Engineering", "Civil Engineering", "Computer Engineering", "Industrial Engineering"]
    },
    "College of Business Administration": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 65.0,
        "interests": ["التحليل والرياضيات 📊", "القانون والقراءة 📚"],
        "years": 4,
        "paths": ["Finance", "Marketing", "Accounting", "Management Information Systems"]
    },
    "College of Design": {
        "weights": {"gpa": 80, "english": 20},
        "min_score": 65.0,
        "interests": ["الفنون والتصميم 🎨"],
        "years": 4,
        "paths": ["Graphic Design", "Interior Design"]
    }
}

# --- الجامعة الأمريكية في الكويت (AUK) ---
auk_colleges = {
    "College of Arts and Sciences": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 60.0,
        "interests": ["القانون والقراءة 📚", "الفنون والتصميم 🎨"],
        "years": 4,
        "paths": ["English Literature", "Communication & Media", "Graphic Design", "International Relations"]
    },
    "College of Business and Economics": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 60.0,
        "interests": ["التحليل والرياضيات 📊"],
        "years": 4,
        "paths": ["Accounting", "Finance", "Marketing", "Management"]
    },
    "College of Engineering and Applied Sciences": {
        "weights": {"gpa": 80, "english": 20},
        "min_score": 70.0,
        "interests": ["الهندسة والتقنية ⚙️"],
        "years": 4,
        "paths": ["Computer Engineering", "Electrical Engineering"]
    }
}

# --- الجامعة الخليجية للعلوم والتكنولوجيا (GUST) ---
gust_colleges = {
    "College of Business Administration": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 70.0,
        "interests": ["التحليل والرياضيات 📊"],
        "years": 4,
        "paths": ["Accounting", "Finance", "Marketing", "Management", "Economics"]
    },
    "College of Arts and Humanities": {
        "weights": {"gpa": 90, "english": 10},
        "min_score": 65.0,
        "interests": ["القانون والقراءة 📚", "الفنون والتصميم 🎨"],
        "years": 4,
        "paths": ["English Literature", "Mass Communication", "Public Relations", "Linguistics"]
    }
}
# List of universities
universities = ["جامعة الكويت", "جامعة الخليج (GUST)", "الجامعة الأمريكية (AUK)", "جامعة الشرق الأوسط (AUM)"]

# --- Streamlit UI ---
st.title("🎓 نظام ترشيح التخصصات الجامعية")

# User selects university
university = st.selectbox("اختر الجامعة:", universities)

# Input fields
gpa = st.number_input("📊 المعدل التراكمي (من 100):", min_value=0.0, max_value=100.0, value=85.0)
math = st.number_input("🧮 درجة الرياضيات:", min_value=0.0, max_value=100.0, value=90.0)
english = st.number_input("📘 درجة الإنجليزي:", min_value=0.0, max_value=100.0, value=80.0)
arabic = st.number_input("📕 درجة العربي:", min_value=0.0, max_value=100.0, value=85.0)

interest = st.selectbox("🎯 مجال الاهتمام:", ["هندسة", "علوم", "طب", "آداب", "تقنية", "لغة", "إدارة", "قانون"])

# Display results only for الكويت الجامعة as an example
if university == "جامعة الكويت":
    st.subheader("🏛️ التخصصات المتاحة بناءً على بياناتك")
    
    results_found = False
    
    for college_name, college_data in kuwait_university_colleges.items():
        # Skip if interest doesn't match
        if interest not in college_data["interests"]:
            continue
        
        # Calculate معدل المكافئ
        weights = college_data["weights"]
        composite = (
            (weights.get("gpa", 0) * gpa / 100) +
            (weights.get("math", 0) * math / 100) +
            (weights.get("english", 0) * english / 100) +
            (weights.get("arabic", 0) * arabic / 100)
        )

        # Show college if you meet minimum score
        if composite >= college_data["min_score"]:
            results_found = True
            st.markdown(f"### 🎓 {college_name}")
            st.write(f"⚖️ معدل المكافئ: **{composite:.2f}**")
            st.write(f"⏳ عدد سنوات الدراسة: {college_data['years']}")

            # Display paths (if they exist)
            if "paths" in college_data:
                st.markdown("<b>📌 المسارات المتاحة:</b>", unsafe_allow_html=True)
                for path in college_data["paths"]:
                    if composite >= path["min_score"]:
                        st.markdown(f"<span style='color: green; font-weight: bold;'>✔ {path['name']} (الحد الأدنى: {path['min_score']})</span>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<span style='color: red;'>✘ {path['name']} (الحد الأدنى: {path['min_score']})</span>", unsafe_allow_html=True)
            st.write("---")
    
    if not results_found:
        st.warning("ما في تخصصات مطابقة حالياً. جرب تغيير الاهتمام أو تحسين درجاتك. 💡")

else:
    st.info(f"🚧 الدعم الكامل لـ {university} سيتم إضافته قريبًا!")

