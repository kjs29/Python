Tried on 5/28(o)

Let's say you are given a dictionary like this.

```
statistics_traders = {"futures":0.4, "options":0.2, "stocks":8}
```

And you want to individually print out like this:
```
Futures traders success rate in the long term is 0.4 percent.
Options traders success rate in the long term is 0.2 percent.
Stocks traders success rate in the long term is 8 percent.
We must be aware of trading, and we must trade only with statistical data.
```

# Below is answer
```
statistics_traders = {"futures":0.4, "options":0.2, "stocks":8}
print(statistics_traders)


for a,b in statistics_traders.items():
    print("{} traders success rate in the long term is {} percent.".format(a.capitalize(), b))
print("We must be aware of trading, and we must trade only with statistical data.")


print(statistics_traders)
"""
Futures traders success rate in the long term is 0.4 percent.
Options traders success rate in the long term is 0.2 percent.
Stocks traders success rate in the long term is 8 percent.
We must be aware of trading, and we must trade only with statistical data.
"""
```  

# Here is another answer I came up with 5/28
```
def important_function(dic):
    for key,value in dic.items():
        print(f"{key.title()} traders success rate in the long term is {value} percent")
    print("We must be aware of trading, and we must trade only with statistical data.")
```
