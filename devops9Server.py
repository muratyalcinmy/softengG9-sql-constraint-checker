##from __future__ import print_function
import time,sys,logging,requests
import ctypes
import datetime,threading
from flask import Flask, render_template, jsonify
#import getdist
app = Flask(__name__)

light_on = False
buffer_size = 0

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

@app.route('/start')
def start():
	'''
	# stop the function test
	global light_on
	light_on=True
	t1 = thread_with_exception('Thread 1')
	
	t1.start() 
	t1.raise_exception() 
	t1.join() '''
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
	logging.info("Main    : before creating thread")
	x = threading.Thread(target=thread_function, args=(1,))
	logging.info("Main    : before running thread")
	x.start()
	logging.info("Main    : wait for the thread to finish")
	#x.join()
	logging.info("Main    : all done")
	return "started"

@app.route('/stop')
def stop():
    global light_on
    light_on = False
    r = requests.get('http://localhost:5555/get')
    return 'stopped'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)



'''
@app.before_first_request
def light_thread():
    def run():
        global light_on
        while light_on:
            

    thread = threading.Thread(target=run)
    thread.start()
'''

'''
def func():
	with open('output.log', 'a', buffer_size) as f:
		while(light_on):
			f.write('{}\n'.format(datetime.datetime.now()))
			time.sleep(1)

class thread_with_exception(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 
              
	def run(self): 

	# target function of the thread class 
		try: 
			with open('output.log', 'a', buffer_size) as f:
				while(light_on):
					f.write('{}\n'.format(datetime.datetime.now()))
					time.sleep(1) 
		finally: 
			print('ended') 
	           
    def get_id(self): 
  
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure')
'''

# logmaker.py

 # This makes it so changes appear without buffering

