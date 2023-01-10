There is a dictionary.

```py
info = {"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }
```
Create a function that returns a dictionary like this

```py
{'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
```

<details>
  <summary>answer</summary>

  ```py
  def random_function(info):
      new = {}
      for k,v in info.items():
          for each in v:
              # print(each)
              new.setdefault(each,[])
        
              if each in new:
                  new[each].append(k)
      return new
  ```
</details>