Tried on 7/10(o)
----

We have two strings

```
s1 = "abc"
s2 = "bs0ck02poa"
```

## Two questions

### 1. Create a function if all each letters in s1 are present in s2, return True, otherwise return False

### 2. If all each letters in s1 are present in s2, Create a function that returns a dictionary

    where individual letter is a key, and the position of that key in s2 is a value

for exameple,
```
{'a': 9, 'b': 0, 'c': 3}
```
Answer # 1
---
<details>
  <summary>answer #1</summary>
  
  ```py
  def a(b,c):
      for each_letter in b:
          if each_letter not in c:
              return False
      return True
  ```
</details>


Answer #2
---

<details>
  <summary>answer #2</summary>
  
  ```py
  s1 = "abc"
  s2 = "bs0ck02poa"
  dic = {}
  def a(b,c):
      for each_letter in s1:
          if each_letter in s2:
              dic[each_letter] = s2.find(each_letter)

      return dic

  print(a(s1,s2))
  ```
  
</details>
  
<details>
  <summary>another answer for #2 I came up with on 7.10</summary>
  
  ```py
  def second(a,b):
      dic = {}
      for each in a:
          if each in b:
              dic.setdefault(each,b.index(each))
      return dic
  ```
</details>
