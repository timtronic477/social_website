from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): #checks if valid
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active: #checks if user account is active
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse("Disabled Account")
        else:
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
    # return HttpResponse("Hello")
    

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})