# 7/1 Today I learned...

# Strings

### Two ways to iterate through a string

Strings are just like lists, except that they are immutable,

Strings can be accessed with index
```py
str1 = "hello"
print(str1[0])      #
print(str1[:-1])    #hell
```
<em>First way to iterate string</em>
```py
str1 = "hello"
for each_letter in str1:
    print(each_letter)
```
<em>result</em>
```
h
e
l
l
o
```

<em>Second way to iterate string</em>
```py
str2 = "world"
for index in range(len(str2)):
    print(str2[index])
```

<em>result</em>
```
w
o
r
l
d
```
