import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

log_files = [f'log{i}.log' for i in range(1, 4)]

def api_call(data, log_file):
    """Simulate an API call and log to a specific file"""
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f'Calling API with data: {data}')
    logger.info('API call successful')

def process_data(data):
    """Process data and log at different stages"""
    for log_file in log_files:
        log_entry = {
            'level': 'info',
            'log_string': f'Processing data: {data}',
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'metadata': {
                'source': log_file
            }
        }
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        log_entry['log_string'] = 'Stage 1: Preparing data'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        log_entry['log_string'] = 'Stage 2: Calling API'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        api_call(data, log_file)

        log_entry['log_string'] = 'Stage 3: Post-processing data'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        log_entry['log_string'] = 'Data processing complete'
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')



