#!/usr/bin/python

import math

# Write a function that receives a recipe in the form of a dictionary,


def recipe_batches(recipe, ingredients):
    batches = -1
    for item in recipe:
        if item in ingredients.keys()


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
