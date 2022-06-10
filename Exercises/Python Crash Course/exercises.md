# 4.1 Pizzas
Think of at least three kinds of your favorite pizza. Store these pizzas name in a list, and use a for loop to print the name of each pizza


#modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. 


#For each pizza you should have one line of output containing a simple sentence like "I like pepperoni pizza."

<details>
  <summary>code</summary>
  
  ```
  favorite_pizzas = ["Cheese pizza", "Sweet potato pizza", "Big pizza"]
  for a in favorite_pizzas:
      print(a)
      print("I like {}.".format(a))
  ```
</details>
<details>
  <summary>another code</summary>
  
  ```
  favorite_pizzas = ["Cheese pizza", "Sweet potato pizza", "Big pizza"]
  for pizza in favorite_pizzas:
      
      #f-string
      print(f"I love {pizza}")
  ```
</details>

add a line at the end of your program outside the for loop.

<details>
  <summary>code</summary>
 
  ```
  favorite_pizzas = ["Cheese pizza", "Sweet potato pizza", "Big pizza"]
  for a in favorite_pizzas:
      print(a)
      print("I like {}.".format(a))
  
  print("I love pizza!")
  ```
</details>

# 4.2 Animals

Think of at least three animals that have a common characteristics. Store the names in a list, use a for loop to print out each animal's name

```
lion
zebra
cheetah
```

<details>
  <summary>code</summary>
  
  ```
  animals = ["lion", "zebra", "cheetah"]
  for animal in animals:
    print(animal)
  ```
</details>

modify your program to print a statement about each animal, 

such as 
```
lion is strong
zebra has stripes
cheetah is fast
```

<details>
  <summary>code</summary>
  
  ```
  animals = ["lion", "zebra", "cheetah"]
  for animal in animals:
      print(animal)
  
  #this should not be inside the for loop
  print(f"{animals[0]} is strong")
  print(f"{animals[1]} has stripes")
  print(f"{animals[2]} is fast")
  ```

</details>

Add a line at the end of your program stating what these animals have in common.
```
lion
zebra
cheetah
lion is strong
zebra has stripes
cheetah is fast
These animals live in Africa
```
<details>
  <summary>code</summary>
  
  ```
  animals = ["lion", "zebra", "cheetah"]
  for animal in animals:
      print(animal)
  print(f"{animals[0]} is strong")
  print(f"{animals[1]} has stripes")
  print(f"{animals[2]} is fast")
  
  print("These animals are in Africa")
  ```
</details>

# 4.3 Counting to twenty

Use a for loop to print the numbers from 1 to 20, inclusive
```
1
2
3
4
5
...
17
18
19
20
```
<details>
  <summary>code</summary>
  
  ```
  for number in range(1,21):
    print(number)
  ```
</details>

# 4.4~4.5 One Million, summing a million

Make a list of 1~1,000,000 using for loop and find max and min values, and sum all the numbers in the list
```
[1,2,3,4,5...999998,999999,1000000] 1 1000000 500000500000
```
<details>
  <summary>code</summary>
  
  ```
  n = []
  for number in range(1,1000001):
    n.append(number)
  print(n,min(n),max(n),sum(n))
  ```
</details>  

# 4.6 Odd numbers

Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number
<details>
  <summary>code</summary>
  
  ```
  print(list(range(1,21,2)))
  ```
</details>

# 4.7 Threes

Make a list of multiple of 3 from 3 to 30. use a for loop to print the numbers in your list
<details>
  <summary>code</summary>
  
  ```
  threes = []
  for a in range(3,31):
   if (a % 3 == 0):
      threes.append(a)
  print(threes)
  ```
</details>

# 4.8 Cubes

Make a list of first 10 cubes and use a for loop to print out the value of each cube
```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
<details>
  <summary>code</summary>
  
  ```
  cubes = []
  for cube in range(1,11):
   cubes.append(cube**3)
  print(cubes)
  ```
</details>

# 4.9 Cube comprehensions

Use a list comprehension to print the first cubes in a list
<details>
  <summary>code</summary>
  
  ```
  cubes_list_comprehension = [cube**3 for cube in range(1,11)]
  print(cubes_list_comprehension)
  ```
</details>

# 4.10 Slices

#Use any list you created before

Print the message "The first three items in the list are:" then use a slice to print the first three items from that program's list
<details>
  <summary>code</summary>
  
  ```
  print("The first three items in the list are:")
  print(cubes_list_comprehension[:3])
  ```
</details>
Print the message "The three items from the middle of the list are:" then use a slice to print the three items from the middle of the list
<details>
  <summary>code</summary>
  
  ```
  print("The three items from the middle of the list are:")
  print(cubes_list_comprehension[2:5])
  ```
</details>
print the message "The last three items in the list are:" then use a slice to print the last three items in the list
<details>
  <summary>code</summary>
  
  ```
  print("The last three items in the list are:")
  print(cubes_list_comprehension[-3:])
  ```
</details>

# 4.11 My Pizzas, your pizzas

start with the program from exercise 4.1. Make a copy of the list of pizzas and call it friend_pizzas
<details>
  <summary>code</summary>
  
  ```
  print(favorite_pizzas)
  friend_pizzas = favorite_pizzas[:]
  ```
</details>

add a new pizza in the original list 
<details>
  <summary>code</summary>
  
  ```
  favorite_pizzas.append("Spinach pizza")
  ```
</details>

#add a different pizza to the list friend_pizzas
<details>
  <summary>code</summary>
  
  ```
  friend_pizzas.append("Pepperoni pizza")
  ```
</details>

#use a for loop to print out elements of the two lists. Make sure that they are different lists.
<details>
  <summary>code</summary>
  
  ```
  print("This is original pizza list : "+ str(favorite_pizzas))
  print("This is a new list : " + str(friend_pizzas))
  ```
</details>

# 4.12 More Loops

choose a list and write two for loops to print each list of foods.
<details>
  <summary>code</summary>
  
  ```
  for pizza in favorite_pizzas:
    print(pizza)
  for pizza in friend_pizzas:
    print(pizza)
  ```
</details>

# 4.13 Buffet

A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
<details>
  <summary>code</summary>
  
  ```
  fivefoods = ("Kimchi", "Soft tofu spicy soup", "Spagehtti", "Chicken", "Pizza")
  ```
</details>
use a for loop to print each food the restaurant offers
<details>
  <summary>code</summary>
  
  ```
  for food in fivefoods:
    print(food)
  ```
</details>

try to modify one of the items, and make sure that python rejects the change
<details>
  <summary>code</summary>
  
  ```
  fivefoods[0] = "Dumpling"
  ```
</details>
The restaurant changes its menu, replacing two of the items with different foods.
Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
<details>
  <summary>code</summary>
  
  ```
  fivefoods = ("Kimchi","Soft tofu spicy soup", "Hamburger", "Chicken", "Soda")
  for food in fivefoods:
    print(food)
  ```
</details>

# 6.1 Person

Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
You should have ekys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.
<details>
  <summary>code</summary>
  
  ```
  personal_info = {"first_name":"Robertson", "last_name":"Fox", "age": 70, "city":"Long Beach"}
  print(personal_info["first_name"])                            #Robertson
  print(personal_info["last_name"])                             #Fox
  print(personal_info["age"])                                   #70
  print(personal_info["city"])                                  #Long Beach
  ```
</details>

# 6.2 Favorite numbers

Use a dictionary to store people's favourite numbers. Think of five names, and use them as keys in your dictionary.

#Think of a favourite number for each person, and sotre each as a value in your dictionary.
#Print each person's name and their favourite number. For even more fun, poll a few friends and get some actual data for your program.
<details>
  <summary>code</summary>
  
  ```
  favourite_number = {"Remy":23, "Jin":29, "Ricky": 77, "Alyssa":7,}
  favourite_number["Raveena"] = 50
  print(favourite_number)                                         #{'Remy': 23, 'Jin': 29, 'Ricky': 77, 'Alyssa': 7, 'Raveena': 50}
  ```
</details>

# 6.3 Glossary

Think of five programming words you've learned about in the previous chapters.

#Use these words as the keys in your glossary, and store their meanings as values.
#Use the newline character(\n) to insert a blank line between each word-meaning pair in your output
<details>
  <summary>code</summary>
  
  ```
  five_programming_languages = {
    "dictionaries":"A collection of key-value pairs.",
    "To make a numerical lists, What function is the best? : ":"range()\n",
    "How to decide whether I should use pop() or del :":"If I want to use the removed item use pop(),\n if I don't want to use it anyway, use del.\n",
    "How to copy the whole list using indexing? : ":"[:]\n",
    "How to access value in a dictionary?(2 ways) : ":"1. dictionary_name[key]\n2. dictionary_name.get(key,\"No value exists\")",
    }
  ```
</details>

# 6.7 People

Start with the program you wrote in exercise 6.1. Make Two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.

Exercise 6.1 dictionary
-
```
personal_info = {"first_name":"Robertson", "last_name":"Fox", "age": 70, "city":"Long Beach"}
```
We want the result to look like this
-

```
First_Name : Robertson
Last_Name : Fox
Age : 70
City : Long Beach
First_Name : Jeffery
Last_Name : Bezos
Age : 55
City : Hollywood
First_Name : Stephen
Last_Name : Covey
Age : 98
City : New York
```

or

```
Robertson Fox 70 Long Beach
Jeffery Bezos 55 Hollywood
Stephen Covey 98 New York
```

<details>
  <summary>code</summary>
  
  ```
  personal_info = {"first_name":"Robertson", "last_name":"Fox", "age": 70, "city":"Long Beach"}
  personal_info2 = {"first_name":"Jeffery","last_name":"Bezos","age":55,"city":"Hollywood"}
  personal_info3 = {"first_name":"Stephen","last_name":"Covey","age":98,"city":"New York"}
  
  people = []
  people.append(personal_info)
  people.append(personal_info2)
  people.append(personal_info3)

  print(people)
  
  """
  [{'first_name': 'Robertson', 'last_name': 'Fox', 'age': 70, 'city': 'Long Beach'},
   {'first_name': 'Jeffery', 'last_name': 'Bezos', 'age': 55, 'city': 'Hollywood'}, 
   {'first_name': 'Stephen', 'last_name': 'Covey', 'age': 98, 'city': 'New York'}]
  """
  
  #Or this can be done like this
  people1 = [personal_info,personal_info2,personal_info3]

  #loop through the whole list's profile
  for eachinfo in people:
    
      #loop through each person's profile
      for key,value in eachinfo.items():
          print(f"{key.title()}:{value}")
  ```
</details>

<details>
  <summary>another code</summary>
  
  ```
  people = []
  people.append(personal_info)
  people.append(personal_info2)
  people.append(personal_info3)

  print(people)
  for a in people:
      name = a["first_name"] + a["last_name"]
      age = str(a["age"])
      city = a["city"]
    
      print(name,age,city)
  
  ```
</details>

# 6.8 Pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name.

Store these dictionaries in a list called pets. Next loop through your list and as you do, print everything you know about each pet.

You want the result to look like this.
```
Jin has a cat named Nabi
Ricky has a dog named Haru
Amber has a snake named Mochi
```
-

<details>
  <summary>code</summary>
  
  ```
  #This is similar to the 6.7 exercise

  #first make dictionaries
  pet1 = {"name":"nabi","kind":"cat","owner's name":"jin",}
  pet2 = {"name":"haru","kind":"dog","owner's name": "ricky",}
  pet3 = {"name":"mochi","kind":"snake","owner's name":"amber"}

  #create empty list
  pets = []

  #add each dictionary into pets list
  pets.append(pet1)
  pets.append(pet2)
  pets.append(pet3)

  print(pets)

  #Loop through the list
  for eachpet in pets:
      name = eachpet["name"]
      kind = eachpet["kind"]
      owner = eachpet["owner's name"]
      print(owner.title()+ " has a " + kind + " named " + name.title())
    
  ```
</details>

Another answer using the indexing,

<details>
  <summary>code</summary>
  
  ```
  for eachpet_dict in pets:
    
    owner = list(eachpet_dict.values())[2]
    kind = list(eachpet_dict.values())[1]
    name = list(eachpet_dict.values())[0]
    
    print(f"{owner.title()} has a {kind} named {name.title()}")
  ```
  
</details>

# 6.9 Favourite Places
Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.

To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person's name and their favorite places.
<details>
  <summary>code</summary>
  
  ```
  
  favorite_places = {}
  favorite_places["Jin"] = "California"
  favorite_places["Charlotte"] = "Finland"
  favorite_places["Han"] = "Vancouver"

  print(favorite_places)


  for each_key in favorite_places:
      print(each_key, favorite_places[each_key])
  ```
</details>

# 6.10 Favorite numbers
Modify your program from exercise 6.2 so each person can have more than one favorite number.

Then print each person's name along with their favorite numbers.

```

favourite_number = {'Remy': 23, 'Jin': 29, 'Ricky': 77, 'Alyssa': 7, 'Raveena': 50}
```

<details>
  <summary>code</summary>
  
  ```
  favourite_number["Remy"] = [23,520]
  favourite_number["Jin"] = [29,30]
  
  for key,value in favourite_number.items():
      print(f"{key.title()}'s favourite number is : {value}")
  """
  Remy's favourite number is : [23, 520]
  Jin's favourite number is : [29, 30]
  Ricky's favourite number is : 77
  Alyssa's favourite number is : 7
  Raveena's favourite number is : 50
  """
  ```
</details>

# 6.11 Cities
Make a dictionary called ```cities```. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.

The keys for each city's dictionary should be something like country, population, and fact. 

Print the name of each city and all of the information you have stored about it.

<details>
  <summary>code</summary>
  
  ```
  cities = {
    "Seoul" : {"country": "Korea",
               "population": 9700000,
               "fact":"The world's busiest air route is over Seoul"
               },
    "Mountain View" : {"country": "USA",
                       "population":81000,
                       "fact": "Google's HQ is in Mountain View"
                        },
    "New York" : {"country":"USA",
                  "population":8000000,
                  "fact":"The New York Public Library has over 50 million books 
                          and other items and is the second largest library system
                          in the nation after the Library of Congress. 
                          It is also the 3rd largest library in the world."}
    }       
  for cityname,details_of_each_city in cities.items():
      print(f"{cityname} : ")
      for eachkey in details_of_each_city:    
          print(f"\t{eachkey} : {details_of_each_city[eachkey]}")
  ```
</details>

# 6.12 Extensions
We're now working with examples that are complex enough that they can be extended in any number of ways.

Use one of the example programs from this chapter, and

extend it by adding new keys and values, changing the context of the program or improving the formatting fo the output.

<details>
  <summary>code</summary>
  
  ```
  people = [{'first_name': 'Robertson', 'last_name': 'Fox', 'age': 70, 'city': 'Long Beach'},
            {'first_name': 'Jeffery', 'last_name': 'Bezos', 'age': 55, 'city': 'Hollywood'},
            {'first_name': 'Stephen', 'last_name': 'Covey', 'age': 98, 'city': 'New York'},
            {'first_name': 'Jin', 'last_name': 'Kim', 'age': 29, 'city': 'Toronto'}]

  for eachdict in people:
    
      name = eachdict["first_name"] +" "+ eachdict["last_name"]
      age = eachdict["age"]
      city = eachdict["city"]
    
      print(f"Hey I am {name.title()}, and I am {str(age).title()} years old, and I live in a beautiful city called {city}")
  
  """
  Hey I am Robertson Fox, and I am 70 years old, and I live in a beautiful city called Long Beach
  Hey I am Jeffery Bezos, and I am 55 years old, and I live in a beautiful city called Hollywood
  Hey I am Stephen Covey, and I am 98 years old, and I live in a beautiful city called New York
  Hey I am Jin Kim, and I am 29 years old, and I live in a beautiful city called Toronto
  """
  
  
  ```
  
</details>

# 7.1 Rental car
Write a program that asks the user what kind of rental car they would like. 

Print a message about that car, such as "Let me see if I can find you a Subaru."

<details>
  <summary>code</summary>
  
  ```
  
  rental = input("Let me see if I can find you a Subaru : ")
  print(rental)
  ```
</details>

# 7.2 Restaurant Seating
Write a program that asks the user how many people are in their dinner group.

If the answer is more than 8, print a message saying they will have to wait for a table.

Otherwise, report that their table is ready.
<details>
  <summary>code</summary>
  
  ```
  restaurant = int(input("How many people are in your dinner group? : "))
  
  if restaurant > 8:
      print("Sorry, there might be a wait to find a table for you")
  else:
      print("The table is ready")
  ```
</details>

# 7.3 Multiples of Ten
Ask a user for a number, and then report whether the number is a multiple of ten or not.

<details>
  <summary>code</summary>
  
  ```
  multiples_ten = int(input("What number? : "))
  if multiples_ten % 10 == 0:
      print(True)
  else:
      print(False)
  ```
</details>

# 7.4 Pizza Toppings
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.

As they enter each topping, print a message saying you'll add that topping to their pizza.

<details>
  <summary>code</summary>
  
  ```
  prompt = "\nTell me what pizza topping you want : "
  message = ""

  while message.lower() != "quit":
      message = input(prompt)
      print(message)
  ```
  
</details>

# 7.5 Movie Tickets
A movie theater charges different ticket prices depending on a person's age.

If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;

and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

<details>
  <summary>code</summary>
  
  ```
  msg = "\nWelcome to the best movie theater!\n(Type \"pay\" to end the program)\nWhat is your age? : "

  price = 0

  numberoftoddler = 0
  numberofkids = 0
  numberofregular = 0

  while True:
    
      age = input(msg)
    
      if age.lower() != "pay":
          age = int(age)
        
          print(f"{'Toddlers ($0)': <15}{'Kids ($10)':^15}{'Regular ($15)':^15}{'|'}{'# of people':^15}{'Total $':>7}")

        
          if age < 3:
              price += 0
              numberoftoddler += 1
              numberofpeople = numberoftoddler + numberofkids + numberofregular
              print(f"{numberoftoddler:<15}{numberofkids:^15}{numberofregular:^15}{'|'}{numberofpeople:^15}{price:>7}")
        
          elif age >= 3 and age <= 12:
              price += 10
              numberofkids += 1
              numberofpeople = numberoftoddler + numberofkids + numberofregular
              print(f"{numberoftoddler:<15}{numberofkids:^15}{numberofregular:^15}{'|'}{numberofpeople:^15}{price:>7}")
        
          elif age > 12:
              price += 15
              numberofregular += 1
              numberofpeople = numberoftoddler + numberofkids + numberofregular
              print(f"{numberoftoddler:<15}{numberofkids:^15}{numberofregular:^15}{'|'}{numberofpeople:^15}{price:>7}")

      elif age.lower() == "pay":
          numberofpeople = numberoftoddler + numberofkids + numberofregular
          print(f"\n\nTotal : ${price}")
          print(f"Total # of people : {numberofpeople}")
          break
     
  ```
</details>


# 7.6 Three Exits
Write different versions of either Exercise 7.4 or Exercise 7.5 that do each of the following at least once:

```
prompt = "\nTell me what pizza topping you want : "
message = ""

while message.lower() != "quit":
    message = input(prompt)
    print(message)
```
  
- Use a conditional test in the while statement to stop the loop
- Use an active variable to control how long the loop runs
- Use a break statement to exit the loop when the user enters a 'quit' value

<details>
  <summary>Code for conditional test</summary>
  
  ```
  prompt = "\nTell me what pizza topping you want : "
  message = ""
  
  #use conditional test : while message is NOT "hawaiian", keep it going.
  while message != "hawaiian".lower():
      message = input(prompt)
      print(message)
      if "hawaiian" in message.lower():
          print("I don't think we can be friends anymore.")
  ```
</details>
  
<details>
  <summary>Code for active variable</summary>
  
  ```
  prompt = "\nTell me what pizza topping you want : "
  message = ""
  active = True

  while active:
      message = input(prompt)
    
      if message == "quit":
          active = False
      else:
          print(message)
  ```
</details>
  
<details>
  <summary>code for break statement</summary>
  
  ```
  prompt = "\nTell me what pizza topping you want"
  prompt += "\nType 'quit' to quit : "
  message = ""

  while message != "quit".lower():
      message = input(prompt)
    
      if message != "quit".lower():
          print(message)
          if "hawaiian" in message.lower():
              print("Seriously?")
  ```
</details>

  
# 7.8 Deli
Make a list called ```sandwich_orders``` and fill it with the names of various sandwiches.
  
Then make an empty list called ```finished_sandwiches```. Loop through the list of sandwich orders and print a message for each order,
  
such as ```I made your tuna sandwich``` As each sanwich is made, move it to the list of finished sandwiches.
  
After all the sandwiches have been made, print a message listing each sandwich that was made.
  
<details>
  <summary>code</summary>
  
  ```
  sandwich_orders = ["tuna","cheese","ham"]
  finished_sandwiches = []
  
  #as long as sandwich_orders is not empty
  while sandwich_orders:
      item = sandwich_orders.pop()
      print(f"I made your {item} sandwich")
      
      finished_sandwiches.append(item)

  for new_item in finished_sandwiches:
      print(new_item)
  ```
</details>

# 7.9 No Pastrami
  
Using the list ```sandwich_orders``` from exercise 7.8, make sure the sandwich ```'pastrami'``` appears in the list at least three times.
  
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then 
  
use a while loop to remove all occurrences of ```'pastrami'``` from ```sandwich_orders```.
  
Make sure no pastrami sandwiches end up in ```finished_sandwiches```.

```
sandwich_orders = ["tuna", "cheese", "ham"]
```
<details>
  <summary>code</summary>
  
  ```
  sandwich_order = ["tuna", "pastrami", "cheese", "pastrami", "ham", "pastrami"]
  finished_sandwiches = []
  print("Sorry, pastrami has run out.")

  while "pastrami" in sandwich_order:
      sandwich_order.remove("pastrami")

  while sandwich_order:
      each = sandwich_order.pop()
      finished_sandwiches.append(each)
    
  print(finished_sandwiches)

  ```
</details>
  
# 7.10 Dream vacation
  
Write a program that polls users about their dream vacation. Write a prompt similar to
  
```If you could visit one place in the world, where would you go?```

Include a block of code that prints the results of the poll.
  
<details>
  <summary>code</summary>
  
  ```
  vacation = {}

  random = True

  while random:
      response = input("If you could visit one place in the world, where would you go?")
      name = input("Enter your name")
    
      vacation[name] = response

      repeat = input("Would you like to continue? (y/n) : ")
      if repeat.lower() == "n":
          random = False
  print(f"\n{'Name': ^10} {'Dream Place': ^25}\n")
  for key,value in vacation.items():
      print(f"{key: ^10} {value: ^25}")
  ```
</details>

# 8.1 Message
Write a function called ```display_message()``` that prints oe sentence telling everyone what you are learning about in this chapter.
  
Call the function, and make sure the message displays correctly.
  
<details>
  <summary>code</summary>
  
  ```
  def display_message(msg):
      print(msg)
  
  display_message("I am learning programming to be the best programmer steadily and systematically")
  ```
  
</details>
  
# 8.2 Favorite Book
Write a function called ```favorite_book()``` that accepts one parameter, ```title```.
  
The function should print a message, such as ```One of my favorite books is Alice in Wonderland```.
  
Call the function, making sure to include a book title as an argument in the function call.
  
<details>
  <summary>code</summary>
  
  ```
  def favorite_book(title):
      print(f"This book, entitled {title}, has changed my life.")
  
  favorite_book("7 Habits of Highly Effective People")
  ```
  
</details>
  
# 8. 3 T-shirt
Write a function called ```make_shirt()``` that accepts a size and the text of a message that should be printed on the shirt.
  
The function should print a sentence summarizing the size of the shirt and the message printed on it.
  
Call the function once using posiitonal arguments to make a shirt. Call the function a second time using keyword arguments.
  
<details>
  <summary>code</summary>
  
  ```
  def make_shirt(size, message):
      print(f"\'{message}\'\nsize : {size}")
    
  #positional arguments
  make_shirt("large", "I love python")

  #keyword arguments 
  make_shirt(message = "I love python3", size = "big")
  ```
  
</details>
  
# 8. 4 Large Shirts
  
Modify the ```make_shirt()``` function so that shirts are large by default with a message that reads ```I love python```.
Make a large shirt with the default message, and a medium shirt with a default message, and a shirt of any size with a different message.

<details>
  <summary>code</summary>
  
  ```
  def make_shirt(size = "large", message = "I love python"):
      print(f"\'{message}\'\nsize = {size}")

  #call large shirt , default message
  make_shirt()
  #call medium shirt, default message
  make_shirt(size = "medium")
  #any size, any message
  make_shirt(size = "extra small", message = "Python will dominate!")
  ```
  
</details>
  
# 8.5 Cities
  
Write a function called ```describe_city()``` that accepts the name of a city and its country.
  
The function should print a simple sentence, such as  ```Reykjavik is in Iceland```.
  
Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
  
<details>
  <summary>code</summary>
  
  ```
  def describe_city(city, country = "korea"):
      print(f"{city} is in {country}")

  describe_city("Seoul")
  describe_city("Anyang")
  describe_city(country = "Australia", city = "Sidney")
  ```
</details>
  
# 8.6 City Names
Write a function called ```city_country()``` that takes in the name of a city and its country. The function should return a string formatted like this:
  
```
"Santiago, Chile"  
```
Call your function with at least three city-country pairs, and print the values that are returned.
<details>
  <summary>code</summary>
  
  ```
  def city_country(cityname,country):
      a = f"{cityname}, {country}"
      return a.title()

  print(city_country("anyang","korea"))
  print(city_country("Washington","USA"))
  print(city_country("rome","italy"))
  ```
</details>

# 8. 7 Album
  
<details>
  <summary>code</summary>
  
  ```
  def make_album(song, album, number = None):
      dic = {"song": song ,"album": album}
      if number:
          dic["# of songs"] = number
      return dic

  print(make_album("IDOL","Love yourself", 25))
  print(make_album("Someone like you", "21", 11))
  print(make_album("Some Nights", "Some Nights", 10))
  ```
</details>
  
# 8.8 User Albums
  
<details>
  <summary>code</summary>
  
  ```
  def make_album(song, album, number = None):
      dic = {"song": song ,"album": album}
      if number:
          dic["# of songs"] = number
      return dic
  while True:

      print("Tell me your favorite song, and the album that has the song, and hopefully the number of the songs.")
      print("If you want to quit any time, type \'q\'")

      songs = input("\nWhat is your favourite song?")

      if songs.lower() == 'q':
          break

      albums = input("\nWhat is the name of the album that has the song?")

      if albums.lower() == 'q':
          break

      numbers = int(input("\nHow many songs are in the album? : "))

      if numbers == 'q':
          break

      elif type(numbers) == str:
          print("Enter a number\n")


      final = make_album(songs, albums, numbers)
      print(final)
  ```
</details>
  
# 8 .9 Messages
  
<details>
  <summary>code</summary>
  
  ```
  def show_messages(lst):
      for each in lst:
          print(each)
  
  hello = ["Hello!", "Did you eat yet?", "Good morning", "Good luck"]
  show_messages(hello)
  ```
</details>

# 8. 10 Sending Messages
<details>
  <summary>code</summary>
  
  ```
  hello = ["Hello!", "Did you eat yet?", "Good morning", "Good luck"]
  sent_messages = []
  def send_messages(lst1,lst2):
      while lst1:
          msg = lst1.pop(0)
          lst2.append(msg)
  
  send_messages(hello,sent_messages)
  print(hello)
  print(f"\n{sent_messages}")
  ```
  
</details>
  
# 8. 11 Archived Messages
<details>
  <summary>code</summary>
  
  ```
  hello = ["Hello!", "Did you eat yet?", "Good morning", "Good luck"]
  sent_messages = []
  def send_messages(lst1,lst2):
      while lst1:
          msg = lst1.pop(0)
          lst2.append(msg)
  
  #copy of the original list 'hello'
  send_messages(hello[:],sent_messages)
  print(hello)
  print(f"\n{sent_messages}")
  
  
  ```
  
</details>

# 8.12 Sandwiches
<details>
  <summary>code</summary>
  
  ```
  def prepare_sandwich(*a):
      print("What Kind Of Sandwich")
      for each in a:
          print(f"- {each}")

  prepare_sandwich("pizza", "homemade", 15)
  prepare_sandwich("ham","sobeys",10)
  prepare_sandwich("vegetables","walmart",18)

  ```

</details>
  
# 8.13 User Profile

<details>
  <summary>code</summary>
  
  ```
  def build_profile(first,last,**random):
      random["first name"] = first
      random["last name"] = last
      return random
  
  build_profile("Jin","Kim",age = 29, passion = 100, Sincerity = True)
  ```
</details>
  
# 8.14 Cars

<details>
  <summary>code</summary>
  
  ```
  def make_car(a,b,**c):
      c["Manufacturer"] = a.title()
      c["Model"] = b.title()
      return c
  
  car = make_car("subaru", "outback", color="blue", tow_package=True)
  ```
</details>

# 9.1 Restaurant
<details>
  <summary>code</summary>
  
  ```
  class Restaurant:
      def __init__(self, restaurant_name, cuisine_type):
          self.restaurant_name = restaurant_name
          self.cuisine_type = cuisine_type

      def describe_restaurant(self):
          print(f"Name : {self.restaurant_name}\nCuisine Type : {self.cuisine_type}")

      def open_restaurant(self):
          print(f"{self.restaurant_name} is open")

  restaurant = Restaurant("THE KING & QUEEN", "Asian")

  #Calling both attributes
  print(restaurant.restaurant_name)
  print(restaurant.cuisine_type)

  #Calling both methods
  restaurant.describe_restaurant()
  restaurant.open_restaurant()
  ```
</details>

# 9.2 Three Restaurants
<details>
  <summary>code</summary>
  
  ```
  #Calling three different instances
  restaurant2 = Restaurant("Gangnam Style", "Korean")
  restaurant3 = Restaurant("Fish & Chips", "British")
  restaurant4 = Restaurant("Catching the wave", "Japanese")

  #Calling describe_restaurant() method for each instance
  restaurant2.describe_restaurant()
  restaurant3.describe_restaurant()
  restaurant4.describe_restaurant()
  ```
</details>
  
# 9.3 Users

<details>
  <summary>code</summary>
  
  ```
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info


      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")
        
  person1 = User("Haru", "Jackson", MBTI = "ESTP", age = 35)
  person2 = User("Josh", "Groban", Hobbies = ["Break Dancing", "Painting"])
  
  #print all attributes
  attrs1 = vars(person1)
  attrs2 = vars(person2)
  
  #print attrs
  print(attrs1)
  print(attrs2)

  #print each item in attrs
  print(", ".join("%s : %s" % item for item in attrs1.items()))
  print(", ".join("%s : %s" % item for item in attrs2.items()))

  person1.describe_user()
  person1.greet_user()

  person2.describe_user()
  person2.greet_user()

  ```
</details>
  
# 9.4 Number Served
<details>
  <summary>code</summary>
  
  ```
  class Restaurant:
      def __init__(self, restaurant_name, cuisine_type):
          self.restaurant_name = restaurant_name
          self.cuisine_type = cuisine_type
          self.number_served = 0

      def describe_restaurant(self):
          print(f"Name : {self.restaurant_name}\nCuisine Type : {self.cuisine_type}")

      def open_restaurant(self):
          print(f"{self.restaurant_name} is open")

      def set_number_served(self, customers):
          self.number_served = customers

      def increment_number_served(self, customers):
          self.number_served += customers




  restaurant = Restaurant("THE KING & QUEEN", "Asian")

  #print the number_served
  print(restaurant.number_served)

  #changing value of number_served directly
  restaurant.number_served = 15

  #print it again
  print(restaurant.number_served)

  #calling method set_number_served
  restaurant.set_number_served(20)
  print(restaurant.number_served)

  #calling method increment_number_served
  restaurant.increment_number_served(22)
  print(restaurant.number_served)

  ```
</details>
  
# 9. 5 Login Attempts
<details>
  <summary>code</summary>
  
  ```
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info
          self.login_attempts = 0

      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")

      def increment_login(self):
          self.login_attempts += 1

      def reset_login_attempts(self):
          self.login_attempts = 0

  # Make instance        
  user1 = User("K","J")

  # Calling increment_login()
  user1.increment_login()

  user1.increment_login()

  user1.increment_login()

  # Check
  print(user1.login_attempts)

  #calling reset_login_attempts
  user1.reset_login_attempts()

  #check
  print(user1.login_attempts)

  ```
</details>

  
# 9.6 Ice Cream Stand

<details>
  <summary>code</summary>
  
  ```
  class Restaurant:
      def __init__(self, restaurant_name, cuisine_type):
          self.restaurant_name = restaurant_name
          self.cuisine_type = cuisine_type
          self.number_served = 0

      def describe_restaurant(self):
          print(f"Name : {self.restaurant_name}\nCuisine Type : {self.cuisine_type}")

      def open_restaurant(self):
          print(f"{self.restaurant_name} is open")

      def set_number_served(self, customers):
          self.number_served = customers

      def increment_number_served(self, customers):
          self.number_served += customers


  #subclass
  class IceCreamStand(Restaurant):

      def __init__(self, restaurant_name, cuisine_type):
          super().__init__(restaurant_name, cuisine_type)

          self.flavors = []

      def display_flavors(self):
          print("we have amazing flavors : \n")
          for a in self.flavors:
              print(f"- {a}")



  icecream1 = IceCreamStand("Sunday", "Icecream")
  icecream1.flavors = ["chocolate","vanila","cookie and cream","coffee"]
  icecream1.display_flavors()
  ```
  
</details>

# 9.7 Admin
  
<details>
  <summary>code</summary>
  
  ```py
  
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info
          self.login_attempts = 0

      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")

      def increment_login(self):
          self.login_attempts += 1

      def reset_login_attempts(self):
          self.login_attempts = 0

  class Admin(User):
      def __init__(self, first_name, last_name, **random_info):
          super().__init__(first_name, last_name, **random_info)
          self.privileges = []

      #creating a method for displaying privileges
      def show_privileges(self):
          print("Admins have these privileges : \n")
          print(self.privileges)
          for a in self.privileges:   
              print(f"- {a}")

  user1 = Admin("JG","K")

  #define user1.privileges directly
  user1.privileges = ["Can promote new memebers", "Can view log history of other people"]

  user1.show_privileges()
  ```
</details>
  
  
# 9. 8 Privileges
  
<details>
  <summary>code</summary>
  
  ```
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info
          self.login_attempts = 0

      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")

      def increment_login(self):
          self.login_attempts += 1

      def reset_login_attempts(self):
          self.login_attempts = 0

  class Privileges:

      def __init__(self, privileges = []):
          self.privileges = privileges

      def show_privileges(self):
          print("Admins have these privileges : \n")

          for a in self.privileges:   
              print(f"- {a}")



  class Admin(User):
      def __init__(self, first_name, last_name, **random_info):
          super().__init__(first_name, last_name, **random_info)
          self.privileges = Privileges()


  user1 = Admin("Jin","Kim", hobby = "hiking")
  user1.privileges.show_privileges()


  a= ["resetting passwords", "can moderate discussion"]
  user1.privileges.privileges = a
  user1.privileges.show_privileges()
  ```
</details>
  
# 9.9 Battery Upgrade
  
<details>
  <summary>code</summary>
  
  ```
  class Car:
      def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year
          self.odometer = 0

      def get_descriptive(self):
          long_name = f"{self.make} {self.model} {self.year}"
          return long_name.title()

      def read_odometer(self):
          print(f"This car has {self.odometer} miles on it.")

      def update_odometer(self, mileage):
          if mileage >= self.odometer:
              self.odometer = mileage
          else:
              print("You can't roll back an odometer!")

      def increment_odometer(self, miles):
          self.odometer += miles


  class Battery:
      def __init__(self, battery_size = 75):
          self.battery_size = battery_size

      def describe_battery(self):
          print(f"This car has a {self.battery_size} -kWh battery")

      def get_range(self):
          if self.battery_size == 75:
              range = 260
          elif self.battery_size == 100:
              range = 315
          print(f"This car can go about {range} miles on a full charge.")

      def upgrade_battery(self):
          if self.battery_size < 100:
              self.battery_size = 100


  class ElectricCar(Car):
      def __init__(self, make, model, year):
          super().__init__(make, model, year)
          self.battery = Battery()


  #create an instance ofelectric car with a default battery size
  electric1 = ElectricCar("TSLA", "Y", 2022)

  electric1.battery.get_range()

  electric1.battery.upgrade_battery()
  electric1.battery.get_range()
  ```
</details>
  
  
# 9.10 Imported Restaurant
<details>
  <summary>code</summary>
  
  
  
  <em>restaurant.py</em>
  
  ```py
  class Restaurant:
      def __init__(self, name, cuisine, since):
          self.name = name
          self.cuisine = cuisine
          self.since = since

      def introduce(self):
          print(f"Hello! We are {self.name}, we have {self.cuisine} food, and we have been open since {self.since}")




  rest1 = Restaurant("THE BEST", "asian", 2002)


  rest1.introduce()
  ```
  
  
  <em>new_file.py</em>
  
  ```py
  
  from restaurant import Restaurant   #import restaurant.py module

  #create an instance and call one of the restaurant's methods
  rest1 = Restaurant("The GReat", "Thai", 2008)
  rest1.introduce()
  ```
</details>
  
# 9.11 Imported Admin
<details>
  <summary>code</summary>
  
  <em>user.py</em>
  
  ```py
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info
          self.login_attempts = 0

      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")

      def increment_login(self):
          self.login_attempts += 1

      def reset_login_attempts(self):
          self.login_attempts = 0

  class Privileges:

      def __init__(self, privileges = []):
          self.privileges = privileges

      def show_privileges(self):
          print("Admins have these privileges : \n")

          for a in self.privileges:   
              print(f"- {a}")



  class Admin(User):
      def __init__(self, first_name, last_name, **random_info):
          super().__init__(first_name, last_name, **random_info)
          self.privileges = Privileges()


  user1 = Admin("Jin","Kim", hobby = "hiking")
  user1.privileges.show_privileges()


  a= ["resetting passwords", "can moderate discussion"]
  user1.privileges.privileges = a
  user1.privileges.show_privileges()
  ```
  
  <em>new_file.py</em>
  ```py
  from user import Admin

  #make an Admin instance
  user1= Admin("DoRe","Mi",hobby= "reading")

  #setting privileges
  user1.privileges.privileges = ["banning users", "viewing log history"]

  #check if it works well
  user1.privileges.show_privileges()
  ```
</details>
  
# 9.12 Multiple Modules
<details>
  <summary>code</summary>
  
  <em>userclass.py</em>
  ```py
  class User:
      def __init__(self, first_name, last_name, **random_info):
          self.first_name = first_name
          self.last_name = last_name
          self.random_info = random_info
          self.login_attempts = 0

      def describe_user(self):
          print(f"Name : {self.first_name} {self.last_name}")
          for key,value in self.random_info.items():
              print(f"{key} : {value}")
      def greet_user(self):
          print(f"Welcome, {self.first_name} {self.last_name}!")

      def increment_login(self):
          self.login_attempts += 1

      def reset_login_attempts(self):
          self.login_attempts = 0
  ```
  
  <em>userclass2.py</em>
  ```py
  from userclass import User      #since there is Admin class which is a subclass of User class from another module, we must import User module from userclass.py


  class Privileges:

      def __init__(self, privileges = []):
          self.privileges = privileges

      def show_privileges(self):
          print("Admins have these privileges : \n")

          for a in self.privileges:   
              print(f"- {a}")


  class Admin(User):
      def __init__(self, first_name, last_name, **random_info):
          super().__init__(first_name, last_name, **random_info)
          self.privileges = Privileges()
  ```
  
  <em>new_file.py</em>
  ```py
  from userclass import User
  from userclass2 import Admin, Privileges

  person = Admin("JB","Park", hobby = "singing")

  person.privileges.privileges = ["viewing social media account", "banning users"]

  person.privileges.show_privileges()
  ```

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
  for a in range(4):
      b = choice(lst_num)
      print(b)
      lottery.append(b)
  print(lottery)
  ```
</details>
