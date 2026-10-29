players = ["Ravi", "Sita", "Raju"]
scores = [
    [20, 30, 40],
    [40, 35, 45],
    [25, 25, 25]
]

results = []

for i in range(len(players)):
    total = sum(scores[i])
    average = total / len(scores[i])

    if scores[i][-1] > scores[i][0]:
        trend = "Improving"
    elif scores[i][-1] < scores[i][0]:
        trend = "Declining"
    else:
        trend = "Unchanged"

    results.append((players[i], average))
    print(players[i], total, average, trend)

results.sort(key=lambda x: x[1], reverse=True)

print("Rankings:")
for item in results:
    print(item)
