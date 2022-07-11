Let users have two arbitrary numbers

Find the Least Common Multiple

<details>
  <summary>answer</summary>
  
  ```py
  a = int(input("Enter the first number: \n"))
  b = int(input("Enter the second number: \n"))
  maxNum = max(a,b)

  while (maxNum % a != 0 or maxNum % b != 0):
      maxNum += 1
  print(f"lcm of {a} and {b} is {maxNum}")
  ```
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  a = int(input("Enter the first number : \n"))
  b = int(input("Enter the second number : \n"))
  
  maxNum = max(a,b)
  while True:
      if maxNum % a == 0 and maxNum % b == 0:
          break
      maxNum += 1
  print(f"lcm of {a} and {b} is {maxNum}")
  
  ```
</details>


<details>
  <summary>answer 7/10</summary>
  
  ```py
  def lcm(n1,n2):
      if max(n1,n2) % min(n1,n2) == 0:
          return max(n1,n2)
      else:
          for a in range(min(n1,n2), 0, -1):
              if n1 % a == 0 and n2 % a == 0:
                  first = n1//a
                  second = n2//a
                  return first * second * a
  ```
</details>
