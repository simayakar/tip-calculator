#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill? $")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people = input("How many people to split the bill? ")
#Write your code below this line 👇
each_person =  (float(total_bill) / int(people)) * float((100 + int(tip))/100)
rounded_person = round(each_person,2)
print(f"Each person should pay: ${rounded_person}")
