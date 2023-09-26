from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required

# Decorator to ensure that only authenticated users can access the home view.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'index.html', context={'form': form, 'todos': todos})

# Login view handles both GET and POST requests for user authentication.
def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form": form1
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context=context)

# Signup view handles both GET and POST requests for user registration.
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

# Add a new TODO item view.
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'index.html', context={'form': form})

# Delete a TODO item view.
def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')

# Change the status of a TODO item view.
def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')

# Signout view for user logout.
def signout(request):
    logout(request)
    return redirect('login')
