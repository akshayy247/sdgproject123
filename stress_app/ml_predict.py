import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "stress_model.pkl")
model = joblib.load(MODEL_PATH)

FEATURE_NAMES = [
    "study_hours", "sleep_hours", "academic_pressure", "social_interaction",
    "physical_activity", "screen_time", "deadline_pressure", "mood_level",
    "anxiety_level", "concentration_difficulty", "attendance_percentage",
    "study_life_balance", "emotional_support", "fatigue_level", "relaxation_time"
]

def predict_stress(study_hours, sleep_hours, academic_pressure, social_interaction,
                   physical_activity, screen_time, deadline_pressure, mood_level,
                   anxiety_level, concentration_difficulty, attendance_percentage,
                   study_life_balance, emotional_support, fatigue_level, relaxation_time):
    values = [[study_hours, sleep_hours, academic_pressure, social_interaction,
               physical_activity, screen_time, deadline_pressure, mood_level,
               anxiety_level, concentration_difficulty, attendance_percentage,
               study_life_balance, emotional_support, fatigue_level, relaxation_time]]
    return model.predict(values)[0]


def calculate_stress_score(study_hours, sleep_hours, academic_pressure, social_interaction,
                           physical_activity, screen_time, deadline_pressure, mood_level,
                           anxiety_level, concentration_difficulty, attendance_percentage,
                           study_life_balance, emotional_support, fatigue_level, relaxation_time):
    # A transparent 0-100 indicator for UI only; the ML classification remains the primary result.
    components = [
        min(10, academic_pressure), min(10, deadline_pressure), min(10, anxiety_level),
        min(10, concentration_difficulty), min(10, fatigue_level), min(10, screen_time / 1.2),
        min(10, max(0, 10 - sleep_hours)), min(10, 10 - mood_level),
        min(10, 10 - study_life_balance), min(10, 10 - emotional_support),
        min(10, 10 - physical_activity), min(10, 10 - social_interaction),
        min(10, max(0, (100 - attendance_percentage) / 10)), min(10, max(0, 7 - relaxation_time)),
        min(10, study_hours / 1.2)
    ]
    return round(sum(components) / len(components) * 10, 1)
