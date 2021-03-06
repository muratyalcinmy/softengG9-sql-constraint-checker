import os
import json
import requests
import logging.config
from base64 import b64decode
from collections import namedtuple

logging_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.ini')
logging.config.fileConfig(fname=logging_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

Table = namedtuple('Table', ['name', 'body'])


class SQLParse(object):
	@staticmethod
	def find_blocks(text, keyword_name):
		detect_bgn = text.split(keyword_name)[1:]
		parsed_blocks = []
		for each in detect_bgn:
			detect_end = each.split(';')[0]
			purify_spc = ' '.join(detect_end.split())
			parsed_blocks.append(purify_spc)
		return parsed_blocks

	@staticmethod
	def read_as_list(file_path):
		with open(file_path, 'r') as f:
			return f.read().split()


class TableParse(SQLParse):
	def __init__(self, sql_text, filename_constraints, filename_data_types):
		self.__upper_text = sql_text.upper()
		self.__constraints = self.read_as_list(filename_constraints)
		self.__data_types = self.read_as_list(filename_data_types)

	def parse(self):
		return [self.__table_parser(block) for block in self.find_blocks(self.__upper_text, 'CREATE TABLE')]

	def __table_parser(self, block):
		name_idx = block.find(' ')
		name_str = block[:name_idx]
		body_idx = block.find('(')
		body_str = block[body_idx+1:-1]
		body = {}
		for line in body_str.split(','):
			col_part = ''.join(s for s in line if s.isalpha() or s.isspace()).split()
			col_name = ' '.join([s for s in col_part if s not in self.__constraints and s not in self.__data_types])
			col_cons = [' '.join([s for s in col_part if s in self.__constraints])]
			if col_name in body:
				body[col_name] += col_cons
			else:
				body[col_name] = col_cons
		return Table(name_str, body)


class TableCheck:
	def __init__(self, old_text, new_text, filename_constraints, filename_data_types):
		self.__table_old = TableParse(old_text, filename_constraints, filename_data_types).parse()
		self.__table_new = TableParse(new_text, filename_constraints, filename_data_types).parse()
		self.__check_new = []
		self.__check_err = []

	def diff(self):
		result = self.__check_diff()
		if result:
			logger.info('-----> ALLOWED!')
			for each in self.__check_new:
				logger.info('-----> ADDED:')
				logger.info(each)
		else:
			logger.info('-----> NOT ALLOWED!')
			for each in self.__check_err:
				logger.info('-----> ERROR:')
				logger.info(each)
		return result

	def __check_diff(self):
		for new in self.__table_new:
			try:
				old = next(old for old in self.__table_old if old.name == new.name)
				if set(old.body).issubset(set(new.body)):
					for new_col_name, old_col_name in zip(new.body, old.body):
						if new_col_name == old_col_name:
							if set(new.body[new_col_name]) != set(old.body[old_col_name]):
								tbl = 'TABLE NAME: {} | '.format(new.name)
								col = 'COLUMN NAME: {} | '.format(new_col_name)
								dif = 'DIFFERENCE: {} != {}'.format(new.body[new_col_name], old.body[old_col_name])
								self.__check_err.append(tbl + col + dif)
				else:
					self.__check_err.append('COLUMN REMOVE IS DETECTED IN \'{}\''.format(new.name))
			except StopIteration:
				self.__check_new.append(new)
		return False if self.__check_err else True


def main(json_obj):
	data = json.loads(json_obj)
	old_text = str(b64decode(data['old']).decode('utf-8'))
	new_text = str(b64decode(data['new']).decode('utf-8'))

	output = dict()
	output['name'] = data['name']
	output['reminder'] = data['reminder']
	output['result'] = TableCheck(old_text, new_text, 'constraints.txt', 'data_types.txt').diff()
	output['op'] = 'check'
	output['origin'] = 9
	output['destination'] = 8

	logger.info('-----> RESULT: ' + str(output['result']))

	# r = requests.post('http://localhost:8081/', json=output)
	# logger.info('-----> RESPONSE: ' + str(r.status_code))
