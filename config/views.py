#!/usr/bin/env python

"""
Generic views such as authentication views are declared here.
"""


from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from food.forms import RegistrationForm
from django.shortcuts import redirect, render


class Register(TemplateView):
    """
    Registration form handling
    """
    def get(self, request, **kwargs):
        """
        Render registration form
        """
        if request.user.is_authenticated():
            return redirect('/')
        register_form = RegistrationForm()
        return render(request, 'auth/register.html', {'form': register_form})


    def post(self, request, **kwargs):
        """
        Registration form validation
        """
        if request.user.is_authenticated():
            return redirect('/')
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        return render(request, 'auth/register.html', {'form': register_form}) 
