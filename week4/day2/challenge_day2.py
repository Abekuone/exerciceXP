"""
number=int(input("Enter a number : "))
ln=int(input("Enter the lenth of the list : "))
list_number=[]
for i in range(1,ln+1):
	list_number.append(i*number)
print(list_number)
"""
#########################################################
word=input("Enter a word : ")
list_word=word.strip()
new_list_word = []
for words in list_word:
  if words not in new_list_word:
    new_list_word.append(words)
word2=''.join(new_list_word)
print(word," ==============> ",word2,"\n")










