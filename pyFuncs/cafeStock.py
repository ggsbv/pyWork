#Function to calculate stock on hand. Takes stock amount and price as hash maps and returns total
#stock on hand.
def stockOnHand(stock, price):
    total = 0
    for item in stock:
        total += stock[item] * price[item]
    return total

menu    = ["Burger with Mushroom Sauce", "Pulled Pork Burger", "Vegetarian Burger", "Dagwood Burger"]

stock   = {
    'Burger with Mushroom Sauce'    : 4,
    'Pulled Pork Burger'            : 11,
    'Vegetarian Burger'             : 15,
    'Dagwood Burger'                : 3,
    }

price   = {
    'Burger with Mushroom Sauce'    : 85,
    'Pulled Pork Burger'            : 80,
    'Vegetarian Burger'             : 75,
    'Dagwood Burger'                : 90,
    }

print "Total stock on hand is R" + str(stockOnHand(stock, price))
