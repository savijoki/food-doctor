#!/usr/bin/env python

"""
Views for the application food are declared here.
"""

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')