import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="امتحان شامل", layout="centered")
st.title("امتحان تفاعلي - القيادة، الإدراك، التوافق، العدوانية")

questions = [
    {
        "question": "ما هو تعريف القيادة من المنظور التربوي؟",
        "options": ["A - استخدام السلطة لتحقيق أهداف شخصية", "B - توجيه نشاط الجماعة نحو هدف مشترك", "C - السيطرة على الآخرين بوسائل رسمية", "D - فرض النظام داخل الجماعة"],
        "answer": "B",
        "explanation": "القيادة هي توجيه نشاط الجماعة نحو هدف مشترك في بيئة تعليمية."
    },
    {
        "question": "أي من الصفات التالية لا تُعتبر من خصائص القائد الناجح؟",
        "options": ["A - الثقة بالنفس", "B - الجمود العقلي", "C - القدرة على التأثير", "D - الذكاء الاجتماعي"],
        "answer": "B",
        "explanation": "الجمود العقلي لا يتماشى مع القيادة الفعالة."
    },
    {
        "question": "القائد الذي يعتمد على مشاورة الأفراد واتخاذ القرار الجماعي يتبع النمط:",
        "options": ["A - الفوضوي", "B - الديمقراطي", "C - الأوتوقراطي", "D - الإداري"],
        "answer": "B",
        "explanation": "النمط الديمقراطي يعتمد على التشاور."
    },
    {
        "question": "القيادة هي عملية:",
        "options": ["A - سلوكية فقط", "B - جماعية وبيئية", "C - فردية فقط", "D - رسمية دومًا"],
        "answer": "B",
        "explanation": "القيادة عملية اجتماعية وبيئية تشاركية."
    },
    {
        "question": "من وظائف القيادة:",
        "options": ["A - القمع والتحكم", "B - التخطيط، التوجيه، التقييم", "C - تنفيذ أوامر المدير فقط", "D - تجنب التواصل"],
        "answer": "B",
        "explanation": "التخطيط والتقييم من وظائف القيادة."
    },
    {
        "question": "القيادة لا يمكن أن تحدث بدون وجود جماعة.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "القيادة تتطلب وجود جماعة للتفاعل معها."
    },
    {
        "question": "النمط الأوتوقراطي يشجع على الإبداع والمشاركة.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "النمط الأوتوقراطي يعتمد على فرض السلطة."
    },
    {
        "question": "من صفات القائد: الخوف من اتخاذ القرار.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "القائد الفعّال يتميز بالحسم واتخاذ القرار."
    },
    {
        "question": "القيادة تتطلب دائمًا منصب رسمي.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "القيادة قد تكون غير رسمية أيضاً."
    },
    {
        "question": "التواصل جزء أساسي من نجاح القيادة.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "بدون تواصل فعّال لا تتحقق القيادة."
    },
    {
        "question": "الإدراك الاجتماعي هو:",
        "options": ["A - تفسير الظواهر البيولوجية", "B - فهم الذات فقط", "C - إدراكنا للآخرين وتفسير سلوكهم", "D - القدرة على الرسم التحليلي"],
        "answer": "C",
        "explanation": "الإدراك الاجتماعي هو فهم سلوك الآخرين."
    },
    {
        "question": "من خصائص الإدراك الاجتماعي:",
        "options": ["A - ثابت لا يتغير", "B - عملية حسية فقط", "C - انتقائية، تفسيرية، غرضية", "D - لا تتأثر بالثقافة"],
        "answer": "C",
        "explanation": "من خصائصه: الانتقائية والغرضية."
    },
    {
        "question": "العامل الذي لا يؤثر في الإدراك الاجتماعي هو:",
        "options": ["A - الذكاء", "B - التشابه", "C - الخبرة", "D - الطول الجسدي"],
        "answer": "D",
        "explanation": "الطول الجسدي ليس عامل مؤثر في الإدراك الاجتماعي."
    },
    {
        "question": "الإدراك الاجتماعي عملية موضوعية بالكامل.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "هو عملية ذاتية تتأثر بالمشاعر."
    },
    {
        "question": "الإدراك يتأثر بالانفعالات والتجارب السابقة.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "تؤثر الخبرات السابقة على الإدراك."
    },
    {
        "question": "الرؤية النمطية تؤثر في إدراكنا للآخرين.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "الرؤية النمطية تعيق الفهم الموضوعي."
    },
    {
        "question": "التعاطف من مكونات الإدراك الاجتماعي.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "التعاطف مهم لفهم الآخرين وتقدير مشاعرهم."
    },
    {
        "question": "الإدراك الاجتماعي يحدث دون أي تأثير من البيئة.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "البيئة تلعب دوراً في تشكيل الإدراك الاجتماعي."
    },
    {
        "question": "التوافق النفسي يعني:",
        "options": ["A - السيطرة على الآخرين", "B - التفاعل مع البيئة بكفاءة", "C - العزلة عن المجتمع", "D - فقدان الانسجام الداخلي"],
        "answer": "B",
        "explanation": "التوافق النفسي يعني التفاعل بكفاءة."
    },
    {
        "question": "التوافق الشخصي يُقاس بـ:",
        "options": ["A - الإنجاز المهني", "B - السلام الداخلي والتوازن", "C - عدد الأصدقاء", "D - مقدار الدخل الشهري"],
        "answer": "B",
        "explanation": "السلام الداخلي هو مقياس أساسي للتوافق الشخصي."
    },
    {
        "question": "من الحيل الدفاعية النفسية:",
        "options": ["A - الإبداع", "B - الكبت", "C - الصراخ", "D - العناد"],
        "answer": "B",
        "explanation": "الكبت هو آلية دفاعية شائعة."
    },
    {
        "question": "التوافق هو عملية مستمرة وليست لحظية.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "التوافق يتطلب جهداً مستمراً."
    },
    {
        "question": "التوافق لا يتأثر بالحالة النفسية.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "الحالة النفسية لها تأثير كبير على التوافق."
    },
    {
        "question": "الحيل الدفاعية قد تكون مفيدة في تقليل التوتر.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "الحيل الدفاعية قد تساعد في التعامل مع التوتر مؤقتاً."
    },
    {
        "question": "الإنكار نوع من الحيل الدفاعية.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "الإنكار هو آلية دفاعية شائعة."
    },
    {
        "question": "التوافق الاجتماعي يعني رفض القواعد العامة.",
        "options": ["صح", "خطأ"],
        "answer": "خطأ",
        "explanation": "التوافق الاجتماعي يتطلب احترام القواعد."
    },
    {
        "question": "العدوان غير المباشر هو:",
        "options": ["A - الهجوم اللفظي المباشر", "B - كسر ممتلكات شخص آخر", "C - الدفاع عن النفس", "D - توجيه الأذى لمن تسبب بالإحباط"],
        "answer": "D",
        "explanation": "العدوان غير المباشر يكون ملتوياً."
    },
    {
        "question": "أحد أسباب السلوك العدواني النفسية هو:",
        "options": ["A - النوم الجيد", "B - الشعور بالنقص", "C - النجاح الأكاديمي", "D - العطف الزائد"],
        "answer": "B",
        "explanation": "الشعور بالنقص قد يؤدي إلى العدوانية."
    },
    {
        "question": "نظرية التنفيس تشير إلى أن:",
        "options": ["A - العدوان غريزة فطرية", "B - السلوك العدواني دائم", "C - العدوان يُخفف عبر تفريغ الانفعالات", "D - العدوان لا علاقة له بالعوامل البيئية"],
        "answer": "C",
        "explanation": "نظرية التنفيس ترى أن تفريغ الانفعالات يقلل العدوان."
    },
    {
        "question": "أي من الخيارات لا يُعتبر من أشكال العدوان حسب الوجهة:",
        "options": ["A - عدوان مباشر", "B - عدوان نحو الذات", "C - عدوان جماعي", "D - عدوان لفظي"],
        "answer": "D",
        "explanation": "العدوان اللفظي يصنف حسب الوسيلة وليس الوجهة."
    },
    {
        "question": "العدوان السوي يهدف إلى الدفاع عن النفس.",
        "options": ["صح", "خطأ"],
        "answer": "صح",
        "explanation": "العدوان السوي يكون دفاعياً."
    }
]

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.last_correct = False
    st.session_state.last_explanation = ""

# عرض السؤال الحالي
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    
    st.subheader(f"سؤال {st.session_state.q_index + 1} من {len(questions)}")
    st.progress((st.session_state.q_index + 1) / len(questions))
    st.write(q['question'])

    with st.form(key=f"question_form_{st.session_state.q_index}"):
        user_answer = st.radio("اختر الإجابة:", q['options'], key=f"radio_{st.session_state.q_index}")
        submitted = st.form_submit_button("التالي")
        
        if submitted:
            selected_option_letter = user_answer.split(" - ")[0] if " - " in user_answer else user_answer
            if selected_option_letter == q['answer']:
                st.session_state.score += 1
                st.session_state.last_correct = True
            else:
                st.session_state.last_correct = False
            st.session_state.last_explanation = q['explanation']
            st.session_state.show_result = True

    if st.session_state.show_result:
        if st.session_state.last_correct:
            st.success("إجابة صحيحة")
        else:
            st.error("❌ إجابة خاطئة")
        st.info(f"الشرح: {st.session_state.last_explanation}")
        if st.button("السؤال التالي"):
            st.session_state.q_index += 1
            st.session_state.show_result = False
            st.experimental_rerun()

else:
    st.balloons()
    st.success(f"انتهى الامتحان! نتيجتك: {st.session_state.score} من {len(questions)}")
    percentage = round((st.session_state.score / len(questions)) * 100, 2)
    st.write(f"نسبة النجاح: {percentage}%")

    if st.button("إعادة الامتحان"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.experimental_rerun()