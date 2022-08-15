# Tried on 8/14 (o)

Let's say there is a list of sets

```py
a = [{1,2,3},{4,5}]
```

Now you want to create a new set that has each element in each subset in `a`

just like

```py
new_set = {1,2,3,4,5}
```

How would you write the code?

<details>
  <summary>answer</summary>
  
  ```py
  a = [{1,2,3},{4,5}]
  new_set = set()
  for each in a:
      new_set |= each
  print(new_set)
  ```
  
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  a = [{1,2,3},{4,5}]
  new_set = {each_element for each_subset in a for each_element in each_subset}
  print(new_set)
  ```
</details>

<details>
  <summary>answer3 I came up with on 8/14</summary>
  
  ```py
  a = [{1,2,3},{4,5}]
  new_set = set()
  for each_set in a:
      for aa in each_set:
          new_set.add(aa)
  print(new_set)
  ```
</details>
