from django.shortcuts import render,redirect
from . forms import InfoForm

# Create your views here.

def form(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')



    form = InfoForm()
    

    context = {
        'form' : form,

    }
    return render(request, 'info.html', context)
