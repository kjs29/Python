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

  find_gcd(123132, 12312)
  ```
</details>
