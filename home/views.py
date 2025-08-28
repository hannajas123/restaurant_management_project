from django.shortcuts import render
from django.conf import settings
# Create your views here.

def homepage(request):
    context= (settings, "RESTAURANT_NAME","My Restaurant","phone_number": settings.RESTAURANT_PHONE)
    return render(request,"homepage.html",{'restaurant_name':restaurant_name},context)