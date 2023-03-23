from django.shortcuts import render
from registr.models import Profile


def HomePageView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=request.user.id)
            return render(request, 'petcloud/home_page.html', {"profile":profile})
        else:
            return render(request, 'petcloud/home_page.html')
            