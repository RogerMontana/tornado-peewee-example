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
    timegap = TextField()
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

    recipe3 = Recipes.create(
    title = 'Кролик в томатно-чесночном соусе',
    subtitle = '2|50',
    description  = 'Мясо кролика всегда считалось одним из лучших — оно легкое, нежное, очень вкусное, при этом питательное и полезное. В нем содержится полноценный белок, жир, минеральные вещества и витамины, количество которых значительно выше, чем в мясе свиней, кур и других животных. В этом рецепте мы будем готовить мясо кролика в нежном томатно-чесночном соусе, что добавит немного пикантности данному блюду.',
    price = 110,
    tag = "Мясо",
    photo = 'http://rocket04.imgix.net/krolik-v-tomaton-soyse.jpg?s=34fc5eb5bf2adcd0e36852c6a8e48e51',
    ingredients = 'Томаты в собственном соку|Перец болгарский красный|Чеснок|Лук репчатый|Перец чили мини|Лист лавровый|Петрушка|Тимьян|Лимон|Кролик|Кинза|Фольга для запекания|Оливковое масло|Соль',
    nutrients= '644|67|35|16',
    )
    print(str(recipe3))
    recipe3.save()

    recipe4 = Recipes.create(
        title = 'Баранина с розмарином, цукини и мятой',
        subtitle = '2|30',
        description  = 'Баранина - невероятно нежное и полезное мясо, в довершении с приготовленными цуккини и соком из лайма, является идеальным белковым ужином для тех кто следит за своей фигурой.',
        price = 90,
        tag = "Мясо",
        photo = 'http://rocket04.imgix.net/baranina_rozmarin.jpg?s=c704f7599ccd316fd9f334d6cdb2f589',
        ingredients = 'Баранина мякоть|Тмин|Цукини|Лайм|Чеснок|Мята|Розмарин',
        nutrients= '295|20|22|5',
    )
    print(str(recipe4))
    recipe4.save()

    recipe5 = Recipes.create(
       title = 'Каша из Булгура с тыквой и яблоками',
        subtitle = '2|30',
        description  = 'Каша из Булгура является невероятно сытным и аппетитным блюдом что даст отличный старт на долгий день. Это блюдо зарядит энергией и подарит чувство насыщения на несколько часов, ведь крупа под названием “Булгур” очень богата железом, калием, витаминами, фолиевой кислотой и клетчаткой. Она оказывает благотворное влияние на работу сердечно-сосудистой системы, способствует сжиганию жиров и снижению сахара в крови. Содержащиеся в составе крупы сложные углеводы усваиваются медленно, не нанося ущерб фигуре.',
        price = 40,
        tag = "Завтраки",
        photo = 'http://rocket04.imgix.net/blugur_tikva.jpg?s=77f6134c53d48acddefcb590f4d42f66',
        ingredients = 'Булгур|Корица молотая|Сахар|Курага|Молоко|Тыква|Яблоко зеленое|Мята|Масло сливочное',
        nutrients= '556|14|19|82',
    )
    print(str(recipe5))
    recipe5.save()

    recipe6 = Recipes.create(
        title = 'Курица с Пармезаном',
        subtitle = '2|40',
        description  = 'Приготовление “parmigiana,” а именно так с итальянского переводится курица с пармезаном, очень легкое и простое. Это блюдо состоит из тонко нарезанного куриного филе, покрытым  оливковым маслом, затем покрытым томатным соусом и слегка запеченного. В нашем рецепте мы остаемся верными традициям, поэтому накрываем на стол курицу вместе с пастой. Паста из цельных сортов пшеницы очень вкусно сочетается со шпинатом и цукини с невероятным вкусом пикантного пармезана.',
        price = 80,
        tag = "Мясо",
        photo = 'http://rocket04.imgix.net/kyriza-s-parmezanom.jpg?s=09680ca6da37a4aeba2f8f542b7e170d',
        ingredients = 'Филе курицы|Спагетти|Томатная паста|Сыр Моцарелла|Чеснок|Шпинат|Лук|Цукини|Мука|Сыр Пармезан|Петрушка|Оливковое масло|Соль',
        nutrients= '700|34|38|50',
    )
    print(str(recipe6))
    recipe6.save()

    recipe7 = Recipes.create(
        title = 'Форель с Грейпфрутом и Фенхелем',
        subtitle = '2|25',
        description  = 'Если времени совсем нет, попробуйте за 25 минут приготовить на обед или ужин нежную рыбу в сочетании с рукколой, маринованным фенхелем и сочными дольками цитрусовых.',
        price = 160,
        tag = "Рыба",
        photo = 'http://rocket04.imgix.net/forel-s-graipfruit.jpg?s=5e1e8305417f92d2279b7ee744e160ec',
        ingredients = 'Паприка копченая|Форель спина|Петрушка|Руккола|Фенхель|Грейпфрут|Маслины|Оливковое масло|Соль|Перец черный молотый',
        nutrients= '533|32|37|18',
    )
    print(str(recipe7))
    recipe7.save()

    recipe8 = Recipes.create(
        title = 'Глинтвейн',
        subtitle = '6|20',
        description  = 'Название напитка глинтвейн, обратившись к немецкому языку, можно охарактеризовать как "пылающее вино". Глинтвейн действительно подают горячим, и также пламенно-согревающе он возвращает силы и бодрость, почти обжигая сложным пряным вкусом.Его рецепты более чем разнообразны, но сегодня мы предлагаем попробовать наш вариант глинтвейна.',
        price = 20,
        tag = "Напитки",
        photo = 'http://rocket04.imgix.net/glintvein.jpg?s=92e97ab8624af11048254ab3055c12aa',
        ingredients = 'Красное вино|Сахар|Мускатный Орех|Молотый имбирь|Гвоздика',
        nutrients= '766|2|0|60',
    )
    print(str(recipe8))
    recipe8.save()


    recipe9 = Recipes.create(
        title = 'Греческий Салат',
        subtitle = '2|10',
        description  = 'Главный ингредиент греческого салата — хориатики это фета, традиционный греческий же сыр из овечьего или козьего молока. По консистенции он напоминает твердый творог, а во вкусе имеет приятную ненавязчивую кислинку. В отличие от соленой и резкой брынзы, которой в этом салате часто заменяют фету остальные европейцы, он не забивает собой вкус свежих овощей, оливок и оливкового масла.',
        price = 70,
        tag = "Салаты",
        photo = 'http://rocket04.imgix.net/greek_salad.jpg?s=b5fa718ff3519a674afa6463dbd96c70',
        ingredients = 'Орегано|Сыр Фета|Помидоры Черри|Лук красный|Маслины|Огурец|Перец болгарский',
        nutrients= '558|9|50|18',
    )
    print(str(recipe9))
    recipe9.save()

    recipe10 = Recipes.create(
        title = 'Каша из Киноа с Соте из Груш',
        subtitle = '2|40',
        description  = 'Киноа невероятно полезная крупа, которая может посоревноваться с известной овсянкой. Биологическая ценность киноа делает ее идеальным блюдом для начала длинного дня. Тогда как соте из груш, сделает вкус невероятно нежным и заставит вас влюбиться в это блюдо.',
        price = 65,
        tag = "Завтраки",
        photo = 'http://rocket04.imgix.net/kinoa_grysha.jpg?s=c0fde9e14b5028e8cbc28b7a6cdbe619',
        ingredients = 'Киноа|Корица молотая|Смородина черная|Сахар тростниковый|Молоко 3,2%|Масло топленое|Мед цветочный|Груша',
        nutrients= '327|8|9|53',
        )
    print(str(recipe10))
    recipe10.save()

    recipe11 = Recipes.create(
        title = 'Куриная Лапша',
        subtitle = '2|20',
        description  = 'Куриная лапша – один из самых популярных супов. Он всегда получается очень нежным и вкусным. Это очень легкий суп, который ко всему прочему очень быстро и просто готовится. При всем этом куриная лапша - это очень питательный обед, идеальный в любых случаях будь вы на работе, или дома.',
        price = 60,
        tag = "Супы",
        photo = 'http://rocket04.imgix.net/kyrinaya-lapsha.jpg?s=5813b13c72a9aae702ecf9b036692670',
        ingredients = 'Бульон куриный|Куриное бедро|Укроп|Чеснок|Морковь|Оливковое масло|Соль|Перец черный молотый',
        nutrients= '462|56|14|28',
        )
    print(str(recipe11))
    recipe11.save()

    recipe12 = Recipes.create(
        title = 'Французский маффин с горячим шоколадом',
        subtitle = '2|20',
        description  = 'Французский маффин является гордостью французской кухни, но даже за пределами Франции, практически, в каждом уважающем себя заведении вы сможете отведать уникальную интерпретацию этого рецепта. В нашем рецепте мы попытались сохранить основы здорового питания и как бы смешно это не звучало, это так и есть. Данный рецепт подходит одинаково хорошо как для тех, кто любит что-то сладкое к чаю, так и для тех, кто старается максимально строго придерживаться правильного питания.',
        price = 70,
        tag = "Десерты",
        photo = 'http://rocket04.imgix.net/maffin-s-shokoladom.jpg?s=02ba546d99e1fa4cdd65279a040daa15',
        ingredients = 'Крахмал кукурузный|Сахар|Какао|Дрожжи|Творог обезжиренный|Яйцо|Соль',
        nutrients= '220|17|8|20',
        )
    print(str(recipe12))
    recipe12.save()

    recipe13 = Recipes.create(
        title = 'Овощные Оладьи',
        subtitle = '2|20',
        description  = 'Из самых обычных овощей можно приготовить различные изысканные блюда, да еще и менее чем за полчаса. Предлагаем рецепт очень вкусных оладьев из овощей. Отличный завтрак и перекус.',
        price = 50,
        tag = "Завтраки",
        photo = 'http://rocket04.imgix.net/ovoshnie-oladya.jpg?s=ebd3a54efb6d5095448f931ef79dadbe',
        ingredients = 'Тимьян|Яйцо куриное|Сметана|Мука пшеничная|Цукини|Картофель|Морковь|Лук зеленый',
        nutrients= '356|10|20|33',
        )
    print(str(recipe13))
    recipe13.save()

    recipe14 = Recipes.create(
        title = 'Панини с Моцареллой и баклажанами',
        subtitle = '2|40',
        description  = 'Панини - это итальянский бутерброд, который традиционно готовят на гриле или на сковородке. В этом рецепте мы сделаем панини из изысканной чиабатты, баклажана и Моцареллы на плите. Мы будем использовать тяжелую кастрюлю чтобы надавить на хлеб и придать особую, хрустящую текстуру, как на гриле. К панини мы приготовим классический томатный соус, наряду с невероятно вкусным удовольствием: салата из рукколы и карамельной сливы. При нагревании природная сахароза в сливе придаст богатый, сложный и идеально сладкий вкус с хрустящим бутербродом.',
        price = 45,
        tag = "Ризотто & Овощи",
        photo = 'http://rocket04.imgix.net/panini-s-mozarelloi.jpg?s=a42ebabd2d66f90c706b07bdb6acb4e2',
        ingredients = 'Чиабатта|Томатная паста|Сыр Моцарелла|Чеснок|Руккола|Баклажан|Базилик|Горчица|Слива|Оливковое масло|Соль',
        nutrients= '690|36|8|46',
        )
    print(str(recipe14))
    recipe14.save()

    recipe15 = Recipes.create(
        title = 'Творожная запеканка',
        subtitle = '2|50',
        description  = 'Диетическая запеканка из творога входит в меню разноплановых диет. Это блюдо используется в спортивном питании, оно полезно людям с различными патологиями, а кроме того, идеально подходит тем, кто стремится похудеть. Приготовленная по нашему рецепту творожная запеканка не перегружает организм калориями и идеально подходит как десерт даже вечером.',
        price = 60,
        tag = "Десерты",
        photo = 'http://rocket04.imgix.net/tvorozhnya-sapekanka.jpg?s=978819c51af9f767e4fc43baf2251f08',
        ingredients = 'Яйцо куриное|Творог обезжиренный|Крахмал кукурузный|Сахар|Лимон|Ваниль стручковая|Мята|Дрожжи',
        nutrients= '219|17|7|22',
        )
    print(str(recipe15))
    recipe15.save()

    recipe16 = Recipes.create(
        title = 'Панна-Котта',
        subtitle = '2|50',
        description  = 'Кажется, все самые вкусные десерты пришли к нам из прекрасной Италии! Нежная северо итальянская гостья Панакота или Panna Cotta в переводе "вареный крем" по консистенции напоминает желе и дополняется различными ягодами. У нас сегодня яркая летняя клубника - "ягода любви"!',
        price = 70,
        tag = "Десерты",
        photo = 'http://rocket04.imgix.net/Panna-Kota.jpg?s=9696d4e8577617e0ab366e07a4425da7',
        ingredients = 'Молоко 3,2%|Сливки 38%|Ваниль стручковая|Желатин листовой|Сахар|Клубника',
        nutrients= '510|10|42|24',
        )
    print(str(recipe16))
    recipe16.save()

    recipe17 = Recipes.create(
        title = 'Пицца с красным луком и брокколи',
        subtitle = '2|35',
        description  = 'В этом рецепте, мы приготовим идеальное блюдо для холодных вечеров - пиццу. Всегда свежий брокколи в сочетании с Пармезаном передает очень тонкий и насыщенный вкус. Пока пицца выпекается в духовке, сыры Пармезан и Моцарелла покрываются тонкой хрустящей корочкой, добавляя немного сладкого привкуса вместе с красным луком, акцентирующим внимание на Моцарелле. После того, как пицца выйдет из печи, можно посыпать еще немного свежего Пармезана.  По желанию можно взбрызнуть лимонным соком на еще горячую пиццу. Салат из рукколы, нарезанного миндаля и красного лука отлично сочетается вместе с пиццей в этот вечер.',
        price = 90,
        tag = "Ризотто & Овощи",
        photo = 'http://rocket04.imgix.net/Pizza-Broccoli.jpg?s=9efa965415fda00dc2295ddf5eedf194',
        ingredients = 'Тесто для пиццы|Сыр Моцарелла|Томатная паста|Руккола|Чеснок|Лимон|Брокколи|Порезанный Миндаль|Сахар|Сыр Пармезан|Оливковое масло|Соль',
        nutrients= '720|30|36|70',
        )
    print(str(recipe17))
    recipe17.save()

    recipe18 = Recipes.create(
        title = 'Ризотто из Ячменя с Буряком',
        subtitle = '2|30',
        description  = 'Для этого невероятно вкусного ризотто, мы будем использовать брынзу для идеального сочетания с одним из наших любимых овощей - буряка. Помните, кулинарные шефы, комбинация из брынзы и буряка это не просто эстетическое удовольствие, но это и идеальное сочетание сладкого и терпкого вкусов. Во время приготовления буряк отдает свой цвет и вкус ячменю что в сочетании с салатом и луком делает данное блюдо незабываемым.',
        price = 40,
        tag = "Ризотто & Овощи",
        photo = 'http://rocket04.imgix.net/Rizotto-s-byryakom.jpg?s=d12ebc53c7129abb8f66d81b94f529e3',
        ingredients = 'Ячмень|Салат|Молодой лук|Чеснок|Буряк|Лимон|Лук|Сливочное масло|Брынза|Оливковое масло|Соль',
        nutrients= '600|22|12|60',
        )
    print(str(recipe18))
    recipe18.save()

    recipe19 = Recipes.create(
        title = 'Стейк с Сальса-Росса',
        subtitle = '2|30',
        description  = 'Брокколи это уникальный и полезный продукт, который отлично сосчитается с вкусным и сочным стейком. Верьте или нет, брокколи это член семьи горчицы и очень связан с репой. На итальянском, рабе брокколи звучит как “cime di rappa” что в переводе означает репа. В этом рецепте сладкая и тянучая Сальса-Росса, или соус из печеного красного перца прекрасно сбалансирует горечь брокколи, перемешавшись с ароматом хорошего стейка.',
        price = 80,
        tag = "Мясо",
        photo = 'http://rocket04.imgix.net/steak-s-salsa-rossa.jpg?s=05fa6f610ea0de7f57a6f6a5ec3d4acd',
        ingredients = 'Красный перец|Оливковое масло|Соль|Чеснок|Лук|Брокколи|Говяжий стейк|Орегано',
        nutrients= '590|80|2|5',
        )
    print(str(recipe19))
    recipe19.save()

    recipe20 = Recipes.create(
        title = 'Тальятелле с креветками и цукини',
        subtitle = '4|10',
        description  = 'О том как влияет цвет еды на наши вкусовые рецепторы известно всем. Тальятелле с креветками - это как раз яркий пример блюда, которое можно съесть уже глазами! Нежные цвета креветок, светлого цукини, алых томатов, зеленой петрушки, белого сливочного соуса и яичной лапши тальятелле дополняет изумительный аромат.',
        price = 160,
        tag = "Ризотто & Овощи",
        photo = 'http://rocket04.imgix.net/taliatelle-s-krevetkami.jpg?s=921d2ae98f9a8d4eeac65757bbeb424f',
        ingredients = 'Сливки|Креветки|Тальятелле|Помидоры черри|Петрушка|Тимьян|Сыр Пармезан|Лук|Чеснок|Цукини',
        nutrients= '988|41|58|77',
        )
    print(str(recipe20))
    recipe20.save()

    recipe21 = Recipes.create(
        title = 'Томатный суп с курицей и сельдереем',
        subtitle = '2|20',
        description  = 'Сельдереевый суп известен нам давно, но вот то, что можно его использовать для похудения, мы узнали недавно. Суп для похудения из сельдерея основывается на том, что он обладает отрицательной калорийностью. То есть чтобы переварить диетический суп из сельдерея организм затрачивает больше энергии, чем получает от из самого блюда.',
        price = 80,
        tag = "Супы",
        photo = 'http://rocket04.imgix.net/tomatniy-soup-seldereiy.jpg?s=f9471ee8a4d4e0d94cec40d1a4a5f6c6',
        ingredients = 'Бульон куриный|Кимчи|Куриная грудка|Помидоры Черри|Лук репчатый|Чеснок|Стебель сельдерея|Базилик зеленый|Лист лавровый|Соль|Перец черный молотый',
        nutrients= '316|38|23|14',
        )
    print(str(recipe21))
    recipe21.save()

    recipe22 = Recipes.create(
        title = 'Крем-суп из белых грибов с крутонами',
        subtitle = '2|30',
        description  = 'Суп - это идеально блюдо для обеда или ланча. Нежный, горчий бульон позволяют не сильно нагружать работу желудка, при этом сочетая в себе все необходимые питательные вещества. Также в нашем аутентичном рецепте, привычный вкус этого нежного и сытного супа оттеняют необычные крутоны. Порой, главный секрет кроется в мелочах!',
        price = 70,
        tag = "Супы",
        photo = 'http://rocket04.imgix.net/krem-soup-s-gribami.jpg?s=456dffc0f1856805afb04c0236a05433',
        ingredients = 'Крутоны|Масло сливочное|Сливки 33%|Шампиньоны|Лук|Корень сельдерея|Картофель|Петрушка|Грибы белые',
        nutrients= '489|8|42|20',
        )
    print(str(recipe22))
    recipe22.save()

    recipe23 = Recipes.create(
        title = 'Окунь Пикатта и свежие Феттучини',
        subtitle = '2|20',
        description  = 'Пикатта это традиционная итальянская подготовка, которая подразумевает покрытие тонкого филе мяса или рыбы в муку, затем жарку на сковородке сочетая с лимонным соусом. В этом рецепте мы делаем Окуня Пикатта, смешивая с ярким чувственным соусом, покрывая свежими феттучини и шпинатом. Розмарин и молотый красный перец добавят травяного теплого вкуса и придадут гурманской сложности данному блюду.',
        price = 130,
        tag = "Рыба",
        photo = 'http://rocket04.imgix.net/okyn-fetuccini.jpg?s=246f62a77e49f28d1290cd712bb5c698',
        ingredients = 'Филе Окуня|Феттучини|Шпинат|Чеснок|Лимон|Розмарин|Сливочное масло|Оливковое масло|Красный молотый перец|Мука|Соль',
        nutrients= '700|69|24|28',
        )
    print(str(recipe23))
    recipe23.save()

    recipe24 = Recipes.create(
        title = 'Чай со смородиной',
        subtitle = '2|5',
        description  = 'Смородиновый чай на Руси известен с древности, когда-то его называли напитком долголетия. Действительно, чай из смородины очень полезен, он обладает противовоспалительным и антистрессовым действием. Да и, помимо этого, он очень вкусный и ароматный.',
        price = 10,
        tag = "Напитки",
        photo = 'http://rocket04.imgix.net/tea-smorodina.jpg?s=e09527e26b00dfe51b593cd034227631',
        ingredients = 'Смородина|Черный чай|Мед цветочный',
        nutrients= '40|0|5|10',
        )
    print(str(recipe24))
    recipe24.save()

    recipe25 = Recipes.create(
        title = 'Крем-суп из брокколи с мятой',
        subtitle = '2|15',
        description  = 'Вкус брокколи иногда мешает полностью насладиться этим невероятно полезным овощем. Но в данном рецепте, мы придумали отличный способ сохранить всю полезность брокколи перемешав в тонким ароматом от мяты, базилика и лимона. Очень вкусный и полезный суп, идеально подходящий для быстрого перекуса.',
        price = 60,
        tag = "Супы",
        photo = 'http://rocket04.imgix.net/krem-soup-s-myatoi.jpg?s=b850118e0facf64432fb98d5b47a1aca',
        ingredients = 'Сливки 33%|Брокколи|Лимон|Базилик|Мята|Чеснок|Бульон|Лук|Лист лавровый|Оливковое масло|Перец черный молотый|Соль',
        nutrients= '551|27|39|24',
        )
    print(str(recipe25))
    recipe25.save()

    recipe26 = Recipes.create(
        title = 'Паста Карбонара',
        subtitle = '2|15',
        description  = 'Очень сытная, с ярким ароматом и пикантным вкусом паста Карбонара имеет спорную историю и свои маленькие секреты приготовления. А главная особенность этого блюда в том, что яичный соус доходит до готовности буквально на тарелке, то есть от жара только сваренных спагетти.',
        price = 60,
        tag = "Ризотто & Овощи",
        photo = 'http://rocket04.imgix.net/Pasta-Karbonara.jpg?s=6957bf93f61332e83ac46d652ca4f9d1',
        ingredients = 'Петрушка|Яйцо|Пармезан|Спагетти|Сливки|Лук|Чеснок|Грудинка сырокопченая|Оливковое масло|Вино белое|Перец черный молотый',
        nutrients= '1032|26|69|78',
        )
    print(str(recipe26))
    recipe26.save()

    recipe27 = Recipes.create(
        title = 'Руккола с креветками и авокадо',
        subtitle = '2|20',
        description  = 'Орехово-перечный вкус итальянки (по происхождению) рукколы встречается с южно-американским нежным авокадо, который туземцы называли " маслом леса", пикантным любимцем Аппенин пармезаном, тигровыми креветками, и кедровыми орешками, хорошо знакомыми всем с детства. Завершает этот праздник вкуса легкая заправка, которая бережно сохраняет вкусовой букет!',
        price = 110,
        tag = "Салаты",
        photo = 'http://rocket04.imgix.net/rukkola-s-krevetkami.jpg?s=7223cca912cbfa9edd3c82855b89e8f3',
        ingredients = 'Креветки|Руккола|Авокадо|Сыр пармезан|Помидоры черри|Орех кедровый|Мед цветочный|Лайм|Соус соевый|Крем бальзамический|Масло оливковое|Соль|Перец черный молотый',
        nutrients= '562|27|40|23',
        )
    print(str(recipe27))
    recipe27.save()

    recipe28 = Recipes.create(
        title = 'Салат с грушей и сыром Рокфор',
        subtitle = '2|20',
        description  = 'Груши, совершенно недооцененные ингредиенты для салатов, особенно если их запечь, закарамелизировать или просто отварить. В этом салате мы исправляем это неравенство и будем сочетать грушу, сыр Рокфор и замечательную рукколу.',
        price = 80,
        tag = "Салаты",
        photo = 'http://rocket04.imgix.net/salad-s-gryshei.jpg?s=8757545817fdab71430412b294e92fe5',
        ingredients = 'Мед цветочный|Орех грецкий|Сыр рокфор|Руккола|Груша|Лимон|Мята|Оливковое масло|Перец черный молотый|Соль',
        nutrients= '609|12|42|46',
        )
    print(str(recipe28))
    recipe28.save()
