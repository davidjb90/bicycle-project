### basic testing script before adding wheel and frame classes
from bicycle import *
import random

customer1 = Customer("David", 1000)
customer2 = Customer("Will", 500) #customers and his/her's given budget
customer3 = Customer("Wayne", 200)
cus_list = [customer1, customer2, customer3]

bike1 = Bicycle("Stump Jumper", 20, 100)   ### {model_name, weight lbs, $ production cost}
bike2 = Bicycle("Rock Hopper", 16, 300)
bike3 = Bicycle("Hard Rock", 14, 700)
bike4 = Bicycle("Epic", 12, 1250)
bike5 = Bicycle("Allez", 10, 1500)
bike6 = Bicycle("Roubaix", 8, 2000)
bike_list = [bike1, bike2, bike3, bike4, bike5, bike6]

shop_inventory1 = {
"Stump Jumper": 5,   ### bike.i.d. = {model_name, stock count}
"Rock Hopper": 5,
"Hard Rock": 5,
"Epic": 3,
"Allez": 2,
"Roubaix": 1
} # stock count
shop_inventory2 = {
"Stump Jumper": 100,   ### bike.i.d. = {model_name, cost}
"Rock Hopper": 300,
"Hard Rock": 700,
"Epic": 1250,
"Allez": 1500,
"Roubaix": 2000
} # prices

'''for bike, stock in shop_inventory1.items():
    print("Model: {0}, Number in stock: {1}".format(bike, stock))'''  ### prints initial inventory for Dave's Bike Depot

Shop1 = Bike_Shop("Dave's Bike Depot", 0.20, shop_inventory1, shop_inventory2)   ###initializing the Bike Shop

profit = []    ### creating list of bikes that customers purchase, then able to calculate profit from this list 
for person in cus_list:   ### loops through our list of customers initialized above
    
    for bike in shop_inventory1.keys():
        if person.budget >= Shop1.get_price(bike) and shop_inventory1[bike] > 0:  ###Checks to see if customer has enough money for given bike and it's in stock
            person.bikes_afforded.append(bike)
    
    if person.bikes_afforded == []:  #handling for ValueError if customer can't afford any bikes
        print("Sorry {}, the shop is out of stock of bikes you can afford.".format(person.Name)) 
    else:    
        print("{0} can afford these bikes: {1}".format(person.Name, person.bikes_afforded))  ###prints list of bikes each customer can afford
        
        person.purchase_decision(person.bikes_afforded) ### initializing customer's 'random' logic in puchase_decision() function to choose a bike
                                                     
        profit.append(person.bike_purchased()) ###this line appends bike purchased by each customer to empty list 'profit' outside of loop, calculate profit from list 
        shop_inventory1[person.bike_purchased()] -= 1 # decrements the stock count for the model purchased at Dave's Bike Depot
        print("{} purchased the {} for {} dollars".format(person.Name, person.bike_purchased(), Shop1.get_price(person.bike_purchased()))) #print customer name, purchased bike, bike's price @ Shop1
        
        new_budget = person.budget - Shop1.get_price(person.bike_purchased())    #### updating customer's budget by subtracting price paid for the bike purchased
        print("{} now has {} dollars available".format(person.Name, new_budget))  #print updated budget (available funds) after purchase

print(shop_inventory1) ### Printing updated inventory list after customers make his/her purchases
print("The total profit from sales at Dave's Bike Depot is {} dollars".format(Shop1.shop_profit(profit)))
#print(profit)
