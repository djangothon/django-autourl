from django.shortcuts import render
from .models import logs,urls
import json
# Create your views here.
def home(request):
	log= urls.objects.all() 	
	
	return render(request,"ubuild/home.html",{
		"log":log,
		"top_url1":log[0].httpRefer,
		"top_url2":log[1].httpRefer,
		"top_url3":log[2].httpRefer,
		"top_url4":log[3].httpRefer,
		"top_url5":log[4].httpRefer,	
		"count1":log[0].count,
		"count2":log[1].count,
		"count3":log[2].count,
		"count4":log[3].count,
		"count5":log[4].count
		})

def details(request,url):
	url= url[1:]+"/"
	log= logs.objects.filter(httpRefer=url)
	return render(request,"ubuild/details.html",{
		"logs":log
		})


