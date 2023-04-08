You are given a list of dictionaries, each representing a person with attributes such as name, age, and occupation. 

Your task is to write a function that takes in this list and returns a new list of dictionaries, 

where each dictionary represents a group of people with the same occupation. 

Each dictionary should have the occupation as the key and a list of names as the value.

For example, given the list of dictionaries:

```py
[     
      {"name": "Alice", "age": 25, "occupation": "teacher"},
      {"name": "Bob", "age": 30, "occupation": "teacher"},    
      {"name": "Charlie", "age": 35, "occupation": "doctor"},    
      {"name": "David", "age": 40, "occupation": "doctor"},    
      {"name": "Eve", "age": 45, "occupation": "engineer"}
]
```

Your function should return

```py
{
    "teacher": ["Alice", "Bob"],
    "doctor": ["Charlie", "David"],
    "engineer": ["Eve"]
}
```

<details>

  <summary>Answer 4.8</summary>
  
  ```py
  
  """
  create a dictionary

  iterate trhough the list
  iterate through the dictionary,

  if the value ('teacher') exists in the new dictionary, 
      if the value of the name doesnt exist in the value of the occupation
          a. add the value of the name to the value of the new dictionary.
  if the value('teacher') doesnt exist in the new dictionary, create a list and add the value of the name.
  return dictionary
  """
  
  def group(lst):
      dic = {}
      for individual in a:
          for k,v in individual.items():
              if k == 'occupation':
                  if v not in dic:
                      dic.setdefault(v, [individual['name']])
                  else:
                      dic[v].append(individual['name'])
      return dic
  ```
</details>
