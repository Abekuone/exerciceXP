import random
import exo_XP
from exo_XP import Dog

#Choice of sentence
str1="fait un tonneau"
str2="se dresse sur ses pattes arrière"
str3="te serre la main"
str3="fait le mort"

#Building of the class
class PetDog(Dog):
	def __init__(self, trained = False):
		self.trained = trained

	def train(self):
		print(f"{Dog1.name} bark\n")
		self.trained = True
		return self.trained

	def play(self,*arg):
		print(f"{Dog1.name} , {Dog2.name} and {Dog3.name} play together\n")

	def do_a_trick(self):
		if True:
			print(Dog1.name, random.choice([str1, str2, str3]))
		else:
			pass

Dog1 = Dog("Ray",14,150)
Dog2 = Dog("Milou",14,200)
Dog3 = Dog("Mica",18,300)

Pd = PetDog("Boby")
Pd.train()
Pd.play()
Pd.do_a_trick()



