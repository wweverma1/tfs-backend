# Standard library imports
import time
from datetime import datetime
import smtplib
import os

# Related third party imports
from flask import request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Local app specific imports
from app import app

from app.utils.email_templates import (
    email_verification_template_p1,
    email_verification_template_p2,
    forgot_password_template_p1,
    forgot_password_template_p2,
)


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    if request.endpoint:
        end_time = time.time()
        latency = int((end_time - request.start_time) * 1000)
        print(f'[ {str(datetime.now())}] endpoint {request.endpoint} latency {latency} \
               req_id {request.environ.get("FLASK_REQUEST_ID")}')
    return response


def serve_otp_signup_email(receiver_address, otp):
    sender_address = os.getenv("SMTP_USERNAME")
    sender_pass = os.getenv("SMTP_PASSWORD")

    mail_content = email_verification_template_p1 + \
        str(otp) + email_verification_template_p2

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = '"TFS IIT Kharagpur"'
    message['To'] = receiver_address
    message['Subject'] = 'Lets get you verified 🎬'  # The subject line

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("OTP sent for verification.")


def serve_otp_password_email(receiver_address, otp):
    sender_address = os.getenv("SMTP_USERNAME")
    sender_pass = os.getenv("SMTP_PASSWORD")

    mail_content = forgot_password_template_p1 + \
        str(otp) + forgot_password_template_p2

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = '"TFS IIT Kharagpur"'
    message['To'] = receiver_address
    message['Subject'] = 'Reset Your Password'  # The subject line

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("OTP sent for password reset.")
