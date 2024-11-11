from dotenv import load_dotenv
import os
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv(dotenv_path=r"C:\Users\asus\Desktop\sms api\twilioPython\.env")

# Retrieve Twilio credentials and other environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")
verify_sid = os.getenv("VERIFY_SID")

# Ensure that all environment variables are correctly loaded
if not all([account_sid, auth_token, phone_number, verify_sid]):
    raise ValueError("One or more environment variables are missing or incorrect.")

# Debugging print statements
print(f"Account SID: {account_sid}")
print(f"Auth Token: {auth_token}")
print(f"Phone Number: {phone_number}")
print(f"Verify SID: {verify_sid}")

# Initialize Twilio Client
client = Client(account_sid, auth_token)

try:
    # Create a verification request
    print("Sending OTP to phone number...")
    otp_verification = client.verify.v2.services(verify_sid).verifications.create(
        to=phone_number, channel="sms"
    )
    
    # Print the status of the verification request
    print(f"OTP Verification Status: {otp_verification.status}")

    # Prompt user to enter OTP
    otp_code = input("Please enter the OTP sent to you: ")

    # Verify the OTP entered by the user
    otp_vcheck = client.verify.v2.services(verify_sid).verification_checks.create(
        to=phone_number, code=otp_code
    )

    # Print the status of OTP verification
    print(f"OTP Verification Check Status: {otp_vcheck.status}")

except Exception as e:
    print(f"An error occurred: {e}")
    # Optionally, log the error or send an alert if needed
