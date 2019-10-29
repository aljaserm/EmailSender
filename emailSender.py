import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Meriel J'
# To is removed
email['subject'] = 'You won $1,000,000'
# email.set_content("I am from Python Planet")
email.set_content(html.substitute({'name':'Tim'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # password is removed
    smtp.login('pythonemailsenderztm@gmail.com', '')
    smtp.send_message(email)
    print('Sent!!!')
