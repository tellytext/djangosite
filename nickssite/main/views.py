from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Review, Team, Categorie
from .forms import CreateNewList
# Create your views here.

def home(response):
	return render(response, "main/home.html", {})

def casinooffers(response):
	return render(response, "main/casinooffers.html", {})

def betfred(request):
	return render(request = request, template_name='main/betfred.html', context = {"reviews":Review.objects.all})

	
def betvictor(request):
	return render(request = request, template_name='main/betvictor.html', context = {"reviews":Review.objects.all})

def cowboys(request):
	return render(request = request, template_name='main/cowboysbetting.html', context = {"teams": Team.objects.all})

def nflbetting(request):
	return render(request = request, template_name='main/nflbetting.html', context = {"categories": Categorie.objects.all})