from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile


class SignUpForm(forms.ModelForm):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = StudentProfile

        fields = [
            'age',
            'gender',
            'department',
            'semester'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username