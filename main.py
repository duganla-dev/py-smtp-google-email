import smtplib
from email.message import EmailMessage
import requests

def send_email_allert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    account =
    account = json.load(account)

    user = account['user']
    password = account['password'] 
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()

subject = "Email Subject"
body = "Email Body"
sendto = "someone@anymail.com"
send_email_allert(subject, body, sendto)
