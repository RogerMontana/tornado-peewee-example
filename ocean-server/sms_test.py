from twilio.rest import TwilioRestClient

# if __name__ == '__main__':
#         body = ''
#         try:
#             body="Vash zakaz bydet dostavlen " + "24 JAN" + ". K oplate " + 100 + "UAH"
#             print(body)
#
#
#         except:
#             print("sms was not sended")
#             pass
#


import json


jsons = [{"subtitle": "2|30", "description": "\u0411\u0430\u0440\u0430\u043d\u0438\u043d\u0430 - \u043d\u0435\u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u043d\u0435\u0436\u043d\u043e\u0435 \u0438 \u043f\u043e\u043b\u0435\u0437\u043d\u043e\u0435 \u043c\u044f\u0441\u043e, \u0432 \u0434\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u0441 \u043f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u043c\u0438 \u0446\u0443\u043a\u043a\u0438\u043d\u0438 \u0438 \u0441\u043e\u043a\u043e\u043c \u0438\u0437 \u043b\u0430\u0439\u043c\u0430, \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u044b\u043c \u0431\u0435\u043b\u043a\u043e\u0432\u044b\u043c \u0443\u0436\u0438\u043d\u043e\u043c \u0434\u043b\u044f \u0442\u0435\u0445 \u043a\u0442\u043e \u0441\u043b\u0435\u0434\u0438\u0442 \u0437\u0430 \u0441\u0432\u043e\u0435\u0439 \u0444\u0438\u0433\u0443\u0440\u043e\u0439.", "photo": "http://rocket04.imgix.net/12_2.jpg?s=a34e78f1c3ef3f0ec1d4e304073224e7", "price": "165.0", "diet": "7|6|5|4|3", "tag": "\u041c\u044f\u0441\u043e", "id": "1", "ingredients_photo": "http://rocket04.imgix.net/12_1.jpg?s=cbdbbb0586921be7e4fc956963c8dc47", "title": "\u0411\u0430\u0440\u0430\u043d\u0438\u043d\u0430 \u0441 \u0420\u043e\u0437\u043c\u0430\u0440\u0438\u043d\u043e\u043c, \u0426\u0443\u043a\u0438\u043d\u0438 \u0438 \u041c\u044f\u0442\u043e\u0439", "nutrients": "840|80|20|37", "ingredients": "\u0411\u0430\u0440\u0430\u043d\u0438\u043d\u0430 \u043c\u044f\u043a\u043e\u0442\u044c 360 \u0433\u0440|\u0422\u043c\u0438\u043d 4 \u0433\u0440|\u0426\u0443\u043a\u0438\u043d\u0438 300 \u0433\u0440|\u041b\u0430\u0439\u043c 1 \u0448\u0442|\u0427\u0435\u0441\u043d\u043e\u043a 12 \u0433\u0440|\u041c\u044f\u0442\u0430 5 \u0433\u0440|\u0420\u043e\u0437\u043c\u0430\u0440\u0438\u043d 5 \u0433\u0440"}]

n = json.dumps(jsons)
json.load(n)
d = "1|2|3".split("|")

obj = {'obj':2,
       'list':d }

json = json.dumps(obj)

print(json)
