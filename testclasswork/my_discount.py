def getmy_discount(price , discount):
	if type(price) is int and type(discount) is int:
		amount = (price - (price/100 *discount))
		return amount
	if type(price) is float and type(discount) is float:
		amount = (price - (price/100 *discount))
		finalamount = round(amount,3)
		return finalamount
	if type(price) is float and type(discount) is int:
		amount = (price - (price/100 *discount))
		finalamount = round(amount, 3)
		return finalamount
	if type(price) is chr and type(discount) is int:
		return none