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
from food.forms import CommentForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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

@login_required
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
        'form': CommentForm()
    }
    return render(request, 'recipes/recipe_details.html', values)


def recipe_comments(request, id):
    """
    Function to retrieve comments for certain recipe.
    Returns comments in rendered HTML.
    """
    comments = Comment.objects.filter(recipe_id=id).order_by('-date')
    values = {
        'comments': comments,
        'user': request.user
    }
    content = loader.render_to_string('recipes/comments.html', values)
    return HttpResponse(content)


@login_required
def add_comment(request):
    """
    Function to add comment to certain recipe.
    """
    user = request.user
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.save()
    return HttpResponse(200)


@login_required
def edit_comment(request, id):
    """
    Function to edit comment to certain recipe.
    """
    user = request.user
    try:
        comment = Comment.objects.get(id=id)
    except ObjectDoesNotExist:
        comment = None
    if not comment or comment.user != user:
        return HttpResponse(403)
    else:
        comment.body = request.POST.get('body')
        comment.save()
    return HttpResponse(200)


@login_required
def delete_comment(request, id):
    """
    Function to delete comment from certain recipe.
    """
    user = request.user
    try:
        comment = Comment.objects.get(id=id)
    except ObjectDoesNotExist:
        comment = None
    if not comment or comment.user != user:
        return HttpResponse(403)
    else:
        comment.delete()
    return HttpResponse(200)
