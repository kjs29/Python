
1.
How to read/modify files
.read()
.readlines()
iterate through object
csv.DictReader()
csv.DictWriter()
.readline()
.write()
json.load()
json.dump()

#why we use 'with'?
#because 'with' creates a context-manager, which performs cleanup after mixing the adjacent indented block.

2.
Reading csv file (Comma-Separted Values)


3.
What is pandas?
Pandas is a fast, poweful, and easy to use data analysis and manipulation tool
Pandas is a module with extensive funcitonality for working with tabular data.
Tabular data : spreadsheet, excel

4.
Reading  json file(Javascript Object Notation)
Writing json file on python script

---

#Basic Syntax for reading the whole file
with open("file_name.txt") as object_name:
    variable_name = object_name.read()
print(variable_name)




#Basic Syntax for reading each line
with open("file_name.txt") as object_name:
    for a in object_name:       #for a in object_name.readlines():
        print(a)
        
        
        
        
#Basic Syntax for reading first line ONLY
with open("file_name.txt") as object_name:
    another_object_name = object_name.readline()
    print(another_object_name)
    
    
    
#Basic Syntax for OVERwriting a file

#normally open file has "r" as a default argument
with open("file_name.txt","w") as object_name:
    object_name.write("Any text we can write it but if the name of the file already exists, then it overwrites it")
    
     
    
    
#example of writing a file in Python program:
    
with open("any file.txt","w") as hello:
    hello.write("""
#To write any textfile in python IDE. Write a code as below:
#WARNING: be careful that this will overwrite any files that stored previously
    
with open("any file.txt","w") as hello:
    hello.write("write anyting, which will store as textfile.")""")

    
#Basic Syntax for appending to an existing file
with open("any file.txt","a") as chooga:      #notice that we have "a" as an argument, this means append.
    chooga.write("\nhello")                   #this will append "\nhello" to 'any file.txt' file.
    
    
    
    
#How to open csv file

#we first import csv library 
import csv

with open("csv_file_name.csv") as object_name:
  print(object_name.read())
  
  
  
  
---
#How to read json file
#It is same as reading a txt file

"""
let's suppose there is a json file called 'json_file_name.json'

{
 "user": "Jin",
 "occupation" : "software engineer",
 "age" : "29"
}

"""


#import json package
import json

with open("json_file_name.json") as object_name:
    variable_for_json = json.load(object_name)
print(variable_for_json['user'])                                #Jin




#how to write json file in python script

#let's say we have dictionary made in python script
bank_accounts = {'Jin': 25, 'Mary': 35000, 'John': 240000, 'Jay': 6630000, 'Aaron': 220, 'Bill': 35000}

#import json package
import json

with open("bank_accounts.json","w") as bank_accounts_object:            #notice that now ther is the second argument "w" 
    
    json.dump(bank_accounts, bank_accounts_object)                      #.dump() has two arguments, first being the name of the dictionary, and the file object
    
