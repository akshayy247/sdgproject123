import os
import joblib

# Resolve path relative to the script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "stress_model.pkl")

model = joblib.load(MODEL_PATH)

result = model.predict([
    [8, 4, 9, 2, 1]
])

print("Predicted Stress Level:", result[0])