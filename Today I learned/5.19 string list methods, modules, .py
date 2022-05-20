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
