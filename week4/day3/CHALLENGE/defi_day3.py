word=input("Enter a word : ")
list_word=[]
index=[]
values=[]

################Building of the first dictionnary###########################
for i in word:
    list_word.append(i)
print("list from the word is : ",list_word,"\n")

dico_word=dict(zip(list_word,range(len(list_word))))
print("Word as dico is : ",dico_word,"\n")

################Building of the list of tuples#############################
from collections import defaultdict
 
L = list_word
dico_index = defaultdict(list)
 
for index, value in enumerate(L):
    dico_index[value].append(index)
 
list2=list(dico_index.items())
print("List of tuples from list_word is : ",list2,"\n")

################Building of the last dictionnary###########################
list_of_tuples_dict = dict(list2)
print("Dico of list_tuples is : ",list_of_tuples_dict,"\n")

