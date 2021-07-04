from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from travello.models import Destination, FacultData
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if (request.method =='POST'):
       first_name = request.POST['firstname']
       last_name = request.POST['lastname']
       username = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       if (password1 == password2):
           if (User.objects.filter(username=username).exists()):
               messages.info(request,'Username already taken')
               return redirect('register')
           elif (User.objects.filter(email=email).exists()):
               messages.info(request,'Email already taken')
               return redirect('register')
           else:
               user= User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password = password1,email=email)
               user.save();
               print(username, ' User Created')
               return request("login.html")
       else:
           messages.info(request,'Password did not match')
       return redirect('register')
    else:
        return render(request,'request.html')
    
    
def fac(request,id):
    obj = FacultData.objects.get(id=id)
    print (obj.name)
    print (obj.Designation)
    return render(request,'fac_01.html',{"object":obj})