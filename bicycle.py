##This is the final 'model the bicycle industry' project in unit 1
### Create the Bicycle Class
class Bicycle:
    
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def money_compare(self):
        self.money = 0
        self.money += self.cost * 1.2
        return self.money
    
    def modelname(self):
        self.thing = ""
        self.thing += self.model
        return self.thing
      
class Bike_Shop:
    
    def __init__(self, name, margin, inventory={}, bikecost={}):
        self.name = name
        self.margin = margin + 1
        self.inventory = inventory
        self.bikecost = bikecost
        
    def get_price(self):
        for bike, price in self.bikecost.items():
            self.bikecost[bike] = price * self.margin
        return self.bikecost

   
class Customer:

    def __init__(self, Name, budget):
        self.Name = Name
        self.budget = budget
    
    def customermoney(self):
        self.funds = 0
        self.funds += self.budget
        return self.funds
    
    def customername(self):
        self.name = ""
        self.name += self.Name
        return self.name

    def get_profit(self, bikepr):
        return bikepr
        
    def shop_pr(self):
        return self









