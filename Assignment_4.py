
## 1. Write a Python program to create a class named Car. Define attributes like brand, model, and year.
# Create an object of the class and display the details of the car?

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_details(self):
#         print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")
#
# # Create an object of the Car class
# my_car = Car("Toyota", "Corolla", 2020)
#
# # Display the details of the car
# my_car.display_details()



## 2. Create a class Student with attributes name, roll_number, and marks.
# Define a constructor to initialize these attributes and a method display_info() to print the student's details?

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks
#
#     def display_info(self):
#         print(f"Student Details:\nName: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}")
#
# # Create an object of the Student class
# student1 = Student("Alice", "101", 95)
#
# # Display the details of the student
# student1.display_info()


## 3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle.
# Create multiple objects and display the area and perimeter for each?


# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def calculate_area(self):
#         return self.length * self.breadth
#
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.breadth)
#
#     def display_info(self):
#         print(f"Rectangle Details:\nLength: {self.length}\nBreadth: {self.breadth}")
#         print(f"Area: {self.calculate_area()}")
#         print(f"Perimeter: {self.calculate_perimeter()}\n")
#
# # Create multiple objects of the Rectangle class
# rectangle1 = Rectangle(10, 5)
# rectangle2 = Rectangle(7, 3)
# rectangle3 = Rectangle(15, 8)
#
# # Display the area and perimeter for each rectangle
# rectangle1.display_info()
# rectangle2.display_info()
# rectangle3.display_info()


## 4. Write a class Circle with an attribute radius and methods get_area() and get_circumference().
#These methods should return the area and circumference of the circle, respectively ?

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * (self.radius ** 2)
#
#     def get_circumference(self):
#         return 2 * math.pi * self.radius
#
# # Create an object of the Circle class
# circle1 = Circle(5)
#
# # Display the area and circumference of the circle
# print(f"Circle Details:\nRadius: {circle1.radius}")
# print(f"Area: {circle1.get_area()}")
# print(f"Circumference: {circle1.get_circumference()}")


## 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self, account_no, balance=0):
#         self.account_no = account_no
#         self.balance = balance
#
#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print(f"Debited: {amount}. New balance: {self.balance}")
#
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Credited: {amount}. New balance: {self.balance}")
#
#     def print_balance(self):
#         print(f"Account No: {self.account_no}, Balance: {self.balance}")
#
# # Create an object of the Account class
# account1 = Account("123456789", 1000)
#
# # Perform some operations
# account1.print_balance()
# account1.credit(500)
# account1.debit(200)
# account1.print_balance()


## 6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created.
#Show the updated employee count after creating new objects.

# class Employee:
#     employee_count = 0  # Class variable to keep track of the number of employees
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         cls.employee_count += 1
#
#     @classmethod
#     def get_employee_count(cls):
#         return cls.employee_count
#
# # Create multiple objects of the Employee class
# employee1 = Employee("Alice")
# employee2 = Employee("Bob")
# employee3 = Employee("Charlie")
#
# # Show the updated employee count
# print(f"Total number of employees: {Employee.get_employee_count()}")


##7. Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value).
#Display the details of the book using an instance method.

# class Book:
#     def __init__(self, title, author, price=0.0):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_details(self):
#         print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")
#
# # Create objects of the Book class
# book1 = Book("1984", "George Orwell", 15.99)
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
#
# # Display the details of the books
# book1.display_details()
# book2.display_details()

## 8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent.
#Create an object of the class and use the method to convert various temperatures.

# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return (celsius * 9/5) + 32
#
# # Create an object of the TemperatureConverter class
# converter = TemperatureConverter()
#
# # Convert various temperatures from Celsius to Fahrenheit
# temperatures_in_celsius = [0, 20, 37, 100]
# for temp in temperatures_in_celsius:
#     fahrenheit = converter.celsius_to_fahrenheit(temp)
#     print(f"{temp}°C is {fahrenheit}°F")


## 9. Create a class Time with attributes hours and minutes.
# Add a method add_time() that takes another Time object, adds its values to the current object,
# and returns a new Time object with the resulting sum.

# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def add_time(self, other_time):
#         total_minutes = self.minutes + other_time.minutes
#         total_hours = self.hours + other_time.hours + total_minutes // 60
#         total_minutes = total_minutes % 60
#         return Time(total_hours, total_minutes)
#
#     def display_time(self):
#         print(f"Time: {self.hours} hours and {self.minutes} minutes")
#
# # Create objects of the Time class
# time1 = Time(2, 45)
# time2 = Time(1, 30)
#
# # Add the two time objects
# result_time = time1.add_time(time2)
#
# # Display the resulting time
# result_time.display_time()


## 10.Create a class EmployeeSalary with class variables basic_salary and bonus_percentage.
# Write a class method set_bonus_percentage() to change the bonus percentage for all employees.
# Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.


# class EmployeeSalary:
#     basic_salary = 0
#     bonus_percentage = 0
#
#     def __init__(self, basic_salary):
#         self.basic_salary = basic_salary
#
#     @classmethod
#     def set_bonus_percentage(cls, bonus_percentage):
#         cls.bonus_percentage = bonus_percentage
#
#     def calculate_total_salary(self):
#         bonus_amount = (self.basic_salary * EmployeeSalary.bonus_percentage) / 100
#         return self.basic_salary + bonus_amount
#
# # Set the bonus percentage for all employees
# EmployeeSalary.set_bonus_percentage(10)
#
# # Create instances of the EmployeeSalary class
# employee1 = EmployeeSalary(50000)
# employee2 = EmployeeSalary(60000)
#
# # Calculate and display the total salary for each employee
# print(f"Total salary for employee 1: {employee1.calculate_total_salary()}")
# print(f"Total salary for employee 2: {employee2.calculate_total_salary()}")




