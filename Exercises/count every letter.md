Create a function that counts every letter and stores in a dictionary with {"word":"count"}

For example, 

```
count_every_letter("Hello")
```
will return
```
{'H':1,'e':1,'l':2,'o':1}
```

<details>
  <summary>answer</summary>
  
  ```py
  def every_word_count(word):
      empty_dic = {}

      for each_letter in word:
          if each_letter not in empty_dic:
              empty_dic[each_letter] = 1
          elif each_letter in empty_dic:
              empty_dic[each_letter] += 1
      return empty_dic
  ```
  
</details>
