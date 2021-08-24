from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("betfred/", views.betfred, name="betfred"),
path("betvictor/", views.betvictor, name="betvictor"),
path("cowboysbetting/", views.cowboys, name="cowboys"),
path("nflbetting/", views.nflbetting, name="nflbetting"),
path("casinooffers/", views.casinooffers, name="casinooffers")
]