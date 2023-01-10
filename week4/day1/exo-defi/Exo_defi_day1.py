a=input("Input a string : ")
if len(a)<10:
	print("This string is not long enough.""\n")
elif len(a)>10:
	print("This string is too long.""\n")
else:
	print("The length of this string is : ",len(a),"\n")
print("The first character of this string is : ",a[0],"\n")
print("The last character of this string is : ",a[-1],"\n")

##################################################################
for i in range(len(a)+1):
	print(a[0:i])
print()

##################################################################
import random
from random import shuffle
def shuffle_string(string):
	a_list=list(string)
	shuffle(a_list)
	return "".join(a_list)
string=a
print("The mixture of characters gives : ",shuffle_string(string),"\n")
print("The daily challenge is done""\n")