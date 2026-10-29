appliances = ["Fan", "Light", "AC"]
before = [100, 80, 300]
after = [70, 40, 240]

results = []

for i in range(len(appliances)):
    saved = before[i] - after[i]
    percentage = saved / before[i] * 100

    results.append((appliances[i], percentage))
    print(appliances[i], "Saved:", saved)
    print("Savings percentage:", percentage)

results.sort(key=lambda x: x[1], reverse=True)

print("Ranking:")
for item in results:
    print(item[0], item[1])
