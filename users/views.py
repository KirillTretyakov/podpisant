from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from django.urls import reverse
from users.forms import UserrLoginForm, UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def login(request):
    if request.method == 'POST':
        form = UserrLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('table'))
    else:
        form = UserrLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
