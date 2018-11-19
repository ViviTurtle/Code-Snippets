# Formatting used from Python Tricks the Book: A Buffet of Awesome Python Features
class Fruits_v1(object):
	"""Normal Class implementation"""
	def __init__(self, name):
		self.name = name


class Fruits_v2(object):
	"""
	Python Version 3.0+
	Class Rep with str and repr
	"""
	def __init__(self, name):
		self.name = name
	def __str__(self):
		"""When printed, this will print a human-friendly format"""
		return(f'This fruits is a {self.name!r}')
	def __repr__(self):
		"""when queries in REPL, will show how this object was made"""
		return(f'{self.__class__.__name__}({self.name!r})')


class Fruits_v3(object):
	"""
	Python Version 2.X
	Class Rep with str and repr
	Python String interpreted are encoded in bytes via __unicode__
	__string__() just encodes __unicode__() in utf-8
	"""
	def __init__(self, name):
		self.name = name
	def __unicode__(self):
		"""When printed, this will print a human-friendly format"""
		return u'This fruits is a {self.name}'.format(self=self)
	def __repr__(self):
		"""when queries in REPL, will show how this object was made"""
		return '{class_name}({name})'.format(class_name=self.__class__.__name__, name=self.name)
#	def __unicode__(self):
#		"""When printed, this will print a human-frie™ndly format"""
#		return unicode(self).encode("utf-8")


if __name__ == "__main__":
	fruit_v1 = Fruits_v1("apple")
	fruit_v2 = Fruits_v2("apple")

	print(fruit_v1)
	print(fruit_v2)
	# >>> fruit_v1
	# <__main__.Fruits_v1 object at 0x105492390>
	# >>> fruit_v2
	# Fruits_v2(apple)

