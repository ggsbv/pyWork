#Hotel cost, n = number of nights, price = price per night
def hotel_cost(n, price):
    total = n * price
    
    return total

#Plane cost
def plane_cost(city):
    if city == "Durban":
        price = 800
    elif city == "Johannesburg":
        price = 1000
    elif city == "Port Elizabeth":
        price = 1100

    return price

#Car rental, d = n of days that the car is being rented for, price = price per day for car
def car_rental(d, price):
    total = d * price
    
    return total

#Holiday Cost
def holiday_cost(nights, hotelPricePerNight, city, days, carPricePerDay):
    hotel = hotel_cost(nights, hotelPricePerNight)
    plane = plane_cost(city)
    car = car_rental(days, carPricePerDay)
    
    return hotel + plane + car

#Test Functions
total = holiday_cost(4, 500, "Durban", 5, 250)
print "Total cost for holiday is: " + str(total)
