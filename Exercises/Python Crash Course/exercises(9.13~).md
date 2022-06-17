# 9. 13 Dice
<details>
  <summary>code</summary>
  
  ```py
  from random import randint


  class Die:


      #define how many sides a Die can have, and also define an empty list called result to contain results
      def __init__(self, sides = 6):
          self.sides = sides
          self.result = []
      def roll_die(self):
          print(randint(1,self.sides))


      #parameter 'num' represents how many times we roll the die
      def show_results(self,num = 10):

          for a in range(1,num+1):
              self.result.append(randint(1,self.sides))
          print(self.result)


      #analyze how many times certain number hits
      def analyze(self):
          dic = {}
          for key in self.result:
              if key not in dic:
                  dic[key] = 0
              dic[key] += 1
          print(dic)


  #create a die which, by default, has 6 sides
  a = Die()

  #roll die once and print
  a.roll_die()

  #roll die 'a' 10 times(by default) and print the results
  a.show_results()

  #create a die with 10 sides
  b = Die(10)

  #create a die with 20 sides
  c = Die(20)

  #roll die 'b' 20 times
  b.show_results(20)

  #roll die 'c' 20 times
  c.show_results(20)

  #analyze what number hits how many times
  a.analyze()



  d = Die(25)
  d.show_results(25)
  d.analyze()
  ```
  
</details>

# 9. 14 Lottery
  
<details>
  <summary>code</summary>
  
  ```py
  from random import choice, randint
  lst_num = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
  lottery = []
  while len(lottery) < 4:
      b = choice(lst_num)
      if b not in lottery:
          lottery.append(b)
  print(lottery)
  ```
</details>

# 10.1 Learning python
<details>
  <summary>code</summary>
  
  <em>python_so_far_6.12txt</em>
  ```
  Python is amazing!
  I love you python!
  ```
  
  ```py
  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/python_so_far_6.12.txt") as file:
      first = file.read()
  print(first)

  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/python_so_far_6.12.txt") as file:
      for a in file:
          print(a.strip())

  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/python_so_far_6.12.txt") as file:
      third = file.readlines()
  for a in third:
      print(a.strip())
  ```
</details>
  
# 10.2 Learning C
<details>
  <summary>code</summary>
  
  ```py
  with open(filename) as h:
      a = h.readlines()
  for bb in a:
      print(bb.strip().replace("python","c")
  
  ```
</details>
# 10.3 guest
<details>
  <summary>code</summary>
  
  ```py
  name = input("What is your name? \n")

  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/guest.txt", "w") as a:
      a.write(name)

  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/guest.txt", "r") as a:
      guest = a.read()
  print(guest.strip())
  ```
</details>
  
# 10.4 Guest Book
<details>
  <summary>code</summary>
  
  ```py
  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/guest_book.txt", "a") as file:
    while True:
        name = input("What is your name?\n")
        name += "\n"
        file.write(name)
        print(f"hello, {name}\n")
  ```
  
</details>
  
# 10.5 Programming Poll
<details>
  <summary>code</summary>
  
  ```py
  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/reason to program.txt","a") as file:
      reason = input("Why do you like programming?\n")
      file.write(f"reason : {reason}\n")


  with open("C:/Users/daily/Desktop/Coding/Python/git_practice/reason to program.txt") as file:
      reason_to_program = file.read()
      print(reason_to_program.strip())
  ```
</details>

# 10.6 Addition
<details>
  <summary>code</summary>
  
  ```py
  try:    
      a = input("Enter the first number : ")
      a = int(a)
      b = input("Enter the second number : ")
      b = int(b)

  except ValueError:
      if type(a) != int:
          print("The first input was not a number, try again!")
      elif type(b) != int:
          print("The second input was not a number, try again!")
  else:
      print(f"the sum of {a} and {b} : {a+b}")
  ```
</details>

# 10.7 Addition Calculator
<details>
  <summary>code</summary>
  
  ```py
  while True:
      try:    
          a = input("Enter the first number : ")
          a = int(a)
          b = input("Enter the second number : ")
          b = int(b)


      except ValueError:
          if type(a) != int:
              print("The first input was not a number, try again!")
          elif type(b) != int:
              print("The second input was not a number, try again!")
      else:
          print(f"the sum of {a} and {b} : {a+b}")
          break
  ```
</details>
  
# 10.8 Cats and Dogs

<details>
  <summary>code1</summary>
  
  ```py
  try:
      with open("cats.txt") as f:
          cats = f.read()
  except FileNotFoundError:
      print("the cats file has not been found")
  else:
      print(cats)

  try:
      with open("dogs.txt") as f:
          dogs = f.read()
  except FileNotFoundError:
      print("the dogs file has not been found")
  else:
      print(dogs)
  ```
</details>
  
<details>
  <summary>code2</summary>
  
  ```py
  filename = ["cats.txt","dogs.txt"]
  for each in filename:
      print(f"opening file {each}")
      try:
          with open(each) as f:
              content = f.read()
      except FileNotFoundError:
          print("{each} hasn't been found")
      else:
          print(content)
  ```
  </details>

# 10.10 Common words
<details>
  <summary>code</summary>
  
  ```py
  try:
      with open("C:/Users/daily/Desktop/science of getting rich.txt") as f:
          content = f.read()
  except FileNotFoundError:
      print("File Not Found")
  else:
      print(content.lower().count("the "))
  ```
</details>
# 10.11 Favorite number
<details>
  <summary>code</summary>
  
  ```py
  
  import json
  
  #write the file
  a = int(input("\nWhat is your favourite number? : "))
  filename = "favorite_number.json"
  with open(filename,"w") as f:
      json.dump(a,f)

  #read the file
  with open(filename) as f:
      file = json.load(f)
      print(f"I know your favorite number! It is {file}")
  ```
</details>

# 10.12 Favorite Number Remembered
  
<details>
  <summary>code</summary>
  
  ```py
  
  import json


  filename = "favorite_nussmberr.json"

  try:
      with open(filename) as f:
          file = json.load(f)
  except FileNotFoundError:
      a = int(input("\nWhat is your favourite number? : "))
      with open(filename,"w") as f:
          json.dump(a,f)
      print(a)
  else:
      print(file)
  ```
</details>
  
