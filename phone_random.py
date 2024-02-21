import random
import os
import re
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Explicitly load environment variables and validate their presence
load_dotenv()

def validate_env_variables():
    required_vars = ['TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN', 'TWILIO_PHONE_NUMBERS']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

validate_env_variables()

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(ACCOUNT_SID, AUTH_TOKEN)
twilio_phone_numbers_list = os.getenv('TWILIO_PHONE_NUMBERS').split(',')

# Enhanced logging to include more details
log_file_path = 'call_attempts.log'

def format_phone_number(number):
    """Ensure phone numbers are in E.164 format."""
    clean_number = re.sub(r'[^\d+]', '', number)
    return '+1' + clean_number if not clean_number.startswith('+') else clean_number

def log_call_attempt(from_phone_number, to_phone_number):
    """Log call attempts with timestamps, from and to numbers."""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{current_time}, From: {from_phone_number}, To: {to_phone_number}\n")

def dial_numbers():
    """Iterate over destination numbers and initiate calls."""
    with open('destination_numbers.txt', 'r') as file:
        destination_numbers = [format_phone_number(line.strip()) for line in file]

    for to_phone_number in destination_numbers:
        from_phone_number = random.choice(twilio_phone_numbers_list)
        try:
            call = client.calls.create(
                twiml='<Response><Say>Hello! This is a message from your script.</Say></Response>',
                to=to_phone_number,
                from_=from_phone_number
            )
            print(f"Call initiated from {from_phone_number} to {to_phone_number} with SID: {call.sid}")
            log_call_attempt(from_phone_number, to_phone_number)
        except Exception as e:
            print(f"Error making call from {from_phone_number} to {to_phone_number}: {e}")

if __name__ == "__main__":
    dial_numbers()
