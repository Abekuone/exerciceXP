M=[[7,"i",3],["T","s","i"],["h","%","x"],["i"," ","#"],["s","M",""],["$","a",""],["#","t","%"],["^","r","!"]]
l1=[]

a=[]
aa=[]
b=[]
bb=[]
c=[]
cc=[]

alpha=["a","b","c","d","e","f","g","h","i","j","k","l,","m","n","o","p","q","r","s","t","u","v","w,","x","y","z"]
alpha1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in M:
    if i[0] in alpha or i[0] in alpha1:
        a.append(i[0])
    else:
        a.append(" ")
    
    
    if i[1] in alpha or i[1] in alpha1:
        b.append(i[1])
    else:
        b.append(" ")
    

    if i[2] in alpha or i[2] in alpha1:
        c.append(i[2])
    else:
        c.append(" ")
    
char_a="".join(a)
char_b="".join(b)
char_c="".join(c)
"""
print("a ==========>",a)
print("b==========>",b)
print("c==========>",c)
print(char_a)
print(char_b)
print(char_c)
"""

word=char_a + char_b + " "+ char_c
print(word)