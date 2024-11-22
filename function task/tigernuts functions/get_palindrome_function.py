def get_palindrome(word):
	wordcase = word.upper
	reversedword = wordcase[::-1]
	if reversedword == wordcase:
		return true
	else:
		return false 