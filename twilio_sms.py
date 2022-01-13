from twilio.rest import Client


account_sid = "your sid"
account_token = "your auth token"
client = Client(account_sid, account_token)

message = client.messages.create(
    body='Good Evening My Friend!',
    from_='from number',
    to='to number'
)

print(message.sid)
