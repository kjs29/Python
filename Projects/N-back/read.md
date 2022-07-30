### 2 - back
```py
import random
lst = []
for each in range(21):
    lst.append(random.randint(1,9))
print(f"lst : {lst}")

lst2 = []
for i in range(len(lst)):
    if 0 <= i < 2 :
        lst2.append(lst[i])
    if i >= 2:
        #print(f"lst[i]:{lst[i]}")
        #print(f"lst[i-2]:{lst[i-2]}")
        if lst[i] == lst[i-2]:
            lst2.append("O")
        else:
            lst2.append("X")
        

print(f"lst2: {lst2}")
```


```
lst : [5, 1, 9, 9, 9, 5, 8, 5, 2, 7, 1, 2, 1, 2, 7, 8, 7, 4, 4, 4, 7]
lst2: [5, 1, 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'X']
```

### 3 - back
```py
import random
lst = []
for each in range(21):
    lst.append(random.randint(1,9))
print(f"lst : {lst}")

lst2 = []
for i in range(len(lst)):
    if 0 <= i < 3 :
        lst2.append(lst[i])
    if i >= 3:

        if lst[i] == lst[i-3]:
            lst2.append("O")
        else:
            lst2.append("X")
        

print(f"lst2: {lst2}")
```

```
lst : [4, 4, 3, 4, 4, 7, 5, 6, 4, 5, 3, 5, 7, 1, 3, 3, 1, 4, 9, 8, 8]
lst2: [4, 4, 3, 'O', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X']
```
