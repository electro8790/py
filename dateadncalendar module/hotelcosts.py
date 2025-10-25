def hotel_cost(nights):
    return 140*nights
def planecost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Pitssburgh':
        return 200
    elif city == 'Los angeles':
        return 250
    elif city == 'Tampa':
        return 290
def carcost(days):
    if days>=7:
        return 40*days -50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
    
def tripcost(city,days,nights,spendingmoney):
    return hotel_cost(nights)+planecost(city)+carcost(days)+spendingmoney
print('cost of car:',carcost(5))
print('cost of plane cost:',planecost('Los angeles'))
print('cost of hotel room',hotel_cost(7))
print('the total cost of trip',tripcost('Los angeles',7,7,800))
print(tripcost('Tampa',7,5,500))