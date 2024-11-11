import os
from flask import Flask, request, render_template, flash, redirect, url_for
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Function to send a message via email
def send_message(recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, recipient_email, msg.as_string())
        server.quit()
        print("Message sent successfully")
    except Exception as e:
        print("Failed to send message:", e)

@app.route('/')
def home():
    return redirect(url_for('send_message_route'))  # Redirect to the send message page

@app.route('/send_message', methods=['GET', 'POST'])
def send_message_route():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        send_message(email, subject, message)
        flash("Message sent successfully!")
        return redirect(url_for('send_message_route'))
    return render_template('send_message.html')

if __name__ == '__main__':
    app.run(debug=True)
