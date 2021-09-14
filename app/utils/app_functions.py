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

    mail_content = """<h1>𝓗𝓮𝓵𝓵𝓸</h1><h3>Use the one time password given below to verify your acccount.</h3>
                      <h3 style="display:inline;">One Time Password: </h3>
                      <h2 style="color:red; display:inline; letter-spacing: 10px;">""" + \
        str(otp) + """</h2><br><h3>Its valid only for 10 minutes.</h3><br>
                      <h3>TFS<br>IIT Kharagpur</h3>
                      <img src="https://static.toiimg.com/thumb/msid-67397064,width-1200,height-900,resizemode-4/.jpg"
                      alt="TFS LOGO" height="200px" width="200px">"""

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

    mail_content = """<h1>𝓗𝓮𝓵𝓵𝓸</h1><h3>Use the one time password given below to reset your password.</h3>
                      <h3 style="display:inline;">One Time Password: </h3>
                      <h2 style="color:red; display:inline; letter-spacing: 10px;">""" + \
        str(otp) + """</h2><br><h3>Its valid only for 10 minutes.</h3><br>
                      <h3>TFS<br>IIT Kharagpur</h3>
                      <img src="https://static.toiimg.com/thumb/msid-67397064,width-1200,height-900,resizemode-4/.jpg"
                      alt="TFS LOGO" height="200px" width="200px">"""

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
