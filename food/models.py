from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Class for defining recipes
    """

    title = models.CharField(
        max_length=128,
    )
    recipe_id = models.PositiveIntegerField(
        "Related recipe's id",
    )
    date = models.DateTimeField(
        "Added to favourites",
        auto_now_add=True,
        blank=True,
    )


class Comment(models.Model):
    """
    Users' comments on recipes.
    """

    recipe_id = models.PositiveIntegerField(
        "Related recipe's id",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    body = models.TextField(
        "Comment",
    )
    date = models.DateTimeField(
        "Comment's date",
        auto_now_add=True,
        blank=True,
    )
