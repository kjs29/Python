Tried on 6/12(x), 7/2(x), 7/10(o), 11/10(o), 04/08(x)
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
