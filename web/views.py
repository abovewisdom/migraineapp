from web.forms import RegisterForm, LoginForm, MgEntryForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render
import pdb
#from helpers import apology - needs to be created right

# Create your views here.
def index(request):
    return render(request, 'index.html')

def entry(request):
    if request.method == 'POST':
        form = MgEntryForm(request.POST)
        
    else:
        return render(request, 'entry.html', {'form': MgEntryForm})

def register(request):
    if request.method == 'POST':
        #pdb.set_trace()
        prequest = request.POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=prequest['username'], password=prequest['password1'])
            if user is not None:
                login(request, user)
                return render(request, 'index.html') 
            else:
                raise Http404("User is not logged in.")
            #messages.success(request, 'Account created successfully')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': RegisterForm})

def userlogin(request):
    logout(request)
    username = password = ''
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
        else:
            raise Http404("Username and or password not found")
    else:
        form = LoginForm()
        return render(request, 'userlogin.html', {'form': LoginForm})

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'index.html')
    else:
        raise Http404("User is not logged in so can not be logged out.")
