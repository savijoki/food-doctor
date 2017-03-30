from django.db import models


class Recipe(models.Model):
    """
    Class for defining recipes
    """

    title = models.CharField(
        max_length=128,
        primary_key=True,
    )
    time = models.PositiveSmallIntegerField(
        "Cooking time in minutes",
    )
    imageURL = models.URLField(
        "URL to recipe's image",
        max_length=128
    )
    summary = models.CharField(
        "Summary of the recipe",
        max_length=256,
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
