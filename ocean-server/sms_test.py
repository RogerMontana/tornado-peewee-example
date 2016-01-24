from twilio.rest import TwilioRestClient

if __name__ == '__main__':
        try:
            client = TwilioRestClient(account="AC62c3e1728fb6f97d87e04c923a364450", token="75f320c1bbe0b77ac012e9a796c2f2b5")
            message = client.messages.create(body="Vash zakaz bydet dostavlen " + "24 JAN" + ". K oplate " + "100" + "UAH",
                to="+380638910420",    # Replace with your phone number
                from_="Rocket04") # Replace with your Twilio number

        except:
            print("sms was not sended")
            pass

