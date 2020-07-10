from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Request, User
from .forms import HelpForm, RealUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from django.contrib import messages
# Create your views here.

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('/home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def homepage(request):
    return render(request=request, template_name="main/home.html", context={'requests': Request.objects.all})
    #return HttpResponse("aba")

def community(request):
    return render(request=request, template_name="main/community.html", context={'requests': Request.objects.all})

def helpform(request):
    if request.method == "POST":
        form = HelpForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                helpcard = form.save(commit=False)
                helpcard.dt = datetime.now()
                helpcard.author = request.user
                helpcard.save()
                return redirect("/home")
            else:
                messages.error(request, f"Please login to submit!")
        else:
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, '{}: {}'.format(field, item))
            return render(request=request, template_name="main/helpform.html", context = {"form": form})

    form = HelpForm()
    return render(request=request, template_name="main/helpform.html", context = {"form": form})

def register(request):
    if request.method == "POST":
        form = RealUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login(request,user)
            messages.success(request, f"Logged in as {username}!")
            return redirect("/home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = RealUserCreationForm
    return render(request=request, template_name="main/register.html", context={'form': form})
