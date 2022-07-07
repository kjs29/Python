# 7/7 Today I learned...

# `map()`

Before start getting into map() function, let's first take a look at real use of `map()`

<em>example1</em>
```py
lst1 = [1,2,3,4]
answer = list(map(lambda x: x**2, lst1))
print(answer)
```
And we get
```
[1, 4, 9, 16]
```
Another easier way to express this is..

<em>example2</em>
```py
lst1 = [1,2,3,4]
def square(number):
    return number ** 2
answer = list(map(square, lst1))
print(answer)
```
As we noticed in these two <em>examples</em>,

1. lambda functions allow us to not define functions(when it is not necessary), 

2. and `map()` takes two arguments where the first argument is a function.

(Notice `map(square, lst1)` in <em>example2</em>)


In order to use map, we need to first understand what a higher order function is.

Higher order functions mean that it is a function that takes another function as arguments.

