Create a function that returns True if brackets are matched.

If strings are like `{[()]}`, `{}[()]` or `{()}`,

They are matched, which returns True

if strings are like `{(}` , `{]` or `{(}{)}`, the function returns False.

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
