Tried on 6/12(x), 7/10(o), 11/10(o), 04/08(o)
---

We have a dictionary below,
```
favourite_languages = {
    "sarah":["c"],
    "jin":["python"],
    "scott":["c++","C"],
    "jules":["ruby"]
    }
```

But we actually don't know what the third key and value in the dictionary.
We want to print 3rd key:value pair like this using indexing.

```
Third key:value is Scott : ['c++', 'C']
```

How would we get it?

### Below is an answer


<details>
  <summary>Answer</summary>
    
  ```py
  print(f"Third key:value is {list(favourite_languages)[2].title()} : {list(favourite_languages.values())[2]}")
  ```
</details>

<details>
  <summary>Answer on 7/10</summary>
    
  ```py
  count = 0
  for k,v in favourite_languages.items():
      if count == 2:
          print(f"Third key:value is {k.title()}:{v}")
      count += 1
  ```
</details>

<details>
    
  <summary>Answer 11/10</summary>
    
  ```py
  favourite_languages = {
      "sarah":["c"],
      "jin":["python"],
      "scott":["c++","C"],
      "jules":["ruby"]
      }

  a = list(favourite_languages.keys())
  b = list(favourite_languages.values())

  print(f"Third key:value is {a[2].title()} : {favourite_languages[a[2]]}")
  ```
    
</details>

<details>
  <summary>Answer 04/08</summary>
    
  ```py
  for i in list(favourite_languages.keys()):
      if i == 2:
          print(f"{i} : {favourite_languages[i]}")
  ```
    
</details>
