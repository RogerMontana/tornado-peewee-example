# -*- coding: utf-8 -*-
import os
import sys, inspect
import tornado.web
import tornado.template as templates

dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')

current_module = sys.modules[__name__]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class InfoApiHandler(tornado.web.RequestHandler):
    def get(self):
        clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        template = templates.Loader(TEMPLATE_PATH)
        self.write(template.load("api_info.html").generate(info=clsmembers))
