# Palindrome

Palindrome is a word that is the same as the reversed ordered word

For example,

`Never Odd or even`
`kayak`

are palindrome words.

Create a function that takes a string as a parameter, and returns True if that argument is palindrome, or False if it is not Palindrome.

Do not care about the whitespaces, or Capital/small letters.

<details>
  <summary>answer</summary>

  ```py
  def is_palindrome(input_string):
    return input_string.lower().replace(" ","") == input_string.lower().replace(" ","")[::-1]
  ```
</details>