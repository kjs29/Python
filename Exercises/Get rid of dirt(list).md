Tried on 6/12(o),7/10(o)
---

You have a list

```
house = ["dirt", "furniture", "tv", "dirt", "dirt", "plant", "lamp"]
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

