rooms = [101, 102, 201, 202]
floors = [1, 1, 2, 2]
electricity = [120, 180, 100, 250]
water = [500, 700, 400, 900]

for i in range(len(rooms)):
    electric_charge = electricity[i] * 5
    water_charge = water[i] * 0.05
    total = electric_charge + water_charge

    print("Room:", rooms[i], "Floor:", floors[i])
    print("Total charge:", total)

    if electricity[i] > 200 or water[i] > 800:
        print("Warning: High consumption")
    else:
        print("Normal consumption")
