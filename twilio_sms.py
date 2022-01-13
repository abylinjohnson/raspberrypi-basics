from twilio.rest import Client


account_sid = "AC19b46169d02b236d553d811b00e53b54"
account_token = "5ef95754e3a23280ef75091057cf851e"
client = Client(account_sid, account_token)

message = client.messages.create(
    body='Good Evening My Friend!',
    from_='+16085120530',
    to='+919488588505'
)

print(message.sid)
