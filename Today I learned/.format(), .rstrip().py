5/17 Today I learned...

1.
#we can modify strings using .format
.format() 

"""
Basic usage of .format is like this.
"""

name = "JK"
print("hello, my name is {}".format(name))                #hello, my name is JK


#to remove whitespaces in strings, we use this strips for user input and save their inputs in our database
.rstrip()
.lstrip()
.strip()


---example of .format(), .rstrip() .lstrip() .strip()
#usage of .format()
name = "Jin"
option = "NFLX C 360"

mydata = "My name is {}, and I have option of {}.".format(name,option)
print(mydata)

#usage of .rstrip()
#rstrip removes whitespace that is on the right side
a = "\tJin NFLX\t"
b = "Jin NFLX"

print(len(a.rstrip()), a.rstrip())          #9 	Jin NFLX
print(len(a.lstrip()), a.lstrip())          #9 Jin NFLX	
print(len(a.strip()), a.strip())            #8 Jin NFLX

