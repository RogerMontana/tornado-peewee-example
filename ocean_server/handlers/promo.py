# -*- coding: utf-8 -*-
import json

from ocean_server.handlers.peewee import PeeweeRequestHandler
from ocean_server.promo import PromoCodes


class PromoCodeHandler(PeeweeRequestHandler):
    response_promotion1 = {'provider':"Ekipazh", 'discount':25}
    response_promotion2 = {'provider':"Test1", 'discount':10}
    response_error = {'provider':'ERROR', 'discount':0}
    codes = PromoCodes()
    promocodes_p1 = codes.promo
    promocodes_p2 = ["test22",]

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


