Let's say there is a class
```py
class Car:
    def __init__(self, make, model, year, **comment):
        self.make = make
        self.model = model
        self.year = year
        self.comment = comment
        self.odometer = 0
    
    
    def start_engine(self):
        print(f"Manufacturer : {self.make}\nModel : {self.model}\nYear : {self.year}")
        print(self.comment)

car1 = Car("Tesla", "X", 2023, comment = "This has been used by world class pop star 'BTS'")

print(car1.__dict__)
```
My original question was `Is it possible to print comment that user defined in the instantiation?`

But then I realized that I can just write `print(self.comment)`

