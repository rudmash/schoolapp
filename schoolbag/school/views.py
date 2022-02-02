from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from matplotlib.style import context
from .models import Grade
from users.models import Learner, Class, Subject, Teacher


# laerner
#learners subject list view cbv
class LearnerSubjectView(LoginRequiredMixin,generic.ListView):
    template_name = "school/learner/subject_list.html"
    context_object_name = "class_list"

    def get_queryset(self):
        request_user_id = self.request.user.id
        learner = Learner.objects.get(user = request_user_id)
        queryset = Class.objects.filter(grade = learner.grade)
        queryset = queryset.filter(learner__id = learner.id)
        return queryset

#learners subject detailn view
class LearnerSubjectDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "school/learner/detail_subject.html"
    context_object_name = "subject"

    def get_queryset(self):
        return Subject.objects.all()

#admin
#admin teachers list  view
class AdminTeachersView(LoginRequiredMixin,generic.ListView):
    template_name = "school/admin/teachers_list.html"
    context_object_name = "teachers_list"

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

#admin learners list  view
class AdminLearnersView(LoginRequiredMixin,generic.ListView):
    template_name = "school/admin/learners_list.html"
    context_object_name = "learners_list"

    def get_queryset(self):
        queryset = Learner.objects.all()
        return queryset