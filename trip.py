def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city): 
    if 'Charlotte' == city:
        return 183
    elif 'NYC' == city:
        return 208
    elif 'Tampa Bay' == city:
        return 220
    elif 'LA' == city:
        return 475
    elif 'Washington DC' == city:
        return 18
    elif 'Atlanta' == city:
        return 257
    elif 'Pittsburgh' == city:
        return 222
    
def rental_car_cost(days):
    if days >=7:
        return 40*(days)-50
    elif days>=3:
        return 40*(days)-20
    else:
        return 40*(days)
    
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print('Cost of car rental: ', rental_car_cost(6))
print('Cost of plane ride: ', plane_ride_cost('LA'))
print('Cost of hotel room: ', hotel_cost(7))
print('Total cost of the trip: ', trip_cost('LA', 7, 500))
print('Total cost for Tampa Bay: ', (trip_cost('Tampa Bay', 6, 500)))
