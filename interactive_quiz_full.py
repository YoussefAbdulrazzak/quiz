import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="امتحان تفاعلي شامل", layout="centered")
st.title("📘 امتحان تفاعلي - القيادة والإدراك والتوافق والعدوانية")

# قاعدة بيانات الأسئلة (80+ سؤال) - عينة موسعة
questions = [
    {"question": "ما هو تعريف القيادة من المنظور التربوي؟",
     "options": ["A - استخدام السلطة لتحقيق أهداف شخصية", "B - توجيه نشاط الجماعة نحو هدف مشترك", "C - السيطرة على الآخرين بوسائل رسمية", "D - فرض النظام داخل الجماعة"],
     "answer": "B", "explanation": "القيادة هي توجيه نشاط الجماعة نحو هدف مشترك."},
    {"question": "القيادة لا يمكن أن تحدث بدون وجود جماعة.",
     "options": ["صح", "خطأ"], "answer": "صح", "explanation": "القيادة تحتاج إلى جماعة لتحقيق تفاعل وتوجيه."},
    {"question": "الإدراك الاجتماعي يشمل القدرة على التنبؤ بالمواقف الاجتماعية.",
     "options": ["صح", "خطأ"], "answer": "صح", "explanation": "من مهارات الإدراك الاجتماعي التنبؤ بالمواقف."},
    {"question": "التوافق النفسي يعني:", 
     "options": ["A - السيطرة على الآخرين", "B - التفاعل مع البيئة بكفاءة", "C - العزلة عن المجتمع", "D - فقدان الانسجام الداخلي"],
     "answer": "B", "explanation": "التوافق هو توازن داخلي وتفاعل خارجي سليم."},
    {"question": "العدوان غير المباشر هو:",
     "options": ["A - الهجوم اللفظي المباشر", "B - كسر ممتلكات شخص آخر", "C - الدفاع عن النفس", "D - توجيه الأذى لمن تسبب بالإحباط"],
     "answer": "B", "explanation": "العدوان غير المباشر موجّه نحو بديل."},
    {"question": "من الحيل الدفاعية النفسية:",
     "options": ["A - الإبداع", "B - الكبت", "C - الصراخ", "D - العناد"],
     "answer": "B", "explanation": "الكبت أحد الحيل الدفاعية اللاشعورية."},
    {"question": "العنف عند الشباب قد يكون وسيلة لتحدي السلطة.",
     "options": ["صح", "خطأ"], "answer": "صح", "explanation": "العنف يُستخدم أحيانًا للتعبير عن التمرد أو الهوية."}
    # ... باقي الأسئلة تُضاف هنا بنفس التنسيق ...
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
