# Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the 
# shopping amount is greater than 25000, the category is GOLD. If the shopping amount is 
# between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The 
# discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is 
# 10% of the shopping amount and 5% otherwise. Design a program in python that asks the user 
# to input the total shopping amount, outputs the category and amount to be paid.

amt=int(input('Enter total amount '))
if amt>25000:
    amt=amt-(0.2*amt)
elif amt>=10000 and amt<=25000:
    amt=amt-(0.1*amt)
else:
    amt=amt-(0.05*amt)
print(amt)