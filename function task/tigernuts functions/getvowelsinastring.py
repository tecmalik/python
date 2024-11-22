def get_vowels_in_a_string(phrase)->int:
	if type(phrase) is not str:
		raise TypeError
	else:
		phrase=phrase.upper()
		counter = 0
		for count in phrase:
			if count == 'A'or count =='E'or count =='I'or count =='O'or count =='U':
				counter += 1
		return counter