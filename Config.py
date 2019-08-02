import os
import ConfigParser


class Config(object):
    def __init__(self):
        # load config file
        config_file = "config.ini"

        if not os.path.exists(config_file):
            print("Couldn't get a vm_agent config[{}] file descriptor".format(config_file))
            raise RuntimeError("Config File Not Found")

        conf = ConfigParser.ConfigParser()
        conf.read(config_file)

        self.file_delay = float(conf.get('FILE_MONITOR', 'FILE_DELAY'))
        self.syslog_address = conf.get('SYSLOG', 'ADDRESS')


if __name__ == '__main__':

    conf = Config()
    members = vars(conf)
    for k, v in members.items():
        print("{}: {}".format(k, v))
