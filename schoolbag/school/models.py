from unicodedata import name
from xml.parsers.expat import model
from django.db import models


class Grade(models.Model):
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"Grade: {self.grade}"
   

   
