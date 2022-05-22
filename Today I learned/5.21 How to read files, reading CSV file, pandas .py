
1.
How to read/modify files
.read()
.readlines()
iterate through object
.readline()
.write()

2.
Reading csv file (Comma-Separted Values)


3.
What is pandas?
Pandas is a fast, poweful, and easy to use data analysis and manipulation tool
Pandas is a module with extensive funcitonality for working with tabular data.
Tabular data : spreadsheet, excel



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
  
  
  
  
