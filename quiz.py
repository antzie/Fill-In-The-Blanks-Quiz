# 28-01-2018
def difficulty_level(choice): 
	"""Retrieves the paragraph and associated missing spaces and 
	answers that are connected to each difficulty level (easy, medium, 
	hard)

	Args: 
		choice: the user's choice of either: easy, medium or hard.

	Returns:
		paragraph: 
		answers: a list of the answers
		quiz_spaces: a list of numbered spaces e.g. ___1___.
	"""
	
	if 	choice == 'easy':
		paragraph = ('\n' '___1___; Age of ___2___ ' "\n"
					 '    After a successful raid on a HYDRA base, Tony ___3___ and Bruce ___4___'
					 ' create an Artificial Intelligence called ___2___, a peacekeeping protocol'
					 ' designed to help the ___1___ protect the world from their enemies. But'
					 ' things go wrong when ___2___ sees the human race as a threat and sets out'
					 ' to destroy it along with the ___1___.  '"\n"
					 '    Now the ___1___, Iron Man, Thor, Captain ___5___, the ___6___, B____ W____'
					 ' and Hawkeye, must reassemble to stop ___2___ from causing mass destruction.'
					 ' Aside from this, the ___1___ also must take on the powerful twins'
					 ' Quicksilver and Scarlet Witch as well as a new entity called Vision.' '\n'  
					 '    After discovering a power beyond their comprehension, the ___1___ find'
					 ' that things may never be the same again. ''\n' 
					 )
		answers = ['Avengers', 'Ultron', 'Stark', 'Banner', 'America', 'Hulk', 'Black Widow']
		quiz_spaces = ['___1___', '___2___','___3___', '___4___', '___5___', '___6___', 'B____ W____'] 
	
	elif choice == 'medium':
		paragraph = ('\n' "___1___: ___2___:" '\n'
					 '___1___ is imprisoned on the other side of the universe without his mighty ___3___ '
					 'and finds himself in a race against time to get back to ___4___ to stop ___2___'
					 '--the destruction of his homeworld and the end of ___4___ian civilization--at'
					 ' the hands of an all-powerful new threat, the ruthless ___5___. But first he must'
					 ' survive a deadly gladiatorial contest that pits him against his former ___6___ and'
					 ' fellow ___7___--the ___8___ ___9___!' '\n'
					 )
		answers = ['Thor', 'Ragnarok', 'hammer', 'Asgard', 'Hela', 'ally', 'Avenger', 'Incredible', 'Hulk']
		quiz_spaces = ['___1___', '___2___','___3___', '___4___', '___5___', '___6___',
					   '___7___', '___8___','___9___'
					   ]
	
	elif choice == 'hard':
		paragraph = ('\n' '___1___ for the Wilderpeople:' '\n'
					 '     Raised on hip-hop and foster ___2___, defiant ___3___ kid Ricky gets a fresh start'
					 ' in the ____ 4 _______ countryside. He quickly finds himself at home with his new foster'
					 ' ___5___: the loving Aunt Bella, the cantankerous Uncle Hec, and ___6___ Tupac. When a ___7___'
					 ' strikes that threatens to ship Ricky to another home, both he and Hec go on the run in'
					 ' the ___8___. As a national ___9______1___ ensues, the newly branded ___10___ must face their options:'
					 ' go out in a blaze of glory or overcome their differences and survive as a family.' '\n'
					 '     Director Taika Waititi, (upcoming Thor:___11___) masterfully weaves lively humor' 
					 ' with emotionally honest performances by Sam Neill and Julian Dennison.'
					 ' ___1___ for the Wilderpeople is a hilarious touching ___12___-pleaser.' '\n'
					 )
		answers = ['Hunt', 'care', 'city', 'New Zealand', 'family', 
					'dog', 'tragedy', 'bush', 'man', 'outlaws',
				    'Ragnarok', 'crowd'
				    ]
		quiz_spaces =  ['___1___', '___2___','___3___', '____ 4 _______', '___5___',
						'___6___', '___7___', '___8___','___9___', '___10___',
						'___11___', '___12___'
					    ]
	return paragraph, answers, quiz_spaces


# Preparatory Functions

def fix_input(inputtted_answer):  
	"""Strips spaces and lowercases a string.
	Args:
		inputted_answer: string that requires formatting - usually 
						 user inputted string
	Returns:
		inputted_answer: formatted string!
	"""
	inputtted_answer = inputtted_answer.strip()
	inputtted_answer = inputtted_answer.lower() 
	return inputtted_answer


def show_answers(empty_spaces, official_answers):
	"""Shows and formats the appropriate official answers, 
	depending on the user's choices	
	Args:
		empty_spaces: the list of numbered spaces associated with
					  the paragraph/difficulty level user previously
					  chose.
		official_answers: the list of answers connected to the 
						  empty spaces
	Returns:
		answers: formatted string matching an element of empty_spaces to
		 		 its corresponding element in official answers.
	"""
	format_answer = ()
	see_answers = fix_input(raw_input('Do you want to see the answers? Yes/No? '))
	if see_answers in ('yes', 'y'):
		for spaces, answers in zip(empty_spaces, official_answers):
			format_answer = format_answer + (spaces, answers)
		answers = ' '.join(format_answer)
		return 'Answers:' '\n' + answers
	else:
		return ' '


def restart_game(main_function, empty_spaces, official_answers):
	"""
	Starts the entire game again or exits game entirely, 
	depending on the user's choices.
	Args:
		main_function: function this function re-starts.
		empty_spaces: the list of numbered spaces associated with
					  the paragraph/difficulty level user previously
					  chose.
		official_answers: the list of answers connected to the 
						  empty spaces
	Returns:
		main_function(): restarts the game
		sys.exit(): Exits game entirely
	"""
	import sys
	restart = fix_input(raw_input("Would you like to restart the game? Yes/No? "))
	if restart in ('yes', 'y'):
		print '\n' 'New Game'
		return main_function()     #restart the game function.
	elif restart in ('no', 'n'):
		print show_answers(empty_spaces, official_answers)
		return sys.exit("Game Over")
	else: 
		return sys.exit('Do you mind? Bye-bye')


def ask_level_attempts():
	""" Asks user to choose the difficulty level and to choose 
	either the default number of permissable wrong attempts or define
	the number of atempts. 
	To prevent errors, loops until user inputs acceptable input.
	
	Returns:
			user_level: user's choice of ('easy', 'medium', 'hard').
			user_attempts: user's choice of 'yes' or 'no'.
	"""
	while True: 
		user_level = fix_input(raw_input('\n' 'Choose difficulty level: easy, medium, hard: '))
		if user_level in ('easy', 'medium', 'hard'):
			break
		print '\n' 'Please choose one of the specified inputs.'	
	while True:
		user_attempts = fix_input(raw_input('\n' 'Would you like to choose how many wrong attempts are allowed? (Yes) Or accept the default? (No): '))		
		if user_attempts in ('yes', 'y', 'n', 'no'):
			break
		print '\n' 'Please choose one of the specified inputs.'
	return user_level, user_attempts


def default_attempts(choice):
	"""Returns the default number of wrong attempts allowed.
	Args:
		choice: user's choice of difficulty level ('easy', 'medium', 'hard')
	Returns:
		int(default_options[choice]): the integer associated with the key, with the user's choice
	"""
	default_options = {'easy': 8,    
				   	   'medium': 5,
				   	   'hard': 1
				  	   }
	return int(default_options[choice]) 


def acceptable_attempts_ranges(choice_level):  
	"""Asks user to choose number of wrong attempts and keeps user's choice of integer 
	within an acceptable range for the already chosen difficulty level.
	Args:
		choice_level: difficulty level that user chose previously
	Returns:
		user_number: the user's choice of number of wrong attempts permitted.
	"""
	acceptable_ranges = {'easy': range(1,13),    
		   	    	 	 'medium': range(1,9),
		         	     'hard': range(1,5)
		                }
	while True:
		user_number = raw_input('\n''Permitted number of wrong attempts for level ' 
								+ choice_level 
								+ ': ' 
								+ str(acceptable_ranges[choice_level]) 
								+ '\n' 'Enter an appropriate integer: ')
		#Check if numbers are in dictionary: acceptable_ranges.
		if choice_level in acceptable_ranges and int(user_number) in acceptable_ranges[choice_level]: 
			break
	return int(user_number)


def choose_specs(): 
	"""Asks user to choose the difficulty level and whether he chooses to adjust the number of 
	wrong attempts. 
	If yes to the wrong attempts, users then choose a number in an acceptable range. 
	If no - wrong attempts are the default.
	
	Returns:
		level: string, difficulty level
		num_attemtps: integer, number of wrong attempts allowed.
	"""
	level, ask_attempts = ask_level_attempts()
	if ask_attempts in ('yes', 'y'):
		num_attempts = acceptable_attempts_ranges(level) # Returns an number in an acceptable range
	else:
		num_attempts = default_attempts(level)  #returns default settings for attempts
	return level, num_attempts


def quiz():
	""" The actual game!!
	1). Users asked to choose the difficulty level and number of wrong attempts allowed.
	2). Depending on their choices, the appropriate paragraph etc. is returned.
	3). User asked to replace space in paragraph - loops until either correct word is inputted
		or number of wrong attempts used up.
	4).
	Returns:
		restart_game(quiz, quiz_spaces, answers): Option to restart the game upon either losing
												  or winning. See function def for restart_game
												  for more info.
	"""
	import string
	level, attempts_allowed = choose_specs()	
	paragraph, answers, quiz_spaces = difficulty_level(level)
	attempts_made = 0
	print paragraph 
	for space, word in zip(quiz_spaces, answers):
		while True: 	
			user_input = raw_input("\n" "What word should replace " + space + '? ' )			
			if fix_input(user_input) == fix_input(word): 
				user_input = word               		    
				break	
			if attempts_made == attempts_allowed: 
				return restart_game(quiz, quiz_spaces, answers)
			print "\n" 'Wrong. Total attempts remaining:  ' + str(attempts_allowed - attempts_made)
			attempts_made = attempts_made + 1     # Counter.
		paragraph = string.replace(paragraph, space, user_input)	
		print paragraph
	print 'You Win! Congratulations' '\n'
	return restart_game(quiz, quiz_spaces, answers)
print quiz()
