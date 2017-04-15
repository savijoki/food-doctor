from django.contrib import admin
from food.models import Recipe, Comment

class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'recipe_id', 'date'
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
