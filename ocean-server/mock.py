import datetime
from models import *
from peewee import *


recipe = Recipes.create(
        title = 'sdfsdf',
        smallTitle = 'sdfsdf',
        description = 'sdfsdf',
        shortDescription = 'sdfsdf',
        portion = 1,
        complexity_rate =  1,
        price = 1,
        photo = 'sdfsdf',
        ingredientsPhoto = 'sdfsdf',
        ingredients = 'sdfsdf',
        main_ingredient = 'sdfsdf',
        nutrients_fat = 1,
        nutrients_carbohydrates = 1,
        nutrients_proteins = 1,
        nutrients_calories = 1,
        publication_date = datetime.datetime.now(),
        is_published =True
        )

recipe2 = Recipes.create(
        title = 'sdfsdsdfsdfsdf',
        smallTitle = 'sdfsdsdfsdfsdf',
        description = 'sdfsdsdfsdfsdf',
        shortDescription = 'sdfsdsdfsdfsdf',
        portion = 1,
        complexity_rate =  1,
        price = 1,
        photo = 'sdfsdf',
        ingredientsPhoto = 'sdfsdf',
        ingredients = 'sdfsdf',
        main_ingredient = 'sdfsdf',
        nutrients_fat = 1,
        nutrients_carbohydrates = 1,
        nutrients_proteins = 1,
        nutrients_calories = 1,
        publication_date = datetime.datetime.now(),
        is_published =True
        )
recipe.save()
recipe2.save()