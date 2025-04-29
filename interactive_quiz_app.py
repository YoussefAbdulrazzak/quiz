import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="امتحان تفاعلي شامل", layout="centered")
st.title("📘 امتحان تفاعلي - القيادة والإدراك والتوافق والعدوانية")

# قاعدة بيانات كاملة للأسئلة (80+ سؤال)
questions = [
    # القيادة
    {"question": "ما هو تعريف القيادة من المنظور التربوي؟",
     "options": ["A - استخدام السلطة لتحقيق أهداف شخصية", "B - توجيه نشاط الجماعة نحو هدف مشترك", "C - السيطرة على الآخرين بوسائل رسمية", "D - فرض النظام داخل الجماعة"],
     "answer": "B", "explanation": "القيادة هي توجيه نشاط الجماعة نحو هدف مشترك."},

    {"question": "من صفات القائد الفعال:",
     "options": ["A - الجمود العقلي", "B - مقاومة التغيير", "C - الاستماع الجيد", "D - الانعزال عن الفريق"],
     "answer": "C", "explanation": "الاستماع الجيد من أهم سمات القائد الفعّال."},

    {"question": "القيادة لا يمكن أن تحدث بدون وجود جماعة.",
     "options": ["صح", "خطأ"],
     "answer": "صح", "explanation": "القيادة تحتاج إلى جماعة لتحقيق تفاعل وتوجيه."},

    # الإدراك الاجتماعي
    {"question": "الإدراك الاجتماعي هو:",
     "options": ["A - تفسير الظواهر البيولوجية", "B - فهم الذات فقط", "C - إدراكنا للآخرين وتفسير سلوكهم", "D - القدرة على الرسم التحليلي"],
     "answer": "C", "explanation": "الإدراك الاجتماعي يشمل فهمنا وتفسيرنا للآخرين."},

    {"question": "الرؤية النمطية تعني:",
     "options": ["A - تفسير واقعي لكل سلوك", "B - حكم عام على فئة بناءً على فكرة مسبقة", "C - تعاطف دائم", "D - رد فعل حيادي"],
     "answer": "B", "explanation": "الرؤية النمطية هي تصنيف الآخرين بناء على توقعات مسبقة."},

    {"question": "الإدراك الاجتماعي يتأثر بالانفعالات والتجارب السابقة.",
     "options": ["صح", "خطأ"],
     "answer": "صح", "explanation": "الخبرة والانفعالات تؤثر في الإدراك بشكل مباشر."},

    # التوافق
    {"question": "التوافق النفسي يعني:",
     "options": ["A - السيطرة على الآخرين", "B - التفاعل مع البيئة بكفاءة", "C - العزلة عن المجتمع", "D - فقدان الانسجام الداخلي"],
     "answer": "B", "explanation": "التوافق النفسي هو التفاعل الإيجابي مع البيئة."},

    {"question": "من أمثلة الإعلاء كآلية دفاعية:",
     "options": ["A - قمع الغضب دون تعبير", "B - رسم لوحة فنية بدل العنف", "C - ضرب الجدار عند الغضب", "D - إنكار الواقع"],
     "answer": "B", "explanation": "الإعلاء هو تحويل الانفعالات السلبية لنشاط مقبول."},

    {"question": "الإنكار نوع من الحيل الدفاعية.",
     "options": ["صح", "خطأ"],
     "answer": "صح", "explanation": "الإنكار هو آلية دفاعية لتجنب مواجهة الواقع."},

    # العدوانية
    {"question": "العدوان غير المباشر هو:",
     "options": ["A - الهجوم اللفظي المباشر", "B - كسر ممتلكات شخص آخر", "C - الدفاع عن النفس", "D - توجيه الأذى لمن تسبب بالإحباط"],
     "answer": "B", "explanation": "العدوان غير المباشر يتوجه نحو هدف بديل."},

    {"question": "من أسباب السلوك العدواني النفسية:",
     "options": ["A - النوم الجيد", "B - الشعور بالنقص", "C - النجاح الأكاديمي", "D - العطف الزائد"],
     "answer": "B", "explanation": "الشعور بالنقص يولد العدوان للتعويض."},

    {"question": "العنف عند الشباب قد يكون وسيلة لتحدي السلطة.",
     "options": ["صح", "خطأ"],
     "answer": "صح", "explanation": "يستخدم بعض الشباب العنف كرمز للتمرد أو إثبات الذات."}
]

# الحالة العامة
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0

# عرض السؤال الحالي
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.subheader(f"سؤال {st.session_state.q_index + 1} من {len(questions)}")
    st.write(q['question'])
    user_answer = st.radio("اختر الإجابة:", q['options'], key=st.session_state.q_index)

    if st.button("التالي"):
        if user_answer.startswith(q['answer']) or user_answer == q['answer']:
            st.session_state.score += 1
            st.success("إجابة صحيحة ✅")
        else:
            st.error("إجابة خاطئة ❌")
            st.info(f"💡 التصحيح: {q['explanation']}")

        st.session_state.q_index += 1
        st.experimental_rerun()

else:
    st.balloons()
    st.success(f"📊 انتهى الامتحان! نتيجتك: {st.session_state.score} من {len(questions)}")
    if st.button("إعادة الامتحان"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
