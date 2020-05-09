# 邮件配置
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class email_set:
    def __init__(self):
        self.host = ''
        self.user = ''
        self.password = ''
        
    def sender(self, sender):
        self.sender = sender

    def send(self):
        if self.sender:

        else:
            print('error')

sender = "from@qq.com"
receiver = ['']
