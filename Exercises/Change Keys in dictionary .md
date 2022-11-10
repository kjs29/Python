Tried on 6/12(x) 7/10(x) 11/10(x)
---

# Change Keys

We have dictionaries,
```
personal = {"name":"J","address": "somewhere over the rainbow",}
personal2 = {"name":"H","address": "heeee"}
personal3 = {"name":"R","address":"earth"}
```

We want to change the names of the ```personal2``` to ```name2```,```address2```
And for the ```personal3```, ```name3```, ```address3```

<details>
  <summary>answer</summary>
  
  ```py
  personal2 = {k + str(2):v for k,v in personal2.items()}
  personal3 = {k + str(3):v for k,v in personal3.items()}
  
  print(personal2)
  print(personal3)
  ```
  
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  personal2_new = {}
  for k,v in personal2.items():
      k = k + str(2)
      personal2_new[k] = v
  print(personal2_new)

  personal3_new = {}
  for k,v in personal3.items():
      k = k + str(3)
      personal3_new[k] = v
  print(personal3_new)
  ```
</details>


<details>
  <summary>answer 11/10</summary>
  
  ```py
  personal = {"name":"J","address": "somewhere over the rainbow",}
  personal2 = {"name":"H","address": "heeee"}
  personal3 = {"name":"R","address":"earth"}

  personal2 = {}
  for k,v in personal.items():
      if k == "name":
          personal2[k+str(2)] = "H"
      elif k == "address":
          personal2[k+str(2)] = "heeee"

  personal3 = {}
  for k,v in personal.items():
      if k == "name":
          personal3[k+str(3)] = "R"
      elif k == "address":
          personal3[k+str(3)] = "earth"

  print(personal2)
  print(personal3)
  ```
</details>
