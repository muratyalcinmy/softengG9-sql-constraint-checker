import json
import sql_constraint_checker
from base64 import b64encode


def read_as_text(file_path):
    with open(file_path, 'r') as f:
        return f.read().replace('\n', ' ')


data = dict()
data['name'] = 'difference'
data['reminder'] = 'reminder'
data['old'] = b64encode(str(read_as_text('difference1-test.sql')).encode('utf-8'))
data['new'] = b64encode(str(read_as_text('difference2-test.sql')).encode('utf-8'))

sql_constraint_checker.main(json.dumps(data))
