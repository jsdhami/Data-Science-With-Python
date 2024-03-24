# this is a first code in python
print("Hello World !")
# if you have question, whay we print Hello World! in python using syntax even we can write directly Hello World! without syntax print() ?
# Answer: In python, print() is a function that is used to print the output to the console. So, we use print() to print the output to the console. and our machine/laptop/pc can understand this function but not understand the direct text. so, we use print() function to print the output to the console.
# name = input("Enter your name:")
# print("Hello", name)



# Data Types in Python

#  String DataType
name = "Janak Singh Dhami" 

# Integer Data Type
grade = 12

# Float Data Type
presentage = 90.5

# Boolean Data Type
isPassed =True

# List Data Type
subjects = ["Math", "Science", "English"]

# Tuple Data Type
marks = (90, 80, 70)

# Dictionary Data Type
student = {
    "name": "Janak Singh Dhami",
    "grade": 12,
    "presentage": 90.5,
    "isPassed": True
}

# Set Data Type
subjects = {"Math", "Science", "English"}

# None Data Type
value = None

# Type Casting
# Integer to Float
grade = 12
grade = float(grade)

# Float to Integer
presentage = 90.5
presentage = int(presentage)

# String to Integer
grade = "12"
grade = int(grade)

# String to Float
presentage = "90.5"
presentage = float(presentage)

# String to List
subjects = "Math, Science, English"
subjects = subjects.split(", ")

# List to String
subjects = ["Math", "Science", "English"]
subjects = ", ".join(subjects)

# List to Tuple
#  tople is immutable and list is mutable so we can convert list to tuple and tuple to list in python

marks = [90, 80, 70]
marks = tuple(marks)

# Tuple to List
marks = (90, 80, 70)
marks = list(marks)


# Operators in Python
# Arithmetic Operators
# Addition
a = 10
b = 20
c = a + b

# Subtraction
a = 10
b = 20
c = a - b

# Multiplication
a = 10
b = 20
c = a * b

# Division
a = 10
b = 20
c = a / b

# Modulus
a = 10
b = 20
c = a % b

# Exponentiation
a = 10
b = 20
c = a ** b

# Floor Division
a = 10
b = 20
c = a // b

# Comparison Operators
# Equal
a = 10
b = 20
c = a == b

# Not Equal
a = 10
b = 20
c = a != b

# Greater Than
a = 10

b = 20
c = a > b

# Less Than

a = 10
b = 20
c = a < b

# Greater Than or Equal To
a = 10
b = 20
c = a >= b

# Less Than or Equal To
a = 10
b = 20

c = a <= b

# Logical Operators
# AND
a = 10
b = 20
c = a > 5 and b < 30

# OR
a = 10
b = 20
c = a > 5 or b < 30

# NOT
a = 10
b = 20
c = not a > 5

# Assignment Operators

# =
a = 10

# +=
a = 10
a += 5

# -=
a = 10
a -= 5

# *=
a = 10
a *= 5

# /=
a = 10
a /= 5

# %=
a = 10
a %= 5

# **=
a = 10
a **= 5

# //=
a = 10
a //= 5

# Identity Operators
# is
a = 10
b = 10
c = a is b

# is not
a = 10
b = 20
c = a is not b

# Membership Operators
# in
subjects = ["Math", "Science", "English"]
c = "Math" in subjects

# not in
subjects = ["Math", "Science", "English"]
c = "Math" not in subjects

# Bitwise Operators
# &
a = 10
b = 20
c = a & b

# |
a = 10
b = 20
c = a | b

# ^
a = 10
b = 20
c = a ^ b

# ~
a = 10
c = ~a

# <<
a = 10
c = a << 2

# >>

a = 10
c = a >> 2

# Conditional Statements
# if
a = 10
if a > 5:
    print("a is greater than 5")
    
# if else
a  = 55
if a > 50:
    print("a is greater than 50")
else:
      print("a is less than 50")
      
# if elif else
a = 50
if a > 50:
    print("a is greater than 50")
elif a == 50:
      print("a is equal to 50")
else:
      print("a is less than 50")
      
# Loops in Python
# for loop
for i in range(5):
    print(i)
    
# while loop
i = 0
while i < 5:
    print(i)
    i += 1
    
# break statement
for i in range(5):
    if i == 3:
        break
    print(i)
    
# continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)
    
# Functions in Python
def greet():
    print("Hello")
    
greet()

def greet(name):
      print("Hello", name)
      
greet("Janak Singh Dhami")

def add(a, b):
      return a + b

result = add(10, 20)
print(result)

# Classes in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hello", self.name)
        
person = Person("Janak Singh Dhami", 20)
person.greet()

# Inheritance in Python
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        
    def study(self):
        print(self.name, "is studying")
        
student = Student("Janak Singh Dhami", 20, 12)
student.greet()
student.study()

# Modules in Python
# Math Module
import math

print(math.pi)

print(math.sqrt(16))

# Random Module
import random


