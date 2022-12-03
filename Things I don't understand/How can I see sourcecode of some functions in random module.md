```py
import random

#generate random integer between 1<=n<=10
number1 = random.randrange(1,11)
```
Now I am curious how this code is generated.

does this generate each number with 10% chance?

I think `get.source(object)` does not work on built in modules.

We can also see where compiled files are located as well by

```
print(random.__file__)
```
