Tried on 7/10(o),11/25(o)
---

# we have a dictionary
```py
users = {
    "aeinstein": {
        "first":"albert",
        "last":"einstein",
        "location":"princeton",
        },
    "mcurie": {
        "first":"marie",
        "last":"curie",
        "location":"paris",
        }
    }
```
And we want console to look like this,

```
Username: aeinstein
	Fullname: Albert Einstein
	Location: Princeton

Username: mcurie
	Fullname: Marie Curie
	Location: Paris
```

# Below is an answer
---
<details>
  <summary>answer</summary>
	
```py
for x,y in users.items():

   
    thirdkey = list(users[x])[2]
    firstname = list(users[x].values())[0]
    lastname = list(users[x].values())[1]

    print(f"\nUsername: {x}")
    print(f"\t{'fullname'.title()}: {firstname.title()} {lastname.title()}")
    print(f"\t{thirdkey.title()}: {list(users[x].values())[2].title()}")
```
</details>
<details>
  <summary>answer2</summary>
	
  ```py

  for x,y in users.items():
      print(f"Username : {x}")
      print(f"\tFullname : {y['first'].title()} {y['last'].title()}")
      print(f"\tLocation : {y['location'].title()}")
  ```
</details>

<details>
  <summary>answer I came up with on 7/10</summary>
  
  ```py
  for key in users:
      print(f"Username: {key}")
      #print(users[key])
      fullname = users[key]["first"].title() + " " + users[key]["last"].title()
      location = users[key]["location"].title()
      print(f"\tFullname: {fullname}")
      print(f"\tLocation : {location}")
  ```
</details>
