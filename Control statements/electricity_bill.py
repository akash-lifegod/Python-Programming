unit=int(input('Enter Total Units: '))
if unit<=50:
    bill=unit*0.50
elif unit>50 and unit<=150:
    bill=50*0.50 + (unit-50)*0.75
elif unit>150 and unit<=250:
    bill=50*0.50 + 100*0.75 + (unit-150)*1.20
elif unit>250:
    bill=50*0.50 + 100*0.75 + 100*1.20 + (unit-250)*1.50
bill=bill+bill*0.20
print("Your total Electricity bill is Rs.{}".format(bill))