
from django.urls import path

from . import views



urlpatterns = [
    path('', views.landing),
    path('login/', views.login),
]
