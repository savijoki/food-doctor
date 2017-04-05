#!/usr/bin/env python

"""
Views for the application food are declared here.
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from food.models import Recipe
from config.settings import API_URL, IMG_URL, API_KEY
import requests
from django.http import JsonResponse
import json

def index(request):
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
            params = {'query': search}
            res = requests.get(url, params=params, headers=headers)
            results = res.json()['results'] if res.status_code == 200 else []
            response = {
                'results': results,
                'IMG_URL': IMG_URL
            }
            # print (json.dumps(results, indent=4, sort_keys=True))
            return JsonResponse(response)

        return render(request, 'recipes/show_recipes.html')

