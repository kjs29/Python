Tried on 5/28(o)


```
Every Three Numbers
Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 
starting from a number that is passed to the function as an input parameter. 

Here is what we need to do:

1.Define the function to accept one parameter for our starting number
2.Calculate the numbers between the starting number and 100 while incrementing by 3
3.Store the numbers in a list
4.Return the list
```

# Below is answer
<details>
  <summary>answer</summary>
  ```py
  def some_function(start):
      #2.3.4
      return list(range(start,101,3)) 
  ```
</details>

<details>
  <summary>Another answer I came up with on 5/28</summary>

  ```py

  def increase_by_three(starting_number):
      lst = []

      while starting_number<=100:
          lst.append(starting_number)
          starting_number += 3
      return lst
  
  print(increase_by_three(88))        #[88, 91, 94, 97, 100]
  
  ```
</details>

<details>
  <summary>answer 7.10</summary>
  
  ```py
  def every_three_numbers(starting_number:int) -> list:
      return list(range(starting_number, 101, 3))
  ```
</details>
