I want to take user inputs stored in the dictionary

where user types 'q' to quit the program.


# this is what I came up with.

```
while True:
    print("Tell me your favorite number : ")
    
    fav_num = int(input("\n"))
    
    if type(fav_num) != int:
        break
      
```

But this appears error that says 
```ValueError: invalid literal for int() with base 10: 'q'```
