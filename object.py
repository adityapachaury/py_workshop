##creating an object-
#class Dog:
#    def __init__(self, name):
#        self.name = name

#dog1 = Dog("Buddy")
#print(dog1.name)

##creating a class
#class Car:
#    def __init__(self, make, model):
#        self.make = make
#        self.model = model
#car1 = Car("Toyota", "Camry")
#car2 = Car("Honda", "Civic")
#print(car1.make, car1.model)
#print(car2.make, car2.model)

##Encapsulate example
#class BankAccount:
#    def __init__(self, account_number, balance):
#        self._account_number = account_number
#        self.__balance = balance
#    def get_balance(self):
#        return self.__balance
#account1 = BankAccount("12345", "1000")
#print(account1._account_number)
#print(account1.get_balance())

##inharitance
#inharitance allows you to create new classes that inharit properties and method fromexisting classes.
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog  = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, dog.speak())
print(cat.name, cat.speak())







