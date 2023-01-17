class Farm(object):
	def __init__(self, nom_Farm):
		self.nom_Farm =nom_Farm
		print("McDonald's farm""\n")
	
	def add_animal(self,name,age=2):
		self.name=name
		print(name,":",age,"\n")
		
	
	def get_info(self):
		print("\tE-I-E-I-0!\n")
	
	def get_animal_types(self):
		self.list_animals=[macdonald1.name,macdonald2.name,macdonald3.name]
		return sorted(self.list_animals)

	def get_short_info(self):
		print(f"McDonald’s farm has {sorted(self.list_animals)}")

macdonald=Farm("McDonald")
macdonald1=Farm("McDonald")
macdonald2=Farm("McDonald")
macdonald3=Farm("McDonald")	


macdonald1.add_animal("cow",5)
macdonald2.add_animal('sheep')
macdonald3.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()

