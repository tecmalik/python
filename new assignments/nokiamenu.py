print(" Nokia menu")
		
print("\n sellect an option : \n1. phone book \n2. messages \n3. chats \n4. call \n5. Tones \n6. Settings \n7. call divert \n8. games \n9. calculator \n10. reminders \n11. clock \n12. profiles \n13. SIM services \n enter number : ")		
menuList =int(input("Enter number :" ))
		  
switch (menuList){
	case 1: 
		phonebook = int(input("\nPhone book  \n1. search \n2. Services Nos. \n3. Add name \n4. Erase \n5. Edit \n6. Assign tone \n7. send b'card \n8. Options \n9. speed dail \n10.Voice tags \n enter number : "))
		switch(phonebook){
				case 1:
			    	print("search .......")
				break
				case 2:
			    	print("service nos .......")
				break
				case 3:
			    	print("Add name .......")
				break
				case 4:
			    	print("Erase .......")
				break
				case 5:
			    	print("Edit .......")
				break
				case 6:
			    	print("Assign tone .......")
				break
				case 7:
			    	print("send b'card .......")
				break
				case 8:
			    	options = int(input("\nOptions \n1. Type of view \n2. Memory \n enter number :"))
				
					switch(options){
						case 1 : 
						print("view...")
						break
						case 2:
						.print("\nmemory ....")
						break
						}
				break
				case 9:
			    	print("\nSpeed dial .......")
				break
				case 10:
			    	print("\nVoice tags .......")
				break
				}
		
	
		break
		case 2:
			messageType = int(input(" \nMessages \n1. write messages \n2. inbox \n3. outbox \n4. picture messages \n5.Templates \n6. Smileys \n enter number :"))
			 
			switch(messageType){
				case 1:
				print(" \nwrite message .......")
				break
				case 2: 
				print("\ninbox messages.......")
				break
				case 3: 
				print("\nOutbox messges .......")
				break
				case 4:
				print("\n Picture messages ....... ")
				break;
				case 5: 
				print("\nTemplates .....")
				break;
				case 6: 
				print("\nSmileys .......")
				break;
				case 7: 
				set = int(input("\nmessages settings \n1. set 1 \n2. commom \n enter number :"))
				  
				switch(set){
				case 1: 
					message = int(input(" \n1. message Center number \n2. messages sent \n3. message validity \n enter number :"))
					
					switch(message) {
						case 1:
						print(" \nMessage center number .... ")
						break;
						case 2:
						print(" \nmessage sent ...... ")
						break
						case 3:
						print(" \n message validity .......")
						break
						}

					
				break	
				case 2: 
					int(input(" \nCommon \n1. Delivery report \n2. reply via same center \n3. character support \n enter number : "))
					 
					switch(support){
						case 1:
						print(" \nDelivery report ..... ");
						break
						case 2:
						print(" \nreply via same center ..... ")
						break
						case 3:
						print(" \ncharacter support ..... ")
						break
					}
				break	
				}
			break
			case 8 :
				print("\ninfo services  ")
			break;
			case 9 :
				print("\nVoice mailbox  ")
			break;
			case 10 :
				print("\nVoicemailbox  ")
			break;

			}
			
		case 3 :
			chats = int(input("\n chats \n1. chats \nenter number"))
			 
			switch(chats){
				case 1:
				print("chats .......")
				break;
			}
		break
			
		case 4:
			register =(input("\ncall register \n1 Missed calls \n2. Receive calls duration  \n3. dialled numbers \n enter number :  " ))
			
			switch(register){
				case 1:
				print(" missed calls")
				break
				case 2:
				print("Receive calls duration....")
				break;
				case 3:
				print(" dailled numeber ......")
				break
			case 4:
				print("Erase recent call list ")
			break
			case 5:
				show =int(input(" \nShow call duration \n1. last call duration \n2. All call's duration \n3. Received call's duration \n4. Dialled call's \n5. Clear timers\n enter number :"))
				 
				switch(show){
					case 1:
					print("last call duration")
					break
					case 2:
					print("All call's duration")
					break
					case 3:
					print("Received call's duration")
					break;
					case 4:
					print("Dialled call's")
					break;
					case 5:
					print("Clear timers")
				break
				}
			break
			case 6:
				cost =int(input(" \nShow call cost \n1. last call cost \n2. All call's cost \n3. Clear Counters \n enter number :"))
				 
				switch(cost){
					case 1:
					print("last call cost");
					break;
				case 2:
					print("All call's cost");
				break;
				case 3:
					print("Clear Counters");
				break;
				}
			break
			case 7:
				settings = int(input(" \n call cost settings \n1. call cost limit \n2. show costs in \n enter number : "))
				 
				switch(settings){
					case 1:
					print("call cost limit")
					break
					case 2:
					print("show costs in")
					break
				}

					break
				c	ase 8:
				print("prepaid credit")
			break

			}
			
		break;
		case 5:
				 tones =int(input("\n Tones \n1. Ringing tone \n.2 Ringing volume \n3. incoming call alert \n4. Compose \n5. Messages \n6. Keypad tones \n7. warning and game tones\n8. Vibrating alert\n9. Screen saver \n enter number :"))
				int tones = .nextInt
				switch(tones){
				case 1:
					print(" Ringing tone .....")
				break;
				case 2:
					print(" Ringing volume ..... ")
				break
				case 3:
					print(" incoming call alert..... ")
				break
				case 4:
					print(" Compose...... ")
				break
				case 5:
					print(" Messages..... ")
				break
				case 6:
					print(" Keypad tones..... ")
				break
				case 7:
					print(" warning and game tones.... ")
				break;
				case 8:
					print(" Vibrating alert.......  ")
				break;
				case 9:
					print(" Screen saver..... ");
				break
				}
		
		break
		case 6:
				settings =int(input(" \nSettings \n1. call settings \n2. Phone Settings \n3.Security Settings \nRestore factory settings \n enter number :"))
				
				switch(settings){
					case 1: 
					int( input("call settings \n1. Automatic redial \n2. Speed dailling \n3. Speed dialling \n4. Own number sending \n5. phone line in use \n6. Automatic answer \n enter number :")
					callsettings =.nextInt()
						switch(callsettings){
						case 1: 
							print("Automatic redial........")
						break
						case 2: 
							print("Speed dailling......")
						break
						case 3: 
							print("Speed dialling......")
						break
						case 4: 
							print("Own number sending......")
						break
						case 5: 
							print("phone line in use.....")
						break
						case 6: 
							print("Automatic answer.....")
						break
						}


				break;
				case 2: 
					phonesettings = int(input("Phone Settings \n1. language \n2. Cell info display \n3.Welcome note \n4. Network selection \n5. Light \n6. Confirm SIM service actions \n enter number :"))
						
						switch(phonesettings){
							case 1: 
							print(" Language........")
							break
							case 2: 
							print("Cell info display......")
							break
							case 3: 
							print("Welcome Note......")
							break
							case 4: 
							print("Network selection......")
						break
						case 5: 
							print("Light.....")
						break;
						case 6: 
							print("Confirm SIM service actions.....")
						break;
						}

				break
				case 3: 
					int(input("Securitysettings \n1. PIN code request \n2. Call barring service \n3. fixed dailing \n4. Closed user group \n5. phone security \n6. Change access codes \n enter number :"))
						 securitysettings = .nextInt()
						switch(securitysettings){
						case 1: 
							System.out.print(" PIN code request........")
						break;
						case 2: 
							System.out.print("Call barring service......")
						break;
						case 3: 
							System.out.print("fixed dailing......")
						break;
						case 4: 
							print("Closed user group......")
						break
						case 5: 
							print("phone security.....")
						break
						case 6: 
							print("Change access codes.....")
						break
						}
				break
				case 4: 
					System.out.print("Restore factory .........")
				break
				}
		break

		case 7:
				print(" Call divert...... ")
		break
		case 8:
				print(" Games ")
		break
		case 9:
				print(" Calculator ")
		break
		case 10:
				print(" Reminders.... ")
		break
		case 11:
				clock = int(input(" Clock \n1. Alarm clock \n2. Clock setting \n3. Date Setting \n4. StopWatch \n5. Countdown timer \n6. Auto update 0f date and time \n enter number :"))					 
						switch(clock){
							case 1: 
							print(" Alarm clock........")
							break
							case 2: 
							System.out.print("Clock setting......")
						break
						case 3: 
							print("Date Setting......")
						break
						case 4: 
							print("StopWatch ......")
						break
						case 5: 
							print("Countdown timer.....")
						break
						case 6: 
							print("Auto update 0f date and time.....")
						break
						}

		break
		case 12:
				print(" profiles.... ")
		break;
		case 13:
				print("SIM Services....")
		break
		}
