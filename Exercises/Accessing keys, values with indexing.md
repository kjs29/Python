We have a dictionary below,
```
favourite_languages = {
    "sarah":["c"],
    "jin":["python"],
    "scott":["c++","C"],
    "jules":["ruby"]
    }
```

But we want to print 3rd key:value pair like this,
```
Third key:value is Scott : ['c++', 'C']
```
How would we get it?

# Below is an answer
---

```
print(f"Third key:value is {list(favourite_languages)[2].title()} : {list(favourite_languages.values())[2]}")
```
