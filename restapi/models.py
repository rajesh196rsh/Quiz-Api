from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.

class quiz(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.name 

class questions(models.Model): 
    name = models.CharField(max_length=60, unique=True)
    options = models.CharField(max_length=60)
    correct_option = models.CharField(max_length=60)
    quiz = models.ForeignKey(quiz,default=1, on_delete=models.DO_NOTHING)
    #quiz = models.CharField(max_length=60, default="")
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name 

