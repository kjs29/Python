5/15 Today I learned...

1.
Defining a function = 

def function_name(): 
  <execution>

Calling a function = executing a function.

Parameters (how to include parameters in a function)

3 types of arguments (positional arguments, keyword arguments ,default arguments)

2. built-in-functions and user-defined functions
#we can use built in functions like print() , or max() 
#or we can use user defined functions

3.return
return allows us to save a variable in a function = we call this function a returned function value
---
#Defining a function

"""
Syntax for defining a function

def function_name():
  <expression>
  
"""

#Defining a function
def trader_name():
  print("Hello, I am a function")

#Calling a function = Executing a function
trader_name()

#parameter is a variable used in function body
def trader_name(name):
  print("Hello I am a trader, and my name is " + name)
trader_name("Larry Williams")                 #Hello I am a function, and my name is Larry Williams

#parameters
def total(price,quantity):
  print(price*quantity)
total(220,2)                                #440

---example of 3 different types of arguments

#1. positional arguments
def hello(name, age, country):
  print("Hello, my name is " + name + " " + str(age) + " and I am from " + country)

#calling a function using positional arguments - Jake being the first position, 24 the second, and the Korea the third.
hello("Jake", 24, "Korea")

#2. calling a function using keyword arguments - notice that the orders of the arguments are different than the order defined in function definition. It is because we used keyword arguments.
hello(country = "CANADA", age = 29, name = "Jin")         

#3. calling a function using default arguments

#define a new function and the default argument is iq = 140
def introduction(name, iq = 140):
  print("Hello my name is " + name + ", and my IQ is " + str(iq))
  
introduction("Agent Smith")                 #Hello my name is Agent Smith, and my IQ is 140

#we can also modify default argument
introduction("Agent Smith", iq= 75)         #Hello my name is Agent Smith, and my IQ is 75

---example of return

#in a function we can save a return as a result

commission = 5
budget = 500


def tradingbudget(a,b):
  
  #this line saves a function as a value of (a-b)
  return a - b

#calling a tradingbudget funciton
print(tradingbudget(budget,commission))                #495



