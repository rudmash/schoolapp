from pyexpat import model
from tkinter import CASCADE

from django.db import models
from django.contrib.auth.models import  AbstractUser

from school.models import Grade

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.user.username

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self) :
        return self.user.username

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject",on_delete=models.CASCADE)
    learner = models.ManyToManyField(Learner, blank=True)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.name}    Grade: {self.grade.grade}"