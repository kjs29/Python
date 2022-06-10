# 6/9 Today I learned...

# choice(), randint()

Creating some random game
```py
#we will bring built in modules called 'random' and import randint, choice functions
from random import randint, choice

#choice randomly chooses one element out of list, or tuples.
a = [1,2,3,4,5]
random_a = choice(a)
print(random_a)

b = randint(1,5)
print(b)

if random_a == b:
    print("Heck yeah!")
```

`choice()` takes one random element out of a list, or tuple
```
print(choice([1,2,3,4,5]))
#this will return any random element in the list
```

`randint()` takes two arguments(numbers), and it returns a random number between the two numbers.
```
print(randint(1,5))
#this will generate a random number between 1 to 5(including 5)
```
