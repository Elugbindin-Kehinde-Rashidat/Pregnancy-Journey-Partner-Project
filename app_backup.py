import streamlit as st

from src.prediction import predict_pregnancy_risk
from src.chatbot import generate_answer


# ============================================
# Page configuration
# ============================================

st.set_page_config(
    page_title="Pregnancy Journey Partner",
    page_icon="🤰",
    layout="wide"
)


# ============================================
# Header
# ============================================

st.title("🤰 Pregnancy Journey Partner (PJP)")

st.subheader(
    "Your educational companion for a safer pregnancy journey"
)

st.write(
    "Pregnancy Journey Partner (PJP) combines a machine learning "
    "risk assessment model with an evidence-based pregnancy "
    "information assistant."
)

st.divider()


# ============================================
# Main sections
# ============================================

tab1, tab2 = st.tabs([
    "🩷 Pregnancy Risk Assessment",
    "💬 Pregnancy Information Assistant"
])


# ============================================
# TAB 1 — Risk Assessment
# ============================================

with tab1:

    st.header("Pregnancy Risk Assessment")

    st.write(
        "Enter the available pregnancy information below to receive "
        "a machine-learning-based risk prediction."
    )

    st.info(
        "This assessment is for educational purposes only and does "
        "not replace assessment by a qualified healthcare professional."
    )

    # ----------------------------------------
    # Basic information
    # ----------------------------------------

    st.subheader("Basic Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age_years = st.number_input(
            "Age (years)",
            min_value=10,
            max_value=60,
            value=28
        )

    with col2:
        gravidity = st.number_input(
            "Gravidity",
            min_value=0,
            max_value=20,
            value=2
        )

    with col3:
        parity = st.number_input(
            "Parity",
            min_value=0,
            max_value=20,
            value=1
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        gestational_age_weeks = st.number_input(
            "Gestational Age (weeks)",
            min_value=1,
            max_value=45,
            value=32
        )

    with col2:
        bmi_pre_pregnancy = st.number_input(
            "Pre-pregnancy BMI (kg/m²)",
            min_value=10.0,
            max_value=60.0,
            value=24.5,
            step=0.1
        )

    with col3:
        anc_visits = st.number_input(
            "ANC Visits",
            min_value=0,
            max_value=30,
            value=5
        )

    # ----------------------------------------
    # Health measurements
    # ----------------------------------------

    st.subheader("Health Measurements")

    col1, col2 = st.columns(2)

    with col1:
        systolic_bp_mmhg = st.number_input(
            "Systolic Blood Pressure (mmHg)",
            min_value=50,
            max_value=250,
            value=120
        )

    with col2:
        diastolic_bp_mmhg = st.number_input(
            "Diastolic Blood Pressure (mmHg)",
            min_value=30,
            max_value=150,
            value=80
        )

    col1, col2 = st.columns(2)

    with col1:
        hemoglobin_gdl = st.number_input(
            "Hemoglobin (g/dL)",
            min_value=3.0,
            max_value=25.0,
            value=12.5,
            step=0.1
        )

    with col2:
        fasting_glucose_mgdl = st.number_input(
            "Fasting Blood Glucose (mg/dL)",
            min_value=30,
            max_value=400,
            value=90
        )

    # ----------------------------------------
    # Other information
    # ----------------------------------------

    st.subheader("Additional Information")

    col1, col2 = st.columns(2)

    with col1:
        proteinuria = st.number_input(
            "Proteinuria",
            min_value=0,
            max_value=4,
            value=0
        )

    with col2:
        hiv_status = st.selectbox(
            "HIV Status",
            options=["Negative", "Positive"]
        )

    col1, col2 = st.columns(2)

    with col1:
        delivery_mode = st.selectbox(
            "Delivery Mode",
            options=["Vaginal", "Caesarean"]
        )

    with col2:
        pregnancy_outcome = st.selectbox(
            "Pregnancy Outcome",
            options=[
                "Live Birth",
                "Stillbirth",
                "Maternal Death"
            ]
        )

    st.divider()

    # ----------------------------------------
    # Convert categorical values to model codes
    # ----------------------------------------

    hiv_code = {
        "Negative": 0,
        "Positive": 1
    }[hiv_status]

    delivery_code = {
        "Caesarean": 0,
        "Vaginal": 1
    }[delivery_mode]

    outcome_code = {
        "Live Birth": 0,
        "Maternal Death": 1,
        "Stillbirth": 2
    }[pregnancy_outcome]

    # ----------------------------------------
    # Prediction button
    # ----------------------------------------

    if st.button(
        "🔍 Predict Pregnancy Risk",
        type="primary",
        use_container_width=True
    ):

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
            outcome_code
        )

        risk_level = result["risk_level"]

        st.subheader("Prediction Result")

        if risk_level == "High Risk":
            st.error(
                f"⚠️ Predicted Risk Level: **{risk_level}**"
            )

        elif risk_level == "Mid Risk":
            st.warning(
                f"⚠️ Predicted Risk Level: **{risk_level}**"
            )

        else:
            st.success(
                f"✅ Predicted Risk Level: **{risk_level}**"
            )

        st.caption(
            "This is a machine-learning prediction and not a medical diagnosis."
        )


# ============================================
# TAB 2 — Pregnancy Information Assistant
# ============================================

with tab2:

    st.header("Pregnancy Information Assistant")

    st.write(
        "Ask Pregnancy Journey Partner a pregnancy-related question. "
        "The assistant retrieves information from the trusted "
        "WHO and UNICEF knowledge base before generating a response."
    )

    question = st.text_area(
        "Ask your question:",
        placeholder=(
            "Example: What are the danger signs during pregnancy?"
        ),
        height=120
    )

    if st.button(
        "💬 Ask Pregnancy Journey Partner",
        type="primary"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question first."
            )

        else:

            with st.spinner(
                "Searching the pregnancy knowledge base..."
            ):

                answer = generate_answer(
                    question
                )

            st.subheader("Answer")

            st.write(answer)


# ============================================
# Footer
# ============================================

st.divider()

st.caption(
    "Pregnancy Journey Partner (PJP) | "
    "Educational information and machine-learning-based risk assessment"
)

st.caption(
    "PJP does not replace professional medical advice, diagnosis, "
    "or treatment. For urgent symptoms or danger signs, seek "
    "appropriate medical care promptly."
)