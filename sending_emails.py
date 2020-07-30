import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# don't need this, because I have 2 factor authentication
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
PYTHON_TEST_PASS = os.environ.get('PYTHON_PASS')


msg = EmailMessage()
# enter the subject of your email
msg['Subject'] = ""
msg['From'] = EMAIL_ADDRESS
# enter the receiver
msg['To'] = ''
# enter your content
msg.set_content("""
   
""")

# enter which files you want to attach
files = [""]

for file in files:
    # enter your file path
    with open("" + file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PYTHON_TEST_PASS)
    smtp.send_message(msg)



