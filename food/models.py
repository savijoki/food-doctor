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


class MealPlan(models.Model):
    """
    A collection of recipes. The amount of recipes
    is defined by period.
    """

    DAY = 1
    WEEK = 7
    PERIOD_CHOICES = (
        (DAY, 'Day'),
        (WEEK, 'Week'),
    )
    period = models.CharField(
        "Meal plan's period",
        max_length=4,
        choices=PERIOD_CHOICES,
        default=DAY,
    )
    recipes = models.ManyToManyField(
        Recipe,
    )


class Comment(models.Model):
    """
    Users' comments on recipes.
    """

    recipe_id = models.PositiveIntegerField(
        "Related recipe's id",
    )
    comment = models.TextField(
        "Comment",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
