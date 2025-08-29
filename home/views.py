from django.shortcuts import render
from django.conf import settings
# Create your views here.

def homepage(request):
    try:
        context= (settings, "RESTAURANT_NAME","My Restaurant","phone_number": settings.RESTAURANT_PHONE)
        return render(request,"homepage.html",{'restaurant_name':restaurant_name},context)

    except ValueError as ve:
        return HttpResponse(f"<h2>Error : {ve}</h2>",  status=404)    
    except Execption as e: 
        return HttpResponse("<h2>Something went wrong.Please try again later </h2>", status=500)    