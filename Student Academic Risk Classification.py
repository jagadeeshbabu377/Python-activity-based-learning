names = ["Ravi", "Sita", "Raju"]
marks = [35, 75, 45]
attendance = [60, 90, 70]
lab = [30, 80, 40]

for i in range(len(names)):
    risk = 0
    reasons = []

    if marks[i] < 40:
        risk += 1
        reasons.append("Low marks")

    if attendance[i] < 75:
        risk += 1
        reasons.append("Low attendance")

    if lab[i] < 40:
        risk += 1
        reasons.append("Low lab score")

    if risk >= 2:
        category = "High Risk"
    elif risk == 1:
        category = "Medium Risk"
    else:
        category = "Low Risk"

    print(names[i], category, reasons)
