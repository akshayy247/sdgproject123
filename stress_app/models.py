from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()

    def __str__(self):
        return self.user.username


class StressAssessment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    study_hours = models.IntegerField()
    sleep_hours = models.IntegerField()
    academic_pressure = models.IntegerField()
    social_interaction = models.IntegerField()
    physical_activity = models.IntegerField()
    screen_time = models.IntegerField(default=0)
    deadline_pressure = models.IntegerField(default=0)
    mood_level = models.IntegerField(default=5)
    anxiety_level = models.IntegerField(default=0)
    concentration_difficulty = models.IntegerField(default=0)
    attendance_percentage = models.IntegerField(default=0)
    study_life_balance = models.IntegerField(default=5)
    emotional_support = models.IntegerField(default=5)
    fatigue_level = models.IntegerField(default=0)
    relaxation_time = models.IntegerField(default=0)
    stress_score = models.FloatField(default=0)
    result = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result


class Psychologist(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hospital = models.CharField(max_length=150)
    address = models.TextField()
    city = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name
