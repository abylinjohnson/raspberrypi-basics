from twilio.rest import Client


account_sid = "ACCOUNT SID"
account_token = "ACCOUNT TOKEN"
client = Client(account_sid, account_token)

message = client.messages.create(
         body='Hello From Raspberry Pi',
         from_='TWILIO PHONE NO',
         to='RECIEVERS NUMBER'
     )

print(message.sid)
