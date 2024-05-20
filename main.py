from newproject.log import process_data
import time
process_data('Sample data')


time.sleep(2)

from newproject.query import query_logs

print('All logs:')
for log in query_logs():
    print(log)

