from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm
from .models import StudentProfile, StressAssessment, Psychologist
from .ml_predict import predict_stress, calculate_stress_score
from .ai_recommendation import get_recommendation


def home(request):
    return render(request, "home.html")


def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            StudentProfile.objects.create(user=user, age=form.cleaned_data["age"], gender=form.cleaned_data["gender"], department=form.cleaned_data["department"], semester=form.cleaned_data["semester"])
            return redirect("login")
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        return render(request, "login.html", {"error": "Invalid Username or Password"})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def dashboard(request):
    assessments = StressAssessment.objects.filter(student__user=request.user)
    latest = assessments.order_by("-created_at").first()
    low = assessments.filter(result="Low").count()
    moderate = assessments.filter(result="Moderate").count()
    high = assessments.filter(result="High").count()
    return render(request, "dashboard.html", {"total": assessments.count(), "latest": latest, "low_count": low, "moderate_count": moderate, "high_count": high})


def test_prediction(request):
    result = predict_stress(8, 4, 9, 2, 1, 8, 9, 3, 8, 8, 70, 3, 3, 8, 1)
    return HttpResponse(f"Predicted Stress Level: {result}")


def _int(request, name, default=0):
    try:
        return int(request.POST.get(name, default))
    except (TypeError, ValueError):
        return default


@login_required
def assessment(request):
    if request.method == "POST":
        values = {
            "study_hours": _int(request, "study_hours"),
            "sleep_hours": _int(request, "sleep_hours"),
            "academic_pressure": _int(request, "academic_pressure"),
            "social_interaction": _int(request, "social_interaction"),
            "physical_activity": _int(request, "physical_activity"),
            "screen_time": _int(request, "screen_time"),
            "deadline_pressure": _int(request, "deadline_pressure"),
            "mood_level": _int(request, "mood_level"),
            "anxiety_level": _int(request, "anxiety_level"),
            "concentration_difficulty": _int(request, "concentration_difficulty"),
            "attendance_percentage": _int(request, "attendance_percentage"),
            "study_life_balance": _int(request, "study_life_balance"),
            "emotional_support": _int(request, "emotional_support"),
            "fatigue_level": _int(request, "fatigue_level"),
            "relaxation_time": _int(request, "relaxation_time"),
        }

        ranges = {
            "study_hours": (0, 24), "sleep_hours": (0, 24), "academic_pressure": (1, 10),
            "social_interaction": (1, 10), "physical_activity": (1, 10), "screen_time": (0, 24),
            "deadline_pressure": (1, 10), "mood_level": (1, 10), "anxiety_level": (1, 10),
            "concentration_difficulty": (1, 10), "attendance_percentage": (0, 100),
            "study_life_balance": (1, 10), "emotional_support": (1, 10), "fatigue_level": (1, 10),
            "relaxation_time": (0, 12),
        }
        errors = [f"{k.replace('_', ' ').title()} must be between {lo} and {hi}." for k, (lo, hi) in ranges.items() if not (lo <= values[k] <= hi)]
        if errors:
            return render(request, "assessment.html", {"errors": errors, "values": values})

        result = predict_stress(**values)
        stress_score = calculate_stress_score(**values)
        recommendation = get_recommendation(result, values)
        doctor = Psychologist.objects.first() if result == "High" else None
        profile = StudentProfile.objects.filter(user=request.user).first()
        if profile is None:
            return HttpResponse(f"No Student Profile found for user: {request.user.username}")

        StressAssessment.objects.create(student=profile, **values, stress_score=stress_score, result=result)

        # Build feature lists for the result chart. Higher values here represent more stress except protective factors.
        factor_values = {
            "Academic Pressure": values["academic_pressure"] * 10,
            "Deadline Pressure": values["deadline_pressure"] * 10,
            "Anxiety": values["anxiety_level"] * 10,
            "Fatigue": values["fatigue_level"] * 10,
            "Screen Time": min(values["screen_time"] / 12 * 100, 100),
            "Concentration Difficulty": values["concentration_difficulty"] * 10,
        }
        return render(request, "result.html", {"result": result, "recommendation": recommendation, "doctor": doctor, "stress_score": stress_score, "factor_values": factor_values})

    return render(request, "assessment.html")


@login_required
def history(request):
    profile = StudentProfile.objects.filter(user=request.user).first()
    if profile is None:
        return HttpResponse("Student Profile not found.")
    records = StressAssessment.objects.filter(student=profile).order_by("-created_at")
    return render(request, "history.html", {"records": records})
