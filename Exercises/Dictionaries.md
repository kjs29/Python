Tried on 5/28(x), 6/12(o), 7/10(o), 11/24(o)
---

# You are given 
```
favourite_languages = {
    "jen": ["python","ruby"],
    "sarah": ["c"],
    "edward":["ruby","go"],
    "phil":["python","haskell"]
    }
```
You want the output to be like this.
```
Jen's favourite languages are: 
	Python
	Ruby

Sarah's favourite language is: 
	C

Edward's favourite languages are: 
	Ruby
	Go

Phil's favourite languages are: 
	Python
	Haskell
```

How would you write the code?

### Below is answer
<details>
  <summary>answer</summary>

  ```py
  for a,x in favourite_languages.items():
      if len(x) != 1:
          print(f"\n{a.title()}'s favourite languages are: ")
      else:
          print(f"\n{a.title()}'s favourite language is: ")
      for each in x:
          print(f"\t{each.title()}")
  ```
</details>

#### another answer

<details>
  <summary>answer2</summary>
	
  ```py
  for a in favourite_languages:
    
      if len(favourite_languages[a]) != 1:
          print(f"\n{a.title()}'s favourite languages are : ")
      else:
          print(f"\n{a.title()}'s favourite language is : ")
      for each_value in favourite_languages[a]:
          print(f"\t{each_value.title()}")
  ```
</details>

<details>
  <summary>answer 11/24</summary>
  
  ```py
  favourite_languages = {
      "jen": ["python","ruby"],
      "sarah": ["c"],
      "edward":["ruby","go"],
      "phil":["python","haskell"]
      }

  for k, v in favourite_languages.items():
      if len(v) > 1:
          print(f"{k.capitalize()}'s favourite languages are:")
      else:
          print(f"{k.capitalize()}'s favourite language is:")
        
      for each in v:
          print(f"\t{each.capitalize()}")
      print("\n")
  ```
</details>
