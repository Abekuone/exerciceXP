"""
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog,age_of_dog, color):
        self.name = name_of_the_dog
        self.age=age_of_dog
        self.color=color
        print("A new dog has been initialized !")
        print(f"His name is {name_of_the_dog} He is {age_of_dog} years hold. His color is {color}")

shelter_dog = Dog('Rex',5,"blue")


class Person():
  def __init__(self, f_name, l_name, age):
    self.f_name = f_name
    self.l_name=l_name
    self.age = age

first_person = Person("SOME","Armel",25)

print(first_person.f_name,first_person.l_name)
print(first_person.age)
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))
    def rename(self, new_name):
        self.name = new_name
        print(f"{self.name}")

shelter_dog = Dog("Rex")
shelter_dog.bark()
shelter_dog.walk(15)
shelter_dog.rename("Boby")

##############################################################################
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)
    def rename(self,new_name):
        self.name = new_name
        print("The new name is ",self.name)

first_person = Person("John", 36)
first_person.show_details()
first_person.rename("Ali")

"""
class BanckAcount(object):
    """docstring for BanckAcount"""
    def __init__(self, balance):
        self.balance =0
        self.transactions=[]
        print("The default account balance is ",self.balance)
   
    def deposit(self):
        nb_depo=int(input("Enter the number of deposit you wannt to make : "))
        for i in range(nb_depo):
            self.amount=int(input("Enter the amount of deposit : "))
            while self.amount<100:
                self.amount=int(input("The min amount for deposit is $100 : "))
            if self.amount>=100:
                self.balance+=self.amount
                self.transactions.append(self.amount)
                print("Deposit Succcessful")
            print("the new balance after deposit is ",self.balance)

    def withdraw(self):
        nb_with=int(input("Enter the number of deposit you wannt to make : "))
        for j in range(nb_with):
            self.amount=int(input("input the amount of Withdrawall : "))
            while self.amount<50:
                self.amount=int(input("The min amount Withdrawall is $50 : "))
            while self.amount>self.balance:
                self.amount=int(input("The max amount Withdrawall is reached "))
            if self.amount<self.balance:
                self.balance-=self.amount
                self.transactions.append(-(self.amount))
                print("Withdraw Approved")
            print("the new balance after Withdrawall is ",self.balance)

    def transaction(self):
        Transactions=[t for t in self.transactions]
        print(Transactions)

MyAcount=BanckAcount(0)
MyAcount.deposit()
MyAcount.withdraw()
MyAcount.transaction()











