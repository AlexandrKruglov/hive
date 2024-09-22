import os

from twilio.rest import Client

def send_sms(text, receiver):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text,
        from_='your_twilio_phone_number',
        to=receiver
    )

    return message.sid