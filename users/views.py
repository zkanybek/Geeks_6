from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, f'Account "{user.username}" has been successfully registered! You can now log in.')
                return redirect('login_view')
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
                return render(request, 'users/register.html', context={'form': form})
        else:
            messages.error(request, 'Form is not valid. Please check the errors below.')
            return render(request, 'users/register.html', context={'form': form})
    else: # Handles GET requests
        form = RegisterForm()
        return render(request, 'users/register.html', context={'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home_view') # <-- Redirect to your homepage URL name
            else:
                form.add_error(None, 'Invalid username or password') 
                return render(request, 'users/login.html', context={'form': form})
        else: # If the form is POST but invalid
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'users/login.html', context={'form': form})
    else: # Handles GET requests
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home_view') # Redirect the user to the homepage after logging out

@login_required
def posts_list_view(request):
    ...

@login_required
def post_detail_view(request, post_id):
    ...

@login_required
def post_create_view(request):
    ...