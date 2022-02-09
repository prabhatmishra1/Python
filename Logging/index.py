import logging
import contextlib
import requests
import http
from http.client import HTTPConnection
import pathlib
import os
# Get current file path
current_path = pathlib.Path(__file__).parent.absolute()
output_folder = os.path.join(current_path, 'Logs')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

filename = os.path.join(output_folder, 'request.log')

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 10

    logging.basicConfig(filename=filename, level=logging.DEBUG)
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    def print_to_log(*args):
      requests_log.debug(" ".join(args))
    print_to_log()

def debug_requests_off():
    '''Switches off logging of the requests module, might be some side-effects'''
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    '''Use with 'with'!'''
    debug_requests_on()
    yield
    debug_requests_off()


with debug_requests():
    resp=requests.post('http://httpbin.org/', data={'msg': 'asls'}, params={'ass':'as'})
