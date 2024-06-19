from datetime import datetime

from colorfield.fields import ColorField
from django.db import models
from django.db.models import TextChoices


class BaseStrModel(models.Model):
    def __str__(self):
        return

    class Meta:
        pass


class Field(models.Model):
    name = models.CharField(max_length=100)
    background_color = ColorField(default='#FFFFFF')
    color = ColorField(default=background_color)


class Job(models.Model):
    name = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    class WorkingType(TextChoices):
        PART_TIME = 'part_time', 'Part Time'
        FULL_TIME = 'full_time', 'Full Time'

    image = models.ImageField(upload_to='users/')
    salary = models.FloatField(default=0)
    work_type = models.CharField(max_length=255)
    join_date = models.DateField(default=datetime.now().date())
    has_star = models.BooleanField(default=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    position = models.ForeignKey(Job, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
