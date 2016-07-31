from tornado.web import RequestHandler

from ocean_server.models.models import db_proxy


class PeeweeRequestHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def prepare(self):
        db_proxy.connect()
        return super(PeeweeRequestHandler, self).prepare()

    def on_finish(self):
        if not db_proxy.is_closed():
            db_proxy.close()
        return super(PeeweeRequestHandler, self).on_finish()
