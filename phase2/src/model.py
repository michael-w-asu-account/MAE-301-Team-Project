# model.py

import pandas as pd
import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# Paths
# -----------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.normpath(os.path.join(script_dir, "..", "data", "emails.csv"))
artifacts_dir = os.path.normpath(os.path.join(script_dir, "..", "artifacts"))

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(data_path)

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# -----------------------------
# Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_features=5000
)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_tfidf, y_train)

# -----------------------------
# Evaluate Model
# -----------------------------
y_pred = model.predict(X_test_tfidf)

report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel Evaluation:\n")
print(report)

print("\nConfusion Matrix:\n")
print(cm)

# -----------------------------
# Save Artifacts
# -----------------------------
os.makedirs(artifacts_dir, exist_ok=True)

joblib.dump(model, os.path.join(artifacts_dir, "model.pkl"))
joblib.dump(vectorizer, os.path.join(artifacts_dir, "vectorizer.pkl"))

# -----------------------------
# Explanation Function
# -----------------------------
def explain_email(text):
    reasons = []

    text_lower = text.lower()

    if any(word in text_lower for word in ["urgent", "now", "immediately"]):
        reasons.append("Contains urgency language")

    if any(word in text_lower for word in ["click", "link", "verify"]):
        reasons.append("Requests clicking a link or verification")

    if any(word in text_lower for word in ["password", "account"]):
        reasons.append("Mentions sensitive account information")

    if any(word in text_lower for word in ["free", "won", "prize", "gift"]):
        reasons.append("Too-good-to-be-true offer")

    if not reasons:
        reasons.append("No obvious phishing patterns detected")

    return reasons

# -----------------------------
# Prediction Function
# -----------------------------
def predict_email(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    label = "Phishing" if pred == 1 else "Legitimate"
    explanation = explain_email(text)

    if pred == 1:
        action = "Do NOT click links. Verify sender before taking action."
    else:
        action = "Email appears safe, but remain cautious."

    return label, explanation, action

# -----------------------------
# Save Sample Outputs
# -----------------------------
sample_emails = [
    "Reset your password now!",
    "Hey, are we still on for dinner?",
    "Click here to claim your reward!",
    "Can you send me the notes from class?",
    "Watch this video for free money!"
]

outputs_path = os.path.join(artifacts_dir, "outputs.txt")
with open(outputs_path, "w") as f:
    for email in sample_emails:
        label, explanation, action = predict_email(email)

        f.write(f"Email: {email}\n")
        f.write(f"Prediction: {label}\n")
        f.write(f"Why: {', '.join(explanation)}\n")
        f.write(f"Next Step: {action}\n\n")

print(f"\nSample outputs saved to {outputs_path}")

# -----------------------------
# Interactive Mode
# -----------------------------
while True:
    print("Enter an email (or type 'exit'): ")
    lines = []
    while True:
        line = input()
        if line == "": break
        lines.append(line)
    text = "\n".join(lines)

    if text.lower() == "exit":
        break

    label, explanation, action = predict_email(text)

    print("\nPrediction:", label)
    print("Why:", ", ".join(explanation))
    print("Next Step:", action)
