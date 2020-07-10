from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth.models import AbstractUser


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length = 200)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subjects = models.ManyToManyField(Category, related_name = "potential_tutors")


class Request(models.Model):
    subject = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.CharField(max_length = 200, default="")
    grade_level = IntegerRangeField(min_value=1, max_value=12)
    dt = models.DateTimeField("DateTime Published", default=datetime.now)
    content = models.TextField()

    def __str__(self):
        return self.subject
