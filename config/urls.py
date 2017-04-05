#!/usr/bin/env python

"""
Base URL Configuration for the food-doctor project
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from config import views
from food.urls import urlpatterns as food_urls

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'', include(food_urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
