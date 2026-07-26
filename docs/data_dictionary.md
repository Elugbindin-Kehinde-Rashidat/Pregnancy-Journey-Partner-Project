# Data Dictionary

This document describes each feature used in the Pregnancy Journey Partner machine learning project.

| Feature | Description | Data Type | Unit |
|---------|-------------|-----------|------|
| id | Unique identifier assigned to each pregnancy record | Integer | N/A |
| age_years | Age of the pregnant woman | Integer | Years |
| gravidity | Total number of times the woman has been pregnant | Integer | Count |
| parity | Number of pregnancies that reached viable birth | Integer | Count |
| gestational_age_weeks | Pregnancy age at assessment | Integer | Weeks |
| bmi_pre_pregnancy | Body Mass Index before pregnancy | Float | kg/m² |
| systolic_bp_mmhg | Systolic blood pressure | Integer | mmHg |
| diastolic_bp_mmhg | Diastolic blood pressure | Integer | mmHg |
| hemoglobin_gdl | Haemoglobin concentration in blood | Float | g/dL |
| anemia_status | Indicates whether the woman has anaemia | Categorical | N/A |
| fasting_glucose_mgdl | Fasting blood glucose level | Float | mg/dL |
| proteinuria | Presence of protein in urine | Categorical | N/A |
| hiv_status | HIV infection status | Categorical | N/A |
| anc_visits | Number of antenatal care visits | Integer | Count |
| delivery_mode | Method of delivery | Categorical | N/A |
| primary_complication | Main pregnancy complication recorded | Categorical | N/A |
| pregnancy_outcome | Outcome of the pregnancy | Categorical | N/A |
| risk_level | Maternal health risk category (Target Variable) | Categorical | Low, Moderate, High |