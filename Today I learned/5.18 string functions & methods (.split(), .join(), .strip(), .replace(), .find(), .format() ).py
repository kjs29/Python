5/18 Today I learned...
1. String functions



.split()
#to split strings
#split is for turns one string into a list with elements

#string -> list(elements)

stockinfo = "NFLX went down about 7 percent on May 18th."

#if we want to turn this string into one a list with elements in it
stockinfo.split()
print(stockinfo)        #this doesn't return the value so we must store into a variable

stockinfo_list = stockinfo.split()
print(stockinfo_list)         #['NFLX', 'went', 'down', 'about', '7', 'percent', 'on', 'May', '18th.']



.join()
#to turn elements into one string together

# list(elements) -> string

ex)
stocks = ["AAPL","used to be 102 Dollars", " before split"]
#if we want to put these elements together into one string,
" ".join(stocks)          #but this does not return value, so we must store it in a variable
a = " ".join(stocks)
print(a)                  #AAPL used to be 102 Dollars  before split




.strip()
#to remove certain strings

#string -> string






.repalce()






.find()





.format()
#if we want to use variables in strings we can use .format()






---example of .split()
line_one = "The sky has given over"

#split the string with whitespace
line_one_split = line_one.split()

print(line_one_split)                       #['The', 'sky', 'has', 'given', 'over']

#split the string with "e"
line_one_split2 = line_one.split("e")

print(line_one_split2)                      #['Th', ' sky has giv', 'n ov', 'r']


#another exame of .split()
#let's say we want to get only ticker names


stocks = "APPL 140, NFLX 190, GPRO 8, KORU 14"
ticker_price = stocks.split(",")
print(ticker_price)                               #['APPL 140', ' NFLX 190', ' GPRO 8', ' KORU 14']

#now let's make list that contains only ticker

#first we have to make an empty list which will contain ticker
ticker = []

for a in ticker_price:
    ticker.append(a.split()[-2])             
print(ticker)                                    #['APPL', 'NFLX', 'GPRO', 'KORU']

---example of .join()

#.join() makes the list with elements into one string

love_yourself = ["For all the times that you rained on my parade.", 
                 "And all the clubs you get in using my name.", 
                 "You think you broke my heart, oh girl, for goodness sake.",
                 "You think I'm crying on my own, well I ain't"]

love_yourself_together = " ".join(love_yourself)
print(love_yourself_together)
#For all the times that you rained on my parade. And all the clubs you get in using my name. You think you broke my heart, oh girl, for goodness sake. You think I'm crying on my own, well I ain't

#we can join the each element together with different lines
love_yourself_lines = "\n".join(love_yourself)

print(love_yourself_lines)
"""
For all the times that you rained on my parade.
And all the clubs you get in using my name.
You think you broke my heart, oh girl, for goodness sake.
You think I'm crying on my own, well I ain't
"""



.replace()
#if we want to replace some string with another string

#string -> string

stockpoem = "When I watched Apple stock back in 2016, it used to be so cheap, now Apple has more than 5 times now."

#I want to replace Apple with SPY
stockpoem_replaced = stockpoem.replace("Apple", "SPY")
print(stockpoem_replaced)



.find()
#when we want to find some string in another string

find_a = "I am going to have a job as a software engineer."

print(find_a.find("a"))                   #2




