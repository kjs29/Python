Tried on 5/28(o),6/18(x),6/30(o),7/10(o)

# Write a function called a_word_count
that takes a string as an input and returns a count of the words in the string that start with the uppercase or lowercase letter, a

# Below is an answer
---

<details>
  <summary>answer</summary>
  
  ```py
  #1st Answer
  #define the function
  def a_word_counter(sentence):

    #counter set to 0
    count = 0

    #every a_word in 'sentence' string
    for a_word in sentence:

      #if a_word.lower is equal to "a"
      if a_word.lower() == "a":

        count += 1

    return count

  print(a_word_counter("AbracabrA"))                  #4
  ```
</details>

<details>
  <summary>2nd Answer</summary>
  
  ```py
  #define the function
  def a_word_counter(sentence):

    count = 0
    for a_word in sentence:

      #if a_word is equal to "a"
      if a_word == "a":
        count += 1

      #if a_word is equal to "A"  
      elif a_word == "A":
        count += 1
    return count

  print(a_word_counter("AbracabrA"))              #4

  ```
</details>

<details>
  <summary>third answer</summary>
  
  ```py
  def a_count(yes):
      count = 0
      for a in yes:

         #we can use or to count either 'a' or 'A'
         if a == "a" or a == "A":
             count += 1
      return count




  print(a_count("SALDNladasmalkdlamdk"))               #5
  ```
</details>

<details>
  <summary>forth answer</summary>
  
  ```py
  def a_word_count(word):
      count = 0
      for a_word in word.lower():
          if a_word == "a":
              count += 1
      return count
  ```
</details>

<details>
  <summary>fifth answer I came up with on 7/10</summary>
  
  ```py
  def a_counter(string):
      string = string.replace("A","a")
      return string.count("a")

  print(a_counter("SALDNladasmalkdlamdk"))              #5
  ```
</details>

<details>
  <summary>sixth answer I came up with on 7/11</summary>
  
  ```py
  def a_counter(word):
    
      return word.count("a") + word.count("A")
  ```
</details>
