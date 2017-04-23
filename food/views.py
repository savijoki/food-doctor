#!/usr/bin/env python

"""
Views for the application food are declared here.
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from food.models import Comment
from config.settings import API_URL, IMG_URL, API_KEY
import requests
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.template import loader, RequestContext


def index(request):
    """
    Function to render the index page of application.
    """
    return render(request, 'index.html')


class Recipes(TemplateView):

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')

        if search:
            url = API_URL + "/recipes/search"
            headers = {
                "X-Mashape-Key": API_KEY,
                "Accept": "application/json"
            }
            params = {
                'query': search
            }
            res = requests.get(url, params=params, headers=headers)
            results = res.json()['results'] if res.status_code == 200 else []
            response = {
                'results': results,
                'IMG_URL': IMG_URL
            }
            return JsonResponse(response)

        return render(request, 'recipes/show_recipes.html')


def recipe_details(request, id):
    """
    Function to render recipe in more detail and comments
    related to the recipe from application's users.
    """
    url = API_URL + "/recipes/%s/information" % (id)
    headers = {
        "X-Mashape-Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        'includeNutrition': True
    }
    res = requests.get(url, params=params, headers=headers)
    results = res.json() if res.status_code == 200 else []
    comments = Comment.objects.filter(recipe_id=id).order_by('-date')
    values = {
        'recipe': results,
        'comments': comments,
    }
    # content = loader.render_to_string('recipes/recipe_details.html', values)
    # print (content)
    return render(request, 'recipes/recipe_details.html', values)


def recipe_comments(request, id):
    """
    Function to retrieve comments for certain recipe.
    Returns comments in rendered HTML.
    """
    comments = Comment.objects.filter(recipe_id=id).order_by('-date')
    values = {
        'comments': comments,
    }
    content = loader.render_to_string('recipes/comments.html', values)
    return HttpResponse(content)
