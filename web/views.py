from web.forms import RegisterForm, LoginForm, MigrainesForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from web.models import Migraines
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
#from helpers import apology - needs to be created right

# Create your views here.
class MigraineListTable(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super(MigraineListTable, self).get_context_data(**kwargs)
        ctx['header'] = ['user','id', 'Migraine Stage','Medicine Taken', 'Migraine Start Time']
        ctx['rows'] = Migraines.objects.filter(user_id = self.request.user.id)
            
        return ctx
    
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    #Get Dashboard data(needs to be updated to get card data)
    def get_context_data(self, **kwargs):
        ctx = super(MigraineListTable, self).get_context_data(**kwargs)
        ctx['header'] = ['user','id', 'Migraine Stage','Medicine Taken', 'Migraine Start Time']
        ctx['rows'] = Migraines.objects.filter(user_id = self.request.user.id)

    return redirect(request, 'dashboard.html')

def tour(request):
    return render(request, 'tour.html')

def whytrack(request):
    return render(request, 'why-track.html')

def entry(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MigrainesForm(request.POST, user=request.user)
            if form.is_valid():
                #finalform is needed to add user before saving, the false commit is used to do this
                finalform = form.save(commit=False)
                finalform.user = request.user
                finalform.save()
                #form.save()
                return render(request, 'dashboard.html') 
            #messages.success(request, 'Migraine Logged Successfully')
            else:
                message = "The form has errors"
                explanation = form.errors.as_data()
                status_code = 400
                raise Http404("Fields not valid.")
        else:
            if request.user.is_authenticated:
                return render(request, 'entry.html', {'form': MigrainesForm})
    else:
        raise Http404("You must be logged in to use this form")

def register(request):
    if request.method == 'POST':
        prequest = request.POST
        form = RegisterForm(request.POST)
        #don't have validation if someone tries to use a username that has already been used.
        if form.is_valid():
            form.save()
            user = authenticate(request, username=prequest['username'], password=prequest['password1'])
            if user is not None:
                login(request, user)
                return render(request, 'index.html') 
            else:
                raise Http404("User is not logged in.")
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
                #return redirect('dashboard')
                return HttpResponseRedirect('dashboard.html')
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
