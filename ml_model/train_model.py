import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "stress_model.pkl")

FEATURES = [
    "study_hours", "sleep_hours", "academic_pressure", "social_interaction",
    "physical_activity", "screen_time", "deadline_pressure", "mood_level",
    "anxiety_level", "concentration_difficulty", "attendance_percentage",
    "study_life_balance", "emotional_support", "fatigue_level", "relaxation_time"
]

data = pd.read_csv(DATASET_PATH)
X = data[FEATURES]
y = data["stress_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=250, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

joblib.dump(model, MODEL_PATH)
print("Model Saved:", MODEL_PATH)
