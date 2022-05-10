#Strings are immutable , but Lists are mutable

squares = [1,4,8,16,25,36]
squares[2] = 9
print(squares)
print(squares[:2])

---
#usage of append
squares = [1,4,8,16,25,36]
squares.append(49)
print(squares)
