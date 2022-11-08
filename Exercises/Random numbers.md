# Tried on 11/08(o)

Create a function that makes two lists of 5 numbers and also shows how many tries it takes until two lists of 5 randomly generated numbers are identical

<em>These are identical</em>
```py
a = [1,5,3,4,7]
b = [1,5,3,4,7]
```
<em>These are not identical</em>
```py
a = [1,5,3,4,7]
b = [5,2,3,7,4]
```
<details>
  <summary>answer</summary>
  
  ```py
  
  def shows_how_many_tries_until_two_lists_of_5_numbers_are_the_same():
      import secrets
      a = []
      b = []
      for _ in range(5):
          a.append(secrets.randbelow(9)+1)
          b.append(secrets.randbelow(9)+1)
      print(a,b)

      count = 0
      while True:
          if a != b:
              a = []
              b = []
              for _ in range(5):
                  a.append(secrets.randbelow(9)+1)
                  b.append(secrets.randbelow(9)+1)
              count += 1
              print(count)
          else:
              print(a,b)
              print(f"count : {count}")
              break


  shows_how_many_tries_until_two_lists_of_5_numbers_are_the_same()


  ```
</details>

<details>
  
  
  <summary>answer on 11/08</summary>
  
  ```py
  
  def random_function():
      import random

      a = []

      b = []

      for _ in range(5):
          a.append(random.randint(1,10))
      # c = [5,4,3,2,1]
      # d = [5,4,3,2,1]
      count = 0

      while True:
          if a == b:
              print(f"count : {count}")
              print(f"a:{a}\nb:{b}")
              break
          else:
              b = []
              for _ in range(5):
                  b.append(random.randint(1,10))
              count += 1
              print(f"count is {count}")
      print(count)


  random_function()
  ```
</details>
