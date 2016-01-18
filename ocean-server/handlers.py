# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
from twilio import *

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
                "id": recipe.id,
                "subtitle" : recipe.subtitle,
                "title" : recipe.title,
                "tag" : recipe.tag,
                "description" : recipe.description,
                "price" : float(recipe.price),
                "photo" : recipe.photo,
                "ingredients" : recipe.ingredients,
                "nutrients" : recipe.nutrients
            }
            response.append(recipe_obj)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

class OrdersHandler(tornado.web.RequestHandler):

    account_sid = "AC62c3e1728fb6f97d87e04c923a364450"
    auth_token = "{{75f320c1bbe0b77ac012e9a796c2f2b5}}"
    number = "+380504814277"

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")


    # def get(self):


    # adress: "kosiora 27"
    # appartment: "24"
    # name: "Alex"
    # order_details: "Панна-Котта - 2"
    # phone: "+380637691431"
    # timegap: "Sun Jan 17 2016 22:13:55 GMT+0200 (Финляндия (зима))|16.00 - 19.00"



    response_ok = {'code':200, 'response':'OK'}
    response_error = {'code':400, 'response':'ERROR'}
    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        result = json.loads(self.request.body)
        try:
            order = Orders.create(
            order_details = result["order_details"] + result["timegap"] + result["appartment"],
            name = result["name"],
            address = result["address"],
            status = "new",
            phone = result["phone"]
            )
            order.save()
            self.write(json.dumps(self.response_ok))
        except:
            self.write(json.dumps(self.response_error))

    def get(self, *args, **kwargs):
        client = TwilioRestClient(self.account_sid, self.auth_token)
        message = client.messages.create(body="rocket04 >:3",
        to=self.number,    # Replace with your phone number
        from_="+17787620364") # Replace with your Twilio number
        print(self.number)
        print(message.sid)
        response =[]
        for order in Orders.select():
            order_obj = {
                "id": order.id,
                "order_details" : order.order_details,
                "address" : order.address,
                "name" : order.name,
                "status" : order.status,
                "phone" : order.phone
            }
            response.append(order_obj)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))
