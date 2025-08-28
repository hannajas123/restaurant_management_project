from django.urls import path
from .views import *

urlpatterns = [
    path('',views.homepage, name='home'),
    path('menu/',views.menu, name='menu'),
    path('contact/',views.contact,name='contact'),
    
]