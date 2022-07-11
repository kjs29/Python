Tried on 7/10(x)

### You want the desired output
```py
"""
Enter the first number : w

Invalid first number, try again: e
    
Invalid first number, try again: 1

First number : 1

Enter the second number : e

Invalid second number, try again: False

Invalid second number, try again: 5

Second number : 5

Division result : 0.2
"""
```
or

```py
"""
Enter the first number : 1

First number : 1

Enter the second number : 0

Second number : 0

Division result : It is infinity, you tried to divide any number by 0
"""
```
### Make sure that no Traceback messages (ex. ZeroDivisionError, ValueError) are printed

<details>
  <summary>Answer</summary>
  
  ```py
  a_input = "Enter the first number: "
  a = input(a_input)

  while type(a) != int:
      try:
          a = int(a)
      except ValueError:
          a = input("\nInvalid first number, try again: ")
    
  print(f"\nFirst number : {a}")

  b = input("\nEnter the second number: ")

  while type(b) != int:
      try:
          b = int(b)
      except ValueError:
          b = input("\nInvalid second number, try again: ")
            
  print(f"\nSecond number : {b}")

  try:    
      result = a/b

  except ZeroDivisionError:
      print("\nIt is infinity, you tried to divide any number by 0")
    
  else:
      print(f"\nDivision result : {result}")
  ```
</details>
