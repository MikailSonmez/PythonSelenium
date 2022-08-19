import logging

# logging.basicConfig(filename="D:/seleniumlogs/test.log,
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("this is debug message")
logging.info("this is debug message")
logging.warning("this is debug message")
logging.error("this is debug message")
logging.critical("this is debug message")
