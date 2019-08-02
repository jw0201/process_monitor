#!/usr/bin/python
# -*- coding:utf-8 -*-
from decorator import connection


@connection
def insert_db(conn, msg):

    sql = """
        INSERT INTO process_monitor (alarm_message) VALUES ('%s')
    """

    cur = conn.cursor()
    cur.execute(sql % msg)


if __name__ == "__main__":
    try:
        insert_db("this is message")
    except Exception, Err:
        print("Exception: %s" % (str(Err)))
