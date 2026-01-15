# -*- coding: utf-8 -*-
from collections import OrderedDict
import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="منصه تخصصي", layout="centered")

# ------------------ CSS ------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');

body {
    direction: rtl;
    text-align: right;
    background-color: #E6F0EE;
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
    font-weight: 500;
}

.stButton button {
    background-color: #2E8B57 !important;
    color: white !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    padding: 12px 28px !important;
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<h1>ابحث عن التخصص المناسب لك</h1>", unsafe_allow_html=True)

# ------------------ UNIVERSITY ------------------
university = st.selectbox(
    "اختر الجامعة",
    [
        "جامعة الكويت",
        "جامعة الخليج للعلوم والتكنولوجيا (GUST)",
        "الجامعة الأمريكية في الكويت (AUK)",
        "جامعة الشرق الأوسط الأمريكية (AUM)"
    ]
)

# ------------------ GPA / PERCENTAGE ------------------
st.markdown("<h3>أدخل معدلك</h3>", unsafe_allow_html=True)

grade_type = st.radio(
    "طريقة إدخال المعدل:",
    ["نسبة مئوية (%)", "GPA (من 4)"],
    horizontal=True
)

if grade_type == "نسبة مئوية (%)":
    gpa_percentage = st.number_input(
        "النسبة في الثانوية (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.1
    )
else:
    gpa_value = st.number_input(
        "GPA (من 4)",
        min_value=0.0,
        max_value=4.0,
        step=0.01
    )
    gpa_percentage = (gpa_value / 4.0) * 100

st.caption("ℹ️ في حال اختيار GPA يتم تحويله تلقائيًا إلى نسبة مئوية.")

# ------------------ TESTS ------------------
english = math = arabic = french = reading = 0.0

if university == "جامعة الكويت":
    st.markdown("### اختبارات القبول – جامعة الكويت")
    english = st.number_input("اختبار قدرات اللغة الإنجليزية", 0.0, 100.0, 0.1)
    math = st.number_input("اختبار قدرات الرياضيات", 0.0, 100.0, 0.1)
    arabic = st.number_input("اختبار قدرات اللغة العربية (اختياري)", 0.0, 100.0, 0.1)
    french = st.number_input("اختبار قدرات اللغة الفرنسية (اختياري)", 0.0, 100.0, 0.1)

elif university == "جامعة الشرق الأوسط الأمريكية (AUM)":
    st.markdown("### اختبارات القبول – AUM")
    english = st.number_input("English Placement Test (EPT)", 0.0, 100.0, 0.1)
    math = st.number_input("Math Placement Test (MPT)", 0.0, 100.0, 0.1)

elif university == "جامعة الخليج للعلوم والتكنولوجيا (GUST)":
    st.markdown("### اختبارات القبول – GUST")
    english = st.number_input("English Placement Test (EPT)", 0.0, 100.0, 0.1)
    math = st.number_input("اختبار تحديد مستوى الرياضيات", 0.0, 100.0, 0.1)

elif university == "الجامعة الأمريكية في الكويت (AUK)":
    st.markdown("### اختبارات القبول – AUK")
    english = st.number_input("TOEFL / IELTS", 0.0, 120.0, 0.1)
    reading = st.number_input("ACCUPLACER Reading", 0.0, 120.0, 0.1)
    math = st.number_input("ACCUPLACER Math", 0.0, 120.0, 0.1)

# ------------------ INTEREST ------------------
interest = st.selectbox(
    "مجال اهتمامك",
    [
        "المجال الطبي والصحي 🏥",
        "الهندسة والتقنية ⚙️",
        "التحليل والرياضيات 📊",
        "القانون والقراءة 📚",
        "الفنون والتصميم 🎨",
        "العلوم الطبيعية 🧪",
        "التربية والتعليم 👩‍🏫"
    ]
)

# ------------------ STREAM ------------------
stream = st.radio("المسار الثانوي", ["علمي", "أدبي"], horizontal=True)
# ------------------ KU COLLEGES ------------------
# ------------------ YOUR ORIGINAL KU COLLEGE DATA (UNMODIFIED) ------------------

colleges = OrderedDict({

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
      "min_score": 85.68,
      "interests": ["المجال الطبي والصحي 🏥"],
      "years": 4,
      "paths": [
        {"name": "العلاج المهني", "min_score": 90.06, "years": 4},
        {"name": "علوم المختبرات الطبية", "min_score": 87.83, "years": 4},
        {"name": "العلاج الطبيعي", "min_score": 91.28, "years": 4},
        {"name": "تكنولوجيا الأشعة التشخيصية", "min_score": 88.57, "years": 4},
        {"name": "المعلوماتية الصحية", "min_score": 85.68, "years": 4},
        {"name": "التمريض", "min_score": 85.68, "years": 4}
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
        {"name": "التصميم المرئي", "min_score": 66.29, "years": 4},
        {"name": "العمارة الداخلية", "min_score": 72.71, "years": 4},
        {"name": "العمارة", "min_score": 80.02, "years": 5}
      ]
    },

    "كلية الهندسة والبترول": {
      "stream": "علمي",
      "weights": {"gpa": 65, "english": 10, "math": 20},
      "min_score": 63.17,
      "interests": ["الهندسة والتقنية ⚙️", "التحليل والرياضيات 📊"],
      "years": 5,
      "paths": [
        {"name": "هندسة البترول", "min_score": 77.42, "years": 4},
        {"name": "هندسة كمبيوتر", "min_score": 76.48, "years": 4},
        {"name": "الهندسة الصناعية والنظم الإدارية", "min_score": 65.07, "years": 4},
        {"name": "الهندسة الكهربائية", "min_score": 70.1, "years": 4},
        {"name": "الهندسة الكيميائية", "min_score": 66.42, "years": 4},
        {"name": "الهندسة المدنية", "min_score": 72.5, "years": 4},
        {"name": "الهندسة الميكانيكية", "min_score": 63.17, "years": 4}
      ]
    },

    "كلية العلوم (علوم رياضية وطبيعية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 70.0,
      "interests": ["العلوم الطبيعية 🧪", "التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "الرياضيات", "min_score": 73.72, "years": 4},
        {"name": "الفيزياء الاساسية", "min_score": 79.63, "years": 4},
        {"name": "الفيزياء الهندسية", "min_score": 74.33, "years": 4},
        {"name": "الليزر والاتصالات البصرية", "min_score": 74.33, "years": 4},
        {"name": "الإحصاء وبحوث العمليات", "min_score": 70.0, "years": 4},
        {"name": "علوم الأمن السيبراني", "min_score": 86.18, "years": 4},
        {"name": "الكيمياء", "min_score": 78.43, "years": 4},
        {"name": "الجيولوجيا", "min_score": 82.61, "years": 4},
        {"name": "الإحصاء التطبيقي", "min_score": 73.41, "years": 4},
        {"name": "الكيمياء التطبيقية", "min_score": 76.82, "years": 4},
        {"name": "الاستشعار عن بعد", "min_score": 74.8, "years": 4},
        {"name": "علوم الحاسوب", "min_score": 79.69, "years": 4},
        {"name": "الرياضيات المالية والاكتوارية", "min_score": 71.88, "years": 4},
        {"name": "علوم البحار", "min_score": 78.8, "years": 4}
      ]
    },

    "كلية العلوم (علوم بيولوجية)": {
      "stream": "علمي",
      "weights": {"gpa": 100},
      "min_score": 82.08,
      "interests": ["العلوم الطبيعية 🧪"],
      "years": 4,
      "paths": [
        {"name": "بيولوجيا الحيوان", "min_score": 84.4, "years": 4},
        {"name": "بيولوجيا النبات", "min_score": 82.08, "years": 4},
        {"name": "الميكروبيولوجيا", "min_score": 93.2, "years": 4},
        {"name": "الكيمياء الحيوية", "min_score": 91.28, "years": 4},
        {"name": "البيولوجيا الجزيئية", "min_score": 90.21, "years": 4}
      ]
    },

    "كلية العلوم الحياتية": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 57.4,
      "interests": ["العلوم الطبيعية 🧪", "الفنون والتصميم 🎨", "التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "علم التغذية", "min_score": 81.1, "years": 4},
        {"name": "اضطرابات التواصل", "min_score": 81.84, "years": 4},
        {"name": "العلوم البيئية", "min_score": 58.46, "years": 4},
        {"name": "علوم المعلومات", "min_score": 57.4, "years": 4},
        {"name": "علوم الأغذية", "min_score": 74.1, "years": 4},
        {"name": "علم البيانات والذكاء الاصطناعي", "min_score": 72.24, "years": 4}
      ]
    },

    "كلية العلوم الإدارية (علمي)": {
      "stream": "علمي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 57.3,
      "interests": ["التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "التسويق", "min_score": 57.27, "years": 4},
        {"name": "الإدارة العامة", "min_score": 61.32, "years": 4},
        {"name": "نظم المعلومات الإدارية", "min_score": 56.48, "years": 4},
        {"name": "التمويل والمنشآت المالية", "min_score": 60.6, "years": 4},
        {"name": "الاقتصاد", "min_score": 60.15, "years": 4},
        {"name": "المحاسبة", "min_score": 73.18, "years": 4},
        {"name": "إدارة العمليات والإمدادات", "min_score": 64.68, "years": 4},
        {"name": "الإدارة", "min_score": 63.03, "years": 4}
      ]
    },

    "كلية العلوم الإدارية (أدبي)": {
      "stream": "أدبي",
      "weights": {"gpa": 70, "english": 15, "math": 15},
      "min_score": 57.3,
      "interests": ["التحليل والرياضيات 📊"],
      "years": 4,
      "paths": [
        {"name": "التسويق", "min_score": 64.64, "years": 4},
        {"name": "الإدارة العامة", "min_score": 63.44, "years": 4},
        {"name": "نظم المعلومات الإدارية", "min_score": 61.64, "years": 4},
        {"name": "التمويل والمنشآت المالية", "min_score": 61.59, "years": 4},
        {"name": "الاقتصاد", "min_score": 69.4, "years": 4},
        {"name": "المحاسبة", "min_score": 70.58, "years": 4},
        {"name": "إدارة العمليات والإمدادات", "min_score": 67.75, "years": 4},
        {"name": "الإدارة", "min_score": 62.55, "years": 4}
      ]
    },

    "كلية الآداب": {
      "weights": {
        "stream": "أدبي",
        "default": {"gpa": 85, "arabic": 15},
        "اللغة الإنجليزية": {"gpa": 85, "english": 15},
        "اللغة الفرنسية وثقافتها": {"gpa": 85, "french": 15}
      },
      "min_score": 66.35,
      "interests": ["القانون والقراءة 📚"],
      "years": 4,
      "paths": [
        {"name": "اللغة العربية", "min_score": 66.35, "years": 4},
        {"name": "اللغة الإنجليزية", "min_score": 66.79, "years": 4},
        {"name": "اللغة الفرنسية وثقافتها", "min_score": 66.59, "years": 4},
        {"name": "التاريخ", "min_score": 66.78, "years": 4},
        {"name": "الفلسفة", "min_score": 69.4, "years": 4},
        {"name": "الإعلام", "min_score": 66.37, "years": 4}
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
      "min_score": 66.33,
      "interests": ["القانون والقراءة 📚", "التربية والتعليم 👩‍🏫"],
      "years": 4,
      "paths": [
        {"name": "الفقه وأصول الفقه", "min_score": 66.66, "years": 4},
        {"name": "الفقه المقارن والسياسة الشرعية", "min_score": 66.53, "years": 4},
        {"name": "التفسير والحديث", "min_score": 66.33, "years": 4},
        {"name": "العقيدة والدعوة", "min_score": 68.1, "years": 4}
      ]
    },

    "كلية التربية (أدبي)": {
      "stream": "أدبي",
      "weights": {"gpa": 80, "english": 10, "arabic": 10},
      "min_score": 77.95,
      "interests": ["التربية والتعليم 👩‍🏫"],
      "years": 4,
      "paths": [
        {"name": "اللغة الإنجليزية متوسط/ثانوي", "min_score": 79.88, "years": 4},
        {"name": "اللغة العربية متوسط/ثانوي", "min_score": 77.95, "years": 4},
        {"name": "الدراسات الإسلامية متوسط/ثانوي", "min_score": 81.85, "years": 4},
        {"name": "الاجتماعيات/جغرافيا متوسط/ثانوي", "min_score": 83.17, "years": 4},
        {"name": "الاجتماعيات/تاريخ متوسط/ثانوي", "min_score": 84.02, "years": 4},
        {"name": "الاجتماعيات/فلسفة متوسط/ثانوي", "min_score": 81.85, "years": 4},
        {"name": "علم النفس متوسط/ثانوي", "min_score": 84.96, "years": 4},
        {"name": "رياض الأطفال", "min_score": 84.63, "years": 4},
        {"name": "ابتدائي – الدراسات الإسلامية", "min_score": 82.61, "years": 4},
        {"name": "ابتدائي – اجتماعيات", "min_score": 84.74, "years": 4},
        {"name": "ابتدائي – اللغة العربية", "min_score": 79.36, "years": 4},
        {"name": "متوسط – اللغة الإنجليزية", "min_score": 80.41, "years": 4}
      ]
    },

    "كلية التربية (علمي)": {
      "stream": "علمي",
      "weights": {"gpa": 80, "english": 7.5, "math": 7.5, "arabic": 5},
      "min_score": 71.37,
      "interests": ["التربية والتعليم 👩‍🏫"],
      "years": 4,
      "paths": [
        {"name": "متوسط/ثانوي – البيولnvm وجيا", "min_score": 80.23, "years": 4},
        {"name": "متوسط/ثانوي – الرياضيات", "min_score": 71.37, "years": 4},
        {"name": "متوسط/ثانوي – الفيزياء", "min_score": 76.15, "years": 4},
        {"name": "متوسط/ثانوي – الجيولوجيا", "min_score": 79.8, "years": 4},
        {"name": "متوسط/ثانوي – الكيمياء", "min_score": 76.78, "years": 4},
        {"name": "ابتدائي – العلوم", "min_score": 79.3, "years": 4},
        {"name": "ابتدائي – الرياضيات", "min_score": 74.78, "years": 4}
      ]
    },

    "كلية العلوم الاجتماعية": {
      "stream": "أدبي",
      "weights": {"gpa": 90, "arabic": 10},
      "min_score": 70.2,
      "interests": ["القانون والقراءة 📚"],
      "years": 4,
      "paths": [
        {"name": "علم الاجتماع", "min_score": 70.21, "years": 4},
        {"name": "علم النفس", "min_score": 72.24, "years": 4},
        {"name": "علم المعلومات الجغرافية", "min_score": 70.28, "years": 4},
        {"name": "العلوم السياسية", "min_score": 70.23, "years": 4},
        {"name": "الجغرافيا التطبيقية", "min_score": 70.2, "years": 4},
        {"name": "الخدمة الاجتماعية", "min_score": 70.35, "years": 4}
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
        "paths": [
            "Mechanical Engineering",
            "Industrial Engineering",
            "Computer Engineering",
            "Civil Engineering"
        ]
    },

    "College of Business Administration": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 65.0,
        "interests": ["التحليل والرياضيات 📊", "القانون والقراءة 📚"],
        "years": 4,
        "paths": [
            "Finance",
            "Marketing",
            "Accounting",
            "Management Information Systems"
        ]
    },

    "College of Design": {
        "weights": {"gpa": 80, "english": 20},
        "min_score": 65.0,
        "interests": ["الفنون والتصميم 🎨"],
        "years": 4,
        "paths": [
            "Graphic Design",
            "Interior Design"
        ]
    }
}

# --- الجامعة الأمريكية في الكويت (AUK) ---
auk_colleges = {
    "College of Arts and Sciences": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 60.0,
        "interests": ["القانون والقراءة 📚", "الفنون والتصميم 🎨"],
        "years": 4,
        "paths": [
            "English Language & Literature",
            "Communication & Media",
            "Graphic Design",
            "International Relations",
            "Social and Behavioral Sciences",
            "Computer Science"
        ]
    },

    "College of Business and Economics": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 60.0,
        "interests": ["التحليل والرياضيات 📊"],
        "years": 4,
        "paths": [
            "Accounting",
            "Finance",
            "Marketing",
            "Management",
            "Economics"
        ]
    },

    "College of Engineering and Applied Sciences": {
        "weights": {"gpa": 80, "english": 20},
        "min_score": 70.0,
        "interests": ["الهندسة والتقنية ⚙️"],
        "years": 4,
        "paths": [
            "Computer Engineering",
            "Electrical Engineering",
            "Information Systems"
        ]
    }
}

# --- الجامعة الخليجية للعلوم والتكنولوجيا (GUST) ---
gust_colleges = {
    "College of Business Administration": {
        "weights": {"gpa": 85, "english": 15},
        "min_score": 70.0,
        "interests": ["التحليل والرياضيات 📊"],
        "years": 4,
        "paths": [
            "Accounting",
            "Finance",
            "Marketing",
            "Management",
            "Economics",
            "Information Systems & Technology"
        ]
    },

    "College of Arts and Humanities": {
        "weights": {"gpa": 90, "english": 10},
        "min_score": 65.0,
        "interests": ["القانون والقراءة 📚", "الفنون والتصميم 🎨"],
        "years": 4,
        "paths": [
            "English Literature",
            "Mass Communication",
            "Public Relations",
            "Visual Communication",
            "Linguistics"
        ]
    }
}
# ========================== MAIN RESULTS =============================
if st.button(" اقترح التخصصات"):

    # Select correct university
    if university == "جامعة الكويت":
        uni_colleges = colleges
    elif university == "جامعة الشرق الأوسط الأمريكية (AUM)":
        uni_colleges = aum_colleges
    elif university == "الجامعة الأمريكية في الكويت (AUK)":
        uni_colleges = auk_colleges
    elif university == "جامعة الخليج للعلوم والتكنولوجيا (GUST)":
        uni_colleges = gust_colleges
    else:
        uni_colleges = {}

    matched = []

    for name, data in uni_colleges.items():

        # Stream check
        if "stream" in data:
            if stream == "أدبي" and data["stream"] == "علمي":
                continue

        # Interest check
        if interest not in data.get("interests", []):
            continue

        # ---- GPA handling (percentage or from 4) ----
        if gpa_type == "GPA من 4":
            gpa_percent = (gpa / 4) * 100
        else:
            gpa_percent = gpa

        # Score calculation
        weights = data.get("weights", {})
        score = 0

        if "gpa" in weights:
            score += gpa_percent * (weights["gpa"] / 100)
        if "math" in weights:
            score += math * (weights["math"] / 100)
        if "english" in weights:
            score += english * (weights["english"] / 100)
        if "arabic" in weights:
            score += arabic * (weights["arabic"] / 100)
        if "french" in weights:
            score += french * (weights["french"] / 100)

        final_score = round(score, 2)

        # Check min score
        if final_score >= data.get("min_score", 0):
            matched.append((name, data, final_score))

    # --- DISPLAY RESULTS ---
    if matched:
        st.success(f" هذه التخصصات تناسبك في {university} حسب درجاتك واهتماماتك")

        for name, data, final_score in matched:

            paths_html = ""

            if "paths" in data and data["paths"]:
                paths_html = "<p><strong> المسارات:</strong></p><ul>"
                for p in data["paths"]:
                    if isinstance(p, dict):
                        color = "green" if final_score >= p.get("min_score", 0) else "red"
                        years_text = f"، مدة الدراسة: {p['years']} سنوات" if "years" in p else ""
                        paths_html += f"<li style='color:{color};'>{p['name']} (الحد الأدنى: {p['min_score']}%{years_text})</li>"
                    else:
                        paths_html += f"<li>{p}</li>"
                paths_html += "</ul>"

            st.markdown(f"""
                <div style='border-right: 6px solid #4F7678; padding: 20px 25px; margin: 20px 0; background-color: #f9f9f9; border-radius: 10px; text-align: right;'>
                    <h3 style='margin-bottom: 10px;'>{name}</h3>
                    <p><strong>معدلك المكافئ:</strong> {final_score}%</p>
                    {paths_html}
                </div>
            """, unsafe_allow_html=True)

        st.markdown("""
            <div style='text-align: center; font-size: 13px; color: #666; margin-top: 30px;'>
                📌 <em>المعلومات مبنية على بيانات رسمية من الجامعات للسنة الدراسية 2025–2026. قد تتغير المعدلات في السنوات القادمة.</em>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.warning(f"عذرًا، لم نجد تخصصات في {university} تتوافق مع درجاتك واهتماماتك.")
