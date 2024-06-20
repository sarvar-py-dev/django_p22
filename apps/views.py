# from math import ceil
#
# from django.shortcuts import render
#
# from apps.models import User
#
#
# def index_view(request):
#     users = User.objects.order_by('-join_date')
#     page = int(request.GET.get('page', 1))
#     last_page_number = -1
#     search = request.GET.get('search')
#     if search:
#         users = users.filter(position__name__icontains=search)
#     elif page:
#         page_size = 2
#         users = users[page_size * (page - 1):page_size * page]
#         last_page_number = ceil(User.objects.count() / page_size)
#
#     context = {
#         'user_': users,
#         'last_page_number': last_page_number,
#     }
#     return render(request, 'apps/index.html', context)
from django.shortcuts import render

from apps.models import Exploiter, Follower


def index_view(request, pk):
    context = {
        'exploiter': Exploiter.objects.get(pk=pk),
        'followers': Follower.objects.all()
    }
    return render(request, 'apps/index.html', context)




