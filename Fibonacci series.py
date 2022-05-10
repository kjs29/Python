
a,b = 0,1
while a < 10 : 
  print(a)
  a,b = b,a+b  
  
'''
First sequence
a = 0
b = 1
a<10 is true
prints a which is 0

The next two lines happens simultaneously
a becomes b which is 1
b becomes a+b which is 0 + 1 , not 1 + 1. a still has value of 0, we should add original value of a.


Second sequence
a = 1
b = 1
a<10 is true
prints a which is 1
a becomes b which is 1
b becomes a+b which is 1+1 = 2


Third sequence
a = 1
b = 2
a<10 is true
prints a which is 1
a becomes b which is 2
b becomes a+b which is 3

Forth sequence
a = 2
b = 3
a<10 is true
prints a which is 2
a becomes b which is 3
b becomes a+b which is 5

Fifth sequence
a = 3
b = 5
a<10 is true
prints a which is 3
a becomes b which is 5
b becomes a+b which is 8
.
.
.
8


result :
0
1
1
2
3
5
8
'''
#Difference between multiple assignments and regular assignments.
#Multiple assignments simultaneously assign values, but regular assignment is affected by chronological order

#let's take a look at the example using regular assignments.
a = 0
b = 1
while a<10:
  print(a)
  a = b
  b = a+b
'''
First sequence
a = 0
b = 1
a < 10 is true
prints a which is 0
a becomes b which is 1
b becomes a + b which is 1 + 1 = 2

Second sequence
a = 1
b = 2
a<10 is true
prints a which is 1
a becomes b which is 2
b becomes a + b which is 2 + 2 = 4

Third sequence
a = 2
b = 4
a < 10 is true
prints a which is 2
a becomes b which is 4
b becomes a + b which is 4 + 4 = 8

Forth sequence
a = 4
b = 8
a < 10 is true
prints a which is 4
a becomes b which is 8
b becomes a + b which is 8+8 = 16

Fifth sequence
a = 8
b = 16
a < 10 is true
prints a which is 8
a becomes b which is 16
b becomes a + b which is 16 + 16 = 32

Sixth sequence
a = 16
b = 32
a < 10 is NOT true
break out of while loop.
'''
