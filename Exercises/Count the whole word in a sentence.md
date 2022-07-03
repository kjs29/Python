We want to find out how many times 'love' is mentioned in the given text.

s = "love love love, lovely lover love each other."


Expected output 
```
6
```
Create a function that takes two arguments, sentence, and a word.

Return the number of times a word is used in the sentence.

<details>
  <summary>answer</summary>
  
  ```py
  s = "love love love, lovely lover love each other."
  
  def pleasefind(sentence, word):
      count = 0
      for i in range(len(sentence)):
        if sentence[i:i+len(sentence)] == word:
          count += 1
      return count
  
  print(pleasefind(s,"love"))
  ```
</details>
