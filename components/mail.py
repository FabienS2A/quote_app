# pip install redmail
from redmail import EmailSender
from dotenv import load_dotenv
import os
# mot de passe d'application google
# compte
# * sécurité 
# * * validation en deux étapes
# * * * mot de passe d'application 
# * * * - créer une nouvelle application pour avoir le mot de passe

def send_email_alert():
    '''Send an email to alert the app has been used'''
    
    load_dotenv(dotenv_path='./components/.env')

    email = EmailSender(
        host='smtp.gmail.com',
        port=587,
        username=os.getenv("mail"),
        password=os.getenv("app_pwd")
        )

    email.send(
        subject="<Someone ask for a Day Quote>",
        sender=os.getenv("mail"),
        receivers=[os.getenv("mail")],
        text="Be gracefull !!! Someone uses your app and most probably, you enlighted his/her day.",
        html="<h1>Be gracefull !!! Someone uses your app and most probably, you enlighted his/her day.</h1>"
    )