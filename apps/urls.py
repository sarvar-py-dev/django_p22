from django.urls import path

from apps.views import index_view

urlpatterns = [
    path('users/', index_view, name='index'),
]
