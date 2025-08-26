from django.shortcuts import render
from django.conf import settings
# Create your views here.

def homepage(request):
    restaurant_name= getattr(settings, "RESTAURANT_NAME","My Restaurant")
    return render(request,"homepage.html",{'restaurant_name'})