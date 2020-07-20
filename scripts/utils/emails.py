import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import yagmail

from settings import sender_email, sender_password, subject

class UnladenSwallow:
  
    @classmethod
    def send_report(cls, from_file=None, receiver_email=None):
        sender_username = sender_email.split("@")[0]
        yag = yagmail.SMTP(sender_username, sender_password)
        
        with open(from_file, "r") as f:
            content = f.read()

        yag.send(receiver_email, subject, content)