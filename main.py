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

"""for bike, stock in shop_inventory1.items():
    print("Model: {0}, Number in stock: {1}".format(bike, stock))"""  ### prints initial inventory for Dave's Bike Depot

Shop1 = Bike_Shop("Dave's Bike Depot", 0.20, shop_inventory1, shop_inventory2)   ###initializing the Bike Shop

#print(Shop1.get_price()) ### prints out updated dictionary with the 'Dave's Bike Depot' prices for each bike

profit = []    
for person in cus_list:   ### loops through our list of customers created above

    bikes_afforded = []  ### list of bikes each customer can afford
    
    if person.customermoney() >= bike1.money_compare() and shop_inventory1["Stump Jumper"] > 0:  ###Checks to see if customer has enough money for given bike and if the given bike is in stock
        bikes_afforded.append(bike1.modelname())
    
    if person.customermoney() >= bike2.money_compare() and shop_inventory1["Rock Hopper"] > 0:
        bikes_afforded.append(bike2.modelname())
        
    if person.customermoney() >= bike3.money_compare() and shop_inventory1["Hard Rock"] > 0:
        bikes_afforded.append(bike3.modelname())
        
    if person.customermoney() >= bike4.money_compare() and shop_inventory1["Epic"] > 0:
        bikes_afforded.append(bike4.modelname())
        
    if person.customermoney() >= bike5.money_compare() and shop_inventory1["Allez"] > 0:
        bikes_afforded.append(bike5.modelname())
        
    if person.customermoney() >= bike6.money_compare() and shop_inventory1["Roubaix"] > 0:
        bikes_afforded.append(bike6.modelname())
        
    
    if bikes_afforded == []:  #handling for ValueError if customer can't afford any bikes
        print("Sorry {}, the shop is out of stock of bikes you can afford.".format(person.customername())) 
    else:    
        print("{0} can afford these bikes: {1}".format(person.customername(), bikes_afforded))  ###list of bikes each customer can afford
        bike_purchased = ""  ### empty string that we add the single random bike we pick in the next line
        bike_purchased += random.choice(bikes_afforded) #picks a random bike among a list of bikes each customer can afford
        
        profit.append(bike_purchased)
        
        shop_inventory1[bike_purchased] -= 1 # decrements the stock count for the model purchased at Dave's Bike Depot
        
        bp = shop_inventory2[bike_purchased]*1.2
        print("{} purchased the {} for {} dollars".format(person.customername(), bike_purchased, bp)) #print customer name, purchase, purchase price

        new_budget = person.customermoney() - bp
        print("{} now has {} dollars available".format(person.customername(), new_budget))  #print updated budget (available funds) after purchase
    

        
print(shop_inventory1) ### Printing updated inventory list after customers make his/her purchases

x = 0
for i in profit:
    x += (int(shop_inventory2[i])*1.2) - int(shop_inventory2[i])

print("The total profit from sales at Dave's Bike Depot is {} dollars".format(x))
    
    
    