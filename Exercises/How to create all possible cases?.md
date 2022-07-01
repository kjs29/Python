We have a string

```
str1 = "USA"
```
Create a function that returns a list of strings of all possible combinations with each letter

```
['USA','UAS','SAU','SUA', 'AUS', 'ASU']
```
<details>
  <summary>Answer but not complete</summary>
  
  ```
  s1 = "USA"

  empty_lst = []
  l = int(len(s1)/2)
  print(s1[0])
  print(s1[l])
  print(s1[len(s1)-1])
    
  #get each position's letter
  first = s1[0]
  second = s1[l]
  last = s1[len(s1)-1]
  
  #maybe add them all?
  ```
</details>
