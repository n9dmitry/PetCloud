from django.contrib import admin
from django.urls import path, include
from news.views import *
from registr.views import *
from oblako.views import *
from django.conf.urls.static import static
from registr.views import SignUp
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oblako/', include('oblako.urls')),
    path('registr/', SignUp.as_view(), name = 'signup'),
    #path('editprofile/', editprofile, name='editprofile'),
    path('news_form/', news_add),
    path('profile/', include('registr.urls')),
    path('', index),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)