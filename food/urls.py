#!/usr/bin/env python

"""
URL Configuration for food application
"""

from django.conf.urls import url
from food import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
]