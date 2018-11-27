class Animals:
	total_animals = 0
	def __init__(self, name, color, food, hair, environment):
		self.name = name
		self.color = color
		self.food = food
		self.hair = hair
		self.environment = environment
		self.__class__.total_animals += 1

	@classmethod
	def monkey(cls):
		""" Creates a monkey"""
		return cls("monkey", "brown", "bananas", "furry", "trees")

	@classmethod
	def sloth(cls):
		""" Creates a sloth"""
		return cls("sloth","white", "bamboo", "furry", "trees")


	@classmethod
	def rat(cls):
		""" Creates a rat"""
		return cls("rat","grey", "chesse", "varies", "homes")

	def __str__(self):
		return(f'I am a {self.color} {self.name} that likes {self.food} and lives in {self.environment}')



test_monkey = Animals.monkey()
test_sloth = Animals.sloth()
test_rat = Animals.rat()

print(test_monkey)
print(test_sloth)
print(test_rat)