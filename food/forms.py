#!/usr/bin/env python

"""
Forms used in the foods application are declared here.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from food.models import Comment


class RegistrationForm(UserCreationForm):
    """
    Form for user registration
    """

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'password1', 'password2'
        )
        widgets = {
            'username': forms.EmailInput(attrs={
                'data-length': User._meta.get_field('username').max_length
                }
            ),
            'first_name': forms.TextInput(attrs={
                'data-length': User._meta.get_field('first_name').max_length
                }
            ),
            'last_name': forms.TextInput(attrs={
                'data-length': User._meta.get_field('last_name').max_length
                }
            ),
        }

class CommentForm(forms.ModelForm):
    """
    Comment form used in recipes
    """
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
    recipe_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Comment
        exclude = ['user']
