# When we create class...


What is the difference between

```py
class Cat:
    def __init__(self, name, age, has_eaten = False):
        self.name = name
        self.age = age
```

and 

```py
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.has_eaten = False
```
?
