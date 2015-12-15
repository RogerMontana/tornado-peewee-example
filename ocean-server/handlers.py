__author__ = 'artem'
import tornado.web
import tornado.template as templates
import sys, inspect
import os
from models import *
import json
import plivo

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
    auth_id = "MAOGQ3NMU1N2EZNJHIM2"
    auth_token = "ZTdmMDdlYjVhMmJjN2VkOTRhZjZlMmMxNjY2Yzc0"
    number = "+14164647135"
    msg = {
        "src": "http://10.10.1.10:3128",
        "dst": "http://10.10.1.10:1080",
        "text":"test"
    }
    def get(self):
        p = plivo.RestAPI(self.auth_id, self.auth_token)
        params = {'dst': self.number,
                  'src': 'OCEAN_04',
                  'text': 'Hello from Ocean04 >:3'
                  }
        p.send_message(params)



