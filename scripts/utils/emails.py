import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from settings import port, sender_email, password, smtp_server

class UnladenSwallow:
  
  @classmethod
  def send_report(cls, from_file=None, receiver_email=None):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python auto test reports"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    # text = "Test report:\n"

    # Read report file
    with open(from_file, "r") as f:
      content = f.read()

    # Turn into plain/html MIMEText objects
    part1 = MIMEText(content, "plain")
    message.attach(part1)

    # Create a secure SSL context and send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
