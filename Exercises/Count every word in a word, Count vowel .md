Tried on 7/10(o), 11/17(o), 4/8(o)
---

Create a function that takes one parameter that is string, and prints the 'vowel count' and returns dictionary of every word as key, and its count as value.
But space is not counted.

For example,

```py
every_word_count("hello from the other side")
```

would return

```
Vowel count : 8
{'h': 3,
 'e': 4,
 'l': 2,
 'o': 3,
 'f': 1,
 'r': 2,
 'm': 1,
 't': 2,
 's': 1,
 'i': 1,
 'd': 1}
```

<details>
  <summary>answer</summary>
 
  ```py
  def every_word_count(string:str) -> dict:
      dic = {}
      for each in string.replace(" ",""):
          if each not in dic.keys():
              dic[each] = 0
          dic[each] += 1
      vowel_count = 0
      for key,value in dic.items():
          if key in "aeiou":
              vowel_count += value
      print(f"Vowel count : {vowel_count}")
      return dic
   ```
 </details>


<details>
  <summary>answer I came up with on 7/10</summary>
 
  ```py
  def every_word_count(string:str):
     count = 0
     dic = {}
     for each in string.replace(" ",""):
         if each in "aeiou":
             count += 1
         dic.setdefault(each,string.count(each))

     print(f"Vowel count : {count}")
     return dic
  ```
</details>

<details>
 
  <summary>answer on 4/8</summary>
 
  ```py
  """
  We are given a sentence, where whitespaces don't count. -> remove whitespaces

  for the vowel count part
      1. create counter variable
      2. create vowels variable
      3. iterate through the string, 
          a. if each letter is in vowels, increment counter by 1
      4. print counter

  for the dictionary part
      1. create an empty dictionary
      2. iterate through the sentence
          set a dictionary where
          a. key is each letter in a sentence
          b. value is the number of occurrences in the sentence
  """

  def every_word_count(sentence):

      sentence = sentence.replace(" ", "")
      counter = 0
      vowels = "aeiou"

      for each_char in sentence:
          if each_char in vowels:
              counter += 1

      print(f"Vowel count : {counter}")

      dic = {}

      for each_letter in sentence:
          dic.setdefault(each_letter, sentence.count(each_letter))

      print(dic)
  ```
</details>
