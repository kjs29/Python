Tried on 6/12 (o)
---

We let the program to generate the random number between 1~100

Let the user guess the number between 1~100

If the random number is higher than user's guess, it says 'up'

if the random number is lower than user's guess, it says 'down'

Make sure to mention how many tries user has also.

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
<details>
  <summary>answer2</summary>
  
  ```py
  from random import randint
  real = randint(1,100)
  count = 0

  a =int(input("What is your guess? Enter a number\n"))
  count += 1
  if a > real:
      print(f"\ndown, count : {count}")
  elif a < real:
      print(f"\nup, count : {count}")
  else:
      print(f"\nwow correct!, count : {count}")

  while real != a:
      a = int(input("\nWhat is your guess? Enter a number\n"))
      count += 1
      if a > real:
          print(f"\ndown, count : {count}")
      elif a < real:
          print(f"\nup, count : {count}")
      else:
          print(f"\nwow correct!, count : {count}")
  ```
</details>               
