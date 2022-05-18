5/17 Today I learned...

1. .format() , fstring
#we can modify strings using .format
.format() 

"""
Basic usage of .format is like this.
"""

name = "JK"
print("hello, my name is {}".format(name))                #hello, my name is JK


#f-string
print(f"hello my name is {name}")                         #hello my name is JK

2.
list comprehension again
places = ["Seoul","San Francisco","New York","Toronto","Vancouver"]

places = ["I will go to {}, and I will have a beautiful house in {}.".format(a,a) for a in places]
print(places) #['I will go to Seoul, and I will have a beautiful house in Seoul.', 'I will go to San Francisco, and I will have a beautiful house in San Francisco.', 'I will go to New York, and I will have a beautiful house in New York.', 'I will go to Toronto, and I will have a beautiful house in Toronto.', 'I will go to Vancouver, and I will have a beautiful house in Vancouver.']

3.
#how to take numbers as input

#input() function takes input as string
#so we have to write like this to take it as integers or float

initialcapital = int(input("Enter your initial capital : "))
print(initialcapital)

---example of rstrip,lstrip, strip
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

---example of adding list
#we can add elements from a different list to another list

activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = []

#we want to add only Q to inactiveusers list
inactiveusers.append(activeusers[0])
print(inactiveusers)                        #["Q"]

#but if we use append for adding multiple elements we get to have another list
inactiveusers.append(activeusers[1:-1])
print(inactiveusers)                         #[Q,["G","A","E","L","C","B"]]

#So if we want to add elements normally we have to use .extend()
activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = []

inactiveusers.extend(activeusers)
print(inactiveusers)                        #["Q","G","A","E","L","C","B","U"]

#inserting an element in certain element
activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = ["Z","ZZ","ZI"]

#we want to insert 'Q' from activeusers to inactiveusers group after ZZ in inactiveusers
inactiveusers.insert(2,activeusers[0])

print(inactiveusers)                        #['Z', 'ZZ', 'Q', 'ZI']

#Let's see what happens to original activeusers list
print(activeusers)                          #['Q', 'G', 'A', 'E', 'L', 'C', 'B', 'U']

#I feel like .insert() function is most useful in real world
#Because .insert() also allows us to insert an element at certain index



---example of removing elements from lists
activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = ["Z","ZZ","ZI"]

#if we want to remove the last item in a list
inactiveusers.pop()
print(inactiveusers)                #['Z', 'ZZ']

#now we want to remove two items , let's say Z, ZZ from inactive users
del inactiveusers[:2]
print(inactiveusers)                                #[]

#But, what if we wanted to copy the elements Z, ZZ and add them to active users initially?
activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = ["Z","ZZ","ZI"]

activeusers.extend(inactiveusers[:2])
removedlist = []
removedlist.extend(inactiveusers[:2])
del inactiveusers[:2]           #delete multiple elements
print(activeusers)              #["Q","G","A","E","L","C","B","U","Z","ZZ"]
print(inactiveusers)            #["ZI"]
print(removedlist)              #["Z","ZZ"]

#Conclusion : to remove multiple elements, del statement is the most useful
#             if we want to copy paste, and remove from the original list , we probably have to make another user-made-function.

activeusers = ["Q","G","A","E","L","C","B","U"]
inactiveusers = ["Z","ZZ","ZI"]



#build function that allows us to copy lst1 and paste it to lst2
def copypaste(lst1,lst2):
  #first we need to add the list to another list
  lst2.extend(lst1)
  del lst1

copypaste(activeusers[:3],inactiveusers)    #copy Q,G,A from activeusers and paste it to inactiveusers
"""
first we add activeusers[:3] to inactiveusers
second we delete activeusers[:3]
"""

print(activeusers)              #What I expected was ["E","L","C","B","U"], but result shows ['Q', 'G', 'A', 'E', 'L', 'C', 'B', 'U']
print(inactiveusers)            #["Z","ZZ","ZI","Q","G","A"]

---example of input()


"""
create a list that shows the return of %5 each year for 10 years 
Let user decide their initial capital
And their return percentage each year
"""

#how to take numbers as input

#input() function takes input as string
#so we have to write like this to take it as integers or float

initialcapital = int(input("\nEnter your initial capital : "))
returns = int(input("\nEnter your return percentage : "))
print("Your initial capital is {}, and your percentage return is {}.".format(initialcapital,returns))

#do it for 10 times
for a in range(10):
    
    initialcapital = initialcapital*(1+(0.01*returns))
    print(initialcapital)

