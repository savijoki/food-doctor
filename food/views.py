#!/usr/bin/env python

"""
Views for the application food are declared here.
"""
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.template import loader, RequestContext
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from config.settings import API_KEY
from food.models import Comment, Recipe
from food.forms import CommentForm


def index(request):
    """
    Function to render the index page of application.
    """
    return render(request, 'index.html')


def recipes(request):
    """
    Function to search for recipes from Foods API.
    """
    search = request.GET.get('search')

    if search:
        url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/search"
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
            'results': results
        }
        return JsonResponse(response)

    values = {
        'navbar': 'recipes'
    }
    return render(request, 'recipes/show_recipes.html', values)

@login_required
def recipe_details(request, recipe_id):
    """
    Function to render recipe in more detail and comments
    related to the recipe from application's users.
    """
    url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/%s/information" % (recipe_id)
    headers = {
        "X-Mashape-Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        'includeNutrition': True
    }
    res = requests.get(url, params=params, headers=headers)
    results = res.json() if res.status_code == 200 else []
    comments = Comment.objects.filter(recipe_id=recipe_id).order_by('-date')
    favourites = Recipe.objects.filter(user=request.user, recipe_id=recipe_id)
    values = {
        'recipe': results,
        'comments': comments,
        'form': CommentForm(),
        'navbar': 'recipes',
        'favourite': favourites
    }
    return render(request, 'recipes/recipe_details.html', values)


def recipe_comments(request, recipe_id):
    """
    Function to retrieve comments for certain recipe.
    Returns comments in rendered HTML.
    This function is used via AJAX.
    """
    comments = Comment.objects.filter(recipe_id=recipe_id).order_by('-date')
    values = {
        'comments': comments,
        'user': request.user,
        'navbar': 'recipes'
    }
    content = loader.render_to_string('recipes/comments.html', values)
    return HttpResponse(content)


@login_required
def add_comment(request):
    """
    Function to add comment to certain recipe.
    This function is used via AJAX.
    """
    user = request.user
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.save()
    return HttpResponse(200)


@login_required
def edit_comment(request, comment_id):
    """
    Function to edit comment to certain recipe.
    This function is used via AJAX.
    """
    user = request.user
    try:
        comment = Comment.objects.get(id=comment_id)
    except ObjectDoesNotExist:
        comment = None
    if not comment or comment.user != user:
        return HttpResponse(403)
    else:
        comment.body = request.POST.get('body')
        comment.save()
    return HttpResponse(200)


@login_required
def delete_comment(request, comment_id):
    """
    Function to delete comment from certain recipe.
    This function is used via AJAX.
    """
    user = request.user
    try:
        comment = Comment.objects.get(id=comment_id)
    except ObjectDoesNotExist:
        comment = None
    if not comment or comment.user != user:
        return HttpResponse(403)
    else:
        comment.delete()
    return HttpResponse(200)


@login_required
def favourites(request):
    """
    Function to show users favourite recipes.
    """
    user = request.user
    try:
        recipes = Recipe.objects.filter(user=user)
    except ObjectDoesNotExist:
        recipes = None
    values = {
        'recipes': recipes,
        'user': user,
        'navbar': 'favourites'
    }
    return render(request, 'recipes/favourites.html', values)


@login_required
def favourites_add(request):
    """
    Function to add recipe to favourites.
    This function is used via AJAX.
    """
    user = request.user
    title = request.POST.get('title')
    recipe_id = request.POST.get('recipe_id')
    image_url = request.POST.get('image_url')
    favourite, created = Recipe.objects.get_or_create(
        title=title,
        recipe_id=recipe_id,
        image_url=image_url,
        user=user
    )
    if created:
        return HttpResponse(201)
    return HttpResponse(200)


@login_required
def favourites_remove(request, recipe_id):
    """
    Function to remove recipe from favourites.
    This function is used via AJAX.
    """
    recipe = Recipe.objects.filter(
        recipe_id=recipe_id,
        user=request.user
    )
    if recipe:
        recipe.delete()
        return HttpResponse(200)
    return HttpResponse(404)