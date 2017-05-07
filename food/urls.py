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
        views.recipes,
        name='recipes'
    ),
    url(
        r'^recipes/(?P<recipe_id>[0-9]+)/$',
        views.recipe_details,
        name='recipe_details'
    ),
    url(
        r'^favourites/$',
        views.favourites,
        name='favourites'
    ),
    url(
        r'^favourites/add/$',
        views.favourites_add,
        name='favourites_add'
    ),
    url(
        r'^favourites/remove/(?P<recipe_id>[0-9]+)$',
        views.favourites_remove,
        name='favourites_remove'
    ),
    url(
        r'^recipes/(?P<recipe_id>[0-9]+)/comments$',
        views.recipe_comments,
        name='recipe_comments'
    ),
    url(
        r'^comments/add$',
        views.add_comment,
        name='add_comment'
    ),
    url(
        r'^comments/edit/(?P<comment_id>[0-9]+)$',
        views.edit_comment,
        name='edit_comment'
    ),
    url(
        r'^comments/delete/(?P<comment_id>[0-9]+)$',
        views.delete_comment,
        name='delete_comment'
    ),
]
