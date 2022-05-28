# we have a dictionary
```
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
```
for x,y in users.items():

   
    thirdkey = list(users[x])[2]
    firstname = list(users[x].values())[0]
    lastname = list(users[x].values())[1]

    print(f"\nUsername: {x}")
    print(f"\t{'fullname'.title()}: {firstname.title()} {lastname.title()}")
    print(f"\t{thirdkey.title()}: {list(users[x].values())[2].title()}")
```
