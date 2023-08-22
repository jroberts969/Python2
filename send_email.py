import smtplib, ssl

password = "eeldhzhbszwnpeid"
username = "dr.jonathan.roberts@googlemail.com"

host = "smtp.gmail.com"
port = 465


receiver = "j_droberts@yahoo.co.uk"
context = ssl.create_default_context()
message  = "hi, how are you"

email_string = f'''Subject: A plain text email
This is a new test email sent by Python.'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, email_string )

print("success")
