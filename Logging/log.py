import logging
import pathlib
import os
# Get current file path
current_path = pathlib.Path(__file__).parent.absolute()
output_folder = os.path.join(current_path, 'Logs')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

filename = os.path.join(output_folder, 'example.log')
logging.basicConfig(filename=filename, format='%(levelname)s:%(asctime)s:%(message)s',
                    filemode='w', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
