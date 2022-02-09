import http
import logging
import requests

# Set up logging to a file
logging.basicConfig(filename="app.log", filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Turn on global debugging for the HTTPConnection class, doing so will
# cause debug messages to be printed to STDOUT
http.client.HTTPConnection.debuglevel = 1

# Monkey patch the print() function and redirect it to a
# logger.debug() call
def print_to_log(*args):
    logger.debug(" ".join(args))
http.client.print = print_to_log
# Test HTTP GET and POST
url = "http://localhost:5000/test"
resp = requests.post(url, data='My Test Data')
