Let's say there is a dictionary
```
favourite_number = {
  "Do":1,
  "Re":[520,23],
  "Mi":[22],
  "Fa":"528"
  }
```

How can we print all keys and values like this?

```
Do's favourite number is 1
Re's favourite number is [520,23]
Mi's favourite number is [22]
Fa's favourite number is 528
```


<details>
  <summary>answer code</summary>
  
  ```
  
  for key,value in favourite_number.items():
    print(f"{key.title()}'s favourite number is : {value}")
  
  """
  Do's favourite number is : 1
  Re's favourite number is : [520, 23]
  Mi's favourite number is : [22]
  Fa's favourite number is : 528
  """
  ```
