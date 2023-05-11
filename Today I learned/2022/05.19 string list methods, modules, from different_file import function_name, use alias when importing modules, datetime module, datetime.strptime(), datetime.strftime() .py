5/19 Today I learned...

1.

How to convert strings into floats

How to calculate string values in a list.
ex. sales = ["$240","$55"] , what is the total sales?



2.
Functions < Modules < Packages < Library

What is module?
Module is a collection that has multiple pre-built functions.


Module has many functions.
Package has many modules.
Library has many packages.


How to use modules
Basic syntax for modules is as below:

from module_name import object_name


3.

Suppose we have two different files file1.py  and file2.py

And I defined a function 'function_random.py' in file1 and I want to be able to use this function in file2.py

In this case, I can write like this in the head of file2.py

from file1 import function_random
   (filename)       (function name) 
  


4.
#this means we can call some functions using 'draw' instead of pyplot
from matplotlib import pyplot as draw

import random

numbers_a = range(1,13)
numbers_b = random.sample(range(1,1001), 12)

draw.plot(numbers_a, numbers_b)
draw.show(numbers_a, numbers_b)



5.
from datetime import datetime

birthday = datetime(1992, 11, 14, 16, 0, 0)
print(birthday.year)                                  #1992
print(birthday.month)                                 #11
print(birthday.day)                                   #14
print(birthday.hour)                                  #15
print(birthday.minute)                                #59
print(birthday.second)                                #00

print(birthday.weekday())                             #5
#0 Monday
#1 Tuesday
#2 Wednesday
#3 Thursday
#4 Friday
#5 Saturday
#6 Sunday

#we can use datetime.now to calculate the current time
now = datetime.now()
print(now)                                               #2022-05-19 21:27:50.839434

#when I purchased first stock
firststock = datetime(2016,10,21)

#we can calculate between dates
diff = datetime(2018,1,1) - datetime(2014,1,1)  
print(diff)                                              #1461 days, 0:00:00

print(now - firststock)                                  #2036 days, 21:47:47.531646





6.

#How to use python docs for datetime.
Google 'python3 datetime'
Go to 'strftime() and strptime() Behavior' in the left menu bar

In this chart

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

we can see that what format we can use.




#How to use datetime.strptime()
#string -> datetime format



#we can put any string date as the first argument, and we can present the data as we like in the second argument.
#in this case, I want it to show like, '%b' = month first in abbreviated form like May,  '%d' = day  , and ', %Y' = a comma and year in 4 digits.
parsed_date = datetime.strptime("May 7, 2022", "%b %d, %Y")


print(parsed_date.month)                                 #5




#How to use datetime.strftime()
#datetime format -> string

date_string = datetime.strftime(now, "%b %d")
print(date_string)                                       #May 19


---example of how to calculate strings in list 

"""
How to get total sales from strings

Suppose we have a list

And we want to get the average price of these stockprices
"""


stockprice = ["$704", "$9.42", "$22", "$0.25", "$512", "$104", "$80", "$2500", "$412", "$65", "$8", "$2", "$900", "$202", "$54"] 



#first we need to make a variable that is sum of all of individual values
total = 0

#now iterate through each value in stockprice to add each value to the total price
for each in stockprice:
  
  #since "total += each" will probably cause some errors due to each being the strings, 
  #we must 1. TAKE AWAY "$" FROM 'EACH' and 2. TURN THE STRING INTO FLOAT by prepending 'float()' 
  total = total +float(each.strip("$"))
  
print(total)                                            #5574.67

average_price = total/len(stockprice)
print(average_price)                                    #371.6446666666667



---
