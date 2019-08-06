#!/usr/bin/env python

ingredients = []

enter_more = raw_input("Do you have any specific ingredients to enter? [y|n]: ").lower()

while enter_more == "y":
    ingredients.append(raw_input("What is the ingredient? One word only please: ").lower())
    enter_more = raw_input("Do you have any more ingredients to enter? [y|n]: ").lower()

recipe_type = raw_input("What kind of recipe do you want to find (no input for anything)? ")

import requests

r = requests.get("http://www.recipepuppy.com/api/?i={}&q={}".format(
    ','.join(ingredients),
    recipe_type))

recipes = r.json()["results"]

print("Your results:")
for i in range(len(recipes)):
    recipe = recipes[i]
    print("%s: %s" % (i, recipe["title"]))
