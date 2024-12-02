def get_password():
	for character in password:
		count += 1
		if count < 16:
			return 'poor passcode'
	
	 