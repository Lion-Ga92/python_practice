def ground_ship_cost(weight):
  if (weight <= 2):
    return (weight * 1.5) + 20
  elif (weight > 2 ) and (weight <= 6):
    return (weight * 3) + 20
  elif (weight > 6) and (weight <= 10):
    return (weight * 4) + 20
  elif (weight > 10):
    return (weight * 4.75) + 20

result = ground_ship_cost(8.4)
print(result)

def drone_ship_cost(weight):
  if (weight <= 2):
    return (weight * 4.5)
  elif (weight > 2 ) and (weight <= 6):
    return (weight * 9)
  elif (weight > 6) and (weight <= 10):
    return (weight * 12)
  elif (weight > 10):
    return (weight * 14.75)

result2 = drone_ship_cost(1.5)
print(result2)

def cheapest_total(weight):
    if (weight > 10):
        return "The cheapest option is premium and the cost is $120"
    elif (weight > 6) and (weight <= 10):
        return print("The cheapest option is drone shipping and the cost is " + str(weight * 12))
    elif (weight > 2) and (weight <= 6):
        return print("The cheapest option is ground shipping and the cost is " + str(weight * 3 + 20))
    elif (weight < 2):
        return print("The cheapest cost is drone shipping " + str(weight * 4.5))



cheapest_total(4)
