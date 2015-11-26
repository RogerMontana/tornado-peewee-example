__author__ = 'artem'
import tornado.web
import tornado.template as templates
import sys, inspect
import os
from models import *
import json
import peewee
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
        recipes = Recipes.select().get()
        json_data = json.dumps(model_to_dict(user_obj))
        self.write(json_data)

