# Narcissistic Number or Armstrong number

Narcissitic number or Armstrong numbers is a number that is the sum of each digits raised to its number of digits 

For example


9 is a armstrong number

9 = 9<sup>1</sup> = 9

10 is not an armstrong number

10 != 1<sup>2</sup> + 0<sup>2</sup> = 1

153 is an armstrong number

153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153

154 is not an armstrong number

154 != 1<sup>3</sup> + 5<sup>3</sup> + 4<sup>3</sup> = 190

```
1. Create a function that figures out if a number is an armstrong number or not

2. And ask user to enter some random number and this will print a list of some armstrong numbers up to that user input
```
<details>
  <summary>answer</summary>
  
  ```py
  def armstrong(n):
      digits = len(str(n))
      total = 0
      for a in str(n):
          total += int(a) ** digits
      print(f"original number : {n}\ntotal sum : {total}")
      return total == n 

  lst_of_armstrong_numbers = []
  random_int = int(input("\nEnter number and up to that number, we will find you some armstrong numbers : "))
  for each_number in range(1, random_int + 1):
      if armstrong(each_number):
          lst_of_armstrong_numbers.append(each_number)
  print(lst_of_armstrong_numbers)
  ```
</details>

<details>
  <summary>answer on 7/10</summary>
  
  ```py
  def is_armstrong(num):

      num1 = str(num)
      how_many_digit = len(num1)
      sum = 0
      for a in num1:
          sum += int(a) ** how_many_digit
      return sum == num

  def how_many_armstrong(num):
      num = int(input())
      return [n for n in range(1,num+1) if is_armstrong(n)]

  ```
</details>
