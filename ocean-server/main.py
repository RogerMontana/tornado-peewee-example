import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers import *

# TODO Refactor settings
dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/info", InfoApiHandler),
            (r"/login", LoginHandler),
        ]
        settings = {
            "template_path": TEMPLATE_PATH,
            "static_path": STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def create_server(*args, **kwargs):
    '''
    Makes HTTPServer based on 'args' & 'kwargs' that have the same meaining
    as in HTTPServer's constructor.
    If xheaders=True and force_https=True are passed, also patches _RequestDispatcher
    to generate redirects to https URLs.
    '''
    kw = dict(kwargs)
    force_https = kw.pop('force_https', False)
    if kw.get('xheaders', False) and force_https:
        class PatchedDispatcher(tornado.web._RequestDispatcher):
            def _find_handler(self):
                req = self.request
                if req.headers.get('X-Forwarded-Proto') != 'https':
                    self.handler_class = tornado.web.RedirectHandler
                    self.handler_kwargs = {'url': 'https://%s%s' % (req.headers['Host'], req.uri)}
                    return
                return super(PatchedDispatcher, self)._find_handler()
        tornado.web._RequestDispatcher = PatchedDispatcher
    return tornado.httpserver.HTTPServer(*args, **kw)


def main():
    applicaton = Application()
    http_server = create_server(applicaton,
                       xheaders=True,
                       force_https=os.environ.get('FORCE_HTTPS') in ('true', 'True'))
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()