#!/usr/bin/env python

"""
Forms used in the foods application are declared here.
"""

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    Form for user registration
    """

    