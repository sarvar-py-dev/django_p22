from django.shortcuts import render

from apps.models import Field, Job, Country, City, Company, User


def index_view(request):
    context = {
        'user_': User.objects.all()
    }
    return render(request, 'apps/index.html', context)
