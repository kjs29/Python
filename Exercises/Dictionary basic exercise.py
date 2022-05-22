"""
we have a basic dictionary
Create two different functions which figures out 
1. that returns keys
2. that returns values

"""



#Create a function to print out keys
def keys_dictionary(dic):
  
  #this prints out keys in a dictionary
  for a in dic:
    print(a)
  return a
    
#Create a function to print out values
def values_dictionary(dic):
  for b in dic:
    print(dic[b])
  return dic[b]
    
    
commodities = {"gold":1400, "silver":130, "iron":5}    
    
keys_dictionary(commodities)
values_dictionary(commodities)
