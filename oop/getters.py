class Student:
    def __init__(self, marks):
        self.__marks = marks
    @property
    def marks(self):
        return self.__marks
stud = Student(101)
print(stud.marks

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def display_balance(self):        
bnk = BankAccount(100000000000)
bnk.display_balance()

class Person:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age
humn = Person(19)
print(person1.age)

class Stud:
    def __init__(self, mrks):
        self.__mrks = mrks
    @property
    def mrks(self):
        return self.__mrks
    @mrks.setter
    def mrks(self, marks):
        if mrks > 0 and mrks <100:
            self.__mrks = mrks 
        elif:
          print("wow, 0 or 100, you really go all in lol")
          else:
              print("are you stupid?")
stud = Stud(99)
print(stud.mrks)

class Employe:
    def __init__(self,salary):
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
          print("invalid balance, brokie")
employe = Employe(999999)
print(employe.salary)
employe.salary = 100000
print( employe.salary )

class circle:
def init(self, radius):
self.__radius = radius
@property
def radius(self):
return self.__radius
@radius.setter
def radius(self, radius):
if radius > 0:
self.__radius = radius
@property
def area(self):
return 3.14 * self.__radius * self.__radius
circle = circle(19)
print(circle.radius)

class Paswwordtracker:
    def __init__(self, paswword):
        self.__paswword = paswword
    def Newpassword(self, Prevpaswword, Newpaswword):
        if Prevpassword == self.__paswword:
            self.__paswword = Newpaswword
          paswrd = Paswwordtracker("pass1pass")

class temperature:
    def __init__(self,heat):
        self.__heat = heat
    @property
    def heat(self):
        return self.__heat
    @heat.setter
    def heat(self,heat):
        self.__heat = heat
heat = temperature(12)

 class Stud:
    def __init__(self, mrks):
        self.__mrks = mrks
    @property
    def mrks(self):
        return self.__mrks
    @mrks.setter
    def mrks(self, marks):
        if mrks > 0 and mrks <100:
            self.__mrks = mrks 
        elif:
          print("wow, 0 or 100, you really go all in lol")
          else:
              print("are you stupid?")
stud = Stud(99)
print(stud.mrks)