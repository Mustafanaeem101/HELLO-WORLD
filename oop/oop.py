class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_information(self):
        print(self.title)
        print(self.author)
        print(self.year)


book1 = Book("MY BOOK =)", "MUSTAFA", 2026)

book1.display_information()


class book:
    pass


book01 = book()

print("A book has been created")


class Employee:
    def __init__(self, employeeid, name, department):
        self.emp_id = employeeid
        self.name = name
        self.department = department


emp1 = Employee(100, "Mustafa", "Compsci Floor 1")

print(emp1.emp_id)
print(emp1.name)
print(emp1.department)

class laptop:
    pass


laptop01 = laptop()
laptop02 = laptop()
laptop03 = laptop()

print(id(laptop01))
print(id(laptop02))
print(id(laptop03))




class employee:
    pass


employee01 = employee()
employee02 = employee()

print(id(employee01))
print(id(employee02))

print("Employees are the same")




class MobilePhone:
    pass


phone1 = MobilePhone()

phone1.brand = "Apple"
phone1.model = "iPhone 17 Pro"
phone1.price = 1000000

print(phone1.price)
print(phone1.model)
print(phone1.price)




class University:
    pass


university1 = University()
university2 = University()
university3 = University()

university1.name = "aus"
university2.name = "flnders"
university3.name = "Monash"

print(university1.name)
print(university2.name)
print(university3.name)




class Movie:
    pass


movie1 = Movie()
movie2 = Movie()

movie1.title = "minins"
movie1.year = 2001

movie2.title = "rise of the dead"
movie2.year = 20011

print("Movie 1:", movie1.title, movie1.year)
print("Movie 2:", movie2.title, movie2.year)




class Restaurant:
    pass


restaurant1 = Restaurant()
restaurant2 = Restaurant()

restaurant1.name = "McDonald's"
restaurant1.location = "Lahore"

restaurant2.name = "KFC"
restaurant2.location = "Islamabad"

print("Restaurant 1:", restaurant1.name, restaurant1.location)
print("Restaurant 2:", restaurant2.name, restaurant2.location)




class BankBranch:
    pass


branch1 = BankBranch()
branch2 = BankBranch()
branch3 = BankBranch()

branch1.code = 01
branch2.code = 02
branch3.code = 03

print("Branch 1 code:", branch1.code)
print("Branch 2 code:", branch2.code)
print("Branch 3 code:", branch3.code)



class SmartWatch:
    pass


watch1 = SmartWatch()
watch2 = SmartWatch()

watch1.brand = "Apple"
watch1.model = "Watch Series 9"
watch1.price = 100000

watch2.brand = "Samsung"
watch2.model = "Galaxy Watch 6"
watch2.price = 75000

print("Watch 1:", watch1.brand, watch1.model, watch1.price)
print("Watch 2:", watch2.brand, watch2.model, watch2.price)




class Company:
    pass


company01 = Company()
company02 = Company()
company03 = Company()

company01.name = "Amazon"
company02.name = "Google"
company03.name = "Oracle"

print(company01.name)
print(company02.name)
print(company03.name)




class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


book1 = Book("Someone Famous Ig", "Mustafa", 2007)

print(book1.title)
print(book1.author)
print(book1.year)




class Employee:
    def __init__(self, employeeid, name, department):
        self.emp_id = employeeid
        self.name = name
        self.department = department


emp1 = Employee(100, "Mustafa", "Compsci Floor 1")

print(emp1.emp_id)
print(emp1.name)
print(emp1.department)




class Laptop:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage


laptop1 = Laptop("Supercomputer", "Unavailable", "1000000GB", "Infinity")

print(laptop1.brand)
print(laptop1.processor)
print(laptop1.ram)
print(laptop1.storage)




class HotelRoom:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price


room1 = HotelRoom(1, "Double", 10000)

print(room1.room_number)
print(room1.room_type)
print(room1.price)




class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age




class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours




class Flight:
    def __init__(self, flight_number, departure_city, destination, ticket_price):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.destination = destination
        self.ticket_price = ticket_price




class Subscription:
    def __init__(self, customer_name, subscription_type, monthly_fee):
        self.customer_name = customer_name
        self.subscription_type = subscription_type
        self.monthly_fee = monthly_fee




class Vehicle:
    def __init__(self, registration_number, manufacturer, model, manufacturing_year):
        self.registration_number = registration_number
        self.manufacturer = manufacturer
        self.model = model
        self.manufacturing_year = manufacturing_year




class InsurancePolicy:
    def __init__(self, policy_number, policy_holder):
        self.policy_number = policy_number
        self.policy_holder = policy_holder



class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(self.name)
        print(self.age)
        print(self.salary)


employee1 = Employee("Mustafa", 19, 1000000000000)

employee1.display_details()




class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print(self.balance)


account1 = BankAccount(25546)

account1.display_balance()




class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_information(self):
        print(self.title)
        print(self.author)
        print(self.year)


book1 = Book("MY BOOK =)", "MUSTAFA", 2026)

book1.display_information()

class Student:
    def __init__(self, name,):
        self.name = name
      


stud0 = Student("st1")
stud1 = Student("st2")
stud2 = Student("st3")


Student = []

Student.append(stud0)
Student.append(stud1)
Student.append(stud2)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

prduct0 = Product("rice", 25)
prduct1 = Product("chowmein", 25)
prduct2 = Product("sugr", 25)

products = []

products.append(prduct0)
products.append(prduct1)
products.append(prduct2)

for prduct in products:
    print( Product.name)
    print( Product.price)