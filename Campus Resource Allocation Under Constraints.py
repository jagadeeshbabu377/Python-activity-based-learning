available = 20

activities = [
    ("Sports", 8, 2),
    ("Seminar", 10, 1),
    ("Cultural", 7, 3)
]

activities.sort(key=lambda x: x[2])

for name, required, priority in activities:
    allocated = min(available, required)
    shortage = required - allocated
    available = available - allocated

    print(name, "Allocated:", allocated)
    print("Shortage:", shortage)

print("Remaining equipment:", available)
