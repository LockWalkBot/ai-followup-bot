from twilio.rest import Client

TWILIO_SID = "AC5df906f5467c2d817982b384c4a05ad3"
TWILIO_AUTH_TOKEN = "b8af7980f9391f547f8e926c19484e40"
WHATSAPP_NUMBER = "whatsapp:+14155238886"
YOUR_NUMBER = "whatsapp:+18042524930"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_message(body):
    message = client.messages.create(
        from_=WHATSAPP_NUMBER,
        body=body,
        to=YOUR_NUMBER
    )
    print(f"Message sent: {message.sid}")
