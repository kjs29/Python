Create a function that returns True if it is a leap year ,if it is not a leap year, returns False.

Leap Year rule
```
If year is divisible by 4 but it shouldnt be divisible by 100, unless it is divisible by 400
```

<details>
  <summary>answer</summary>
  
  ```py
  def leap_year(year):
      if year % 4 == 0:
          if year % 100 == 0:
              if year % 400 == 0:
                  return True
              return False
          return True
      return False
  ```
  
</details>
