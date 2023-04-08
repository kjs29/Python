Tried on 7/10(o) 11/10(o), 4/8(o)
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

# Answer 11/10
<details>
  <summary>answer</summary>
  
  ```py
  s1 = "abc"
  s2 = "bs0ck02poa"
  def aaa(first,second):
      for each in first:
          if each not in second:
              return False

      return True


  def bbb(first,second):
      if aaa(first,second) == True:
          dic = {}

          for each in first:
              dic[each] = second.find(each)

          return dic

  print(aaa(s1,s2))
  print(bbb(s1,s2))
  ```
</details>
    
<details>
  <summary>Answer on 4.8</summary>
    
  ```py
  def first(substring, string):
      """Introduction
      Returns True if all letters in a substring exist in string"""

      for each_char in substring:
          if each_char not in string:
              return False

      return True


  def new_dictionary(substring, string):
      """Introduction
      If each letter in a substring exists in a string,
      it returns dictionary where each letter in a substring is key,
      and position of the letter in a string is value.
      """

      if not first(substring, string):
          return "There are some letters that don't exist in string."

      dic = {}

      for each in substring:
          dic.setdefault(each, string.index(each))

      return dic
  ```
</details>
