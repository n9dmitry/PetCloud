from django.contrib import admin
from django.urls import path
from news.views import *
from registr.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registr/', registr),
    path('editprofile/', editprofile, name='editprofile'),
    path('news_form/', news_add),
]
