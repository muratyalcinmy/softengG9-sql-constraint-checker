import json
import sql_constraint_checker
from base64 import b64encode


def read_as_text(file_path) -> str:
    with open(file_path, 'r') as f:
        return f.read().replace('\n', ' ')


data = dict()
data['name'] = 'difference'
data['old'] = b64encode(bytes(read_as_text('difference1-test.sql'), 'utf-8')).decode('utf-8')
data['new'] = b64encode(bytes(read_as_text('difference2-test.sql'), 'utf-8')).decode('utf-8')

sql_constraint_checker.main(json.dumps(data))
