print("Welcome to the tip calculator")
total_bill = input("What is your total bill:")
customer_number = input("What is the number of customers:")
tip_percentage = input("put the tip percentage:")
tip_total = float(tip_percentage)/100 + 1
bill_per_person = float(total_bill)/float(customer_number)
bill_with_tip = round((bill_per_person*tip_total),2)
print(bill_with_tip)