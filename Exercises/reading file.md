#### Suppose we have a file named `pi_million.txt` in the directory `C:/Users/daily/Desktop/Coding/Python/git_practice`
Inside the file the file, there are million decimals of pi
```
3.1415926535897932384
626433832795028841971
693993751058209749445
923078164062862089986
280348253421170679...
```

Read the `pi_million.txt` and print it with <strong>50</strong> decimal places.
<details>
  <summary>answer</summary>
  
  ```py
  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/pi_million.txt") as m:
      million_pi = m.readlines()
  str_million = ""
  for line in million_pi:
      str_million += line.strip()
  print(f"{str_million[:52]}")
  ```
</details>
