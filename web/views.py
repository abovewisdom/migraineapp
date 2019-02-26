from web.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
#from helpers import apology - needs to be created

# Create your views here.
def index(request):
   return render(request, 'index.html')

def entry(request):
   return render(request, 'entry.html')
# Change below to handle post requests
def posts(request):
   return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.username, password=form.password)
            if user is not None:
                login(request, user)
            else:
                return render(request,'index.html')# need to add an error message here
            #messages.success(request, 'Account created successfully')
            return render(request, 'index.html') 
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': RegisterForm})

def login(request):
   return render(request, 'login.html')
