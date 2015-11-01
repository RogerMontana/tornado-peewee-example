__author__ = 'artem'
import tornado.web
from moltin.moltin import Moltin

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        m = Moltin();
        access_token = m.authenticate();
        m.set_access_token(access_token);