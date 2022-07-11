Tried on 7/10(o)
---

We have two random numbers

Create a function that returns the greatest common multiple
<details>
  <summary>answer</summary>
  
  ```py
  def find_gcd(num1,num2):
      empty_list = []
      for a in range(1, min(num1,num2)+1):
          if(num1 % a ==0) and (num2 % a == 0):
              empty_list.append(a)
          a+=1
      return max(empty_list)

  print(find_gcd(123132, 12312))   #12
  ```
</details>


<details>
  <summary>answer 7/10</summary>
  
  ```py
  def gcd(n1,n2):
      if n1<n2:
          small = n1
          if n2%small == 0:
              return small
          for each in range(small,0,-1):
              if n1%each == 0 and n2%each == 0:
                  return each
      elif n1>n2:
          small = n2
          if n1%small == 0:
              return small
          for each in range(small,0,-1):
              if n1%each == 0 and n2%each == 0:
                  return each
      else:
          return n1
  ```
  
</details>
