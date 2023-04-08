Tried on 6/12(x), 7/2(x), 7/10(o), 11/10(o), 04/08(x), 04/09(o)
---

This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. 

We need to calculate the number of people who have the same first letter in their last name. Here are the steps we need:

---

We want to create a function that turns
```
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
```
into
```
{"S" : 4, "L": 3}
```



<details>
  <summary>answer</summary>
  
  ```py
  def count(dic):
      
      #we need to create an empty dictionary
      emp = {}
      
      for key in dic.keys():
          if key[0] not in emp.keys():
              emp[key[0]] = 0
          emp[key[0]] += len(dic[key])
      return emp
  
  ```
</details>

<details>
  <summary>answer I came up with on 7/10</summary>
  
  ```py
  def count(s):
      dic = {}
      for key,value in s.items():
          dic.setdefault(key[0],0)
          if key[0] in dic:
              dic[key[0]] += len(value)

      return dic
  ```
</details>

<details>
  <summary>another answer I came up with on 7/10</summary>
  
  ```py
  def count(s):
      dic = {}
      for key,value in s.items():
          if key[0] not in dic:
              dic.setdefault(key[0],len(value))
          else:
              dic[key[0]] += len(value)
      return dic
  ```
</details>

<details>
  <summary>answer 11/10</summary>
  
  ```py
  names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

  def count(s):
      dict1 = {}

      for k,v in s.items():
          alphabets = k[0]
          if alphabets not in list(dict1.keys()):
              dict1[alphabets] = 0
          if alphabets in list(dict1.keys()):
              dict1[alphabets] += len(s[k])

      return dict1

  print(count(names))
  ```
  
</details>


<details>

  <summary>Answer 04/09</summary>
  
  ```py
  def count(dic):
      """ Instruction
      1. create a new dictionary 'newdic' because we can't modify keys in the existing 'dic'. 
      2. iterate through the 'dic',
          a. create a variable 'first_capital_char' that stores the first capical letter of each keys
          b. if the varible doesn't exist in the new dictionary, 
             set length of the corresponding value in the 'dic' as the value. 
          c. if the variable exists in the new dictionary, 
             add the length of the corresponding value in the 'dic' to the value of 'newdic'.
      3. return 'newdic'
      """

      newdic = {}

      for key, value in dic.items():
          first_capital_char = key[0].upper()
          if first_capital_char not in newdic:
              newdic[first_capital_char] = len(value)
          else:
              newdic[first_capital_char] += len(value)

      return newdic
  ```
</details>
