import importlib
from log.Logger import Logger

from leef_format import make_header
from send_mail import Mail, get_emails
from send_qradar import send_qradar


def notify(abnormal, hostname, ip_address, options, subject):
    log = Logger().get_logger()

    if "mail" in options:
        ps_names = "<br>".join(abnormal)
        mail = Mail()
        mail.send_mail("<>", get_emails(), [], "[" + ip_address + "] " + subject, ps_names, None)
        log.info("[mail] %s %s %s %s" %(get_emails(), ip_address, subject, ps_names))

    if "syslog" in options:
        ps_names = ",".join(abnormal)
        message = '%shostname=%s\tprocess=%s\t' % (make_header(ip_address), hostname, ps_names)
        log.info('[syslog] %shostname=%s\tprocess=%s\t' % (make_header(ip_address), hostname, ps_names))
        send_qradar(message)

    if "db" in options:
        insert_db = importlib.import_module("insert_db")
        ps_names = ",".join(abnormal)
        message = 'hostname=%s\tip=%s\tprocess=%s\t' % (hostname, ip_address, ps_names)
        log.info('[db] hostname=%s\tip=%s\tprocess=%s\t' % (hostname, ip_address, ps_names))
        insert_db.insert_db(message)
