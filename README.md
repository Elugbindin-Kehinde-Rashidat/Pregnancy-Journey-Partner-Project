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
## Machine Learning Metrics

The maternal health risk prediction model will be evaluated using the following metrics:

- Accuracy
- Precision
- Recall (Primary Metric)
- F1-Score
- Confusion Matrix
- ROC-AUC (One-vs-Rest for multi-class classification)
## Data Source

The dataset used for this project was obtained from Hugging Face:

**Source:** Electric Sheep Africa - Synthetic Maternal Health & Pregnancy Complications Dataset  
**Platform:** Hugging Face Datasets  
**Link:** https://huggingface.co/datasets/electricsheepafrica/africa-synth-maternal-health-maternal-health-pregnancy-all

This dataset contains synthetic maternal health and pregnancy-related records designed for machine learning research and educational purposes. It includes features such as maternal age, gravidity, parity, gestational age, blood pressure measurements, BMI, haemoglobin level, ANC visits, pregnancy complications, pregnancy outcomes, and risk level classification.

The dataset is entirely synthetic and does not contain real patient information. It was generated based on parameters from published maternal health literature and guidelines, making it suitable for developing and testing predictive models but not for clinical decision-making.
## Status
Project setup in progress.
## Disclaimer
This project is for educational purposes and does not replace professional medical advice. 
