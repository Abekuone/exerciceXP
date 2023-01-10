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
nb_chil=int(input("Enter the number of child of your family : "))
while type(nb_chil)!=type(int):
	nb_chil=int(input("Enter a good number of child of your family : "))
	pass

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
print("Question [3][1]****************""\n")
brand={"name": "Zara",
"creation_date": 197,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{"France": "blue", "Spain": "red", "US": ["pink", "green"]}    
}

#question N°3
print("Question [3][3]****************""\n")
brand["number_stores"]=2

#question N°4
print("Question [3][4]****************""\n")
print(f"Zara costumers are based in : ",brand["major_color"].keys(),"\n")

#question N°5
print("Question [3][5]****************""\n")
brand["country_creation"]="Spain"

#question N°6
print("Question [3][6]****************""\n")
if "international_competitors" in brand:
	brand["international_competitors"].append("Desigual")

#question N°7
print("Question [3][7]****************""\n")
del(brand["creation_date"])

#question N°8
print("Question [3][8]****************""\n")
print("Zara last international competitor is : ",brand["international_competitors"][-1],"\n")

#question N°9
print("Question [3][9]****************""\n")
print("The mains US colors are : ",brand["major_color"]["US"],"\n")

#question N°10
print("Question [3][10]****************""\n")
print("The length of dictionnary is ",len(brand),"\n")

#question N°11
print("Question [3][11]****************""\n")
for keys in brand.keys():
	print(keys)
print("\n")

#question N°12
print("Question [3][12]****************""\n")
more_on_zara={"creation_date": 1975,"number_stores": 10000}

#question N°14
print("Question [3][14]****************""\n")
brand.update(more_on_zara)
print(brand)

#question N°15
print("Question [3][15]****************""\n")
print(brand["number_stores"],"\n""\n")
#The dictionnary is updated so th value of th key "number_stores" is also updated


print("###################     EXO4      ####################################################""\n")
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#question 1
print("Question [1]""\n")
disney_users_A=dict(zip(users,range(5)))
print("disney_users_A : ",disney_users_A,"\n")

#question 2
print("Question [2]""\n")
disney_users_B=dict(zip(range(5),users))
print("disney_users_B : ",disney_users_B,"\n")

#question 3
print("Question [3]****************""\n")
keys = disney_users_A.keys()
sorted_keys = sorted(keys)
print(sorted_keys,"\n")
sorted_disney_users_A = {}
for key in sorted_keys:
  sorted_disney_users_A[key] = disney_users_A[key]
print(sorted_disney_users_A,"\n")

#question [4][1]
print("Question [4][1]****************""\n")
new_users=[]
for i in users:
	sp_i=i.split()
	for j in sp_i:
		if "i" in j:
			new_users.append(j)
			print(f"I is in {j}")
		else:
			print(f"I is out {j}")
print(new_users,"\n")
new_disney_users_A=dict(zip(new_users,range(5)))
print(new_disney_users_A,"\n""\n")
#question [4][2]
print("Question [4][2]****************""\n")
new_users2=[]
for i in users:
	sp_i2=i.split()
	for j in sp_i2:
		if j[0]=="M" or j[0]=="P":
			new_users2.append(j)
			print(f" M/P is in {j}")
		else:
			print(f"M/P is out {j}")
print(new_users2,"\n")
new_disney_users_A2=dict(zip(new_users2,range(5)))
print(new_disney_users_A2,"\n""\n")







print("\t""All exercises are done !!! ")



