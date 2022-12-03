"""
What is the difference between Class variables and Instance Variables?

"""

class Employee:
  def __init__(self, name):
    self.name = name      #when should I use self.name instead of Employee.name?

    
    
    
I guess class variables apply to all instances
and instance variables only apply to that specific instance

When to use Class Variables vs When to use Instance Variables

If we want to create some attributes that can apply individual instance, that is changeable -> we use self.raise_amount
If we want to use the variables that apply to all instances in a class, -> we use Employee.number_of_emps

