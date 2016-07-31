# recipe_obj = {  # "id": recipe.id,
#     "subtitle" : recipe.subtitle,
#     "title" : recipe.title,
#     "tag" : recipe.tag,
#     "vine": recipe.vine,
#     "description" : recipe.description,
#     "price" : float(recipe.price),
#     "size": float(recipe.size),
#     "photo" : recipe.photo,
#     "ingredients_photo": recipe.ingredients_photo,
#     "diet": recipe.diet_type.split("|"),
#     "ingredients" : recipe.ingredients,
#     "nutrients" : recipe.nutrients
# }
from ocean_server.domain.object import Object


class Recipe(Object):
    def __init__(self, id, subtitle, tag, vine, description, price, size, photo, ingredients_photo, diet, ingredients,
                 nutrients):
        self.id = id
        self.subtitle = subtitle
        self.tag = tag
        self.vine = vine
        self.description = description
        self.price = price
        self.size = size
        self.photo = photo
        self.ingredients_photo = ingredients_photo
        self.diet = diet
        self.ingredients = ingredients
        self.nutrients = nutrients
