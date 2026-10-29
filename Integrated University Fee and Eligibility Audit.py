names = ["Ravi", "Sita", "Raju"]
fees = [50000, 50000, 50000]
paid = [50000, 40000, 50000]
attendance = [80, 60, 90]
marks = [45, 60, 30]

for i in range(len(names)):
    reasons = []
    due = fees[i] - paid[i]

    if due > 0:
        reasons.append("Fee pending")

    if attendance[i] < 75:
        reasons.append("Low attendance")

    if marks[i] < 35:
        reasons.append("Low internal marks")

    if len(reasons) == 0:
        print(names[i], "Eligible")
    else:
        print(names[i], "Conditions:", reasons)

    print("Outstanding fee:", due)
