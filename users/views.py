from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import UserCreateForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required #"это отправляет ползоватля регистрацию "

from django.contrib import messages 
# Create your views here.

def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = UserCreateForm()

        if request.method == "POST":
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Вы уже зарегистрировали войдити пожалуста' + user )

                return redirect('login')

        context = {
            'form' : form,

        }
        return render(request, 'account/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Нет такого имя ползователя или парол')

        context = {}
        return render(request, 'account/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')