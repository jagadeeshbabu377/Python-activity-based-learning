weights = [5, 8, 12, 4]
zones = ["A", "B", "A", "B"]
priority = [1, 2, 1, 3]

vehicles = [
    ["Vehicle1", "A", 15],
    ["Vehicle2", "B", 10]
]

packages = list(zip(weights, zones, priority))
packages.sort(key=lambda x: x[2])

for weight, zone, priority in packages:
    assigned = False

    for vehicle in vehicles:
        if vehicle[1] == zone and vehicle[2] >= weight:
            vehicle[2] -= weight
            print("Package", weight, "sent using", vehicle[0])
            assigned = True
            break

    if not assigned:
        print("Package", weight, "cannot be dispatched")

print("Remaining capacities:")
for vehicle in vehicles:
    print(vehicle)
