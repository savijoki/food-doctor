#!/usr/bin/env python

"""
Generic views such as authentication views are declared here.
"""


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from food.forms import RegistrationForm
from django.shortcuts import redirect, render

def logout_successful(request):
    """
    Function to handle logout
    """

    return render(request, 'auth/logout.html')


def registration(request):
    """
    Function to handle registration
    """
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})