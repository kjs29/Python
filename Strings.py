# Strings can't be modified in python

word = 'python'
word[0] = 'J'       #this will cause an error that says "'str' object does not  support item assignment"
---
#to get the length of a string we can use len()
word = 'python'
print(len(word))
