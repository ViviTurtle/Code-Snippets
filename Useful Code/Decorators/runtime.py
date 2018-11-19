#!/usr/bin/env python3

import time

def show_runtime_27(func):
	"""
	Decorates any function via @show_runtime to show how long it takes to run
	Python 2.7 and 3.0 Version
	"""
	def wrapper(*args, **kwargs):
		print(f'===================RUNTIME===================')
		print(f'Calling {func.__name__}{args}, {kwargs}')
		start = time.clock()
		original_result = func(*args, **kwargs)
		end = time.clock()

		print(f'Returned {original_result} ')
		print(f'==============={end-start}===============\n')
		return original_result
	return wrapper

def show_runtime_38(func):
	"""
	Decorates any function via @show_runtime to show how long it takes to run
	Python 3.7+
	"""
	def wrapper(*args, **kwargs):
		print(f'=====================RUNTIME=====================')
		print(f'Calling {func.__name__}{args}, {kwargs}')
		start = time.perf_counter()
		original_result = func(*args, **kwargs)
		end = time.perf_counter()

		print(f'Returned {original_result} ')
		print(f'==============={end-start}===============\n')
		return original_result
	return wrapper

@show_runtime_27
def run_slow_27(name, line):
	""" Example slow function using python 2.7 show_runtime decoration"""
	for _ in range(10000000):
		pass
	return f'Slow 2.7: {name}: {line}'

@show_runtime_27
def run_fast_27(name, line):
	""" Example fast function using python 2.7 show_runtime decoration"""
	for _ in range(1000000):
		pass
	return f'Fast 2.7: {name}: {line}'

@show_runtime_38
def run_slow_38(name, line):
	""" Example slow function using python 3.7+ show_runtime decoration"""
	for _ in range(10000000):
		pass
	return f'Slow 3.8: {name}: {line}'

@show_runtime_38
def run_fast_38(name, line):
	""" Example fast function using python 3.7+ show_runtime decoration"""
	for _ in range(1000000):
		pass
	return f'Fast 3.8: {name}: {line}'

if __name__ == "__main__":
    run_slow_27('Jane', 'Hello, World')
    run_fast_27('Jane', 'Hello, World')
    run_slow_38('Jane', 'Hello, World')
    run_fast_38('Jane', 'Hello, World')

