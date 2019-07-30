from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import newForm 

def home(request): 
    return render(request, 'base.html') 

def new_profile(request):
    context = {}
    return HttpResponse(render(request, 'profiles/new.html', context))

def get_form(request): 
    if request.method == 'POST': 
        form = newForm(request.POST) 
        if form.is_valid(): 
            return HttpResponseRedirect('home')
    else: 
        form = newForm() 
    
    context = {'form': form }
    
    return render(request, 'profiles/new.html', context)
   