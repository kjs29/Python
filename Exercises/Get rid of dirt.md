Tried on 6/12(o)
---

You have a list

```
house = ['dirt','furniture','tv','plant','cup','furniture','lamp','dirt','drapes','sofa','computer','dirt']
```

You want to remove all ```'dirt'``` in the ```house```

<details>
  <summary>answer</summary>
  
  ```py
  while "dirt" in house:
      house.remove("dirt")
  print(house)
  ```
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  while True:
      if "dirt" in house:
          house.remove("dirt")
      else:
          break
  print(house)
  ```
  
</details>
