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
  from itertools import permutations

  def cases(word):
      lst = [y for y in word]
      answer = []
      for a in permutations(lst):
          b = "".join(a)
          answer.append(b)
      return answer

  print(cases("USA"))
  ```
</details>
