#!/usr/bin/env python

"""
Forms used in the foods application are declared here.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    """
    Form for user registration
    """
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.EmailInput()
        }
    