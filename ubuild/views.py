from django.shortcuts import render
from .models import logs,urls
import json
# Create your views here.
def home(request):
	log= urls.objects.all() 	
	return render(request,"ubuild/home.html",{
		"log":log
		})

def details(request,url):
	url= url[1:]+"/"
	log= logs.objects.filter(httpRefer=url)
	return render(request,"ubuild/details.html",{
		"logs":log
		})


