5/15 Today I learned...

1.
Functions

Defining a function = 

def function_name(): 
  <execution>

Calling a function = executing a function.

Parameters (how to include parameters in a function)

3 types of arguments (positional arguments, keyword arguments ,default arguments)

2.

---
#Defining a function
#Syntax for defining a function

"""
def function_name():
  <expression>
"""

2.
#Calling a function = Executing a function
function_name()

---example of 3 different types of arguments

#1. positional arguments
def hello(name, age, country):
  print("Hello, my name is " + name + " " + str(age) + " and I am from " + country)

#calling a function using positional arguments - Jake being the first position, 24 the second, and the Korea the third.
hello("Jake", 24, "Korea")

#2. calling a function using keyword arguments - notice that the orders of the arguments are different than the order defined in function definition. It is because we used keyword arguments.
hello(country = "CANADA", age = 29, name = "Jin")         

#3. calling a function using default arguments

#define a new function
def introduction(name, iq = 140):
  print("Hello my name is " + name + ", and my IQ is " + str(iq))
  
introduction("Agent Smith")                 #Hello my name is Agent Smith, and my IQ is 140
