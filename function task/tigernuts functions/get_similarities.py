def get_similarities_function(firstword:list, secondword:list):
	if firstword.sort() == secondword.sort():
		return True
	else :
		return false
