countries = {
"use":{"california":{"los Angeles":4000000, "San Francisco":8700000}},
"Canada": {"olando":{"Toronto":2930000,"Ottawa":994837}}
}
 #enter country and state


def get_population(countries,state):
	citys = {}
	for states in countries.values():
		for city ,populations in states.items():
			if city == state:
				#citys.keys(city)
				citys[city] = populations
		 	
	#return ((x , y) for x,y in citys.items())
	return citys		

print(get_population(countries,"california"))

#userCountryInput = input("Enter state :")




