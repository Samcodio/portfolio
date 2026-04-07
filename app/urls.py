from .views import *
from django.urls import path

app_name = 'app'

urlpatterns = [
    path("", home, name='home'),
    path("error/", error, name='error')
]