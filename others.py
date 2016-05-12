

Shop = Bike_Shop("Dave's", 0.2, bike_cost)
Shop.price("Epic")

#Shop.inventory = {'bike_model':[object, # in stock]}


#my_budget = 500

#get bike shop inventory and iterate over its keys
for bike, stock in shop_inventory.items():
    if stock > 0:
        #from cost get the price
        price = Shop.price(300) #cost * 1.2
        #check if within budget, print out result
        if price < my_budget:
            print('Can afford ' + bike)
    else:
        continue

