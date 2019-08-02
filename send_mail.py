#!/usr/bin/python
# -*- coding:utf-8 -*-
import ConfigParser
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
from email import Utils
from email.header import Header

from util import get_list_from_file


class Mail(object):
    def __init__(self):

        # load config
        conf = ConfigParser.ConfigParser()
        config_file = "mail.properties"

        if not os.path.exists(config_file):
            print(">> sys.stderr, 'Couldn't get a mail_properties[%s] file descriptor' % config_file")
            raise RuntimeError("Mail Send Fail")

        conf.read(config_file)

        self.smtp_server = conf.get('MAIL', 'SMTP_SERVER')
        self.port = conf.get('MAIL', 'PORT')
        self.userid = conf.get('MAIL', 'USERID')
        self.passwd = conf.get('MAIL', 'PASSWD')

    def send_mail(self, from_user, to_users, cc_users, subject, text, attach):
        commaspace = ", "
        msg = MIMEMultipart("alternative")
        msg["From"] = from_user
        msg["To"] = commaspace.join(to_users)
        msg["Cc"] = commaspace.join(cc_users)
        msg["Subject"] = Header(s=subject, charset="utf-8")
        msg["Date"] = Utils.formatdate(localtime=1)
        msg.attach(MIMEText(text, "html", _charset="utf-8"))

        if attach is not None:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(attach, "rb").read())
            Encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % os.path.basename(attach))
            msg.attach(part)

        smtp = smtplib.SMTP_SSL(self.smtp_server, self.port)
        smtp.login(self.userid, self.passwd)
        smtp.sendmail(from_user, to_users, msg.as_string())
        smtp.close()


def get_emails():
    return get_list_from_file('email.txt')
