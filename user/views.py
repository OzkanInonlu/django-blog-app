from django.shortcuts import redirect, render, HttpResponse
from sympy import re
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def register(request):
    #form = RegisterForm(request.POST or None) "post mu get mi" daha kolay yolu
    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid(): #clean method'u çalışacak

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #auth user'dan oluşturacayık
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            
            #login edebiliriz django ile
            login(request, newUser)

            messages.success(request, "Registration is Done")

            return redirect("index") #anasayfa dönüş
 
    else: #get
        form = RegisterForm()

        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})

def loginUser(request):
    form = LoginForm(request.POST or None)

    if form.is_valid(): #clean method'u çalışacak

        username = form.cleaned_data['username'] #dict
        password = form.cleaned_data['password']

        #If the given credentials are valid, return a User object. Otherwise return None.
        User = authenticate(username = username, password = password)

        if User is None:
            messages.error(request, "Username or Password is invalid")

            return render(request, "login.html", {"form": form})

        messages.success(request, "Logged In")

        login(request, User)
        return redirect("index")

    return render(request, "login.html", {"form": form})



def logoutUser(request):
    #Remove the authenticated user's ID from the request and flush their session data.
    logout(request)

    messages.success(request, "Logged Out")
    
    return redirect("index")