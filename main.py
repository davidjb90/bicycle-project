from bicycle import *
customer1 = Customer("David", 1000)
customer2 = Customer("Will", 500) #customers and his/her's given budget
customer3 = Customer("Wayne", 200)
cus_list = [customer1, customer2, customer3]

wheel_set1 = Wheel("Track Fixie", 5, 50)  # model name, wheel set (2 wheels) weight lbs, cost to produce
wheel_set2 = Wheel("Ultegra", 4, 100)
wheel_set3 = Wheel("Cosmic Elite", 2, 300)

frame1 = Frame("Steel", 15, 50)  # frame material, weight lbs., cost to produce
frame2 = Frame("Aluminum", 12, 100)
frame3 = Frame("Carbon", 10, 300)

bike1 = Bicycle("Trek", "Top Fuel", wheel_set1.weight + frame1.weight, wheel_set1.cost + frame1.cost)   ### {manufacturer, model_name, weight lbs, $ production cost}
bike2 = Bicycle("Trek", "Procaliber", wheel_set2.weight + frame2.weight, wheel_set2.cost + frame2.cost)   ### bikeweight = frameweight + wheelsetweight
bike3 = Bicycle("Trek", "Super Fly", wheel_set3.weight + frame3.weight, wheel_set3.cost + frame3.cost)  ### bikecost = framecost + wheelsetcost
bike4 = Bicycle("Specialized", "Stump Jumper", 12, 800)
bike5 = Bicycle("Specialized", "Allez", 10, 1000)
bike6 = Bicycle("Specialized", "Roubaix", 8, 1500)
bike_list = [bike1, bike2, bike3, bike4, bike5, bike6]

Maker1 = Manufacturer("Trek", 0.1, [bike1, bike2, bike3])
Maker2 = Manufacturer("Specialized", 0.1, [bike4, bike5, bike6])

shop_inventory1 = {
bike1.model: 5,   ### bike.i.d. = {model_name, stock count}
bike2.model: 5,
bike3.model: 5,
bike4.model: 3,
bike5.model: 2,
bike6.model: 1
} # stock count
shop_inventory2 = {
bike1.model: bike1.cost * Maker1.sell_margin,   ### bike.i.d. = {model_name, cost}
bike2.model: bike2.cost * Maker1.sell_margin,
bike3.model: bike3.cost * Maker1.sell_margin,
bike4.model: bike4.cost * Maker2.sell_margin,
bike5.model: bike5.cost * Maker2.sell_margin,
bike6.model: bike6.cost * Maker2.sell_margin
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
print(profit)