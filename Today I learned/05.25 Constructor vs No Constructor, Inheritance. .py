5/25 Today I learned...
1.
Difference between having no constructor in Class and having constructor in Class
Inheritance
Method Overriding


2.
Difference between Class variable and Instance Variables
- In real world, people use Instance variables a lot more than Class variables

---
#Difference between having no constructor and having a constructor
#Inheritance. Why we use Inheritance. Adding new methods in a new Class
#Method overriding

class Twonumber:
    def setdata(self,a,b):
        self.a = a
        self.b = b
    def addnum(self):
        return self.a + self.b
    def subnum(self):
        return self.a - self.b
    def mulnum(self):
        return self.a * self.b
    def divnum(self):
        return self.a / self.b

class Newtwonum(Twonumber):
    def pownum(self):
        return self.a ** self.b
"""
Syntax for inheritance

class Newclassname(Class you want to pass on):

    
Why do we use Inheritance?

Because we don't want to modify original Class
Sometimes we can't modify original Class if the Class is in the library package

"""

#since we didn't use __init__() : constructor, we can create instance like this. Without any argument.
first = Twonumber()

#Now we have to set data though
first.setdata(25,5)

print(first.addnum())   #30
print(first.mulnum())   #125

#But we use __init__() when we created the class, let's see what this does.
class Twonum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addnum(self):
        return self.a + self.b
    def subnum(self):
        return self.a - self.b
    def mulnum(self):
        return self.a * self.b
    def divnum(self):
        return self.a / self.b
    
#it would cause an Error if we didn't have any arguments. It happens because we created constructor( __init__ )
firstnew = Twonum(25,5)

#it works well - 5.0
print(firstnew.divnum())


test1 = Newtwonum()
test1.setdata(15,5)

print(test1.mulnum())    #75
print(test1.pownum())    #759375 / 15^5

#AttributeError: 'Twonumber' object has no attribute 'pownum'
print(first.pownum())



#Method overriding

#If we try this we will get error
first.setdata(5,0)

#ZeroDivisionError: division by zero
print(first.divnum())

#What if we want to return 0 if we divide number by 0
class Noerror(Twonum):
    def divnum(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b
        
firstoverriden = Noerror(5,0)
print(firstoverriden.divnum())      #0
        
---
#Class variables
#Instance variables

class Family:
    
    #we just created a class variable called lastname
    lastname = "Kim"
    

#Now, there are several ways to check the class variables.

#1. enter Family.lastname - Classname.classvariable

print(Family.lastname)    #Kim

#2. enter firstperson.lastname - instance.classvariable

firstperson = Family()
secondperson = Family()

print(firstperson.lastname)    #we can check that the firstperson's lastname is Kim
print(secondperson.lastname)    #we can check that the secondperson's lastname is Kim too



#But, if we set firstperson's lastname to Schwab, we can check that firstperson's lastname has changed.
#From this moment on, now firstperson's lastname indicates to instance variable instead of Class variable 
firstperson.lastname = "Schwab"


print(firstperson.lastname)    #we can check that it has changed to Schwab
print(secondperson.lastname)    #secondperson's lastname hasn't changed. It applied to only the firstperson's lastname

#However, the class variable lastname is still Kim
print(Family.lastname)    #Kim




#If we change class variable to "Rothschild"
Family.lastname = "Rothschild"

#to check class variable
print(Family.lastname)    #Rothschild

print(firstperson.lastname)    #Schwab
print(secondperson.lastname)    #Rothschild
