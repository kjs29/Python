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
