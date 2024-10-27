from twilio.rest import Client

account_sid = 'AC1c5f4320a7ac761d8bb9b5921ef3bd49'
auth_token = '2ddb033ad1f71edef93eaacc166ef81f'
client = Client(account_sid, auth_token)

# ------------------------------------------------------------TEXTOS SIMPLES------------------------------------------------------------
# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your appointment is coming up on July 21 at 3PM',
#   to='whatsapp:+5491140962011'
# )

# ------------------------------------------------------------TEXTOS CON IMAGENES------------------------------------------------------------

# message = client.messages.create(
#     body="Here's that picture of an owl you requested.",
#     media_url=["https://demo.twilio.com/owl.png"],
#     to='whatsapp:+5491140962011',
#     from_='whatsapp:+14155238886',
# )

print(message.body)
