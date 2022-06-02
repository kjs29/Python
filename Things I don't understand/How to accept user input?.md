I want to take user's favorite number as long as they want,

until user types 'q' to quit the program.

If they type q, the program should end, instead of having error message.

# this is what I came up with.

```
while True:
    
    fav_num = input("\nWhat is your favourite number?")
    
    try:
        if type(fav_num) == str:
        
            fav_num = int(fav_num)
    
    except ValueError:
        pass
    
    dic = {"n" : fav_num}
    
    print(f"\n{dic}")
```

edit 6/2
I realized that this has to do with error handling.

