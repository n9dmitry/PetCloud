from django.shortcuts import render

from django.shortcuts import render
from .forms import FilesForm
from django.http import HttpResponseRedirect


def filesadd(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = FilesForm()

    return render(request, "oblako/oblako.html", {
        "form": form
    })