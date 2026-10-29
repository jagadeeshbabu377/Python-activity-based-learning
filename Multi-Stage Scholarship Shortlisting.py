names = ["Ravi", "Sita", "Raju", "Latha"]
marks = [85, 95, 90, 75]
attendance = [80, 90, 85, 70]
income = [90000, 80000, 95000, 70000]

quota = 2
eligible = []

for i in range(len(names)):
    if marks[i] >= 75 and attendance[i] >= 75 and income[i] <= 100000:
        eligible.append((names[i], marks[i]))
    else:
        print(names[i], "Not eligible")

eligible.sort(key=lambda x: x[1], reverse=True)

print("Selected candidates:")
for i in range(min(quota, len(eligible))):
    print(eligible[i])
