import requests
import logging
import time
import sys

def log_head_request_every_hour(url):
    # Initialize logging to stderr with date and time
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.StreamHandler(sys.stderr)])

    while True:
        try:
            response = requests.head(url)
            logging.info(f'Received status code: {response.status_code}')
        except Exception as e:
            logging.error(f'Error occurred: {e}')

        time.sleep(3600)  # Sleep for 3600 seconds (1 hour)

# Call the function with the URL you want to request
log_head_request_every_hour('http://example.com')
