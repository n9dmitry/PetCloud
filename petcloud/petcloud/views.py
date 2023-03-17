from django.shortcuts import render

def HomePageView(request):
    if request.method == 'GET':
        return render(request, 'petcloud/home_page.html')