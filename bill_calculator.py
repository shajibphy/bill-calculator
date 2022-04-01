#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = input("What is the total bill:")
customer_number = input("What is the number of customers:")
tip_percentage = input("put the tip percentage:")
tip_total = float(tip_percentage)/100 + 1
bill_per_person = float(total_bill)/float(customer_number)
bill_with_tip = round((bill_per_person*tip_total),2)
print(bill_with_tip)
