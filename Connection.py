#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import pymysql.cursors
import ConfigParser


class Connection(object):
    def __init__(self):

        # load config
        conf = ConfigParser.ConfigParser()
        db_config_file = "db.properties"

        if not os.path.exists(db_config_file):
            print(">> sys.stderr, 'Couldn't get a db_properties[%s] file descriptor' % db_config_file")
            raise RuntimeError("DB Connection Failed")

        conf.read(db_config_file)

        self.host = conf.get('DB', 'HOST')
        self.user = conf.get('DB', 'USER')
        self.password = conf.get('DB', 'PASSWORD')
        self.db = conf.get('DB', 'DB')

    def connection(self):
        """return Mysql connection instance"""
        return pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)


if __name__ == '__main__':
    print(Connection().connection())
