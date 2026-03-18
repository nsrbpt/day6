
user_input = input("Enter transaction amounts separated by space: ")

transactions = [int(x) for x in user_input.split()]

categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

for t in transactions:
    if t <= 0:
        categories["invalid"].append(t)
    elif t <= 500:
        categories["normal"].append(t)
    elif t <= 2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)

valid_transactions = [t for t in transactions if t > 0]

total_value = sum(valid_transactions)
count = len(transactions)
summary = (total_value, count)

frequent = count > 5
large_spending = total_value > 5000
suspicious = len(categories["high_risk"]) >= 3

if suspicious:
    risk = "High Risk"
elif large_spending or frequent:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

print("\nCategorized Transactions:")
for key, value in categories.items():
    print(f"{key}: {value}")

print("\nSummary (Total Value, Number of Transactions):", summary)
print("Total Transaction Value:", total_value)
print("Number of Transactions:", count)

print("\nFinal Risk Classification:", risk)
