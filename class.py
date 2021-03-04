class User:
    def __init__(self, first_name, last_name, birth, sex, ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.sex = sex

    def grit(self): #метод класса
        print (f"Name: {self.first_name}, {self.last_name}, birth: {self.birth}")

    def calc_age(self, curr_year): #задать год
              return curr_year-self.birth

    @staticmethod #оператор
    def calc_avg(self,other):
       z= (self.calc.age(2021)+ other.calc.age(2021)) /2
       return z

user1 = User("A", "B", 1980, "Male" )
user2 = User("C", "D", 1960, "Female" )

User.calc_avg(user1, user2)







# user1 = User("A", "B", 1980, "Male" )
# user1.grit()
# print(user1.calc_age(2022))



# user1 = User("Paul", "Yo", 23, "Male" )
# user1.grit()

# arr = []
# arr.append()

# user2: User("Maria", "Yo", 23, "Female" )
# user2.grit()
# print(user2.last_name)