import os
import logging
import logging.handlers
import logging.config

log = None


class Logger(object):
    def __init__(self):

        global log

        if log is not None:
            return None

        logger_name = 'process_monitor'
        log_file_name = os.path.join("logs", "process_monitor.log")
        log_config_file = os.path.join("conf", "log.properties")
        log_dir = os.path.dirname(log_file_name)

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        # load config
        if not os.path.exists(log_config_file):
            print("Couldn't get a log_properties[{}] file descriptor. Applied to Default Value".format(log_config_file))
        else:
            logging.config.fileConfig(log_config_file)

        log = logging.getLogger(logger_name)
        log.debug("Log Directory : {}".format(log_dir))

    @staticmethod
    def get_logger():
        return log


if __name__ == '__main__':
    log = Logger().get_logger()

    log.debug('This is a debug message.')
    log.info('This is an info message.')
    log.warning('This is a warning message.')
    log.error('This is an error message.')
    log.critical('This is a critical message.')
