We have a string

```
str1 = "/Jin /is /a /very /skillful /developer/communicator"
```

and we want to change it to 

```
str1 = "#Jin #is #a #very #skillful #developer#communicator"
```

<details>
  <summary>answer</summary>
  
  ```py
  import string
  
  str1 = "/Jin /is /a /very /skillful /developer/communicator"
  
  for each_symbol in string.punctuation:
      str1 = str1.replace(each_symbol, "#")
  print(str1)
  ```
  
</details>
