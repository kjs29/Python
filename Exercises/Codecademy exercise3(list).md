Tried on 5/28(o), 6/20(x), 7/10(o), 11/17(o), 04/08(o)


Let's say there are a list,
and we want to double the index,
and replace the original indexed element with the doubled indexed number.
if index number is too big in the list, it would just return the original list.

Create a function `double_index` that does this.

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

<details>
  <summary>answer</summary>

  ```py
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
</details>        
  
<details>
  <summary>Another answer I came up with on 5/28</summary>
  
  ```py
  def double_index(lst, index):
      if index < len(lst):
          lst[index] = 2 * lst[index]
          return lst
      else:
          return lst
  ```
</details>
  
<details>
  <summary>answer on 11/17</summary>
  
  ```py
  def double_index(a,b):
      if b >= len(a):
          return a
      else:
          a[b]= a[b]*2
          return a

  print(double_index([1,21,25,8],4))
  ```
</details>
