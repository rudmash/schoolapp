from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import  post_save
from django.shortcuts import reverse
from django.views import generic
from matplotlib.style import context
from .models import User, Teacher,AdminUser, Learner
from .forms import CreateTeacherForm, CustomUserCreationForm,LearnerCreationForm, TeacherCreationForm

#register view
class RegisterView(generic.CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

#fatches all users which are teachers CBV and passes to the html page
class TeachersListView(LoginRequiredMixin,generic.ListView):
    template_name = "users/teachers-list.html"
    queryset = Teacher.objects.all()
    context_object_name = "teachers_list"


#create a teacher CBV
class TeacherCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "users/teacher-create.html"
    form_class = TeacherCreationForm

    def get_success_url(self):
        return reverse("admin-teachers-list")

#fatches all users which are leaners CBV and passes to the html page
class LearnersListView(LoginRequiredMixin,generic.ListView):
    template_name = "users/learners-list.html"
    queryset = Learner.objects.all()
    context_object_name = "learners_list"


#create a learners CBV
class LearnerCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "users/learner-create.html"
    form_class = LearnerCreationForm

    def get_success_url(self):
        return reverse("admin-learners-list")


def post_user_created(sender, instance, created, **kwargs):
    print(instance.is_admin, created)

    if instance.is_admin and created:
        AdminUser.objects.create(user=instance)
    elif instance.is_teacher and created:
        Teacher.objects.create(user=instance)
    elif instance.is_learner and created:
        Learner.objects.create(user=instance)

post_save.connect(post_user_created, sender=User)