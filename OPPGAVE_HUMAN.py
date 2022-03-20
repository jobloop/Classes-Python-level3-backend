# Oppgave: 
# 1 ) lag tre til objekter av klassen. Du ser et objekt kalt Bob
# 2 ) lag minst en metode til i klassen som forteller hvilken 
# hobby/interesse objektet har.

class human:
	def __init__(self, gender, firstname, surname):
		self.gender = gender
		self.firstname = firstname
		self.surname = surname

	def speak(self):
		print(f"Hello, I'm {self.firstname}") 

	def sleep(self):
		print("zzzzzz")

	def eat(self):
		print("omnomnom")

	def walk(self):
		print(f'{self.firstname} is moving forward')

	def grab(self):
		print("I'll have that")


bob = human("Male", "Bob", "Roberts")
bob.speak()
bob.sleep()
bob.eat()
bob.walk()
bob.grab()