# -*- coding: utf-8 -*-
import os
import datetime
from peewee import *
import json

db_proxy = Proxy()


class Recipes(Model):
    title = CharField(unique=True)
    subtitle = TextField()
    description = TextField()
    price = DecimalField()
    photo = TextField()
    ingredients_photo = TextField()
    diet_type = TextField()
    size = DecimalField(default=0)
    vine = TextField(default="None")
    tag = TextField()
    ingredients = TextField()
    nutrients = TextField()
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
            (('title',), True),
        )


class Orders(Model):
    order_details = TextField()
    name = TextField()
    address = TextField()
    total_bill = DecimalField(default=0)
    time_gap = TextField()
    status = TextField()
    phone = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_proxy


class Promocodes(Model):
    provider = TextField(default="Rocket04")
    code = TextField(default="TestPromoCode")
    isUsed = BooleanField(default=False)

    class Meta:
        database = db_proxy


if 'HEROKU' in os.environ:
    import urlparse, psycopg2

    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    db = PostgresqlDatabase(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        autocommit=True,
        autorollback=True)

    db_proxy.initialize(db)
else:
    db = SqliteDatabase('ocean04-dev.db')
    db_proxy.initialize(db)
