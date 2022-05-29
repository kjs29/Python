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
  
  ```
  personal2 = {k + str(2):v for k,v in personal2.items()}
  personal3 = {k + str(3):v for k,v in personal3.items()}
  
  print(personal2)
  print(personal3)
  ```
  
</details>
