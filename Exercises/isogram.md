Isogram uses only one letter in a word

For example of isograms
- lumberjacks
- background
- downstream
- six-years-old

create a function if a word is isogram or not

<details>
  <summary>answer</summary>
  
  ```py
  

  def is_isogram(word):
      empty_dic = {}
      word = "".join(word.split()).lower().replace("-","")

      for each_letter in word:
          if each_letter not in empty_dic:
              empty_dic[each_letter] = 1
          elif each_letter in empty_dic:
              empty_dic[each_letter] += 1
      print(empty_dic)
      for key in empty_dic:
          if empty_dic[key] != 1:
              return False
      return True


  is_isogram("six-year-old")      #True
  
  ```
  
</details>
