
import os
import datetime
from peewee import *

db_proxy = Proxy()


class Recipes(Model):
    title = CharField(unique=True)
    smallTitle = CharField()
    description = CharField()
    shortDescription = CharField()
    portion = DecimalField()
    complexity_rate =  DecimalField()
    price = DecimalField()
    photo = CharField()
    ingredientsPhoto = CharField()
    ingredients = CharField()
    main_ingredient = CharField()
    nutrients_fat = DecimalField()
    nutrients_carbohydrates = DecimalField()
    nutrients_proteins = DecimalField()
    nutrients_calories = DecimalField()
    publication_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

    class Meta:
        database = db_proxy
        indexes = (
            # create a unique on fields below
            (('title',), True),
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
            (('type',), True),
        )

if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('persons.db')
    db_proxy.initialize(db)

if __name__ == '__main__':
    db_proxy.connect()
    db_proxy.create_table(Recipes, safe=True)