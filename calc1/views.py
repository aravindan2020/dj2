from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request,'home.html',{'name':'seamreap'})

# GET AND POST ARE THE METHOD FROM HTTP(in the application web browser)
#get and GET

def add(request):

<<<<<<< HEAD
     val1=request.POST['num1'] 
     val2=request.POST['num2']
=======
     val1=int(request.POST['num1'])
     val2=int(request.POST['num2'])
>>>>>>> 1548960f2b70a08da2f56a4c6e8afe877aff7411
     res=val1+val2
     return render(request,'result.html',{'result':res})   
