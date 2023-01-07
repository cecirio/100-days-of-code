#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip Calculator")
bill_amnt = input("What was the total bill? $")
fl_bill = float(bill_amnt)

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_fl = int(tip)

people_amnt = input("How many people to split the bill? ")
p_int = int(people_amnt)
r = ((fl_bill * (tip_fl / 100) + fl_bill) / p_int)
a = round(r, 2)
a = "{:.2f}".format(r)
print(f"Each person should pay: ${a}")
