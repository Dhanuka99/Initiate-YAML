name = input('Enter your name: ')
print('Your name is' , name)

#Tip Calculator 

foodAmount  = float(input('Enter Food Amount: $'))
tipPercentage = float(input('Enter Tip Percentage: ')) /100
tipAmount = foodAmount*tipPercentage

total = foodAmount + tipAmount

print(" $ " + str(total))