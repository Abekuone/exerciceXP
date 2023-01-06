print("\t""\t""############   The exercises of day 2""\n""\n")


print("###################     EXO1      ####################################################""\n")
my_fav_numbers = set("4879")
my_fav_numbers.add("2")
my_fav_numbers.add("1")
my_fav_numbers.pop()
print(my_fav_numbers)
#My friend numbers
friend_fav_numbers=set("35")
print(friend_fav_numbers)
#Updating
my_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbers,"\n""\n")



print("###################     EXO2      ####################################################""\n")

print("It\'s not possible to add more integers to a tuple because it has only 2 elements""\n""\n")



print("###################     EXO3      ####################################################""\n")
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0]
del basket[-1]
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket=[]
print(basket,"\n""\n")


print("###################     EXO4      ####################################################""\n")
print(
"1-An integer is a number without a decimal point. A float is a floating-point number, it is a number that has a decimal place."
"\n""2- Yes there is another way to generate a sequence of floats, by using random"

	)
liste = [i*0.5 for i in range(3,11)]
print(liste,"\n""\n")


print("###################     EXO5      ####################################################""\n")
a=[i for i in range(1,21)]
print(a,"\n")
for i in range(len(a)):
    if i%2==0:
    	print(a[i])
    else:
    	pass
print("\n""\n")



print("###################     EXO6      ####################################################""\n")
name=str(input("Enter your name : "))
while name==("Armel"):
	name=str(input("Enter your name : ""\n""\n"))


print("###################     EXO7      ####################################################""\n")
fruits=str(input ("Input your favorite fruit separated by a single space : "))
list_fruit=fruits.split()
choice=str(input("Enter a name of fruit : "))
if choice in list_fruit:
	print("You chose one of your favorite fruits! Enjoy !""\n""\n")
else:
	print("You chose a new fruit. I hope you enjoy""\n""\n")


print("###################     EXO8      ####################################################""\n")
number=int(input("Enter the number of children : "))
liste_price=[]
for i in range(number):
	age=int(input("Enter the age of the child : "))
	if age<3:
		price=0
	elif age >=3 and age <=12:
		price=10
	elif price>12 :
		price=15
	print("This  child paid ",price,"$""\n")
	liste_price.append(price)
	som=sum(liste_price)
print("You totaly pay ",som,"$""\n""\n")

print("###################     EXO9      ####################################################""\n")

list_name=["Armel","Sidiki","Franck"]
for name in range(len(list_name)):
	age_child=int(input("What is your age ? : "))
	if age_child <16 or age_child>21:
		 list_name.remove(list_name[name])
print("The final autorized name are :",list_name)

print("###################     EXO10      ####################################################""\n")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
for i in range(len(sandwich_orders)):
	finished_sandwiches=sandwich_orders[i]
	print("I cooked your ",finished_sandwiches)
print("\n""\n")


print("\t""###################     EXO11      ####################################################""\n")

sandwich_orders[1]="Pastrami sandwich"
sandwich_orders[2]="Pastrami sandwich"
print("Our deli has run out of Pastrami""\n")
i="Pastrami sandwich"
while i in sandwich_orders:
	sandwich_orders.remove(i)
print(sandwich_orders,"\n""\n")












print("All exercises are done !!!""\n")