# model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Sample dataset (temporary data)
data = {
    "text": [
        "Reset your password now!",
        "Congratulations, you won a prize!",
        "Hey, are we still on for dinner?",
        "Meeting tomorrow at 10am",
        "Click this link to verify your account"
    ],
    "label": [1, 1, 0, 0, 1]  # 1 = phishing, 0 = legit
}

df = pd.DataFrame(data)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# Vectorize
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Demo input
while True:
    user_input = input("\nEnter an email (or type 'exit'): ")
    if user_input.lower() == "exit":
        break
    vec = vectorizer.transform([user_input])
    pred = model.predict(vec)[0]
    print("Prediction:", "Phishing" if pred == 1 else "Legitimate")
