import random
from twilio.rest import Client

# Your Twilio account SID and Auth Token
ACCOUNT_SID = 'Twilio_Account_SID'
AUTH_TOKEN = 'Twilio_Auth_Token'

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# List of Twilio phone numbers you might dial from
twilio_phone_numbers_list = [
    '+17781112222',
    '+17781113333',
    '+17781114444',
    '+17781115555',
    '+17781116666',
    '+17781117777',
    '+17781118888',
    # ... add as many as you have
]

# The phone number you're dialing to
to_phone_number = '+17781110000'

# Select a random Twilio phone number from the list to dial from
from_phone_number = random.choice(twilio_phone_numbers_list)

# Dial the number and say a message
call = client.calls.create(
    twiml='<Response><Say>Hello! This is the message that will be read out when the caller picks up.</Say></Response>',
    to=to_phone_number,
    from_=from_phone_number
)

print(f"Call initiated from {from_phone_number} to {to_phone_number} with SID: {call.sid}")


