# Pregnancy Journey Partner (PJP)
## Project Overview
Pregnancy Journey Partner is an AI-powered Maternal Health Risk Assessment and Education Assistant.
## Problem Definition
- Healthcare professionals assess maternal health risks through antenatal visits, physical examinations, vital sign monitoring, laboratory tests, and clinical judgment. This process relies heavily on manual reviews.
- Pregnant women may not always have timely access to reliable maternal health information and may not understand potential health risks during pregnancy which can delay preventive actions. 
## Proposed solution
Pregnancy Journey Partner supports healthcare professionals and pregnant women by:
1. Using Machine Learning to identify potential maternal health risk levels based on available health indicators 
2. Providing educational information through RAG-based chatbot using trusted maternal health resources. 
This system is designed to assist decision-making and improve access to education information, not to replace healthcare professionals. 
## Business Value

The Pregnancy Journey Partner project aims to:

- Support earlier identification of women who may be at Moderate or High maternal health risk.
- Reduce the time required for preliminary maternal health risk assessment through automated prediction.
- Improve consistency in preliminary risk assessment by applying the same machine learning model to every patient.
- Provide reliable maternal health education through an AI chatbot that is available 24 hours a day.
- Enable healthcare professionals to spend more time caring for patients who require urgent medical attention.
## Business Metrics

The success of the project will be evaluated using the following business metrics:

- Reduce preliminary maternal risk assessment time by approximately **50–70%** compared with manual screening.
- Achieve at least **90% consistency** in preliminary risk classification by applying the same prediction criteria to all patients.
- Correctly identify at least **90% of pregnancies classified as High Risk** for further medical review.
- Provide continuous access to maternal health education through a chatbot with a target availability of **24 hours a day, 7 days a week**.
- Reduce the manual workload involved in preliminary maternal screening, allowing healthcare professionals to focus on higher-risk cases.

## Model Evaluation Results

### Model Comparison

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Random Forest       |   94.07% |    94.32% | 94.07% |   94.03% |
| Tuned Random Forest |   94.03% |    94.31% | 94.03% |   94.00% |
| Decision Tree       |   89.62% |    89.65% | 89.62% |   89.63% |
| Logistic Regression |   78.07% |    78.65% | 78.07% |   78.11% |

### Final Model: Random Forest

The Random Forest was selected as the final model based on its strong overall performance and its ability to identify high-risk pregnancies.

| Metric           |     Result |
| ---------------- | ---------: |
| Accuracy         | **94.07%** |
| Precision        | **94.32%** |
| Recall           | **94.07%** |
| F1-Score         | **94.03%** |
| High-Risk Recall | **85.70%** |

### Confusion Matrix

The confusion matrix for the Random Forest model is shown below:

| Actual / Predicted | High Risk | Low Risk | Mid Risk |
| ------------------ | --------: | -------: | -------: |
| **High Risk**      |     1,258 |        3 |      207 |
| **Low Risk**       |         0 |    2,392 |       28 |
| **Mid Risk**       |         7 |      111 |    1,994 |

### ROC-AUC

| Model               | ROC-AUC |
| ------------------- | ------: |
| Logistic Regression |  91.30% |
| Tuned Random Forest |  98.40% |

### Key Observation

The Random Forest achieved an overall recall of **94.07%** and a High-Risk Recall of **85.70%**. Since identifying high-risk pregnancies is the primary objective of this project, **Recall for the High-Risk class was given particular emphasis during model evaluation**.

## Data Source

The dataset used for this project was obtained from Hugging Face:

**Source:** Electric Sheep Africa - Synthetic Maternal Health & Pregnancy Complications Dataset  
**Platform:** Hugging Face Datasets  
**Link:** https://huggingface.co/datasets/electricsheepafrica/africa-synth-maternal-health-maternal-health-pregnancy-all

This dataset contains synthetic maternal health and pregnancy-related records designed for machine learning research and educational purposes. It includes features such as maternal age, gravidity, parity, gestational age, blood pressure measurements, BMI, haemoglobin level, ANC visits, pregnancy complications, pregnancy outcomes, and risk level classification.

The dataset is entirely synthetic and does not contain real patient information. It was generated based on parameters from published maternal health literature and guidelines, making it suitable for developing and testing predictive models but not for clinical decision-making.

## Disclaimer
This project is for educational purposes and does not replace professional medical advice. 
