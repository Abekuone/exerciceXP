'''
print("###################     EXO1      ####################################################""\n")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d=dict(zip(keys,values))
print(d,"\n""\n")


print("###################     EXO2      ####################################################""\n")

family={}
names=[]
ages=[]
prices=[]
nb_chil=int(input("Enter the number of child : "))

for i in range(nb_chil):
	name=input(f"Enter the name of this child {i} : ")
	names.append(name)
	age=int(input(f"Enter the age of {names[i]} : "))
	ages.append(age)
	print("\n")
#print(names,"\n")
#print(ages,"\n")
for i in names:
	family[i]=age
print(family,"\n")

for value in family.values():
	if value<3:
		p=0
	elif value >3 and value<12:
		p=10
	else:
		p=15
	print("This child paid : ",p,"$""\n")
	prices.append(p)
	summ=sum(prices)
#print(prices)
print("The family totaly pay : ",summ,"$""\n")


print("###################     EXO3      ####################################################""\n")
#question N°1
brand={"name": "Zara",
"creation_date": 197,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{"France": "blue", "Spain": "red", "US": ["pink", "green"]}    
}
#question N°3
brand["number_stores"]=2
#question N°4
print(f"Zara costumers are based in : ",brand["major_color"].keys(),"\n")
#question N°5
brand["country_creation"]="Spain"
#question N°6
if "international_competitors" in brand:
	brand["international_competitors"].append("Desigual")
#question N°7
del(brand["creation_date"])
#question N°8
print("Zara last international competitor is : ",brand["international_competitors"][-1],"\n")
#question N°9
print("The mains US colors are : ",brand["major_color"]["US"],"\n")
#question N°10
print("The length of dictionnary is ",len(brand),"\n")
#question N°11
for keys in brand.keys():
	print(keys)
print("\n")
#question N°12
more_on_zara={"creation_date": 1975,"number_stores": 10000}
#question N°14
brand.update(more_on_zara)
print(brand)
#question N°15
print(brand["number_stores"],"\n""\n")
#The dictionnary is updated so th value of th key "number_stores" is also updated
'''

''
print("###################     EXO4      ####################################################""\n")
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#question 1
disney_users_A=dict(zip(users,range(5)))
print("disney_users_A : ",disney_users_A,"\n")
#question 2
disney_users_B=dict(zip(range(5),users))
print("disney_users_B : ",disney_users_B,"\n")
#question 3
'''
d=sorted(disney_users_A.keys())
disney_users_C=dict(zip(d,range(5)))
print("disney_users_C : ",disney_users_C,"\n")
'''
#################
keys = disney_users_A.keys()
sorted_keys = sorted(keys)
print(sorted_keys,"\n")

sorted_disney_users_A = {}
for key in sorted_keys:
  sorted_disney_users_A[key] = disney_users_A[key]
print(sorted_disney_users_A,"\n")
#question [4][1]








