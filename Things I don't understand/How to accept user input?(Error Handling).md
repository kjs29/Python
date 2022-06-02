I want to take user's favorite number as long as they want,

until user types 'q' to quit the program.

If they type q, the program should end, instead of having error message.

# this is what I came up with originally

```
while True:
    
    fav_num = input("\nWhat is your favourite number?")
    
    if fav_num == "q":
        break
    fav_num = int(fav_num)
    
    dic = {"n" : fav_num}
    
    print(f"\n{dic}")
```

```
What is your favourite number?345345

{'n': 345345}

What is your favourite number?1

{'n': 1}

What is your favourite number?-1

{'n': -1}

What is your favourite number?r
```

But this appears error that says ```ValueError: invalid literal for int() with base 10: 'e'```


# edit 6/2

I realized that this has to do with error handling.
```
while True:
    
    fav_num = input("\nWhat is your favourite number?")
    
    try:
        if fav_num == "q":
            break
        fav_num = int(fav_num)
    except ValueError:
        pass

    
    dic = {"n" : fav_num}
    
    print(f"\n{dic}")
```

This made me realize that I need to study more about 'error handling'
