from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm # allows 'login' click to load page
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Skill

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: # added this to get rid of error page when SIGNUP info doesn't meet requirements
            return redirect('/signup/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def skills_index(request): # matches URL.PY path
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', {'skills': skills}) # NOW we will make NEW DIRECTORY (skills) in TEMPLATE
            # THEN inside "skills directory" make index.html

def skills_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    return render(request, 'skills/detail.html', {
        'skill': skill
    })