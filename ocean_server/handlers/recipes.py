import json

from ocean_server.database.models import Recipes

from ocean_server.domain.recipe import Recipe
from ocean_server.handlers.peewee import PeeweeRequestHandler


class AllRecipesHandler(PeeweeRequestHandler):
    def get(self):
        response = []
        for r in Recipes.select():
            response.append(
                Recipe(
                    r.id,
                    r.subtitle,
                    r.tag,
                    r.vine,
                    r.description,
                    float(r.price),
                    float(r.size),
                    r.photo,
                    r.ingredients_photo,
                    r.diet_type.split("|"),
                    r.ingredients,
                    r.nutrients).convert_to_json()
                )
        self.write(response)
