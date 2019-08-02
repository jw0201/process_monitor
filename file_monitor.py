#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
import socket

from Config import Config
from notify import notify
from util import check_option


def get_mtime(path_to_file):
    stats = os.stat(path_to_file)
    return stats.st_mtime


def get_now_timestamp():
    return time.time()


def log_monitor(options):
    conf = Config()
    hostname = "[" + socket.gethostname() + "]"
    ip_address = socket.gethostbyname(socket.gethostname())
    subject = "Please Check the sensor log file!!!"
    abnormal = []

    log_path = "/path/to/log"
    abnormal.append("{} is delayed over {} seconds".format(log_path, conf.file_delay))

    if get_now_timestamp() - get_mtime(log_path) > conf.file_delay:
        notify(abnormal, hostname, ip_address, options, subject)


if __name__ == "__main__":
    options = check_option()
    print(options)
    log_monitor(options)
