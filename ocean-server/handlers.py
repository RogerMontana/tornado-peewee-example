__author__ = 'artem'
import tornado.web
import tornado.template as templates
import sys, inspect
import os
from models import *
import json
from twilio.rest import TwilioRestClient

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

class AllRecipesHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        recipes = Recipes.select()
        response =[]
        for recipe in recipes:
            response.append((str(recipe.get()).replace('\'','\"')))
        self.write(json.dumps(response))

class OrdersHandler(tornado.web.RequestHandler):
    account_sid = "AC62c3e1728fb6f97d87e04c923a364450"
    auth_token = "75f320c1bbe0b77ac012e9a796c2f2b5"
    number = "+380504814277"

    def get(self):
        client = TwilioRestClient(self.account_sid, self.auth_token)
        message = client.messages.create(body="rocket04 >:3",
        to=self.number,    # Replace with your phone number
        from_=self.account_sid) # Replace with your Twilio number
        print(message.sid)

