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
		sql_file = file.read().replace("\n", " ")
	return sql_file


def find_keyword_blocks(keyword_name: str, txt: str) -> list:
	parsed = txt.split(keyword_name)
	return [" ".join(p.split(";")[0].split()) for p in parsed[1:]]


def create_table_parser(ct_block: str) -> TableConstraints:
	table_name = ct_block.split()[0]
	constraint = {}
	idx = ct_block.index("(")
	parsed = ct_block[idx+1:-1]
	for p in parsed.split(","):
		val = [word for word in CONSTRAINTS if word in p.upper()]
		constraint[p.split()[0]] = val
	return TableConstraints(table_name, constraint)


def check_diff(old_file: TableConstraints, new_file: TableConstraints) -> bool:
	pass


def main():
	file = read_sql_file("difference1-test.sql")
	ct_block_list = find_keyword_blocks("CREATE TABLE", file)
	for ct_block in ct_block_list:
		print(create_table_parser(ct_block))


if __name__ == "__main__":
	main()
