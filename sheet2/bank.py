''' Prompt the user and read in two money amounts (in cent)
 Add the two amounts
 Print out the answer in a human readable format 
 with a euro sign and decimal point between the euro and cent of the amount
'''

number1 = float(input ("Enter amount 1 (in cent):  "))
number2 = float(input ("Enter amount 2 (in cent):  "))
sum = (float(number1 + number2)/100)

print (f"The sum of the two values you entered is €{sum:.2f}")

