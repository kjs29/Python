Tried on 7/10(o), 11/16(x)
---

We have a string

```
str1 = "!Jin @is $a %very ^skillful &developer*communicator"
```

and we want to change it to 

```
str1 = "#Jin #is #a #very #skillful #developer#communicator"
```

<details>
  <summary>answer1</summary>
  
  ```py
  import string
  
  str1 = "/Jin /is /a /very /skillful /developer/communicator"
  
  for each_symbol in string.punctuation:
      str1 = str1.replace(each_symbol, "#")
  print(str1)
  ```
  
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  
  str1 = "!Jin @is $a %very ^skillful &developer*communicator"

  special_chrs = "!@#$%^&*()_+"

  for index in range(len(special_chrs)):
      str1 = str1.replace(special_chrs[index], "#")
  print(str1)
  ```
  
</details>

<details>
  <summary>answer 7.10</summary>
  
  ```py
  def convert(sentence):
      for a in sentence:
          if a in string.punctuation:
              sentence = sentence.replace(a,"#")
      return sentence
  ```
</details>
