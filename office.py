class office:
    name = ""
    work = ""
    
    def descrp(self):
        g = "%s works on %s" %(self.name, self.work)
        return g
    
person =  office()
person.name = "Anit"
person.work = "GOlden Nepal"

print(person.descrp())
