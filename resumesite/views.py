from django.shortcuts import render
from django.views.generic.base import View
from .models import *


# Create your views here.
#def home(request):
#	return render(request,'home.html', {})



class HomeView(View):
	def get(self, request):
		name = Name.objects.all()
		about = About.objects.all()
		cv = Resume.objects.all()
		summary = Summary.objects.all()
		edu = Education.objects.all()
		skills = Skills.objects.all()
		experience = Experience.objects.all()
		context = {
			 'cv': cv,
			 'about':about,
			 'name': name,
			 'summary':summary,
			 'edu':edu,
			 'skills':skills,
			 'experience':experience,
		 }
		return render(request, 'home.html', context)
