how can I turn `somelst` into one list comprehension?

```py
from typing import Iterable

a = [[0],1,2,3,4]
b = [[1,2,3],5,[13,15,[50]]]
c = [1,[2,3,None,4],[None],5]
d = [[[]]]
e = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
f = [None, [[[None]]], None, None, [[None, None], None], None]

def no_secret(lst):
    somelst = []
    for n in lst:
        if not isinstance(n,Iterable) and (n != None):
            somelst.append(n)
        
        if isinstance(n,list):
            for each in no_secret(n):
                somelst.append(each)
        
    return somelst



if __name__ == "__main__":
    print(no_secret(a))
    print(no_secret(b))
    print(no_secret(c))
    print(no_secret(d))
    print(no_secret(e))
    print(no_secret(f))

```
result
```
[0, 1, 2, 3, 4]
[1, 2, 3, 5, 13, 15, 50]
[1, 2, 3, 4, 5]
[]
[0, 2, 2, 3, 8, 100, 4, 50, -2]
[]
```
