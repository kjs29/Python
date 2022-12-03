"""
1.As I learned more about list comprehensions
I got curious as to 
why the order of 'if' in list comprehensions 
And 
why the order of 'else if' in list comprehensions are different

2.How do I print all element in example1?
My ideal outcome would be like [1,2,3,123,0]

"""

#example of using if in list comprehensions

example = [1,2,3,123,0]
#add 5 to each element if elements are positive numbers
listcom1 = [a + 5 for a in example if a > 0]
print(listcom1)

#example of using else if in list comprehensions - if else comes in the middle of the list comprehensions

#if element is less than 15 then multiply it by 2, or subtract element by 3
listcom2 = [b * 2 if b < 15 else b -3 for b in example]
print(listcom2)


# WHEN SOMEONE MADE THIS, WHY DID THEY MAKE LIKE THIS INSTEAD 'IF' CAN GO IN THE MIDDLE OF THE LIST COMPREHENSIONS AS WELL?
