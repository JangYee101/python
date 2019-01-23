import os
import logging
import logging.handlers
log_file = 'my.log'

logger = logging.getLogger('JY')
#日志文件大小最大为1024k，文件个数最多4个，my.log存放最新日志，my.log4存放最旧日志
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024, backupCount=3)

fmt = '%(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(1,1000):
    logger.error('test %d' % i)

