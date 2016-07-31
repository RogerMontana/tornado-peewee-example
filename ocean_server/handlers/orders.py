import json

from twilio.rest import TwilioRestClient
from ocean_server.handlers.peewee import PeeweeRequestHandler
from ocean_server.database.models import Orders


class OrdersHandler(PeeweeRequestHandler):
    account_sid = 'AC62c3e1728fb6f97d87e04c923a364450'
    auth_token = '{{75f320c1bbe0b77ac012e9a796c2f2b5}}'
    number = '+380504814277'

    response_ok = {'code': 200, 'response': 'OK'}
    response_error = {'code': 400, 'response': 'ERROR'}

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    def post(self, *args, **kwargs):

        result = json.loads(self.request.body)
        time_gap = result['timegap']
        total_bill = result['total']
        phone = result['phone']
        mail = result['email']
        oreder_details = result['order_details']
        # SMS NOTIFICATION
        try:
            client = TwilioRestClient(account=account_sid,
                                      token=auth_token)

            client.messages.create(
                body='Vash zakaz bydet dostavlen {timegap}. K oplate + {total} UAH'.format(
                    timegap=time_gap,
                    total=total_bill),

                to=phone,
                from_='Rocket04')

        except KeyError:
            print('sms was not sended', result)

        try:
            order = Orders.create(
                order_details='{details} Email: {email}, total: {total}'.format(
                    details=oreder_details,
                    email=mail,
                    total=total_bill
                ),

                name=result['name'],
                total_bill=result['total'],
                time_gap=result['timegap'],
                address=result['address'],
                status='new',
                phone=result['phone']
            )
            order.save()
            self.write(json.dumps(self.response_ok))
        except:
            self.write(json.dumps(self.response_error))
