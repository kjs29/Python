"""
Write a function called a_word_count that takes a string as an input
and returns a count of the words in the string that start with the uppercase or lowercase letter, a

"""

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
---

#2nd Answer

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
