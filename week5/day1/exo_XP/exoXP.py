print("###################################  EXO_XP DAY5##################################\n")
##################################################################################################
print("######################################   QUESTION 1    ################################\n")

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        self.liste = []

Cat1=Cat("Boby",7)
Cat2=Cat("Madou",14)
Cat3=Cat("Fely",9)

print("The first cat is ", Cat1.name, "He is ", Cat1.age,"years hold")
print("The second cat is ", Cat2.name, "He is ", Cat2.age,"years hold")
print("The third cat is ", Cat3.name, "He is ", Cat3.age,"years hold""\n")

list_cat=[[Cat1.name,Cat1.age], [Cat2.name,Cat2.age], [Cat3.name,Cat3.age]]
print("The list of all cats is : ",list_cat,"\n")
#function to find the holdest cat in the list of cat
def holdcat():
    defaul_age=0
    defaul_name="Cat.name"

    for i in range(len(list_cat)):

        if list_cat[i][1]>defaul_age:
            defaul_age=list_cat[i][1]
            defaul_name=list_cat[i][0]
    print("The holdest cat is : ",defaul_name,"He is ",defaul_age,"years hold""\n")
holdcat()
##################################################################################################
print("######################################   QUESTION 2    ################################\n")

class Dog(object):
    def __init__(self, name,height):
        self.name=name
        self.height=height
    def bark(self):
        print(f"{self.name} will WOOF!")

    def jump(self):
        print(f"{self.name} jump {self.height*2} meters")

Davidog=Dog("Rex",50)
Davidog.bark()
Davidog.jump()

print()
sarahs_dog=Dog("Teacup",20)
sarahs_dog.bark()
sarahs_dog.jump()

print()
if sarahs_dog.height > Davidog.height:
    print(f"{sarahs_dog.name} is the biggest dog !")
else:
    print(f"{Davidog.name} is the biggest dog")

##################################################################################################
print("######################################   QUESTION 3    ################################\n")

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
stairway=Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()        

##################################################################################################
print("######################################   QUESTION 4    ################################\n")

class Zoo(object):
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals=[]
    
    def add_animal(self,new_animal):
        self.new_animal=new_animal
        if Zoo.new_animal not in self.animals:
            self.animals.append(Zoo.new_animal)
        else:
            pass
        print("The list of new_animal is : ",self.animals)
  
    def get_animals(self):
        for i in self.animals:
            print("The list of animal in the zoo is : ",i)
    
    def sell_animal(self,animal_sold):
        self.animal_sold=animal_sold
        for i in self.animals:
            if self.animal_sold != i:
                self.animals.remove(i)
            else:
                pass

print()

def sort_animals(l):
    return l[0]=="C"
def sort_animals1(l):
    return l[0]=="D"

l=["Cat","Dog","chiken","Cow","Dodou"]

filtered_animals = filter(sort_animals, l)
filtered_animals1 = filter(sort_animals1, l)

C_list=list(filtered_animals)
D_list=list(filtered_animals1)

print("The list of the objects start by {C} is : ", C_list)
print("The list of the objects start by {D} is : ", D_list)

print()

def get_groups():
    for i in D_list:
        print(i," is in group C. ")
    for j in C_list:
        print(j," is in group D. ")
get_groups()

l=["Cat","Dog","chiken","Cow","Dodou"]

Zoo=Zoo("MyZoo")
Zoo.add_animal(l)
Zoo.get_animals()
Zoo.sell_animal(l)

#########################################################################################
print("###############################     E.N.N     ########################################\n")

"""
We can use the object ramat_gan_safari and call all the methods
like this 
ramat_gan_safari=Zoo("MyZoo")
ramat_gan_safari.add_animal(l)
ramat_gan_safari.get_animals(l)
ramat_gan_safari.sell_animal(l)
"""