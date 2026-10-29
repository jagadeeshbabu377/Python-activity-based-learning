orders = [100, 80, 60]
dispatched = [70, 80, 50]
returned = [5, 10, 5]
inventory = 20

for i in range(len(orders)):
    if dispatched[i] > orders[i] or returned[i] > dispatched[i]:
        print("Invalid record:", i + 1)
    else:
        pending = orders[i] - dispatched[i]
        inventory = inventory + returned[i]

        print("Order:", i + 1)
        print("Pending:", pending)
        print("Returned:", returned[i])

print("Final inventory:", inventory)
