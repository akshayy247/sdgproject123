from django.contrib import admin
from .models import StudentProfile, StressAssessment, Psychologist
from django.contrib import admin

admin.site.register(StudentProfile)
admin.site.register(StressAssessment)
admin.site.register(Psychologist)