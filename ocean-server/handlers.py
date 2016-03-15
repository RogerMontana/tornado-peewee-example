# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
from twilio import *
from decimal import *
__author__ = 'artem'

import tornado.web
import tornado.template as templates
import sys, inspect
import os
from models import Recipes
from models import Orders
from models import Promocodes
from models import db_proxy
from peewee import *
from promo import PromoCodes
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

class TestRocket(tornado.web.RequestHandler):
    def get(self):
        self.render("rocket.html")

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
                "vine": recipe.vine,
                "description" : recipe.description,
                "price" : float(recipe.price),
                "size": float(recipe.size),
                "photo" : recipe.photo,
                "ingredients_photo": recipe.ingredients_photo,
                "diet": recipe.diet_type.split("|"),
                "ingredients" : recipe.ingredients,
                "nutrients" : recipe.nutrients
            }
            response.append(recipe_obj)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(response))

class OrdersHandler(PeeweeRequestHandler):

    account_sid = "AC62c3e1728fb6f97d87e04c923a364450"
    auth_token = "{{75f320c1bbe0b77ac012e9a796c2f2b5}}"
    number = "+380504814277"

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    response_ok = {'code':200, 'response':'OK'}
    response_error = {'code':400, 'response':'ERROR'}
    def post(self, *args, **kwargs):

        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        result = json.loads(self.request.body)
        print(result)
        # SMS NOTIFICATION
        try:
            client = TwilioRestClient(account="AC62c3e1728fb6f97d87e04c923a364450", token="75f320c1bbe0b77ac012e9a796c2f2b5")
            
            message = client.messages.create(body="Vash zakaz bydet dostavlen " + result["timegap"] + ". K oplate " + str(result["total"]) + "UAH",
                to=result["phone"],    # Replace with your phone number
                from_="Rocket04") # Replace with your Twilio number

            message_to_p = client.messages.create(body="NOVIY ZAKAZ k " + result["timegap"] + "pozvoni na" + result["phone"],
                                                  to ="+380503415646",
                                                  from_="Rocket04")
            print(message_to_p.sid)
            print(message.sid)
            print(result["phone"])
        except:
            print("sms was not sended")
            pass

        try:
            order = Orders.create(
            order_details = result["order_details"] + " EMAIL: " + result["email"] + " TOTAL: " + str(result["total"]) ,
            name = result["name"],
            total_bill = float(str(result["total"])),
            time_gap = result["timegap"],
            address = result["address"]+" / "+result["appartment"],
            status = "new",
            phone = result["phone"]
            )
            order.save()
            self.write(json.dumps(self.response_ok))
        except:
            self.write(json.dumps(self.response_error))



class AdminOrderHandler(PeeweeRequestHandler):
    secret_keys = ["POVARPOVAR",]

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def post(self, *args, **kwargs):
        response =[]
        auth = json.loads(self.request.body)
        key = auth["key"]

        if(key in self.secret_keys):
         for order in Orders.select():
             order_obj = {
                    "id": order.id,
                    "order_details" : order.order_details,
                    "total_bill": float(order.total_bill),
                    "time_gap": order.time_gap,
                    "address" : order.address,
                    "name" : order.name,
                    "status" : order.status,
                    "phone" : order.phone
             }
             response.append(order_obj)
        self.write(json.dumps(response))


class PromoCodeHandler(PeeweeRequestHandler):
    response_promotion1 = {'provider':"Ekipazh", 'discount':25}
    response_promotion2 = {'provider':"Test1", 'discount':10}
    response_error = {'provider':'ERROR', 'discount':0}
    codes = PromoCodes()
    promocodes_p1 = codes.promo
    promocodes_p2 = ["test22",]

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def post(self, *args, **kwargs):
        print("promo code used")
        promo = json.loads(self.request.body)
        code = promo["code"]
        if(code in self.promocodes_p1):
            self.write(json.dumps(self.response_promotion1))
            print(code)
            self.promocodes_p1.remove(code)
        elif (code in self.promocodes_p2):
            self.write(json.dumps(self.response_promotion2))
            print(code)
            self.promocodes_p2.remove(code)
        else:
            self.write(json.dumps(self.response_error))



