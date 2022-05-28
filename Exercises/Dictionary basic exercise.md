Tried on 5/28(x, didn't read the question correctly) 

Question
-
We have a basic dictionary
Create two different functions which figures out 
1. that returns keys
2. that returns values

For example, 
```
commodities = {"gold":1400, "silver":130, "iron":5}  
```
Should return
```
gold
silver
iron
```
```
1400
130
5
```

# Below is answer
---

```
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
      
```

# Here is another answer I came up on 5/28
- I think the knowing the original answer is more important, because it is fundamental to know how to access keys, and values when we deal with dictionaries.
```
def basic_key(dic):
    for a in dic.keys():
        print(a)

def basic_value(dic):
    for a in dic.values():
        print(a)
```
