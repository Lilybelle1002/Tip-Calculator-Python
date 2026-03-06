print("Welcome to the Tip Calculator")

bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("How many people are splitting the bill? "))

tip = bill * (tip_percent / 100)
total = bill + tip
per_person = total / people

print("\nTip amount: $", round(tip, 2))
print("Total bill with tip: $", round(total, 2))
print("Each person pays: $", round(per_person, 2))