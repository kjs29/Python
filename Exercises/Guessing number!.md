We let the program to generate the random number between 1~100

Let the user guess the number between 1~100

If the random number is higher than user's guess, it says 'up'

if the random number is lower than user's guess, it says 'down'

Mkae sure to mention how many tries user has also.

<details>
  <summary>answer</summary>
  
  ```py
  import random

  #create a random number between 1~100, 101 is exclusive
  real_number = random.randrange(1,101)
  
  #count variable to keep track of counts
  count = 0

  
  
  user_guess = int(input("Enter a number (1~100) : "))
  count += 1
  
  if user_guess > real_number:
      print(f"down\ncount: {count}")
  elif user_guess < real_number:
      print(f"up\ncount: {count}")
  else:
      print(f"Correct! I think it is time to buy lottery ticket!\ncount: {count}")

  while count>=1:

      user_guess = int(input("\nEnter a number(1~100) : "))
      count += 1

      if user_guess > real_number:
          print(f"down\ncount: {count}")
      elif user_guess < real_number:
          print(f"up\ncount: {count}")
      else:
          print(f"Correct\ncount: {count}")
          break
  ```
</details>
