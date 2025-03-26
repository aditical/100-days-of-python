print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip_percentage= int(input("How much tip would you like to give? 10, 12, or 15? "))
total_tip = (tip_percentage/100) * total_bill
people = int(input("How many people to split the bill? "))
each_person_split_amount = round((total_bill + total_tip ) / people, 2)
print(f"Each person should pay: ${each_person_split_amount}")