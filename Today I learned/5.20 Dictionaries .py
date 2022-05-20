5/20 Today I learned ...
1.

Dictionaries
Dictionaries is a key : value pair.
  
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


                     
                     
                   
#overwriting key:value in a dictionary
bank_accounts["Hans"] = 5000
print(bank_accounts)                                #{'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Hans': 5000, 'Aaron': 220, 'Bill': 35000}
                     

---examples of dictionaries

#key = string, value = list
students_in_classes = {"Computer science":["John","Mary","Chang"],"Law":["Raveena","Peter"],"Architecture":["Hans","Eugene"]}

#dictionaries can hold many different types of values(string, boolean, list)
person = {"name":"Mike", "college degree": False, "stock holdings" : ["KO", "APPL"]}

#this is empty dictionary
empty_dictionary = {}


#we can add a new pair of single key:value to a dictionary
