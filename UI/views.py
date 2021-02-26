from django.shortcuts import render
from django.http import HttpResponse
from .models import cl1 

# Create your views here.

def index(request):
     d=cl1.objects.all()   

     return render(request,'index.html',{'d':d})
