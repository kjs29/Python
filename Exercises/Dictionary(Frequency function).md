Tried 5/28(x), 6/12(o),7/10(o),11/10(o),02/15(o)
---

# Write a function named 'frequency_dictionary'
that takes a list of elements named words as a parameter.
The function should return a dictionary containing the frequency of each element in words.

---


For example, if we see this list,
```
["milk", "apple", "milk", "apple juice"]
```
should return
```
{"milk":2,"apple":1,"apple juice":1}
```

# Below is answer

<details>
  <summary>answer</summary>
  
  ```py
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
  ```
</details>

<details>
  <summary>answer 7.10</summary>
  
  ```py
  def frequency_dictionary(lst):
      return {a:lst.count(a) for a in lst}
  ```
</details>

<details>
  <summary>answer 8.25</summary>
  
  ```py
  def frequency_dictionary(words):
      dic = {}
      for each in words:
          dic.setdefault(each, words.count(each))
      return dic
  ```
</details>
