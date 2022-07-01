We have a string `ab(c)De$H21@!:<>`

Create a function to print out what are characters, symbols, and digits in the string.


```
['a', 'b', 'c', 'D', 'e', 'H']
['2', '1']
['(', ')', '$', '@', '!', ':', '<', '>']
```

<details>
  <summary>answer</summary>
  
  ```py
  def organizer(string):
      chars_lst = []
      digits_lst = []
      symbols_lst = []
  
 
      for each_letter in string:
          if each_letter.isalpha():
              chars_lst.append(each_letter)
          elif each_letter.isdigit():
              digits_lst.append(each_letter)
          else:
              symbols_lst.append(each_letter)
      print(chars_lst)
      print(digits_lst)
      print(symbols_lst)
  ```
  
  
</details>
