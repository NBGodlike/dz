from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    Name = models.TextField(max_length=255, null=True)
    Duration = models.TextField(max_length=255, null=True)
    Teacher = models.TextField(max_length=255, null=True)
    Value = models.TextField(max_length=255, null=True)
    Picture = models.ImageField(upload_to='css2/', null=True)


class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False, default='login')
    password = models.CharField(max_length=255, null=False, default='12345')
    Phone_number = models.CharField(max_length=255, null=True)
    courses = models.ManyToManyField(Course, related_name='users')


class Useri(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False, default='login')
    password = models.CharField(max_length=255, null=False, default='12345')
    Phone_number = models.CharField(max_length=255, null=True)
    courses = models.ManyToManyField(Course, related_name='toi')


class Comment(models.Model):
    Course = models.TextField(max_length=255, null=False)
    Text = models.TextField(max_length=255, null=False)


class Sub(models.Model):
    id_user = models.IntegerField()
    id_course = models.IntegerField()


