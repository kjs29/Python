# 4.1 
Think of at least three kinds of your favorite pizza. Store these pizzas name in a list, and use a for loop to print the name of each pizza
#modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. 
#For each pizza you should have one line of output containing a simple sentence like "I like pepperoni pizza."
<details>
  <summary>example</summary>
  ```
  favorite_pizzas = ["Cheese pizza", "Sweet potato pizza", "Big pizza"]
  for a in favorite_pizzas:
      print(a)
      print("I like {}.".format(a))
  ```
</details>
add a line at the end of your program outside the for loop.
```
print("I love pizza!")
```
# 4.2
Think of at least three animals that have a common characteristics. Store the names in a list, use a for loop to print out each animal's name
```
animals = ["lion", "zebra", "cheetah"]
for animal in animals:
  print(animal)
  
#modify your program to print a statement about each animal, such as a dog would make a great pet.
  print(f"{animal} is strong")

#add a line at the end of your program stating what these animals have in common.
print("These animals are in Africa")
      
```      
# 4.3
Use a for loop to print the numbers from 1 to 20, inclusive
```
for number in range(1,21):
  print(number)
```
# 4.4~4.5 
Make a list of 1~1,000,000 using for loop and find max and min values, and sum all the numbers in the list
```
n = []
for number in range(1,1000001):
  n.append(number)
print(n,min(n),max(n),sum(n))
```
# 4.6 
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number
```
print(list(range(1,21,2)))
```
# 4.7 
Make a list of multiple of 3 from 3 to 30. use a for loop to print the numbers in your list
```
threes = []
for a in range(3,31):
  if (a % 3 == 0):
    threes.append(a)
print(threes)
```
# 4.8 
Make a list of first 10 cubes and use a for loop to print out the value of each cube
```
cubes = []
for cube in range(1,11):
  cubes.append(cube**3)
print(cubes)
```
# 4.9 
Use a list comprehension to print the first cubes in a list
```
cubes_list_comprehension = [cube**3 for cube in range(1,11)]
print(cubes_list_comprehension)
```
# 4.10 
#Use any list you created before

Print the message "The first three items in the list are:" then use a slice to print the first three items from that program's list
```
print("The first three items in the list are:")
print(cubes_list_comprehension[:3])
```
Print the message "The three items from the middle of the list are:" then use a slice to print the three items from the middle of the list
```
print("The three items from the middle of the list are:")
print(cubes_list_comprehension[2:5])
```
#print the message "The last three items in the list are:" then use a slice to print the last three items in the list
print("The last three items in the list are:")
print(cubes_list_comprehension[-3:])

# 4.11
start with the program from exercise 4.1. Make a copy of the list of pizzas and call it friend_pizzas
```
print(favorite_pizzas)
friend_pizzas = favorite_pizzas[:]

#add a new pizza in the original list 
favorite_pizzas.append("Spinach pizza")

#add a different pizza to the list friend_pizzas
friend_pizzas.append("Pepperoni pizza")

#use a for loop to print out elements of the two lists. Make sure that they are different lists.
print("This is original pizza list : "+ str(favorite_pizzas))
print("This is a new list : " + str(friend_pizzas))
```
# 4.12
choose a list and write two for loops to print each list of foods.
```
for pizza in favorite_pizzas:
  print(pizza)
for pizza in friend_pizzas:
  print(pizza)
```
# 4.13
A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
```
fivefoods = ("Kimchi", "Soft tofu spicy soup", "Spagehtti", "Chicken", "Pizza")

#use a for loop to print each food the restaurant offers
for food in fivefoods:
  print(food)

#try to modify one of the items, and make sure that python rejects the change
fivefoods[0] = "Dumpling"

#The restaurant changes its menu, replacing two of the items with different foods.
#Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
fivefoods = ("Kimchi","Soft tofu spicy soup", "Hamburger", "Chicken", "Soda")
for food in fivefoods:
  print(food)
```  
# 6.1
Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
You should have ekys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.
```
personal_info = {"first_name":"Robertson", "last_name":"Fox", "age": 70, "city":"Long Beach"}
print(personal_info["first_name"])                            #Robertson
print(personal_info["last_name"])                             #Fox
print(personal_info["age"])                                   #70
print(personal_info["city"])                                  #Long Beach
```
# 6.2 
Use a dictionary to store people's favourite numbers. Think of five names, and use them as keys in your dictionary.

#Think of a favourite number for each person, and sotre each as a value in your dictionary.
#Print each person's name and their favourite number. For even more fun, poll a few friends and get some actual data for your program.
```
favourite_number = {"Remy":23, "Jin":29, "Ricky": 77, "Alyssa":7,}
favourite_number["Raveena"] = 50
print(favourite_number)                                         #{'Remy': 23, 'Jin': 29, 'Ricky': 77, 'Alyssa': 7, 'Raveena': 50}
```

# 6.3 
Think of five programming words you've learned about in the previous chapters.

#Use these words as the keys in your glossary, and store their meanings as values.
#Use the newline character(\n) to insert a blank line between each word-meaning pair in your output
```
five_programming_languages = {
    "dictionaries":"A collection of key-value pairs.",
    "To make a numerical lists, What function is the best? : ":"range()\n",
    "How to decide whether I should use pop() or del :":"If I want to use the removed item use pop(),\n if I don't want to use it anyway, use del.\n",
    "How to copy the whole list using indexing? : ":"[:]\n",
    "How to access value in a dictionary?(2 ways) : ":"1. dictionary_name[key]\n2. dictionary_name.get(key,\"No value exists\")",
    }
```
