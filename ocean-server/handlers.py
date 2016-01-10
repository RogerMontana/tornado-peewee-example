# -*- coding: utf-8 -*-


__author__ = 'artem'

import tornado.web
import tornado.template as templates
import sys, inspect
import os
from models import Recipes
from models import Orders
from models import db_proxy
from peewee import *
import json


dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')

current_module = sys.modules[__name__]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("login mocked")

class InfoApiHandler(tornado.web.RequestHandler):
    def get(self):
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        template = templates.Loader(TEMPLATE_PATH)
        self.write(template.load("api_info.html").generate(info = clsmembers))

class PeeweeRequestHandler(tornado.web.RequestHandler):
    def prepare(self):
        db_proxy.connect()
        return super(PeeweeRequestHandler, self).prepare()

    def on_finish(self):
        if not db_proxy.is_closed():
            db_proxy.close()
        return super(PeeweeRequestHandler, self).on_finish()

class AllRecipesHandler(PeeweeRequestHandler):
    def get(self):
        response =[]
        for recipe in Recipes.select():
            recipe_obj = {
                "id": recipe.recipe_id,
                "subtitle": recipe.subtitle,
                "title" : recipe.title,
                "description" : recipe.description,
                "price" : float(recipe.price),
                "photo" : recipe.photo,
                "ingredientsPhoto" : recipe.ingredientsPhoto,
                "ingredients" : recipe.ingredients,
                "nutrients" : recipe.nutrients
            }
            response.append(recipe_obj)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

class OrdersHandler(tornado.web.RequestHandler):
    account_sid = "ACb1df72c332a5e8443e84a6c64fb9cd76"
    auth_token = "75f320c1bbe0b77ac012e9a796c2f2b5"
    number = "+380504814277"
    # def get(self):
    #     client = TwilioRestClient(self.account_sid, self.auth_token)
    #     message = client.messages.create(body="rocket04 >:3",
    #     to=self.number,    # Replace with your phone number
    #     from_='Rocket04') # Replace with your Twilio number
    #     print(message.sid)
    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "text/plain")
        result = json.loads(self.request.body)
        order = Orders.create(
            order_details = result["order_details"],
            name = result["name"],
            address = result["address"],
            status = "new",
            phone = result["phone"]
        )
        order.save()
        self.write("Your order_details " + result )