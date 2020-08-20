print("hello im shree lakshmi")
print('o----')
print(' ||||')
print('*' * 4) # expression

# variables
price = 10
print("price = ",price)
price = 20 #int
print("price = ",price)
rate =20.5 #float
name ="shree" #string
is_published = False #boolean
print(price , rate, name, is_published)

#Exercise 1
name = "John Smith"
age =20
new_patient = True

#Get input from user

var1 = input("What is your name? ")
print("Hi " + var1)

#Excercise 2
var1 = input("What is your name? ")
var2 = input("What is your favorite color? ")
print(var1 + " likes " + var2)

# Type conversion
# birth_year = input("birth year: ")  throws error
birth_year = int(input("birth year: "))
age = 2020-birth_year
print(age)

#Strings
# course = 'python's course for Beginners' error
course = 'pythons course for Beginners'
course = "python's course for Beginners"
mail = '''
#Hi shree
#here is our first email to you

#Thank you for the love.
'''
print(course)
print(mail)
print(course[0])
print(course[-1],course[-2],course[-3])
print(course[0:3])
print(course[:])
print(course[5:-5])

name ='jennifer'
print(name[1:-1])

#Formated string
first = 'john'
last = 'smith'
msg = first + ' [' + last +'] is a coder.'
print(msg)
message = f'{first} [{last}] is a coder'
print(message)


#String Methods
course = "python for beginners"
print(course)
print(len(course)) # general function = len - returns length of string
print(course.isupper())
print(course.upper())
print(course.isupper()) #false because its not saved
print(course.find('o'))
print(course.find('e'))
print(course.find('E'))
print(course.find("beginners"))
print(course.replace('beginners','absolute beginners'))
print('python' in course)
print('Python' in course)

# Arithmetic operations
print(10+3)
print(10-3)
print(10/3)
print(10//3)
print(10*3)
print(10**3)
print(10%3)

x=10
x = x+3
print(x)
x -= 3
print(x)


#Operator precedence
'''
shortcut = "PEMDAS"
p - paranthesis ()
E - exponentiation or power
M,D - multiplication or division
A,S - addition or subtraction
'''

# Math function
x=2.9
print(round(x))
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))
## refer the python3 math functions in python.org documentation

#if condition
x=10
if x<5:
    print("less than 5")
elif x>=5 and x<=10:
    print("nice number")
else :
    print("bad number")

x=True
if x:
    print("true")
else:
    print("false")

x=False
if x:
    print("true")
else:
    print("false")

x=False
y=True
if x:
    print("less than 5")
elif y:
    print("nice number")
else :
    print("bad number")

#Logical operator

# AND OR NOT
has_high_income = False
has_good_credit = True
if has_good_credit and has_high_income :
    print("eligible for loan")
else:
    print("not eligible for loan")

has_high_income = False
has_good_credit = True
if has_good_credit or has_high_income:
    print("eligible for loan")
else:
    print("not eligible for loan")

x = True
print(not x)

# comparison operator
# < , > , <= , >= , == ,

# exercise:

weight = int(input('weight: '))
unit = input('(L)bs or (K)g: ')
unit = unit.upper()
if unit == 'L':
    print(f"you are {weight*0.45} kilos")
elif unit == 'K':
    print(f" you are {weight/0.45} pounds")

#while loop
i=1
while i<=5:
    print(i)
    i+=1

i=1
while i<=5:
    print('*'*i)
    i+=1

# for loop
for i in 'python':
    print(i,end=" ")

for i in ["sara","shanu","vishu","rithuth","trinash"]:
    print(i,end=";")
print("")
for i in [1,2,3,4]:
    print(i,end=",")
print("")
for i in range(10):
    print(i,end= "'")
print("")
for i in range(5,10):
    print(i,end=" ")
print("")
for i in range(0,5,2):
    print(i,end=" ? ")

prices = [10,20,30]
total=0
for price in prices:
    total+=price
print("total=" , total)

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers = [6,2,5,2,2]
for i in numbers:
    print("X"*i)

for i in numbers:
    for j in range(i):
        print("X",end="")
    print("")

# List
names = ["sara","shanu","trinash","rithuth","vishu"]
print(names[-1])
print(names[1])
print(names[2:])
print(names[2:4])
names[2] = "thrinash"
print(names)
print(names.reverse())


#exercise
numbers = [3,6,2,8,4,10]
max =numbers[0]
for i in numbers:
    if max<i:
        max=i
print("max=", max)

#2D list(matrix)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][2])
print(matrix[1])
print(matrix)
matrix[1][1]=55
print(matrix)
for i in matrix:
    for j in i:
        print(j,end=" ")
    print(" ")

# list method
num = [5,2,5,2,2,2]
print(num)
num.append(20)
print("after append(20)",num)
num.insert(2,10)
print("after insert(2,10)",num)
num.remove(5)
print("remove(5)",num)
num.pop()
print("pop()",num)
print("index()",num.index(5))
print(num.count(2))
print(50 in num)
num.sort()
print(num)
num.reverse()
print(num)
num2 = num.copy()
num.append(20)
print(num,num2)
num.clear()
print("clear()",num)

# exercise remove the duplicate list value
number = [2,2,4,4,6,3,6,4,3]
unique = []
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)

# Tuples - immutable(cannot be modified it can only be accessed)
num = (1,2,3,2,7,5,2)
print(num)
print(num.count(2))
print(num.index(2))

# Unpacking
coordinates=(1,2,3)
result = coordinates[0]*coordinates[1]*coordinates[2]
print(result)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
result = x*y*z
print(result)
x,y,z = coordinates
print(x*y*z)

# Dictionaries
customer={
    "name":"shree",
    "age":20,
    "is_verified": True
}
print(customer)
print(customer["name"])
print(customer["age"])
print(customer.get("name"))
print(customer.get("birth_date"))
print(customer.get("birth_date","21/07/2000"))
customer["name"]="virsha"
print(customer["name"])

# exercise ditionary
num ={
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
input =input("phone: ")
output =" "
for ch in input:
    output += num.get(ch,"!")+" "
print(output)

# Functions
def function_name():
    print("hi there")
    print("welcome aboard")


print("start")
function_name()
print("finish")

# Parameter
def greet(name):
    print("hi",name)
    print("welcome aboard")

greet("vikranth")
greet("virshanth")
#greet()  error

def name(first,last):
    print("hi",first,last)
    print("welcome aboard")
name("vikranth","triventhi")
name("virshanth","triventhi") # positional argument
name("virsha","triventhi")

# keyword argument

def name(first,last):
    print("hi",first,last)


name("triventhi","virsha")
name("vikranth","triventhi")
name("virshanth","triventhi")
name(last="triventhi",first="virsha") #keyword argument specifying the name

# return statement
def square(number):
    return number**2

print(square(5))
print(square(4))
print(square(3))

def square(number):
    print( number**2)

print(square(5))

# create a reusable function
def emoji(msg):
    list = msg.split(" ")
    emojis = {
        ":)":"😃",
        ":(":"😢"
    }
    output = ""
    for i in list:
        output += emojis.get(i,i) + " "
    return output

msg = input(">")
print(emoji(msg))

#Exceptions
age = int(input("age: ")) #if age is s then it returns error
print(age)
    
try:
    age = int(input("age: "))
    print(age)
except ValueError:
    print("Invalid value")

try:
    age = int(input("age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")

#comments

# single line comment



'''multiple
line
comment'''





# classes
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2 = Point()
point2.x=40
print(point2.x)

# constructor
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point(10,20)
point1.x =11
print(point1.x)

#exercise
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, i am {self.name}")

john =Person("john smith")
print(john.name)
john.talk()

bob =Person("bob")
bob.talk()

#Inheritance

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):  #inheritance
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass #in python it is neccesary to have a code inside a class instead we can use pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()

#module refer convertor.py file
import convertor
print(convertor.kg_to_lbs(70))


import convertor
from convertor import kg_to_lbs
print(kg_to_lbs(70))

#exercise refer utils.py

from utils import find_max
numbers = [10,4,40,6,30]
print(find_max(numbers))

numbers = [10,4,40,6,30]
print(max(numbers))

# packages
import ecommerce.shipping
ecommerce.shipping.cal_shipping()
ecommerce.shipping.cal_tax()

from ecommerce.shipping import cal_shipping , cal_tax
cal_shipping()
cal_tax()

# Generating Random values
# ## refer python3 module index for built in module
import random
for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

members = ["john","Mary","jack","bob"]
leader = random.choice(members)
print(leader)

#exercise dice roll

# files and directories
#1.Absolute path
#2.Relative path
from pathlib import Path
path = Path("ecommerce")
print(path.exists())
from pathlib import Path
path = Path("emails")
print(path.exists())
from pathlib import Path
path = Path("emails")
print(path.mkdir()) #creates directory
print(path.rmdir()) #del directory
print(path.glob('*.*'))

from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)

from pathlib import Path
path = Path()
for file in path.glob('*.*'):
    print(file)

for file in path.glob('*.xls'):
    print(file)

# Pypi and pip
# refer pypi.org for functionalities

