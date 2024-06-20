# from django.contrib import admin
# from django.contrib.admin import action
#
# from apps.models import User, Field, Job, Country, City, Company
#
#
# @admin.register(User)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = 'id', 'city', 'get_country'
#
#     @action(description='Country')
#     def get_country(self, obj: User):
#         return obj.city.country
#
#
# @admin.register(Field)
# class FieldModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Job)
# class JobModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Country)
# class CountryModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(City)
# class CityModelAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Company)
# class CompanyModelAdmin(admin.ModelAdmin):
#     pass
from django.contrib import admin
from django.contrib.admin import register

from apps.models import Exploiter, Follower, Job


@register(Exploiter)
class ExploiterModelAdmin(admin.ModelAdmin):
    pass


@register(Follower)
class FollowerModelAdmin(admin.ModelAdmin):
    pass


@register(Job)
class JobModelAdmin(admin.ModelAdmin):
    pass
