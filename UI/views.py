from django.shortcuts import render
from django.http import HttpResponse
from .models import cl1 

# Create your views here.

def index(request):
     c1=cl1()
     c1.name='titanic hero'
     c1.desc='sell me this pen'
     c1.img='11.jpg'
     c1.sel=True

     c2=cl1()
     c2.name='iron man'
     c2.desc='i am iron man'
     c2.img='12.jpeg'
     c2.sel=True

     c3=cl1()
     c3.name='batman'
     c3.desc='i am vengence'
     c3.img='13.jpeg'
     c3.sel=True

     c4=cl1()
     c4.name='batman'
     c4.desc='i am vengence'
     c4.img='13.jpeg'
     c4.sel=False
 

     d=[c1,c2,c3,c4]   

     return render(request,'index.html',{'d':d})
