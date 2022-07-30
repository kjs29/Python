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
    if i>=2:
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
