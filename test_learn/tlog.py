import logging
import logging.config
import log_format_conf


def alog():
    logging.config.dictConfig(log_format_conf.LOGGING_DIC)
    logging.getLogger().info("hahaha")


alog()
