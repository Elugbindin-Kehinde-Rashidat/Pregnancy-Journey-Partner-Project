import streamlit as st
from pathlib import Path

from src.prediction import predict_pregnancy_risk
from src.chatbot import generate_answer


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="Pregnancy Journey Partner (PJP)",
    page_icon="🤰",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# Styling
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff7fb 0%, #ffffff 42%, #fbf8ff 100%);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .hero-card {
        background: linear-gradient(135deg, #fff0f7 0%, #f8f0ff 100%);
        border: 1px solid #f4d6e8;
        border-radius: 28px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 30px rgba(104, 61, 126, 0.08);
    }

    .eyebrow {
        display: inline-block;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        background: #ffe5f0;
        color: #c52d72;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        color: #29134d;
        font-size: 3.2rem;
        line-height: 1.05;
        font-weight: 800;
        margin: 0;
    }

    .hero-title span {
        color: #d62f78;
    }

    .hero-subtitle {
        color: #7040a2;
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 1rem;
    }

    .hero-text {
        color: #34303a;
        font-size: 1rem;
        line-height: 1.7;
    }

    .section-title {
        color: #29134d;
        font-weight: 800;
        text-align: center;
        font-size: 2rem;
        margin: 1.5rem 0 1rem 0;
    }

    .feature-card {
        background: white;
        border: 1px solid #eadff0;
        border-radius: 24px;
        padding: 1.5rem;
        min-height: 260px;
        box-shadow: 0 8px 25px rgba(60, 35, 90, 0.06);
    }

    .feature-card.pink {
        border-color: #f4c9dc;
        background: linear-gradient(145deg, #fffafd, #fff4f8);
    }

    .feature-card.purple {
        border-color: #ddd0f5;
        background: linear-gradient(145deg, #ffffff, #faf7ff);
    }

    .feature-icon {
        font-size: 2.4rem;
    }

    .feature-title {
        color: #c92e73;
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: 0.5rem;
    }

    .purple-title {
        color: #6840a4;
    }

    .feature-text {
        color: #39343e;
        line-height: 1.65;
    }

    .info-box {
        background: white;
        border: 1px solid #eee1f3;
        border-radius: 20px;
        padding: 1.2rem;
        height: 100%;
        text-align: center;
    }

    .info-title {
        color: #6b3ca4;
        font-weight: 800;
    }

    .disclaimer {
        background: #fff0f6;
        border: 1px solid #f6c7dc;
        border-radius: 18px;
        padding: 1rem 1.2rem;
        color: #4a3944;
        margin-top: 1.5rem;
    }

    .back-link {
        color: #7040a2;
        font-weight: 700;
    }

    .risk-result {
        border-radius: 20px;
        padding: 1.3rem;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 800;
        margin: 1rem 0;
    }

    .small-muted {
        color: #746b79;
        font-size: 0.9rem;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# Session navigation
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_to(page):
    st.session_state.page = page


# ============================================================
# Shared disclaimer
# ============================================================

def show_disclaimer():
    st.markdown(
        """
        <div class="disclaimer">
        <strong>⚠️ Medical Disclaimer</strong><br>
        Pregnancy Journey Partner (PJP) provides general educational
        information and is not a substitute for professional medical
        advice, diagnosis, or treatment. For urgent symptoms or danger
        signs, please seek appropriate medical care promptly.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HOME PAGE
# ============================================================

def show_home():
    left, right = st.columns([0.9, 1.4], gap="large")

    with left:
        hero_path = Path(__file__).parent / "assets" / "pjp_hero_illustration.png"

        if hero_path.exists():
            st.image(str(hero_path), use_container_width=True)
        else:
            st.markdown(
                "<div style='font-size:7rem;text-align:center;'>🤰</div>",
                unsafe_allow_html=True,
            )

    with right:
        st.markdown(
            '<div class="hero-card">'
            '<div class="eyebrow">🛡️ Evidence-Based · AI-Powered · For You</div>'
            '<div class="hero-title">Pregnancy<br>Journey Partner <span>(PJP)</span></div>'
            '<div class="hero-subtitle">Your educational companion for the pregnancy journey</div>'
            '<p class="hero-text">'
            'Pregnancy Journey Partner combines a machine-learning risk '
            'assessment model with an evidence-based pregnancy information '
            'assistant powered by trusted WHO and UNICEF knowledge.'
            '</p>'
            '</div>',
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)

        with c1:
            if st.button(
                "🩷 Pregnancy Risk Assessment",
                use_container_width=True,
                type="primary",
            ):
                go_to("risk")
                st.rerun()

        with c2:
            if st.button(
                "💬 Ask PJP",
                use_container_width=True,
            ):
                go_to("chat")
                st.rerun()

    st.markdown(
        '<div class="section-title">How would you like PJP to help you today?</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown(
            """
            <div class="feature-card pink">
                <div class="feature-icon">🩷</div>
                <div class="feature-title">Pregnancy Risk Assessment</div>
                <p class="feature-text">
                Assess pregnancy risk using the Random Forest machine-learning
                model. Enter the required information to receive a risk-level
                prediction.
                </p>
                </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Go to Risk Assessment →", key="home_risk", use_container_width=True):
            go_to("risk")
            st.rerun()

    with c2:
        st.markdown(
            """
            <div class="feature-card purple">
                <div class="feature-icon">💬</div>
                <div class="feature-title purple-title">Ask PJP</div>
                <p class="feature-text">
                Ask pregnancy-related questions and receive evidence-based
                answers grounded in the WHO and UNICEF knowledge base.
                </p>
                </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Go to Ask PJP →", key="home_chat", use_container_width=True):
            go_to("chat")
            st.rerun()

    st.markdown(
        '<div class="section-title">What makes PJP different?</div>',
        unsafe_allow_html=True,
    )

    f1, f2, f3, f4 = st.columns(4)

    cards = [
        ("🛡️", "Evidence-Based", "Information from trusted WHO and UNICEF resources."),
        ("🧠", "AI-Powered", "Smart retrieval and responses powered by AI."),
        ("📊", "ML-Powered Assessment", "Machine-learning risk prediction to support awareness."),
        ("💜", "Designed for You", "Simple, educational support for the pregnancy journey."),
    ]

    for col, (icon, title, text) in zip([f1, f2, f3, f4], cards):
        with col:
            st.markdown(
                f"""
                <div class="info-box">
                    <div style="font-size:2rem;">{icon}</div>
                    <div class="info-title">{title}</div>
                    <p>{text}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    show_disclaimer()

    st.markdown(
        "<p style='text-align:center;color:#746b79;margin-top:1.5rem;'>"
        "© 2026 Pregnancy Journey Partner (PJP) · Your educational companion "
        "for the pregnancy journey 🩷"
        "</p>",
        unsafe_allow_html=True,
    )


# ============================================================
# RISK ASSESSMENT PAGE
# ============================================================

def show_risk():
    if st.button("← Back to PJP Home"):
        go_to("home")
        st.rerun()

    st.markdown(
        '<div class="section-title">🩷 Pregnancy Risk Assessment</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Enter the available pregnancy information below. "
        "PJP will use the trained Random Forest model to provide a "
        "risk-level prediction."
    )

    st.subheader("Basic Information")

    c1, c2, c3 = st.columns(3)

    with c1:
        age_years = st.number_input("Age (years)", 10, 60, 28)

    with c2:
        gravidity = st.number_input("Gravidity", 0, 20, 2)

    with c3:
        parity = st.number_input("Parity", 0, 20, 1)

    c1, c2, c3 = st.columns(3)

    with c1:
        gestational_age_weeks = st.number_input(
            "Gestational Age (weeks)", 1, 45, 32
        )

    with c2:
        bmi_pre_pregnancy = st.number_input(
            "Pre-pregnancy BMI (kg/m²)",
            10.0, 60.0, 24.5, step=0.1
        )

    with c3:
        anc_visits = st.number_input("ANC Visits", 0, 30, 5)

    st.subheader("Health Measurements")

    c1, c2 = st.columns(2)

    with c1:
        systolic_bp_mmhg = st.number_input(
            "Systolic Blood Pressure (mmHg)", 50, 250, 120
        )

    with c2:
        diastolic_bp_mmhg = st.number_input(
            "Diastolic Blood Pressure (mmHg)", 30, 150, 80
        )

    c1, c2 = st.columns(2)

    with c1:
        hemoglobin_gdl = st.number_input(
            "Hemoglobin (g/dL)", 3.0, 25.0, 12.5, step=0.1
        )

    with c2:
        fasting_glucose_mgdl = st.number_input(
            "Fasting Blood Glucose (mg/dL)", 30, 400, 90
        )

    st.subheader("Additional Information")

    c1, c2 = st.columns(2)

    with c1:
        proteinuria = st.number_input("Proteinuria", 0, 4, 0)

    with c2:
        hiv_status = st.selectbox("HIV Status", ["Negative", "Positive"])

    c1, c2 = st.columns(2)

    with c1:
        delivery_mode = st.selectbox("Delivery Mode", ["Vaginal", "Caesarean"])

    with c2:
        pregnancy_outcome = st.selectbox(
            "Pregnancy Outcome",
            ["Live Birth", "Stillbirth", "Maternal Death"],
        )

    hiv_code = {"Negative": 0, "Positive": 1}[hiv_status]
    delivery_code = {"Caesarean": 0, "Vaginal": 1}[delivery_mode]
    outcome_code = {
        "Live Birth": 0,
        "Maternal Death": 1,
        "Stillbirth": 2,
    }[pregnancy_outcome]

    if st.button(
        "🔍 Predict Pregnancy Risk",
        type="primary",
        use_container_width=True,
    ):
        with st.spinner("Assessing pregnancy risk..."):
            result = predict_pregnancy_risk(
                age_years,
                gravidity,
                parity,
                gestational_age_weeks,
                bmi_pre_pregnancy,
                systolic_bp_mmhg,
                diastolic_bp_mmhg,
                hemoglobin_gdl,
                fasting_glucose_mgdl,
                proteinuria,
                hiv_code,
                anc_visits,
                delivery_code,
                outcome_code,
            )

        risk_level = result["risk_level"]

        st.subheader("Prediction Result")

        if risk_level == "High Risk":
            st.error(f"⚠️ Predicted Risk Level: {risk_level}")
        elif risk_level == "Mid Risk":
            st.warning(f"⚠️ Predicted Risk Level: {risk_level}")
        else:
            st.success(f"✅ Predicted Risk Level: {risk_level}")

        st.caption(
            "This is a machine-learning prediction for educational purposes "
            "and is not a medical diagnosis."
        )

    show_disclaimer()


# ============================================================
# ASK PJP PAGE
# ============================================================

def show_chat():
    if st.button("← Back to PJP Home"):
        go_to("home")
        st.rerun()

    st.markdown(
        '<div class="section-title">💬 Ask Pregnancy Journey Partner</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Ask a pregnancy-related question. PJP retrieves relevant "
        "information from the trusted WHO and UNICEF knowledge base "
        "before generating a response."
    )

    question = st.text_area(
        "Your question",
        placeholder="Example: What are the danger signs during pregnancy?",
        height=130,
    )

    if st.button(
        "💬 Ask PJP",
        type="primary",
        use_container_width=True,
    ):
        if not question.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Searching the knowledge base and preparing an answer..."):
                answer = generate_answer(question)

            st.subheader("Answer")
            st.write(answer)

    show_disclaimer()


# ============================================================
# App router
# ============================================================

if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "risk":
    show_risk()
elif st.session_state.page == "chat":
    show_chat()
