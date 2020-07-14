from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Request, Category
from .forms import HelpForm, TutorCreationForm, StudentCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from django.contrib import messages
# Create your views here.

def register_main(request):
    return render(request=request, template_name="main/register_main.html", context={})

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
    filtered_requests = []
    if request.method == "GET":
        category_key = request.GET.get('category_key')
        if category_key == None:
            return render(request=request, template_name="main/community.html", context={'requests': Request.objects.all, 'categories': Category.objects.all()})
        elif category_key == "all":
            return render(request=request, template_name="main/community.html", context={'requests': Request.objects.all, 'categories': Category.objects.all()})
        else:
            for i in range(0, len(Request.objects.all())):
                if Request.objects.all()[i].category.name == category_key:
                    filtered_requests.append(Request.objects.all()[i])
            messages.success(request, "Sorted for " + str(category_key))
            print(category_key)
            return render(request=request, template_name="main/community.html", context={'requests': filtered_requests, 'categories': Category.objects.all()})

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

def register_student(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login(request,user)
            messages.success(request, f"Successfully registered as {username}!")
            messages.success(request, f"Logged in as {username}!")
            return redirect("/home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
            return render(request = request,
                          template_name = "main/register_student.html",
                          context={"form":form})

    form = StudentCreationForm
    return render(request=request, template_name="main/register_student.html", context={'form': form})

def register_tutor(request):
    if request.method == "POST":
        form = TutorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            login(request,user)
            messages.success(request, f"Successfully registered as {username}!")
            messages.success(request, f"Logged in as {username}!")
            return redirect("/home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{form.error_messages[msg]}")
            return render(request = request,
                          template_name = "main/register_tutor.html",
                          context={"form":form})

    form = TutorCreationForm
    return render(request=request, template_name="main/register_tutor.html", context={'form': form})
