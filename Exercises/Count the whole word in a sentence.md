We want to find out how many times 'love' is mentioned in the given text.

s = "love love love, lovely lover love each other."


Expected output 
```
6
```


<details>
  <summary>answer</summary>
  
  ```py
  s = "love love love, lovely lover love each other."
  count = 0
  for i in range(len(s)):
      if s[i:i+4] == "love":
          count += 1
  print(count)
  ```
</details>
