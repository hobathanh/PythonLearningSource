print("Welcome to the tip calculator.")
total = float(input('What was the total bill? '))
tip = int(input('what precentage tip would you like to give? 10,12,15 ? '))
person = int(input('How many ? '))
total_end = round(total*(tip/100+1) / person,3)
print('Total person each: $',total_end)