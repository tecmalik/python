principal_amount = int(input('Enter the principal amount:'))
annual_intrest_rate = int(input('Enter the anual intrest rate:'))
duration_of_years = int(input('enter the duration in year:'))

loan_duration = (duration_of_years*12)
annual_intrest_rate2 = annual_intrest_rate/100/12

monthly_payment = principal_amount * ((annual_intrest_rate2 *((1+ annual_intrest_rate2)**(loan_duration)))/(((1+annual_intrest_rate2)**(loan_duration)) -1 ))

print('your monthy payment is $',monthly_payment)