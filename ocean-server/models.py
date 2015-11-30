import os
import datetime
from peewee import *
import json

db_proxy = Proxy()


class Recipes(Model):
    title = CharField(unique=True)
    description = CharField()
    cooking_description = CharField()
    price = DecimalField()
    photo = CharField()
    ingredientsPhoto = CharField()
    ingredients = CharField()
    nutrients_fat = DecimalField()
    nutrients_carbohydrates = DecimalField()
    nutrients_proteins = DecimalField()
    nutrients_calories = DecimalField()
    publication_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


    def __str__(self):
        r = {}
        for k in self._data.keys():
         try:
           r[k] = str(getattr(self, k))
         except:
           r[k] = json.dumps(getattr(self, k))
        return str(r)

    class Meta:
        database = db_proxy
        indexes = (
            # create a unique on fields below
            (('title','main_ingredient','complexity_rate','publication_date',), True),
        )

class Orders(Model):
    type = TextField(unique=True)
    quantity = DecimalField()
    order_details = TextField()
    status = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_proxy
        indexes = (
            # create a unique on Ingredient type
            (('type','status',), True),
        )

if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('ocean04-dev.db')
    db_proxy.initialize(db)

if __name__ == '__main__':
    db_proxy.connect()
    db_proxy.create_table(Recipes , safe=True)
    db_proxy.create_table(Orders , safe=True)
    recipe = Recipes.create(
        title = 'sdfsdf',
        description = 'sdfsdf',
        cooking_description = 'sdfsdf',
        price = 1,
        photo = 'sdfsdf',
        ingredientsPhoto = 'sdfsdf',
        ingredients = 'sdfsdf',
        nutrients_fat = 1,
        nutrients_carbohydrates = 1,
        nutrients_proteins = 1,
        nutrients_calories = 1,
        publication_date = datetime.datetime.now(),
        is_published =True
        )

    print(str(recipe))
    recipe.save()


