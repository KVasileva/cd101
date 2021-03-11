class Composers:
    def __init__ (self, first_name, last_name, birth, death):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.death = death
    def grit(self):
        a =int(self.death)-int(self.birth)
        print(f"Full name: {self.first_name+" "+self.last_name}, age {a}")
com_data = input("Enter first name, last name, birth year, death year separated with space:\n").split(" ")        
com1 =Composers(com_data[0],com_data[1],com_data[2],com_data[3])
print(com1.grit())    
