Create a function that returns only element, if there is a nested list as an element.

Make sure that there is no None value in the list.

For example,
```py
a = [[0],1,2,3,4]
b = [[1,2,3],5,[13,15,[50]]]
c = [1,[2,3,None,4],[None],5]
d = [[[]]]
e = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
f = [None, [[[None]]], None, None, [[None, None], None], None]

print(no_secret(a))
print(no_secret(b))
print(no_secret(c))
print(no_secret(d))
print(no_secret(e))
print(no_secret(f))
```
will result
```
[0, 1, 2, 3, 4]
[1, 2, 3, 5, 13, 15, 50]
[1, 2, 3, 4, 5]
[]
[0, 2, 2, 3, 8, 100, 4, 50, -2]
[]
```

<details>
  <summary>answer</summary>
  
  ```py
  def no_secret(lst):
      empty = []
      for a in lst:
          if isinstance(a, list):
              for each in no_secret(a):
                  empty.append(each)
          if not isinstance(a,list) and a!=None:
              empty.append(a)
      return empty
  ```
</details>
