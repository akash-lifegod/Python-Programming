# Program to input the number of heads and feet in a farm and identify the number of chickens 
# and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150 
# chickens and 190 goats

heads=int(input('Enter no. of heads '))
feet=int(input('Enter no. of feet '))
goat=feet-(heads*2)
goat=goat/2
hen=heads-goat
print(f'Hen {hen}')
print('Goat ',goat)