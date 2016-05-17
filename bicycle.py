##This is the final 'model the bicycle industry' project in unit 1
### Create the Bicycle Class
import random
class Bicycle:
    
    def __init__(self, manufacturer, model, weight, cost):
        self.manufacturer = manufacturer
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Bike_Shop:
    
    def __init__(self, name, margin, inventory={}, bikecost={}):
        self.name = name
        self.margin = margin + 1
        self.inventory = inventory
        self.bikecost = bikecost
        for bike, price in self.bikecost.items():  #### moved logic into the bike shop; where pricing of bike occurs
            self.bikecost[bike] = price * self.margin  #### updates the bikecost dictionary (shop_inventory2 in main.py) within Bike_Shop object
                                                        #### easier than updating it manually each time we want the price of a given bike
    def get_price(self, bike):
        return self.bikecost[bike]
        
    def shop_profit(self, profit):
        x = 0
        for i in profit:
            x += self.bikecost[i] - (self.bikecost[i] / self.margin)
        return x    
    
class Customer:
    
    def __init__(self, Name, budget):
        self.Name = Name
        self.budget = budget
        self.bikes_afforded = []
    
    def purchase_decision(self, bikes_afforded):
        self.purchase = "" ### empty string to which we add the single random bike we pick in the next line
        self.purchase += random.choice(self.bikes_afforded) #picks a random bike among a list of bikes each customer can afford
        return self.purchase
        
    def bike_purchased(self):
        return self.purchase

class Wheel:
    
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class Frame:
    
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

class Manufacturer:
    
    def __init__(self, name, sell_margin, models=[]):
        self.name = name
        self.models = models
        self.sell_margin = sell_margin + 1
        
            
        
    #def wholesale_price(self, bike):
        
            