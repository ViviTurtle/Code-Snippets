def trace(func):
	""" Decorates any function via @trace with a Calling / Return Statement for debugging issues"""
	def wrapper(*args, **kwargs):
		print(f'TRACE: calling {func.__name__}() '
				f'with {args}, {kwargs}')

		original_result = func(*args, **kwargs)

		print(f'TRACE: {func.__name__}() '
			f'returned {original_result!r}')

		return original_result
	return wrapper

@trace
def say(name, line):
	""" Example decoration using trace"""
	return f'{name}: {line}'

#main
say('Jane', 'Hello, World')