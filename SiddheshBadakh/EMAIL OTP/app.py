import os
import random
from flask import Flask, request, render_template, session, redirect, url_for, flash
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management

# Email credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Function to send OTP via email
def send_otp(recipient_email, otp):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg['Subject'] = "Your OTP Code"
    
    body = f"Your OTP code is: {otp}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, recipient_email, msg.as_string())
        server.quit()
        print("OTP sent successfully")
    except Exception as e:
        print("Failed to send OTP:", e)

# Generate a random OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Home route to redirect to the OTP request page
@app.route('/')
def home():
    return redirect(url_for('request_otp'))

@app.route('/request_otp', methods=['GET', 'POST'])
def request_otp():
    if request.method == 'POST':
        email = request.form['email']
        otp = generate_otp()
        session['otp'] = otp
        session['email'] = email
        send_otp(email, otp)
        flash("OTP sent to your email.")
        return redirect(url_for('verify_otp'))
    return render_template('request_otp.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if 'otp' in session and user_otp == session['otp']:
            flash("OTP verified successfully!")
            return redirect(url_for('success'))
        else:
            flash("Invalid OTP. Please try again.")
            return redirect(url_for('verify_otp'))
    return render_template('verify_otp.html')

@app.route('/success')
def success():
    return "OTP Verified! Access granted."

if __name__ == '__main__':
    app.run(debug=True)
