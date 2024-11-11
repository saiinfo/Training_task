from dotenv import load_dotenv
import os
from twilio.rest import Client

# Step 1: Load environment variables from the .env file
load_dotenv()

# Step 2: Get environment variables from .env file
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")
verify_sid = os.getenv("VERIFY_SID")

# Debugging: Print the values to ensure they're loaded correctly
print(f"Account SID: {account_sid}")
print(f"Auth Token: {auth_token}")
print(f"Verify SID: {verify_sid}")
print(f"Phone Number: {phone_number}")

# Step 3: Initialize Twilio client
client = Client(account_sid, auth_token)

# Step 4: Ensure phone number is in correct format (E.164 format)
if not phone_number.startswith('+'):
    print("Error: Phone number must start with a '+' followed by the country code.")
else:
    # Step 5: Create a verification request using Twilio's Verify API
    try:
        otp_verification = client.verify.v2.services(verify_sid).verifications.create(
            to=phone_number,  # Pass the phone number loaded from the .env file
            channel="sms"  # Sending the OTP via SMS
        )
        print(f"Verification response: {otp_verification}")
        print(f"Verification status: {otp_verification.status}")

        # Step 6: Input OTP from the user
        otp_code = input("Please enter the OTP sent to you: ")

        # Step 7: Verify the OTP entered by the user
        otp_vcheck = client.verify.v2.services(verify_sid).verification_checks.create(
            to=phone_number,  # Pass the phone number loaded from the .env file
            code=otp_code  # OTP code entered by the user
        )
        print(f"Verification check status: {otp_vcheck.status}")

    except Exception as e:
        print(f"Error occurred: {e}")
