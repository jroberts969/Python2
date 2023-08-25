import smtplib, ssl
import os

def send_email(receiver, message, option):
    #password = "eeldhzhbszwnpeid"
    password = os.getenv("PASSWORD")

    username = "dr.jonathan.roberts@googlemail.com"
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    message_to_send = f'''Subject: {option}
{message} , {username}'''


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_to_send)
        print("success!")



