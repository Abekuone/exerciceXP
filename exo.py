a= (input("entrer un nombre entre 1 et 100 : "))
while type(a) is not int:
	a=(input("entrer un nombre entier compris entre 1 et 100 : "))
while(a<1 or a>100):
	a= int(input("entrer un nombre entre 1 et 100 : "))
if(a%3==0):
	print("Fizz")
elif(a%5==0):
	print("Buzz")
elif(a%3==0 and a%5==0):
	print("FizzBuzz")
else:
	print("Aucun")
