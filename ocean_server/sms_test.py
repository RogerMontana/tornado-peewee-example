from twilio.rest import TwilioRestClient

if __name__ == '__main__':
        body = ''
        try:
            body="Vash zakaz bydet dostavlen " + "24 JAN" + ". K oplate " + 100 + "UAH"
            print(body)


        except:
            print("sms was not sended")
            pass

import json
import requests
data = {'code': 'test1'}

headers = {'Content-type': 'application/json'}
resp = requests.post('http://0.0.0.0:5000/promo', data=json.dumps(data), headers=headers)
print(resp.status_code)

