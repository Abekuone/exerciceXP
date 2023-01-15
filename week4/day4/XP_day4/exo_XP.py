############################EXO_XP_DAY4####################################

print("############################EXO1####################################")

def display_message():
	print("In this curse I learn functions and the functions arguments.")
display_message()

print("############################EXO2####################################")
def favorite_book(title):
	print(title.upper())

favorite_book(title="One of my favorite books is <>the strange fate of Wangrin<>")

print("############################EXO3####################################")

def describe_city(city,country="USA"):
	print(city, "is in ",country)
describe_city("New York")
#giving default value to a parameter

print("############################EXO4####################################")
import random
from random import randint
def randm(nb1):
	nb2=randint(1,nb1)
	print("nb1 ======>",nb1)
	print("nb2 ======>",nb2)
	if nb1==nb2:
		print("It is the same numbers")
	else:
		print("It is not the same numbers")
randm(50)

print("############################EXO5####################################")
def make_shirt(size=72,text="I love Python !"):
	print("The size of the shirt is <",size,"> and the text is : <",text.upper(),">")

make_shirt(14,"bekaroom center is a web business center")
make_shirt()
make_shirt(size=21,text="I also love C !")

print("############################EXO6####################################")


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
	for i in magician_names:
		print(i)
show_magicians(magician_names)
print("\n")

#Modify the magician_names

def make_great(magician_names):
	for i in magician_names:
		i=i+" The great"
		print(i)
make_great(magician_names)
print("\n")


print("############################EXO7####################################")

import random
from random import randint
def get_random_temp(**saison):
    #tmp=randint(-10,40)
    #return tmp
    for keys, value in saison.items():
    	print(keys, " ===========> ",value)

def main():
	temp=input("Input a saison : ")

	if temp.upper()=="SUMMER":
		print(" An exemple of temperature of SUMMER is : ",randint(25,35))
	elif temp.upper()=="WINTER":
		print(" An exemple of temperature of WINTER is : ",randint(-10,14))
	elif temp.upper()=="AUTUMN":
		print(" An exemple of temperature of AUTUMN is : ",randint(15,20))
	elif temp.upper()=="SPRING":
		print(" An exemple of temperature of SPRING is : ",randint(20,25))


	
	n_mouth=int(input("Input a number of a mouth : "))
	while n_mouth not in range(12):
		n_mouth=int(input("Input a good number betwen 1 and 12 : "))
	if n_mouth in range(7,9):
		print("We are  in SUMMER")
	elif n_mouth in range(10,12):
		print("We are  in AUTUMN")
	elif n_mouth in range(1,3):
		print("We are  in WINTER")
	elif n_mouth in range(4,6):
		print("We are  in SPRING")



get_random_temp(Summer=randint(25,35),Winter=randint(-10,14),Autumn=randint(15,20),Spring=randint(20,25))




"""
	#print("The current temperature is",b,"degrees Celcius""\n")
	
	if ba<0:
		print("Hello Laure ! It's very freezing today! Wear extra layers")
	elif ba>0 and b<=16:
		print("Quite cold ! So don't forget your coat")
	elif ba>16 and b<=23:
		print("The weather is nice today")
	elif ba>23 and b<=32:
		print("It's a little hot today")
	elif ba>32 and b<=40:
		print("It's very hot today, let's go swimming")
	else:
		print("It's like you're in an oven")
	#sai=input("Input a a name of a saison : ")
"""
main()







