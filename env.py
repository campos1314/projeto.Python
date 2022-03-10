import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from time import sleep

#1 startar o servidor smtp
host = 'smtp.gmail.com'
port = '587'
login = 'familiabuscape.1931@gmail.com'
senha = 'matheus99'
tempo = time.strftime('%H:%M:%S', time.localtime())

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login,senha)

html = """\
<html>
  <head></head>
  <body>
    <p align="left"">
        <strong>
        Olá Dona Maria
        </strong>
    </P>
  </body>
</html>
"""

corpo = 'Ideias '
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = 'universal.maria@gmail.com'
email_msg['Subject'] = 'Maria a hora certa é:'


email_msg.attach(MIMEText(tempo,'plain'))
server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

server.quit()
print('Email enviado com sucesso')
