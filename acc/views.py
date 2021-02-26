from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password'] 

        user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
        user.save();
        print("user profile sucess")
        return redirect('https://www.google.com/')
    else:
       return render(request,'register.html')