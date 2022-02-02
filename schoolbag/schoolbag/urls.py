from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView, LandingView
from users.views import ( 
    RegisterView,
    LearnerCreateView,
    TeacherCreateView
)
from school.views import (
    LearnerSubjectView, 
    LearnerSubjectDetailView, 
    AdminTeachersView,
    AdminLearnersView )
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('landing', LandingView.as_view(), name ='home'),
    path('/users/', include('users.urls', namespace='users')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # school urls
    #learner urls
    path('learner-subject-list/', LearnerSubjectView.as_view(), name='learner-subjects'),
    path('<int:pk>/', LearnerSubjectDetailView.as_view(), name='learner-detail-subject'),
    #admin urls
    #teacher
    path('admin-teachers-list/', AdminTeachersView.as_view(), name='admin-teachers-list'),
    path('create-teacher/', TeacherCreateView.as_view(), name='create-teacher'),
    #leaner
    path('admin-learners_list/', AdminLearnersView.as_view(), name='admin-learners-list'),
    path('create-learner/', LearnerCreateView.as_view(), name='create-learner')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
