"""
What is the difference between Class variables and Instance Variables?

"""

class Person:
  def __init__(self, name):
    self.name = name      #when should I use self.name instead of Person.name?
