#..
#Depending ion where an individual is from we need to tax them
#appropiately. The states of CA, Mn, and NY have taxes
#of 7.5%, 9.5%, and 8.9% respectively.
#Use this infromation to take the amount of a purchase and 
#the corresponding state to ssure that they are taxed by the right amount.
#...

state = 'CA'
purchase_amount = 25

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you are from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since your from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result) 