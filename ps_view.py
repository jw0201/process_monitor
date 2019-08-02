#!/usr/bin/python
# -*- coding:utf-8 -*-

from subprocess import Popen, PIPE
import socket

from notify import notify
from util import get_list_from_file, check_option


def process():
    query = "ps -ef"
    p = Popen(query, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    result = "".join(stdout).split("\n")

    return result


def get_process_list():
    return get_list_from_file('process.txt')


def ps_monitor(options):
    hostname = "[" + socket.gethostname() + "]"
    ip_address = socket.gethostbyname(socket.gethostname())
    subject = "Please Check the process list!!!"
    ps_list = get_process_list()
    process_lines = process()
    abnormal = []

    for ps in ps_list:
        processes = grep(ps, process_lines)
        if len(processes) == 0:
            abnormal.append(ps)
            print(ps)

    if len(abnormal) > 0:
        notify(abnormal, hostname, ip_address, options, subject)


def grep(keyword, process_lines):
    output = []

    for line in process_lines:
        if keyword in line:
            output.append(line)

    return output


if __name__ == "__main__":
    options = check_option()
    print(options)
    ps_monitor(options)
