from __future__ import absolute_import, print_function
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers import *


# TODO Refactor settings
dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')
SSL_PATH = os.path.join(dirname, 'ssl')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/rockettest", TestRocket),
            (r"/info", InfoApiHandler),
            (r"/login", LoginHandler),
            (r"/get_recipes", AllRecipesHandler),
            (r"/order", OrdersHandler),
            (r"/promo", PromoCodeHandler)
        ]
        settings = {
            "template_path": TEMPLATE_PATH,
            "static_path": STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()