def pallindrum_string_(word:list)
	for count in range len(word)//2:
		if word[count] != word[len(word)-count]
			return False
	return True 