import logging

#creating your own internal logger
# logger = logging.getLogger(__name__)
# logger.propagate = False #by default it is true
# logger.info("Hello from helper")

logger = logging.getLogger(__name__)

#create my own handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# for each handler , set level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#adding our handler to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is warning')
logger.error('This is error')


