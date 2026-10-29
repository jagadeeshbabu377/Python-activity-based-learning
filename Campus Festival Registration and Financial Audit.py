participants = ["Ravi", "Sita", "Raju", "Ravi"]
fees = [500, 500, 500, 500]

sponsorships = [5000, 3000]
expenses = [2000, 1500, 1000]

valid_names = []
total_fees = 0

for i in range(len(participants)):
    if participants[i] in valid_names:
        print("Duplicate registration:", participants[i])
    else:
        valid_names.append(participants[i])
        total_fees += fees[i]

total_sponsorship = sum(sponsorships)
total_expenses = sum(expenses)

balance = total_fees + total_sponsorship - total_expenses

print("Valid participants:", valid_names)
print("Registration fees:", total_fees)
print("Sponsorships:", total_sponsorship)
print("Expenses:", total_expenses)
print("Final balance:", balance)
