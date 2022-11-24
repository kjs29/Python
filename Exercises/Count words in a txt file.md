Tried on 7/10(x),11/24(x)
---

### Let's say we have a text file called `science of getting rich.txt`.

in a directory `C:/Users/daily/Desktop`

And we are curious how many words there are in the file.

Write code to print how many words there are in the book.

<details>
  <summary>answer</summary>
  
  ```py
  try:
      with open("C:/Users/daily/Desktop/science of getting rich.txt") as f:
          content = f.readlines()
  except FileNotFoundError:
      print("File Not Found")
  else:
      word_count = 0
      for a in content:
          word_count += len(a.split())
      print(word_count)
  ```
</details>
