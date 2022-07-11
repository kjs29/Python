# Tried on 7/11(o)

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


<details>
  <summary>answer 7/11</summary>
  
  ```py
  def count_every_letter(a):
      return {each:a.count(each) for each in a}
  ```
</details>
