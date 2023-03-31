# First go to your gmail account and setup 2 factor authentication
# generate app password
# create a function to send the mail
# TEMPMAIL.COM

from email.message import EmailMessage
from App_password import password
import ssl
import smtplib

email_sender = 'qkingsley436@gmail.com'
email_password = password

email_receiver = 'kquarshie436@gmail.com'

subject = 'UGRC110 Grade Not Showing.'
body = """
Please look sharp and revert my issue. 
Do fast and upload the grade.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
