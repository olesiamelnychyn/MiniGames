from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.hangman),
    path('game', views.game),
]