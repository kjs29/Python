# Create a function
that multiply arbitrary number of numbers and return the answer.


For example,
```
multiply(1,2,3,4,5)
```
should return `120`

<details>
  <summary>code</summary>
  
  ```py
  def multiply(*num):
      answer = 1
      
      #num = (num1, num2, num3 ...) //it is a tuple
      for a in num:
          answer *= a
      return answer
  ```
  
</details>
