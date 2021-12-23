print("welcome to Tip Calculator...")
bill = float(input("what was the total bill? Rs."))
tip = 1.00 + (int(input("what percentage the tip wouldd you like to give? 10, 12 or 15? "))/100)
no_of_persons = int(input("How many people to spilt the bill? "))

bill_per_person = (bill * tip)/no_of_persons

print("Each person should pay: Rs "+str(round(bill_per_person, 2)))
