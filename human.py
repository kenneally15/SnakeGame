#Class Human

class Human:

	def __init__(self, name="None", age=0):
		self.name = name
		self.age = age

	def say(self, msg):
		print("{name}: {message}".format(name=self.name, message=msg))


	
