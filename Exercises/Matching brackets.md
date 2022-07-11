
Tried on 7/11(o)
---

Create a function that returns True if brackets are matched.

If strings are like `{[()]}`, `{}[()]` or `{()}`,

They are matched, which returns True

if strings are like `{(}` , `{]` or `{(}{)}`, the function returns False.


<em>test example</em>
```
print(matchingbrackets("([{]})"))       #False
print(matchingbrackets("([]){]}"))      #False 
print(matchingbrackets("   {}{}}}{{"))  #False
print(matchingbrackets("{[] }"))        #True
```

<details>
  <summary>answer</summary>
  
  ```py
  def is_paired(s):
      dic = {"{":"}",
             "(":")",
             "[":"]"}

      stack = []

      for char in s:
          if char in dic.keys():
              stack.append(char)
          elif char in dic.values():
              if not stack:
                  return False
              else:
                  top = stack.pop()
                  if dic[top] != char:
                      return False

      return False if stack else True


  print(is_paired("([{]})"))
  print(is_paired("([]){]}"))
  print(is_paired("   {}{}}}{{"))
  print(is_paired("{[] }"))
  ```
</details>

<details>
  <summary>answer2</summary>
  
  ```py
  

  def is_paired(text):
      opening = ["(","{","["]
      closing = [")","}","]"]
      dic = dict(zip(opening,closing))
      stack = []

      """
      basically every text has either opening bracket and closing bracket
      we will make the dictionary that has a key of opening bracket , and a value for the corresponding closing bracket.
      dic = {"(":")","{":"}","[":"]"}

      RULE: in each letter in the text, if closing bracket comes first before opening bracket it is false
        False : }{, {)(}, ()]
        True : {([]())}, ()[{}]


      Following the RULE, 
      1. We will put each opening bracket into an empty list called stack.
      2. We will remove the last item in the stack, only if the item removed is corresponded to the closing bracket.

      every opening bracket can always be put into stack, 
      but if any closing bracket is in stack at the end of all iterations, 
      or even unmatched opening bracket, it returns false
      if stack is empty, it returns true.
      """

      #since we are testing the text we iterate through each letter in text
      for a in text:

          #if each letter is in the opening
          if a in opening:

              #copy it in stack
              stack.append(a)

          #if each letter is in the closing
          elif a in closing:

              #if stack is empty
              if not stack:

                  #that means it has closing bracket without opening bracket, so it is false
                  return False

              #if stack is not empty
              elif stack:

                  #we will assign a variable stack.pop() to popped_item
                  popped_item = stack.pop()

                  #check if current bracket we are iterating is matched with its pair in the dictionary
                  if dic[popped_item] != a:

                      #if it is not matched, then it is false
                      return False

          print(f"stack : {stack}")

      #if stack is empty, it returns true otherwise false
      return True if not stack else False

  print(is_paired("()["))
  ```
</details>

<details>
  <summary>answer 7.11</summary>
  
  ```py
  def matchingbrackets(b):
      opening = "({["
      closing = ")}]"
      dic = {"[": "]","(":")","{":"}"}
      #print(dic)
      stack = []
      for each in b:

          if each in opening:
              stack.append(each)

          elif each in closing:
              if len(stack) == 0:
                  print(f"False reason <closing bracket without opening bracket: {each}>")
                  return False
              else:

                  if (dic[stack[-1]] == each):

                      stack.pop()

                  else:
                      print(f"False reason : <different match : iteration of {each}'s matching part is {list(dic.keys())[list(dic.values()).index(each)]} which is different than {stack[-1]} >")
                      return False
          print(f"stack after iteration of {each} : {stack}")

      if len(stack) == 0:
          return True
      else:
          return False
  ```
</details>
