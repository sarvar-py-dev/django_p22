# from django.urls import path
#
# from apps.views import index_view
#
# urlpatterns = [
#     path('users/', index_view, name='index'),
# ]
from django.urls import path

from apps.views import index_view

urlpatterns = [
    path('profile/<int:pk>', index_view, name='index'),
]
