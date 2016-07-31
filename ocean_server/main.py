from __future__ import absolute_import, print_function
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

from ocean_server.handlers.web import MainHandler, InfoApiHandler
from ocean_server.handlers.recipes import AllRecipesHandler
from ocean_server.handlers.orders import OrdersHandler

# TODO Refactor settings
dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')
SSL_PATH = os.path.join(dirname, 'ssl')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/info", InfoApiHandler),
            (r"/get_recipes", AllRecipesHandler),
            (r"/order", OrdersHandler),
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
    print("server address is 0.0.0.0:", str(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()