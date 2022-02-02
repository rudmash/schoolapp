from os import name
from django.urls import path
from .views import (
    TeachersListView,
    TeacherCreateView,
    LearnersListView, 
    LearnerCreateView
)
app_name ="users"

urlpatterns = [
    path('teachers/', TeachersListView.as_view(), name='teachers-list'),
    path('learners/', LearnersListView.as_view(), name='learners-list'),
    
]
