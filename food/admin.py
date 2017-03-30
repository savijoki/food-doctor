from django.contrib import admin
from food.models import Recipe, MealPlan

class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

admin.site.register(Recipe, RecipeAdmin)