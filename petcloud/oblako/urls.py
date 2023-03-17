from django.urls import path
from .views import filesadd

urlpatterns = [
    path('files_add/', filesadd, name='filesadd'),
]
