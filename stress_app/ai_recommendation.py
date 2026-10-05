def get_recommendation(result, values=None):
    values = values or {}
    tips = []
    factor_notes = []

    checks = [
        ("sleep_hours", lambda v: v < 6, "Your sleep duration is low. Try maintaining a consistent sleep schedule and getting adequate rest."),
        ("screen_time", lambda v: v > 7, "Your screen time is high. Try regular digital breaks, especially during study sessions."),
        ("academic_pressure", lambda v: v >= 8, "Academic pressure is high. Break large tasks into smaller goals and use a realistic study timetable."),
        ("deadline_pressure", lambda v: v >= 8, "Upcoming deadlines may be adding pressure. Prioritize tasks and avoid last-minute work."),
        ("anxiety_level", lambda v: v >= 8, "Your reported anxiety is high. Consider relaxation techniques and talking to someone you trust."),
        ("concentration_difficulty", lambda v: v >= 8, "Concentration appears difficult. Try focused study sessions with short breaks and fewer distractions."),
        ("physical_activity", lambda v: v <= 3, "Physical activity is low. Consider adding a short walk or light exercise to your routine."),
        ("emotional_support", lambda v: v <= 3, "You reported limited emotional support. Consider connecting with a trusted friend, family member, teacher or counselor."),
        ("study_life_balance", lambda v: v <= 3, "Your study-life balance is low. Schedule time for hobbies, rest and social activities."),
        ("fatigue_level", lambda v: v >= 8, "Your fatigue level is high. Prioritize rest and review your sleep and daily workload."),
        ("mood_level", lambda v: v <= 3, "Your reported mood is low. Give yourself time for rest and supportive social connection."),
    ]
    for key, condition, note in checks:
        if key in values and condition(values[key]):
            factor_notes.append(note)

    if not factor_notes:
        factor_notes.append("Your responses do not show a single dominant concern. Continue maintaining a balanced routine.")

    if result == "Low":
        title = "😊 Low Stress"
        message = "Your responses indicate a low estimated stress level. Keep maintaining healthy study, sleep and lifestyle habits."
        tips = ["Maintain a consistent sleep routine.", "Take short breaks during long study sessions.", "Continue physical activity and social interaction.", "Keep time for hobbies and relaxation."]
    elif result == "Moderate":
        title = "😐 Moderate Stress"
        message = "Your responses indicate a moderate estimated stress level. A few routine changes may help you manage pressure more comfortably."
        tips = ["Break large academic tasks into smaller goals.", "Use focused study sessions with regular breaks.", "Maintain adequate sleep and hydration.", "Talk with family, friends, mentors or a counselor when needed."]
    else:
        title = "🔴 High Stress"
        message = "Your responses indicate a high estimated stress level. Consider prioritizing rest, reducing avoidable pressure and seeking support if distress persists."
        tips = ["Prioritize adequate sleep and recovery.", "Reduce avoidable screen time and take regular breaks.", "Use relaxation, breathing, yoga or light exercise.", "Talk with a trusted person or qualified professional if needed."]

    return {"title": title, "message": message, "tips": tips, "factor_notes": factor_notes, "doctor": None}
