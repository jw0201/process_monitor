import logging
import logging.handlers
from Config import Config


def send_qradar(msg):

    conf = Config()
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.INFO)
    handler = logging.handlers.SysLogHandler(address=(conf.syslog_address, 514))
    my_logger.addHandler(handler)
    my_logger.info(msg)
