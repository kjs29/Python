Tried on 5/28(x, didn't read the question correctly), 6/18(o), 7/10(o),11/25(o), 4/8(o)

Question
-
We have a basic dictionary
Create two different functions which figures out 
1. that prints keys
2. that prints values

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
<details>
  <summary>answer</summary>
  
  ```py
  #Create a function to print out keys
  def keys_dictionary(dic):

    #this prints out keys in a dictionary
    for a in dic:
      print(a)
    

  #Create a function to print out values
  def values_dictionary(dic):
    for b in dic:
      print(dic[b])

  ```
</details>

# Here is another answer I came up on 5/28
- I think the knowing the original answer is more important, because it is fundamental to know how to access keys, and values when we deal with dictionaries.
<details>
  <summary>answer2</summary>
  
  ```py
  def basic_key(dic):
      for a in dic.keys():
          print(a)

  def basic_value(dic):
      for a in dic.values():
          print(a)
  ```
</details>
