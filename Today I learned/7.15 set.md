# 7/15 Today I learned...


# set

Set is like a dictionary, it has only one element for each.

But items in set are unordered so if order is important, set is not the one to use.

To find if they have common elements
```py
a = {1}
b = {3,2,4}
print(a.isdisjoint(b))      #False
```

```py
c = {1,24,25}
d = {1,25,24,2}
print(c.issubset(d))

print(c.intersection(d))

print(c.union(d))

print(d.difference(c))
```
```py
lst1 = [1,5,3,23,23,23]
dic1 = dict.fromkeys(lst1)
lst1 = list(dic1)
print(lst1)

lst2 = [1,5,3,23,23,23]
dic2 = {}
for each in lst2:
    dic2[each] = None
lst2 = list(dic2)
print(lst2)


lst = [1,3,5,7,9,25]
set1 = set(lst)

print(set1)
```
