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
    status = TextField()
    phone = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_proxy

if 'HEROKU' in os.environ:
    import urlparse, psycopg2
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = PostgresqlDatabase(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port, autocommit=True, autorollback=True)
    db_proxy.initialize(db)
else:
    db = SqliteDatabase('ocean04-dev.db')
    db_proxy.initialize(db)

if __name__ == '__main__':
    db_proxy.connect()
    # db.execute_sql("SET NAMES utf8;")
    # db.execute_sql("SET CHARACTER SET utf8;")
    db_proxy.create_table(Recipes , safe=True)
    db_proxy.create_table(Orders , safe=True)

    recipe = Recipes.create(
        title = 'Творожная запеканка',
        subtitle = '2|1',
        description = 'Диетическая запеканка из творога входит в меню разноплановых диет. Это блюдо используется в спортивном питании, оно полезно людям с различными патологиями, а кроме того, идеально подходит тем, кто стремится похудеть. Приготовленная по нашему рецепту творожная запеканка не перегружает организм калориями и идеально подходит как десерт даже вечером',
        price = 121,
        tag = "десерт",
        photo = 'https://rocket04.imgix.net/tvorozhnya-sapekanka.png?s=cd83c84dcfcad32c78a14870aa20d885',
        ingredients = 'Яйцо куриное|Творог обезжиренный|Крахмал кукурузный|Сахар|Лимон|Ваниль стручковая|Мята|Дрожжи',
        nutrients= '219|17|7|22',
        )

    print(str(recipe))


    recipe2 = Recipes.create(
        title = 'Панна-Котта',
        subtitle = '2|1',
        description = 'Кажется, все самые вкусные десерты пришли к нам из прекрасной Италии! Нежная североитальянская гостья Панакота или Panna Cotta в переводе "вареный крем" по консистенции напоминает желе и дополняется различными ягодами. У нас сегодня яркая летняя клубника - "ягода любви"!',
        price = 120,
        tag = "десерт",
        photo = 'https://rocket04.imgix.net/Panna-Kota.png?s=2b7c0335e2064c7d5a13ef44ea83a48c',
        ingredients = 'Молоко 3,2% 200гр|Сливки 38%|Ваниль стручковая|Желатин листовой|Сахар|Клубника',
        nutrients= '510|10|42|24',
        )

    print(str(recipe2))


    recipe3 = Recipes.create(
        title = 'Кролик в томатно-чесночном соусе',
        subtitle = '2|1',
        description = 'Мясо кролика всегда считалось одним из лучших — оно легкое, нежное, очень вкусное и при этом питательное и полезное. В нем содержится полноценный белок, жир, минеральные вещества и витамины, количество которых значительно выше, чем в мясе свиней, кур и других животных. В этом рецепте мы будем готовить кролик в нежном томатно-чесночном соусе, что добавить немного пикантности данному блюду.',
        price = 100,
        tag = "мясо",
        photo = 'https://rocket04.imgix.net/krolik-v-tomaton-soyse.png?s=471450786fd74b65d87614842e1d50ab',
        ingredients = 'Томаты в собственном соку|Перец болгарский красный|Чеснок|Лук репчатый|Перец чили мини|Лист лавровый|Петрушка|Тимьян|Лимон|Кролик|Кинза|Фольга для запекания|Оливковое масло|Соль',
        nutrients= '644|67|35|16',
        )

    print(str(recipe3))




