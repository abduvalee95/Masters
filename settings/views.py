from django.shortcuts import render
from django.contrib.auth.decorators import login_required #"это отправляет ползоватля регистрацию "
from anketa.models import Info


# Create your views here.
# @login_required(login_url='login')# ,'без регистрация неможет войти отправляет войти чтобы ползоватса'
def home(request):
    home = Info.objects.all()

    context = { 
        'home' : home
    }
    return render(request, 'main.html' )
