import os
import logging.handlers


class myTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when, interval, backup_cnt):

        log_file_name = os.path.join(filename)
        log_dir = os.path.dirname(log_file_name)

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        super(myTimedRotatingFileHandler, self).__init__(log_file_name, when, interval, backup_cnt, encoding="utf8")
