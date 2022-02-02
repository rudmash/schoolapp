from dataclasses import field, fields
from django.contrib.auth import get_user_model
from django import forms
from .models import Teacher, Learner
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email")
        fields_classes = {'username': UsernameField}

class LearnerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("is_learner","username","first_name", "last_name")
        fields_classes = {'username': UsernameField}

class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("is_teacher","username","email","first_name", "last_name")
        fields_classes = {'username': UsernameField}

class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields = (
            'user',
        )

class CreateLearnerForm(forms.ModelForm):
    class Meta:
        model= Learner
        fields = (
            'user',
            'grade',
        )