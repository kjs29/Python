# Tried on 7.11(o), 11/30(o)

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

<details>
  <summary>answer 7.11</summary>
  
  ```py
  import string

  def organizer(str1):
      alphabet = [a for a in str1 if a.isalpha()]
      print(alphabet)
      digit = [a for a in str1 if a.isdigit()]
      print(digit)
      symbols = [a for a in str1 if a in string.punctuation]
      print(symbols)
  ```
  
</details>
