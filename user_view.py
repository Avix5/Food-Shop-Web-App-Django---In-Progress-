from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm this is an user form which is provided by django so we dont need to create
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method=="POST":
        Form=RegisterForm(request.POST)
        if Form.is_valid():
            Form.save()
            username=Form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},your account has been succefully created')
            return redirect('login')

    Form=RegisterForm()
    return render(request,'user/register.html',{'form':Form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    return render(request,'user/profile.html')
   
