print("###########################################	exo1	###############################\n")
class Pets():
	def __init__(self, animals):
		self.animals = animals #[Bengal.name,Chartreux.name,Siamese.name]
	def walk(self):
		for animal in self.animals:
			print(animal)

#Another class
#First class
class Cat():
	is_lazy = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def walk(self):
		print(f"{self.name} is just walking around")

#Another class
class Bengal(Cat):
	def sing(self, sounds):
		return f'{sounds}'
class Chartreux(Cat):
	def sing(self, sounds):
		return f'{sounds}'

#Another class which inherits from the Cat class
class Siamese(Cat):
	def sing(self, sounds):
		return f'{sounds}'

#Creating of instances of classes
Bengal=Bengal("Monkey",10)
Chartreux=Chartreux("Dog",8)
Siamese=Siamese("Mouse",7)
Pets1=Pets("Donkey")

#Making a list from instances classe
all_cats=[(Bengal.name,Bengal.age),(Chartreux.name,Chartreux.age),(Siamese.name,Siamese.age)]
print(f"All cats are : {all_cats} \n")

sara_pets=Pets1

print()
sara_pets.walk()
Bengal.walk()
Chartreux.walk()
Siamese.walk()

print()

print("###########################################	exo2	###############################")
class Dog:
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def bark(self):
		print(f"{self.name} bark")
	
	def run_speed(self,speed):
		self.speed = ((self.weight/self.age)*10)
		return self.speed
		#print(f"the speed of {self.name} is : {self.speed}")

	def fight(self):
		self.arg=other_dog.run_speed(25)

		if self.arg*self.weight > Dog1.weight*Dog1.run_speed(10):
			print(f"The winner is : {other_dog.name} \n")
		elif self.arg*self.weight < Dog1.weight*Dog1.run_speed(10):
			print(f"The winner is : {Dog1.name} \n")
		else:
			print("There is not a winner ! ")

Dog1 = Dog("Ray",14,150)
other_dog = Dog("boby",17,100)

Dog1.bark()
other_dog.bark()

print()

print(f"Speed of {Dog1.name} is : {Dog1.run_speed(10)}")
print(f"Speed of {other_dog.name} is : {other_dog.run_speed(25)}")

print()

other_dog.fight()

#print(f"The name of the main dog is : {Dog1.name}. He is {Dog1.age} years hold and he has {Dog1.weight} Kg")


print("###########################################	exo3	###############################\n")

