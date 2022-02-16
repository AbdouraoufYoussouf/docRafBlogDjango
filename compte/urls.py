from django.urls import path
from . import views

urlpatterns = [
    path('login', views.logine,name='login'),
    path('', views.register,name='register'),
]
