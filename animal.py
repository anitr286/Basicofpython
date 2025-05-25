class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat(Animal):
    pass

print(issubclass(Dog,Animal))
print(issubclass(Animal,Animal))
print(issubclass(Puppy,Dog))
print(issubclass(Cat,Animal))
