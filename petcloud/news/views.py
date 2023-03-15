from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from news.forms import PostNewsForm
from news.models import Post
from registr.models import Profile


@login_required
def news_add(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)

    error = ''
    if request.method == 'POST':
        form = PostNewsForm(request.POST, profile=profile)
        if form.is_valid():
            form.save()
            return render(request, 'news/news_form.html')
        else:
            error = form.errors
            return render(request, 'news/news_form.html', {'error': error, 'form': form})
    else:
        form = PostNewsForm()
        return render(request, 'news/news_form.html', {'error': error, 'form': form})

    # post = Post(profile=profile, title=title, description=description)
    # post.save()
    # if form.is_valid()
    #     return render(request, 'news_form.html', {'forms': forms})


