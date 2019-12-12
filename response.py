import requests, sys, json  #import main Flask class and request object
from sql_constraint_checker import TableCheck

def main():

	if len (sys.argv) != 3 :
		print ("Usage: python file.py filepath1 filepath2")
		sys.exit (1)
	

	data = {  
		"$schema": "http://json-schema.org/draft-04/schema#",
       		"title": "Response information for SQL constraint checking process",
     		"type": "object",
       		"description": "If constraints are proper failure = false(0) else true(1)",
       		"properties": {
       		"failure": {"type": "bool"},
       		},
      		"required": "failure",
		"destination":8
	       }
	
	sql_constraint_check=TableCheck(sys.argv[1], sys.argv[2], 'constraints.txt', 'data_types.txt')
	
	if(sql_constraint_check==False):
	    data["properties"]= " 'properties': {'failure': True }"
	else:
	     data["properties"]= " 'properties': {'failure': False }"
	
	dataJson = json.dumps(data)

	#r = requests.get(url = "http://localhost:8081/post", dataJson = dataJson) 
	r = requests.post(url = 'http://localhost:8081', dataJson = dataJson)
	print (r)


if __name__ == '__main__':
	main()
