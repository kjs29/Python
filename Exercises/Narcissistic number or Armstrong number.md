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

154 != 1<sup>3</sup> + 5<sup>3</sup> + 4<sup>4</sup> = 190

Create a function that figures out if a number is an armstrong number or not

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
