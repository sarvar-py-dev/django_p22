# from colorfield.fields import ColorField
# from django.db import models
# from django.db.models import TextChoices
# from django.utils.timezone import now
#
#
# class BaseStrModel(models.Model):
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         abstract = True
#
#
# class Field(BaseStrModel):
#     name = models.CharField(max_length=100)
#     background_color = ColorField(default='#FFFFFF')
#     color = ColorField(default=background_color)
#
#
# class Job(BaseStrModel):
#     name = models.CharField(max_length=255)
#
#
# class Country(BaseStrModel):
#     name = models.CharField(max_length=255)
#
#
# class City(BaseStrModel):
#     class Meta:
#         verbose_name = 'city'
#         verbose_name_plural = 'cities'
#
#     name = models.CharField(max_length=255)
#     country = models.ForeignKey('apps.Country', on_delete=models.CASCADE)
#
#
# class Company(BaseStrModel):
#     name = models.CharField(max_length=255)
#
#
# class User(models.Model):
#     class WorkingType(TextChoices):
#         PART_TIME = 'part_time', 'Part Time'
#         FULL_TIME = 'full_time', 'Full Time'
#
#     image = models.ImageField(upload_to='users/')
#     salary = models.PositiveIntegerField(default=0)
#     work_type = models.CharField(max_length=25, choices=WorkingType.choices)
#     join_date = models.DateField(auto_now_add=True)
#     has_star = models.BooleanField(default=False)
#     city = models.ForeignKey('apps.City', on_delete=models.CASCADE)
#     position = models.ForeignKey('apps.Job', on_delete=models.CASCADE)
#     company = models.ForeignKey('apps.Company', on_delete=models.CASCADE)
#     field = models.ForeignKey('apps.Field', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.id)
#
#     @property
#     def days_ago(self):
#         return now().day - self.join_date.day
from django.db import models


class BaseStrModel(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Job(BaseStrModel):
    name = models.CharField(max_length=255)


class Follower(BaseStrModel):
    name = models.CharField(max_length=255)
    job = models.ForeignKey('apps.Job', on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    image = models.ImageField(upload_to='follower_image/')
    background_image = models.ImageField(upload_to='background-follower-image/')
    has_follower = models.BooleanField(default=False)
    following = models.ForeignKey('apps.Exploiter', on_delete=models.CASCADE)


class Exploiter(BaseStrModel):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='exploiter/')
    background_image = models.ImageField(upload_to='background-exploiter/')
