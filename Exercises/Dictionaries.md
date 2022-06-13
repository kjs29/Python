Tried on 5/28(x), 6/12(o)
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

# answer
-
```
for a,x in favourite_languages.items():
    if len(x) != 1:
        print(f"\n{a.title()}'s favourite languages are: ")
    else:
        print(f"\n{a.title()}'s favourite language is: ")
    for each in x:
        print(f"\t{each.title()}")
```

# another answer
```
for a in favourite_languages:
    
    if len(favourite_languages[a]) != 1:
        print(f"\n{a.title()}'s favourite languages are : ")
    else:
        print(f"\n{a.title()}'s favourite language is : ")
    for each_value in favourite_languages[a]:
        print(f"\t{each_value.title()}")
```
