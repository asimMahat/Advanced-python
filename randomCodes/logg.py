# import logging

# logging.basicConfig(level = logging.DEBUG)
# logging.debug("This will get logged")

# logging.basicConfig(filename='app.log', filemode ='w',
# format = '%(name)s - %(levelname)s - %(message)s')
# logging.warning("This will get logged to a file")

# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning("This is a warning")

# logging.basicConfig(format='%(asctime)s-%(message)s', level = logging.INFO)
# logging.info('Admin logged in')


# logging.basicConfig(format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

# name = "John"
# logging.error(f'{name} raised an error',)


#capturing stack tress
'''
import logging

a=5
b=0

try:
    c=a/b
except Exception as e:
    # logging.error("Exception occured",exc_info=True)
    logging.exception("Exception occurred")

'''

#creating our custom logger and using handlers

'''

import logging
#create a custom logger
logger = logging.getLogger(__name__)

#create handlers

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#create formatters and add it to the handlers

c_format = logging.Formatter('%(name)s - %(levelname)s-%(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s- %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#add handlers to the logger

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

'''

# Other configuration methods

import logging
import logging.config

logging.config.fileConfig(fname ='logging.conf', disable_existing_loggers=False)

#get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
