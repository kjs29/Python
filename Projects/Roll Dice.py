from random import randint

class Die:
    
    #this constructor defines the number of sides a die will have, default value is 6
    def __init__(self, sides = 6):
        self.sides = sides
        self.result = []
        self.dic = {}
    
    #this die will roll just once and show the result
    def roll_die(self):
        print(randint(1,self.sides))
        
    #this method shows the results in a list, this takes parameter that tells the program how many times it will roll
    def show_results(self, num=10):
        for _ in range(1, num+1):
            self.result.append(randint(1, self.sides))
        print(self.result)
    
    #show results in the dictionary with frequencies
    def analyze(self):
        for key in self.result:
            if key not in self.dic:
                self.dic[key] = 0
            else:
                self.dic[key] += 1
        print(self.dic)
        
    #calculate the probability of hitting the 'number' out of total cases
    def calculate(self, number):
        total_case = sum(self.dic.values())
        for key, value in self.dic.items():
            if number == key:
                percentage = value / total_case * 100
                print(f"\nProbability of hitting '{number}' with {self.sides} sided dice out of {total_case} cases : {percentage:.2f} %")
    
    #calculate the probability of hitting the 'number's out of total cases
    def calculate_multiple(self, *number):
        total_case = sum(self.dic.values())
        case = 0
        for each in number:
            for key, value in self.dic.items():
                if each == key:
                    case += value
        print(f"\n{number}'s # of cases : {case}")
        percentage = case / total_case * 100
        print(f"\nProbability of hitting {number} with {self.sides} sided dice out of {total_case} cases : {percentage:.2f} %")
        
        
        
d = Die(20)
d.roll_die()
d.show_results(10000)
d.analyze()
d.calculate(5)
d.calculate_multiple(1,2,3)
