import datetime
from peewee import *

db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db

class Recipe(BaseModel):
    title = CharField(unique=True)
    smallTitle = CharField()
    description = DecimalField()
    shortDescription = DateTimeField()
    portion = DecimalField()
    complexity_rate =  DecimalField()
    price = DecimalField()
    photo = CharField()
    ingredientsPhoto = CharField()
    ingredients = CharField()
    nutrients = CharField()
    publication_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

    class Meta:
        indexes = (
            # create a unique on fields below
            (('title','portion','complexity_rate','price', 'publication_date'), True),
        )

class Ingredient(BaseModel):
    recipe = ForeignKeyField(Recipe, related_name='recipe_ingredients')
    type = TextField(unique=True)
    quantity = DecimalField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexes = (
            # create a unique on Ingredient type
            (('type'), True),
        )

class Nutrient(BaseModel):
    recipe = ForeignKeyField(Recipe, related_name='recipe_nutrients')
    type = TextField()
    quantity = DecimalField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexes = (
            # create a unique on Nutrient type
            (('type'), True),
        )