5/24 Today I learned...
1.
Class

What is Class?


"""
Let's say we want to create a calculator that has addition function only
So we can write a code like this.
"""
result = 0

def add(a):
  global result
  result += a
  return result

#And we will get a desired result like this

print(add(3))                     #3
print(add(5))                     #8


"""
But! What if we want to have two calculators at the same time in one program?
Then we have to create another function
"""

result2 = 0
def add2(a):
  global result2
  result2 += a
  return result2

print(add2(5))                    #5
print(add2(6))                    #11

"""
What if we want to have 150 calculators at the same time in one program?
Does it mean that we have to create 150 different functions, and variables?
No!
We can create one class that can serve as many instance as we like
"""

class Calculator:
  def __init__(self):
    self.result = 0
  
  def add(self, num):
    self.result += num
    return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))                    #3
print(cal1.add(5))                    #8
print(cal2.add(5))                    #5
print(cal2.add(6))                    #11

"""

Things to keep in mind

1.
Now we call cal1 an OBJECT
Also cal2 is an OBJECT

The result of cal1, and cal2 are independent of each other
I can change cal1's value which has no impact on cal2's value


2.
cal1, cal2 are the products of class Calculator()
so we also say
cal1, cal2 are the INSTANCES of class Calculator()

3.
We call functions inside class METHODS

"""



"""
Let's say that we want to create a class that takes two numbers a,b
and we can set two numbers a,b
and we want to add them (a+b)
subtract them (a-b)
multiply them(a*b)
divide them(a/b)
"""

class Fourcal():
  def setdata(self,a,b):
    self.a = a
    self.b = b
  def add(self):
    result = self.a + self.b
    return result
    
firstobject = Fourcal()
firstobject.setdata(5,10)                 #we set data

#now let's check if number a and number b are set
print(firstobject.a)                      #5
print(firstobject.b)                      #10

#now let's see if they have independent values stored in different objects

#first I will make a new object
secondobject = Fourcal()

#set two numbers 3,11 as secondobject's a, and b
secondobject.setdata(3,11)

print(firstobject.a)                      #5
print(firstobject.b)                      #10
print(secondobject.a)                     #3
print(secondobject.b)                     #11
#even if we set new numbers in secondobject.dataset(a,b) , the firstobject's dataset(a,b) is not affected by it.

#Now we can include add method in class Fourcal()
#
"""
class Fourcal():
  def setdata(self,a,b):
    self.a = a
    self.b = b
    
  def add(self):                                        ex) add(self) : firstobject.add
    addresult = self.a + self.b                         ex) addresult = a + b : addresult = firstobject.a + secondobject.b
    return addresult
"""
