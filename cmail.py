import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('abhiabhilash80971@gmail.com','ixsx jwdg skmu jetv')
    msg=EmailMessage()
    msg['FROM']='abhiabhi80971@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()



