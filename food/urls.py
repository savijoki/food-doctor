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
    url(
        r'^recipes/(?P<id>[0-9]+)/comments$',
        views.recipe_comments,
        name="recipe_comments"
    ),
    url(
        r'^comments/add$',
        views.add_comment,
        name="add_comment"
    ),
    url(
        r'^comments/edit/(?P<id>[0-9]+)$',
        views.edit_comment,
        name="edit_comment"
    ),
    url(
        r'^comments/delete/(?P<id>[0-9]+)$',
        views.delete_comment,
        name="delete_comment"
    ),
]
