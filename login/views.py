from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'login/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned.data.get('username')
            messages.success(request, f'{username}, your account has been created successfully')
        return render(request, 'login/home.html', {'form':form})
        
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'login/profile.html')


def login(request):
    return render(request, 'login/login.html')
