from django.contrib import admin

from apps.models import User, Field, Job, Country, City, Company


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    pass
