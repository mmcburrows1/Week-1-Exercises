bill_amount = float(input("Total bill amount? "))

service_lvl = input("Level of service? Good/Bad/Fair? ").lower()
# set .lower because this will return the users answer in all lower case which is essential for the code to be able to read the if statements

if service_lvl == "good":
    tip_amount = bill_amount * 0.2
elif service_lvl == "fair":
    tip_amount = bill_amount * 0.15
    print(tip_amount)
elif service_lvl == "bad":
    tip_amount = bill_amount * 0.1
else:
    print("Indicate whether service is Good,Bad, or Fair.")
result = bill_amount + tip_amount

print("Tip amount: ${:,.2f}".format (tip_amount))
# I added the ${:,.2f}.format to insert the dollar sign into the output, this is to be added as a part of the string so make sure its inside the quotes

print("Total amount: ${:,.2f}".format (result))
# For some reason it had me take out the str() from in front of the (tip_amount) and (result)

