#!/usr/bin/env python3
# Main source code was pulled from http://code.activestate.com/recipes/576684-simple-threading-decorator/
from threading import Thread

def run_async_thread(func):
	"""
	Decorator to run a function in a seperate thread.
	Only use when variables and resources will not be modified in following code
	"""
	def wrapper(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl
	return wrapper

if __name__ == '__main__':
	from time import sleep

	@run_async_thread
	def print_somedata():
		"""Just prints random data - this will ran 3 times concurrently (With async decorator"""
		print('starting print_somedata')
		sleep(2)
		print('print_somedata: 2 sec passed')
		sleep(2)
		print('print_somedata: 2 sec passed')
		sleep(2)
		print('finished print_somedata')

	def main():
		"""
		Used to POC Async decorator
		Will run print_somedata() with three concurrent threads
		Note: All prints happen in blocks every two seconds
		"""

		print_somedata()
		print('back in main')
		print_somedata()
		print('back in main')
		print_somedata()
		print('back in main')

	main()
