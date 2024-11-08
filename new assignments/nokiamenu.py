print(" Nokia menu")
		
print("\n sellect an option : \n1. phone book \n2. messages \n3. chats \n4. call \n5. Tones \n6. Settings \n7. call divert \n8. games \n9. calculator \n10. reminders \n11. clock \n12. profiles \n13. SIM services \n enter number : ")		
menuList =int(input("Enter number :" ))
		  
match menuList:
	case 1: 
		phonebook = int(input("\nPhone book  \n1. search \n2. Services Nos. \n3. Add name \n4. Erase \n5. Edit \n6. Assign tone \n7. send b'card \n8. Options \n9. speed dail \n10.Voice tags \n enter number : "))
	match phonebook:
		case 1:
			print("search .......")
		case 2:
			print("service nos .......")
		case 3:
			print("Add name .......")
		case 4:
			print("Erase .......")
		case 5:
			print("Edit .......")
		case 6:
			print("Assign tone .......")
		case 7:
			print("send b'card .......")
		case 8:
			options = int(input("\nOptions \n1. Type of view \n2. Memory \n enter number :"))
			match options:
				case 1 : 
					print("view...")
				case 2:
					print("\nmemory ....")
		case 9:
			print("\nSpeed dial .......")
		case 10:
			print("\nVoice tags .......")
				
	case 2:
		messageType = int(input(" \nMessages \n1. write messages \n2. inbox \n3. outbox \n4. picture messages \n5.Templates \n6. Smileys \n enter number :"))
			 
		match messageType:
			case 1:
				print(" \nwrite message .......")
				
			case 2: 
				print("\ninbox messages.......")
				
			case 3: 
				print("\nOutbox messges .......")
				
			case 4:
				print("\n Picture messages ....... ")
				
			case 5: 
				print("\nTemplates .....")
				
			case 6: 
				print("\nSmileys .......")
				
			case 7: 
				set = int(input("\nmessages settings \n1. set 1 \n2. commom \n enter number :"))
				match set :
					case 1: 
						message = int(input(" \n1. message Center number \n2. messages sent \n3. message validity \n enter number :"))
						match(message):
							case 1:
								print(" \nMessage center number .... ")
							case 2:
								print(" \nmessage sent ...... ")
							case 3:
								print(" \n message validity .......")
					case 2: 
						int(input(" \nCommon \n1. Delivery report \n2. reply via same center \n3. character support \n enter number : "))
					 
						match(support):
							case 1:
								print(" \nDelivery report ..... ");
							case 2:
								print(" \nreply via same center ..... ")
							case 3:
								print(" \ncharacter support ..... ")
			case 8 :
				print("\ninfo services  ")
		
			case 9 :
				print("\nVoice mailbox  ")
			
			case 10 :
				print("\nVoicemailbox  ")
			
	case 3 :
		chats = int(input("\n chats \n1. chats \nenter number"))
			 
		match(chats):
			case 1:
				print("chats .......")
				
	case 4:
		register =(input("\ncall register \n1 Missed calls \n2. Receive calls duration  \n3. dialled numbers \n enter number :  " ))
		match(register):
			case 1:
				print(" missed calls")
				
			case 2:
				print("Receive calls duration....")
				
			case 3:
				print(" dailled numeber ......")
				
			case 4:
				print("Erase recent call list ")
			
			case 5:
				show =int(input(" \nShow call duration \n1. last call duration \n2. All call's duration \n3. Received call's duration \n4. Dialled call's \n5. Clear timers\n enter number :"))
				 
				match(show):
					case 1:
						print("last call duration")
					
					case 2:
						print("All call's duration")
					
					case 3:
						print("Received call's duration")
					case 4:
						print("Dialled call's")
					case 5:
						print("Clear timers")
				
			case 6:
				cost =int(input(" \nShow call cost \n1. last call cost \n2. All call's cost \n3. Clear Counters \n enter number :"))
				 match(cost):
					case 1:
						print("last call cost");
					case 2:
						print("All call's cost");
					case 3:
						print("Clear Counters");
			case 7:
				settings = int(input(" \n call cost settings \n1. call cost limit \n2. show costs in \n enter number : "))
				match(settings):
					case 1:
					print("call cost limit")
					break
					case 2:
					print("show costs in")
					
			case 8:
				print("prepaid credit")
			
		
		case 5:
			tones =int(input("\n Tones \n1. Ringing tone \n.2 Ringing volume \n3. incoming call alert \n4. Compose \n5. Messages \n6. Keypad tones \n7. warning and game tones\n8. Vibrating alert\n9. Screen saver \n enter number :"))
			match(tones):
				case 1:
					print(" Ringing tone .....")
				
				case 2:
					print(" Ringing volume ..... ")
				
				case 3:
					print(" incoming call alert..... ")
				
				case 4:
					print(" Compose...... ")
				
				case 5:
					print(" Messages..... ")
				
				case 6:
					print(" Keypad tones..... ")
				
				case 7:
					print(" warning and game tones.... ")
				
				case 8:
					print(" Vibrating alert.......  ")
				
				case 9:
					print(" Screen saver..... ")
				
		case 6:
			settings =int(input(" \nSettings \n1. call settings \n2. Phone Settings \n3.Security Settings \nRestore factory settings \n enter number :"))
			match settings :
				case 1: 
					callsettings=int( input("call settings \n1. Automatic redial \n2. Speed dailling \n3. Speed dialling \n4. Own number sending \n5. phone line in use \n6. Automatic answer \n enter number :"))
					match(callsettings):
						case 1: 
							print("Automatic redial........")
						
						case 2: 
							print("Speed dailling......")
						
						case 3: 
							print("Speed dialling......")
						
						case 4: 
							print("Own number sending......")
						
						case 5: 
							print("phone line in use.....")
						
						case 6: 
							print("Automatic answer.....")
				case 2: 
					phonesettings = int(input("Phone Settings \n1. language \n2. Cell info display \n3.Welcome note \n4. Network selection \n5. Light \n6. Confirm SIM service actions \n enter number :"))
					match(phonesettings):
						case 1: 
							print(" Language........")
						case 2: 
							print("Cell info display......")
						case 3: 
							print("Welcome Note......")	
						case 4: 
							print("Network selection......")
						case 5: 
							print("Light.....")
						case 6: 
							print("Confirm SIM service actions.....")
				case 3: 
					securitysettings =int(input("Securitysettings \n1. PIN code request \n2. Call barring service \n3. fixed dailing \n4. Closed user group \n5. phone security \n6. Change access codes \n enter number :"))
					match(securitysettings):
						case 1: 
							print(" PIN code request........")
						case 2: 
							print("Call barring service......")
						
						case 3: 
							print("fixed dailing......")
						
						case 4: 
							print("Closed user group......")
						
						case 5: 
							print("phone security.....")
						
						case 6: 
							print("Change access codes.....")
				case 4: 
					print("Restore factory .........")
		case 7:
			print(" Call divert...... ")
		case 8:
			print(" Games ")
		case 9:
			print(" Calculator ")
		case 10:
			print(" Reminders.... ")
		case 11:
			clock = int(input(" Clock \n1. Alarm clock \n2. Clock setting \n3. Date Setting \n4. StopWatch \n5. Countdown timer \n6. Auto update 0f date and time \n enter number :"))					 
			match(clock):
				case 1: 
					print(" Alarm clock........")
				case 2: 
					print("Clock setting......")
				case 3: 
					print("Date Setting......")
				case 4: 
					print("StopWatch ......")
				case 5: 
					print("Countdown timer.....")
				case 6: 
					print("Auto update 0f date and time.....")
		case 12:
				print(" profiles.... ")
		case 13:
				print("SIM Services....")
		