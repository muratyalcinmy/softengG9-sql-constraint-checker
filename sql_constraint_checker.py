from typing import NamedTuple
import re


CONSTRAINTS = [
	"NOT NULL",
	"UNIQUE",
	"PRIMARY KEY",
	"FOREIGN KEY",
	"CHECK",
	"DEFAULT",
	"INDEX"
]


class TableConstraints(NamedTuple):
	table_name: str
	constraint: dict


def read_sql_file(file_path) -> str:
	with open(file_path, 'r') as file:
		sql = file.read().replace("\n", " ")
	return sql


def find_keyword_blocks(keyword_name: str, txt: str) -> list:
	parsed = re.split(keyword_name, txt)
	return [" ".join(p.split(";")[0].split()) for p in parsed[1:]]


def get_constraints(file) -> TableConstraints:
	pass


def check_diff(old_file: TableConstraints, new_file: TableConstraints) -> bool:
	pass


def main():
	file = read_sql_file("sample_input.sql")
	print(find_keyword_blocks("CREATE TABLE", file))


if __name__ == "__main__":
	main()
