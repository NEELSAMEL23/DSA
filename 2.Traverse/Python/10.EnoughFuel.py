def fuel_consumption(fuel, distance):
    required = fuel * distance
    if required > 50:
        return "Go On"
    else:
        return "Enough"

fuel = 1
distance = 48
res = fuel_consumption(fuel, distance)
print(res)
