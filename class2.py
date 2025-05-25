class Animal:
    name = ""
    species = ""
    sound = ""
    
    def descrp(self):
        a = "%s is %s who %s" %(self.name,self.species,self.sound)
        return a
    
Dog = Animal()
Dog.name = "Groofg"
Dog.species = "Dog"
Dog.sound = "Barks"

print(Dog.descrp())