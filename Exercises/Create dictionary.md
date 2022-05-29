# Create a dictionary
Get a random number from a user

If that random number is 5

generate a dictionary that looks like 

```{1:1,2:4,3:9,4:16,5:25}```

If the number is 30

```{1:1,2:4,3:9,4:16 ... 29:841,30:900}```

# Below is an answer
<details>
  <summary>answer 1 </summary>
  
  ```
  n = int(input("Enter a number : "))
  sqr = {a:a**2 for a in range(1,n+1)}
  print(sqr)
  ```
</details>

<details>
  <summary>answer 2 </summary>
  
  ```
  n = int(input("Enter a number : "))
  sqr = {}
  for a in range(1,n+1):
      sqr[a] = a**2
  print(sqr)
  ```
</details>

<details>
  <summary>answer 3 </summary>
  
  ```
  n = int(input("Enter a number : "))
  sqr = {}
  for a in range(1,n+1):
      sqr.update({a:a**2})
  print(sqr)
  ```
</details>
