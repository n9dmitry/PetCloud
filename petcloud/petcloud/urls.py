from django.contrib import admin
from django.urls import path, include
from news.views import *
from registr.views import *
from oblako.views import *
from django.conf.urls.static import static
from registr.views import SignUp
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oblako/', include('oblako.urls')),
    path('registr/', SignUp.as_view(), name = 'signup'),
    #path('editprofile/', editprofile, name='editprofile'),
    path('news_form/', news_add),
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile_view'),
    path('', index)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)