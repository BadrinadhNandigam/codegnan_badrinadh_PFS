'''
SMTP (Simple Mail Transfer Protocol)
----------------------------------------------

> This is used to send emails from server to another server

Note:
----------
1.SMTP SSL Port
----------
465

2.SMTP TLS port
----------
587

import smtplib

EmailMessage Class
----------
msg['Subject'] = 'SMTP on Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'

'''

'''
import smtplib
from email.message import EmailMessage
sender = 'nandigambadrinadh4@gmail.com'
password = 'tcjlsecfjoxntaim'
msg = EmailMessage()
msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'karthikyedagiri@gmail.com'
msg.set_content('Hello This is a test email to verify that the email system is working correctly. Please ignore this message.Thank you.')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''

import smtplib
from email.message import EmailMessage
sender = "nandigambadrinadh4@gmail.com"
password = "tcjlsecfjoxntaim"
receiver = [
    "nadhbadri2@gmail.com",
    "badrinadhnandigam@gmail.com",
    "karthikyedagiri@gmail.com"
]
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
for email in receiver:
    msg = EmailMessage()
    msg["Subject"] = "Test Mail"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content(
    "Hello,\n\n"
    "This is a test email.\n\n"
    "Regards,\n"
    "Badrinadh"
)
    server.send_message(msg)

server.quit()

print("Emails sent successfully")
