rate_of_return = 0.07
original_amount_invested = 1000
number_of_years = int(input('enter nmber of years :')) 
amount_on_deposit = original_amount_invested * (1 + rate_of_return)**(number_of_years)
print('amount of deposit in', number_of_years ,' is', amount_on_deposit)