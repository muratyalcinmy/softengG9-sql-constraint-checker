import requests, sys, json  #import main Flask class and request object

def main():

	if len (sys.argv) != 3 :
		print ("Usage: python file.py filepath1 filepath2")
		sys.exit (1)
	

	data = {"name" : "Burak", "age" : "35" } 

	constraint_checker_func(sys.argv[1], sys.argv[2])

	r = requests.get(url = "http://localhost:5000/post", json = data) 

	print (r)

def constraint_checker_func(file1, file2):

	F = open(file1,"r") 
	
	print (F.read()) 

	F2 = open(file2,"r") 
	
	print (F2.read()) 


if __name__ == '__main__':
	main()
