import json
from datetime import datetime

from newproject.log import log_files


def query_logs(level=None, log_string=None, timestamp=None, source=None):
    """Query logs based on criteria"""
    results = []
    for log_file in log_files:
        with open(log_file, 'r') as f:
            logs = f.readlines()

            for log in logs:

                log_entry = json.loads(log)

                if (not level or log_entry['level'] == level) and \
                   (not log_string or log_string in log_entry['log_string']) and \
                   (not timestamp or timestamp == log_entry['timestamp']) and \
                   (not source or source == log_entry['metadata']['source']):
                    results.append(log_entry)
    return results

print('All logs:')
for log in query_logs():
    print(log)

print('\nLogs with "Stage 2" in the message:')
for log in query_logs(log_string='Stage 2'):
    print(log)

print('\nLogs from the last log file:')
for log in query_logs(source='log3.log'):
    print(log)

print('\nLogs between a specific timestamp range:')
start_time = datetime(2023, 9, 15, 8, 0, 0)
end_time = datetime(2024, 9, 15, 8, 0, 10)
for log in query_logs(timestamp=start_time.isoformat() + 'Z'):
    if log['timestamp'] <= end_time.isoformat() + 'Z':
        print(log)
    else:
        break
