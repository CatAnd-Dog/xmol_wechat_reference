# -*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

class send_email():

    def __init__(self,smtpadress,smtpport,username,password):

        self.username=username
        self.password=password
        self.smtpadress=smtpadress
        self.smtpport=smtpport

    title="文献推送"
    def send_content(self,receivers,content):

    # 构建alternative结构
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(self.title)
        msg['From'] = formataddr(("oneperfect.cn--pushpaper", self.username))  # 昵称+发信地址(或代发)
        msg['To'] = receivers

#        msg['Reply-to'] = "aaa@bbb.com"  #用于接收回复邮件，需要收信方支持标准协议

        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()

        texthtml = MIMEText(content, _subtype='html', _charset='UTF-8')
        msg.attach(texthtml)

        # 若需要加密使用SSL，可以这样创建client
        client = smtplib.SMTP_SSL(self.smtpadress, self.smtpport)
        # SMTP普通端口为25或80
        # client = smtplib.SMTP('smtpdm.aliyun.com', 80)
        # 开启DEBUG模式
        client.set_debuglevel(0)
        # 发件人和认证地址必须一致
        client.login(self.username, self.password)
        # 备注：若想取到DATA命令返回值,可参考smtplib的sendmail封装方法:
        # 使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        # print(receivers)
        client.sendmail(self.username, receivers, msg.as_string())  # 支持多个收件人，最多60个
        client.quit()

