#!/usr/bin/env python

"""
URL Configuration for food application
"""

from django.conf.urls import url
from food import views

urlpatterns = [
    url(
        r'^$',
        views.index,
        name='home'
    ),
    url(
        r'^recipes/$',
        views.Recipes.as_view(),
        name="recipes"
    ),
    url(
        r'^recipes/(?P<id>[0-9]+)/$',
        views.recipe_details,
        name="recipe_details"
    ),
]
