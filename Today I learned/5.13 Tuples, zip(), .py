5/13 Today I learned..
1.
Tuples
2.
zip()

---Tuples
#Creating a Tuple
stocks = ("AAPL", 147, "Technology")

#unpacking a tuple
ticker, price, sector = stocks
print(stocks)             #('AAPL', 147, 'Technology')
print(ticker)             #AAPL
print(price)              #147
print(sector)             #Technology

#creating 1 element tuple
one_tuple = (4)       #but this will NOT create a tuple
print(one_tuple)      #4
one_tuple_real = (4,)
print(one_tuple_real) #(4,)

---zip()

#zip() is used to combine two lists together
tickersofstocks = ["AAPL","KO","GPRO"]
namesofstocks = ["APPLE","COCA-COLA","GOPRO"]
stockstotrade = zip(tickersofstocks,namesofstocks)              #<zip object at 0x00000283F0B9BE80>
#use list() to show list
stockstotrade = list(stockstotrade)                             #reassign the list of stockstotrade to stockstotrade
print(stockstotrade)                                            #[('AAPL', 'APPLE'), ('KO', 'COCA-COLA'), ('GPRO', 'GOPRO')] but this is in tuples
