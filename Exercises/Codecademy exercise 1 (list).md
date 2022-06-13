Tried on 5/28(o)


I was working on Codecademy question
and I am struggling with understanding english
a good programmer means a programmer who can understand the problem instantly
and solves questions.
I need to work on English comprehension skills as well as coding skills.


# question.

```
Our factory produces a variety of different flavored snacks and 
we want to check the number of instances of a certain type. 
We have a conveyor belt full of different types of snacks represented by different numbers. 
Our function will accept a list of numbers (representing the type of snack), 
a number for the second parameter (the type of snack we are looking for), 
and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). 
The function will return True if the snack we are searching for appears more times than we provided as our third parameter. 

These are the steps we need:

1. Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
2. Count the number of occurrences of item (the second parameter) in lst (the first parameter)
3. If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False
```
# below is answer
<details>
  <summary>code</summary>
  
  ```py

  def some_function(lst,number,n):
    #2.
    a = lst.count(number)
    #3.
    if a > n:
      return True
    else:
      return False
  ```
</details>

# another answer I came up with on 5/28
<details>
  <summary>code</summary>
  
  ```py
  hello = [15,23,1,12,4,12,12,3,4,1,7463,3463,63,53,4]        

  def factory(lst, number_to_find, instances):
      count = 0
      for number in lst:
          if number == number_to_find:
              count += 1
      print(count)
      if count > instances:
          return True
      else:
          return False


  factory(hello,4,3)      #False
  ```
</details>
