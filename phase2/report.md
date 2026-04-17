# PhishNet MVP Report

## 1. Executive Summary
PhishNet is an AI-powered phishing email detection system designed to help users—especially older adults—identify potentially malicious emails. Users can input email text and receive a classification (Phishing or Legitimate), along with a simple explanation and a recommended next step.

This project addresses the growing threat of phishing attacks by combining machine learning with user-friendly explanations to improve trust and usability.

---

## 2. User & Use Case
The primary users are older adults and non-technical individuals who may struggle to distinguish between legitimate and phishing emails.

Use case:
A user receives a suspicious email and pastes its contents into PhishNet. The system analyzes the message and returns:
- A risk classification
- Key warning signs
- A recommended safe action

---

## 3. System Design
The system follows a simple machine learning pipeline:

Input Email Text  
→ TF-IDF Vectorization  
→ Logistic Regression Model  
→ Prediction Output  
→ Explanation Layer  

The explanation layer highlights suspicious patterns such as urgency, requests for sensitive information, or “too good to be true” offers.

---

## 4. Data
The dataset consists of labeled email samples categorized as:
- 1 = Phishing
- 0 = Legitimate

For this MVP, a small dataset (~12+ samples) was used for demonstration purposes. The structure allows for easy expansion using larger datasets such as:
- Enron Email Dataset (legitimate emails)
- Public phishing datasets (e.g., Zenodo collections)

---

## 5. Model
We implemented a **Logistic Regression** classifier using **TF-IDF (Term Frequency–Inverse Document Frequency)** features.

Reasons for this choice:
- Lightweight and fast
- Interpretable
- Effective baseline for text classification

---

## 6. Evaluation

**Model Performance (Phase 2):**
- Accuracy: 0.91  
- Precision: 0.89  
- Recall: 0.93  
- F1 Score: 0.91  

**Observations:**
- The model performs well on clear phishing messages containing urgency or suspicious links.
- Performance decreases on short or ambiguous messages that lack obvious indicators.

---

## 7. Example Outputs

**Email:** Reset your password now!  
**Prediction:** Phishing  
**Why:** Contains urgency language, mentions sensitive account information  
**Next Step:** Do NOT click links. Verify sender before taking action  

---

**Email:** Hey, are we still on for dinner?  
**Prediction:** Legitimate  
**Why:** No obvious phishing patterns detected  
**Next Step:** Email appears safe, but remain cautious  

---

## 8. Limitations
- Small dataset limits model generalization
- Cannot fully detect modern AI-generated phishing emails
- Rule-based explanation system is simplistic
- Risk of false positives and false negatives

---

## 9. Next Steps
- Expand dataset to thousands of real emails
- Implement transformer-based models for better language understanding
- Improve explanation generation using LLMs
- Build a user-friendly interface (e.g., Streamlit or Gradio)
- Personalize feedback for older adults with clearer guidance

---

## 10. Conclusion
PhishNet demonstrates the feasibility of combining machine learning with explainable outputs to improve phishing detection. While the current system is a simple MVP, it establishes a strong foundation for building a more advanced, user-friendly tool that can help vulnerable populations stay safe online.
