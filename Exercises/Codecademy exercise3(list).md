Tried on 5/28(o)


Let's say there are a list,
and we want to double the index,
and replace the original indexed element with the doubled indexed number.
if index number is too big in the list, it would just return the original list.

Create a function that does this.

For example,
```
double_index([1,21,25,8],2)
```
should return 
```
[1,21,50,8]
```
# Below is answer
---
```
#.Create function with two parameters lst, and index
def double_index(lst,index):
  if index < len(lst):
    a = lst[index] * 2
    lst.remove(lst[index])
    lst.insert(index,a)
    return lst
  else:
    return lst
```

# Here is another answer I came up with on 5/28
```
def double_index(lst, index):
    if index < len(lst):
        lst[index] = 2 * lst[index]
        return lst
    else:
        return lst
```