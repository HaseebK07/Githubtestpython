#multi-line statement
a = 1 + 2 + 3 +\
    4 + 5 + 6 +\
    7 + 8 + 9

#This is a comment

for i in range (1,11):
    print(i)
    if i == 5:
        break

"""This is a
multi line example,
we can also use for multi line comment"""

#Documentation string
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)
#Docstrings are the string literals that appear right after the definition
#of a function, method, class or module.

#Changing the value of a variable
website = "apple.com"
print(website)

# assigning a new variable to website
website = "programiz.com"

print(website)

#Assigning multiple values to multiple variables
a,b,c = 5, 3.2, "Hello"
print(a)
print(b)
print(c)

#Assigning the same value to multiple variables
x=y=z="Same"
print(x),print(y),print(z)

#Declaring and assigning a value to a constant
#Created a seperate file for constants with the constant PI and GRAVITY in it and then called it using important
#We use capital letters to declare constants
import constant
print(constant.PI)
print(constant.GRAVITY)

#creating variable names
#this_is_my_variable #long type

#Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows: Numerical, String, Boolean
#Special and Literal

#Numerical has 3 different types, Integer, float and complex

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

#String Literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = "\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#Boolean Literals
#1 = True and 0 = False
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Special Literals
#Python contains one special literal (none), we use it to specify that the field has not been created. 
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

#Literal Collections
#There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

#Numbers
#We use type() function to know which a class variable or a value belongs to
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#List in python, we can also use [] to extract an item or a range of items from a list
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#Python Tuple
#Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
#Tuple doesnt support item aasignment, so we cannot tell it to assign a number, char or string to a specific place
t = (5,'program', 1+3j)
print("t[1] = ",t[0:3])


#Python Strings
#Just like Python Tuple, strings dont support item assignment
s = "I am testing shit right now BIG BOY"
print(s)


#Pythong sets
#Set is an unordered collection of unique items.
#Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

#We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.
a = {1,2,2,3,3,3}
print(a)
#As we know sets are unordered therefore it does not support indexing

#Python Dictonary
#Dictionary is an unordered collection of key-value pairs.
#It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.
#In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

#Conversion between data types
#We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
a = int(10.6) #converting float to int, truncates the value
print(a)

b = set([1,2,3])
print(b)

c = tuple({5,6,7})
print(c)

d = list('hello')
print(d)

#Implicit Type Conversion
#Python automatically converts one data type to another data type, this doesnt need any user involvement

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Explicit Type Conversion
#This is where the user converts the data type of an object to a required data type, this is also known as typecasting
#In typecasting loss of data may occur as aw enforce the object to a specific data type

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

#The syntax is as follows <required_datatype>(expression)
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

#Printing data
print(1, 2, 3, 4)

#sep operater is used between spaces
print(1, 2, 3, 4, sep='*')

#After all values are printed, end is printed, it defaults into a new line
print(1, 2, 3, 4, sep='#', end='&')

#Ouput formatting
#We use  curly braces {} as placeholders
print('I love {0} and {1}'.format('Naruto','Dragon Ball z'))
print('I love {1} and {0}'.format('Naruto','Dragon Ball Z'))

print('Sup {name}, {greeting}'.format(greeting = 'Whats poppin?', name = 'Haseeb'))

#Python Import
import math
print(math.pi)

#Python Arthimetic Operations
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3, Floor division - division that results into whole number adjusted to the left in the number line
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

#Comparison operators in Python
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

#Logical Operators
x = True
y = False

#True if both the operands are true	
print('x and y is',x and y)

#True if either of the operands is true	
print('x or y is',x or y)

#True if operand is false (complements the operand)	
print('not x is',not x)