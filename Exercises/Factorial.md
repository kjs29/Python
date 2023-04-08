4/8(o)


Create a function that takes one integer as an argument and returns the factorial of that integer

```py
print(factorial(5))   
```

```
120
```

<details>
  <summary>answer</summary>
  
  ```py
  def factorial(n):
      if n == 1:
          return 1
      else:
          n = n * factorial(n-1)
      return n
  ```
</details>
