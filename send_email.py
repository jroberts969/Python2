import smtplib, ssl


def send_email(receiver, message):
    password = "eeldhzhbszwnpeid"
    username = "dr.jonathan.roberts@googlemail.com"
    host = "smtp.gmail.com"
    port = 465
    #receiver = "j_droberts@yahoo.co.uk"
    context = ssl.create_default_context()
    #message1 = "hi, how are you"
    message_to_send = f'''Subject: A plain text email
{message} '''

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_to_send)
        print("success!")



