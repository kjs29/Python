"""
Write a function naemd 'frequency_dictionary'
that takes a list of elements named words as a parameter.
The function should return a dictionary containing the frequency of each element in words.

For example,
["milk", "apple", "milk", "apple juice"]
should return
{"milk":2,"apple":1,"apple juice":1}

"""

#defining a function named 'frequency_dictionary' that has a 'words' parameter
def frequency_dictionary(words):
  
  #set a new dictinoary
  new_dic = {}
  
  #for every word in a list called words
  for word in words:
    
    #if that keyword doesn't exist in a new dictionary called new_dic
    if word not in new_dic:
      
      #set the value as zero
      new_dic[word] = 0
    
    #if it exists, assign value with the corresponding key in a 'words' list
    new_dic[word] += 1
  return new_dic
    
    
print(frequency_dictionary(["milk", "apple", "milk", "apple juice"]))                   #{'milk': 2, 'apple': 1, 'apple juice': 1}

