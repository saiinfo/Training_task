from dotenv import load_dotenv
import os
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv(dotenv_path=r"C:\Users\asus\Desktop\sms api\twilioPython\.env")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")
verify_sid = os.getenv("VERIFY_SID")

print("Account SID:", account_sid)
print("Auth Token:", auth_token)
print("Phone Number:", phone_number)

if not account_sid or not auth_token or not phone_number:
    print("Twilio credentials not found. Check .env file.")
else:
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body="Hello World from Siddhesh Badakh",
            from_=phone_number,  # This must be a Twilio phone number
            to="+919527592580"  # Replace with the recipient's phone number
        )
        print("SMS has been sent!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("An error occurred:", str(e))
