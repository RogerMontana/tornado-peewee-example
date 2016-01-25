from twilio.rest import TwilioRestClient

if __name__ == '__main__':
        body = ''
        try:
            body="Vash zakaz bydet dostavlen " + "24 JAN" + ". K oplate " + 100 + "UAH"
            print(body)


        except:
            print("sms was not sended")
            pass

