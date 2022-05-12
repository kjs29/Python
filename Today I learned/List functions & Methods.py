.append
.remove

.insert
.pop

#difference between .append and .insert
#.append is only for adding an element at the end of a list
#.insert is for adding an element at a specific index in a list


---examples of .append, .insert, .remove, .pop
#.append is used to add an element
grade = [100,80,60,40]
grade.append(50)
print(grade)                                      #[100, 80, 60, 40, 50]

#.append can also be used to 2Dlist
stocks = [["Apple",130],["KO",55],["KORU",50]]
stocks.append(["NFLX",350])
print(stocks)                                      #[['Apple', 130], ['KO', 55], ['KORU', 50], ['NFLX', 350]]

#.append is used to add an element
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]

#I want to add ["GPRO",80] after ["KO",55]
stocks[2].append(["GPRO",80])

#BUT! this adds ["GPRO",80] inside of ["KO",55]
print(stocks)                                     #[['Apple', 130], ['KO', 55, ['GPRO', 80]], ['KORU', 50], ['NFLX', 350]]

#reset the original list
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]

#if we want to add another list use .insert
stocks.insert(2, ["GPRO",80])               
print(stocks)                                   #[['Apple', 130], ['KO', 55], ['GPRO', 80], ['KORU', 50], ['NFLX', 350]]


#reset the original list
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]
#usage of .remove
#We want to remove ["KORU",50] from the list
stocks.remove(["KORU",50])
print(stocks)   

#if we want to remove 55 in ["KO",55]
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]
stocks[1].remove(55)
print(stocks)               #[['Apple', 130], ['KO'], ['KORU', 50], ['NFLX', 350]]

#usage of .pop
#.pop doesn't require any argument in parenthesis
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]
stocks.pop()
print(stocks)         #[['Apple', 130], ['KO', 55], ['KORU', 50]]

#.pop can be used like this
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]
stocks.pop(-2)
print(stocks)         #[['Apple', 130], ['KO', 55], ['NFLX', 350]]

#we can also track what was removed from using .pop
stocks = [["Apple",130],["KO",55],["KORU",50],["NFLX",350]]
removed = stocks.pop(0)
print(stocks)               #[['KO', 55], ['KORU', 50], ['NFLX', 350]]
print(removed)            #['Apple', 130]
