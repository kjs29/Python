5/20 Today I learned ...
1.
Dictionaries
- What is dictionaries?
- When do we use it?
- How to create dictionaries?
- How to put two lists in a dictionary?
- How to add key:value to a dictionary?
- How to access value in a dictionary? 
- How to check if a certain keyword exists in a dictionary?
- Use of Try/Except
- .get()
- How to delete key in a dictionary using .pop()
- How to get all keys in a dictionary? (How to get dict_keys)
- How to get all values in a dictionary? (How to get dict_values)
- How to get both keys and values in a dictionary? 
---

Dictionaries
Dictionaries is a 'key : value' pair.
  
In many cases we have information like this

My bank account has 25 dollars.
Mary's bank account has 35,000 dollars.
John's bank account has 240,000 dollars.

Dictionaries are useful in this case.
bank_accounts = {"Jin":25, "Mary":35000, "John":240000}

Syntax for dictionaries are
name_dictionaries = {"key": value, "key": value, "key":value}
#curly brackets, each items has a key and a value, and each pair is separated by a comma
#key can be a number, it doesn't have to be a string
#value can be any datatype, it can be another set of dictionaries too!


#we can add a new SINGLE PAIR of key:value to a dictionary

Syntax is as below,

dictionary[key] = value

bank_accounts["Jay"] = 6630000
print(bank_accounts)                                #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000}


#we can add a MULTIPLE PAIRS of key:value to a dictionary by using .update()
bank_accounts.update({"Hans":4000,"Aaron":220,"Bill":35000}
print(bank_accounts)                                #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Hans': 4000, 'Aaron': 220, 'Bill': 35000}

#Creating a dictionary - FROM TWO LISTS - Syntax

name_dictionary = {key:value for key,value in zip.(keylist, valuelist)}               #key:value NOT key,value
                 
                    
                     
                     
                   
#overwriting key:value in a dictionary
bank_accounts["Hans"] = 5000
print(bank_accounts)                                #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Hans': 5000, 'Aaron': 220, 'Bill': 35000}

                     

                     

#examples of dictionaries

#key = string, value = list
students_in_classes = {"Computer science":["John","Mary","Chang"],"Law":["Raveena","Peter"],"Architecture":["Hans","Eugene"]}

#dictionaries can hold many different types of values(string, boolean, list)
person = {"name":"Mike", "college degree": False, "stock holdings" : ["KO", "APPL"]}

#this is empty dictionary
empty_dictionary = {}


#we can add a new pair of single key:value to a dictionary
empty_dictionary["maybe not"] = 20
print(empty_dictionary)                             #{'maybe not': 20}

                     
                     
#How to access value in a dictionary
a = empty_dictionary["maybe not"]
print(a)                                              #20
                     
                     
#how to check if they have key in a dictionary
b = "maybe not"
if b in empty_dictionary:
    print(a)                                          #20
                     
                     
#we can also use try/except to check if they have certain keyword
                
                     
#{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Hans': 5000, 'Aaron': 220, 'Bill': 35000}                     
print(bank_accounts)

                     
                     
#.get()
#we can use .get() to find out if they have key in a dictionary
#this is more sustainable and simpler
                     
bank_accounts.get("Mary")
print(bank_accounts.get("Mary"))                             #35000

                     
#if we want to get certain message if keyword doesn't exist in the dictionary
bank_accounts.get("Jonny","No value")
print(bank_accounts.get("Jonny","No value")                       #No value
      
                     
#Your request to Jin's bank account: 25                     
try:
  print("Your request to Jin's bank account: "+str(bank_accounts["Jin"]))
except:
  print("No name found : \"Jin\"")       
      
      
      
      
#How to delete a key from a dictionary
bank_accounts = {'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Hans': 5000, 'Aaron': 220, 'Bill': 35000}
      
#we want to delete 'Hans' from the dictionary
bank_accounts.pop("Hans")
print(bank_accounts)                                    #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000}
      
#There is another way to delete key:value pair

#adding the value again.
bank_accounts["Hans"] = 5000
print(bank_accounts)                                    #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000, 'Hans': 5000}
      
#we can use del      
del bank_accounts["Hans"]                               #delete Hans:5000
print(bank_accounts)                                    #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000}
      
      
      
#We can also have a default value if the keyword we are trying to delete does NOT exist
hong = bank_accounts.pop("Hong", "No value existing")
print(hong)                                             #No value existing
      
      
#what if we want to get all keys in a dictionary?
bank_accounts = {'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000}


#we can get all keys using list()
print(list(bank_accounts))                  #['Jin', 'Mary', 'John', 'Jay', 'Aaron', 'Bill']
      
      
      
#we can also get a dict_keys using .keys()
print(bank_accounts.keys())                       #dict_keys(['Jin', 'Mary', 'John', 'Jay', 'Aaron', 'Bill'])
      
      
      
      
#Individually we can print out what was in dict_keys
for a in bank_accounts.keys():
      print (a)                               
      
"""
Jin
Mary
John
Jay
Aaron
Bill
"""

      
#how to get all values in a dictionary?
#we can use .values()
      
bank_accounts = {'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000}

      
#we can look at values using .values()
print(bank_accounts.values())                            #dict_values([25, 35000, 240000, 6630000, 220, 35000])

#or we can access each individual elements in the dictionary using for iteration
for a in bank_accounts.values():
    print(a)                                            

"""
25
35000
240000
6630000
220
35000
"""
      
#we can put the each values into a list.
aaa = []
for a in bank_accounts.values():
    aaa.append(a)
print(aaa)                                                  #[25, 35000, 240000, 6630000, 220, 35000]
      
      
#or we can also use list() then, we will get a list
print(list(bank_accounts.values()))                         #[25, 35000, 240000, 6630000, 220, 35000]
      
      
      
