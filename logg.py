import logging
import logging .config
'''
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message')
'''


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%m/%d/%Y %H:%M:%S')

#creating my own logger, its great pratice to create
# your own logger
# import helper


#unwanted 

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")


#helpful for troubleshooting issues
'''
import traceback

try:
    a =[1,2,3]
    val=a[4]
except:
    logging.error( "The error is %s", traceback.format_exc())

'''
#rotating file handler
#Have a large application

from logging.handlers import RotatingFileHandler

