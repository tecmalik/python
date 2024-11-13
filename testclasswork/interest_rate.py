def get_interest_rate(investment_amount, monthly_interest_rate, years):
	future_investment_amount = 0
	final_future_investment_amount= 0
	number_of_months = years*12
	future_investment_amount = investment_amount * (1 + monthly_interest_rate) ** number_of_months
	final_future_investment_amount = round(future_investment_amount, 4)
	return final_future_investment_amount 
	if type(investment_amount) not in [int , float] :
		 return TypeError
	if type(monthly_interest_rate) not in [int , float] :
		 return TypeError
	if type(years) not in [int] :
		 return TypeError