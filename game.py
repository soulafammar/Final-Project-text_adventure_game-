import pickle


class Room():
	def __init__(self):
		self.allowed_commands = []
		self.allowed_movements = []
		self.initial_text = ""
		self.after_text = ""
	count = 0

	def text_decision(self):
		if self.count <= 0:
			print(f"\n{self.initial_text}")
			print(f"\nPossible exits: {self.allowed_movements}")
		else:
			print(f"\n{self.after_text}")
			print(f"\nPossible exits: {self.allowed_movements}")

class ObjectRoom(Room):
	def __init__(self):
		super().__init__()
		self.room_text = {}
		self.usable_item = {}
		self.new_action = ""

	room_item = ""

	def text_decision(self):
		try:
			print(f"\n{str(self.room_text[self.room_item])}")
			print(f"\nPossible exits: {self.allowed_movements}")
		except KeyError:
			print(f"\n{str(self.room_text['none'])}")
			print(f"\nPossible exits: {self.allowed_movements}")

	def convo(self):
			response = ""
			response = input('''\nYou take a deep breath, and tell the kids about what's under the table. One of the girls looks coldly at you and asks: "What's the magic word?"\nYou respond: ''')
			if "please" in response.lower():
				print('''\nThe girl suddenly smiles. "Okay!" she says, and ask her friends to scoot their chairs, giving you space to pick it up.\n''')
				current_room.allowed_commands.append(current_room.new_action)
				current_room.allowed_commands.remove("talk")
			else:
				print("\nThe kids at the table burst into laughter. You slink away in embarrassment.\n")

	def new(attempt):
		pass

class ObstacleRoom(Room):
	def __init__(self):
		super().__init__()
		self.room_item = ""
		self.room_text = {}
		self.usable_item = {}
		self.obstacle = ""
		self.new_direction = ""
		self.item_received = ""
		self.speech = {}
	
	def text_decision(self):
			try:
				print(f"\n{str(self.room_text[self.obstacle])}")
				print(f"\nPossible exits: {self.allowed_movements}")
			except KeyError and AttributeError:
				print(f"\n{str(self.room_text['none'])}")
				print(f"\nPossible exits: {self.allowed_movements}")
	

class Exit(Room):
	def __init__(self):
		super().__init__()
		self.room_text = {}
		self.new_direction = ""

	password = ""
		
	def text_decision(self):
			try:
				print(f"\n{str(self.room_text[self.obstacle])}")
				print(f"\nPossible exits: {self.allowed_movements}")
			except KeyError and AttributeError:
				print(f"\n{str(self.room_text['none'])}")
				print(f"\nPossible exits: {self.allowed_movements}")

	def unlock_attempt(self, guess):
		if guess == self.password:
			print('\nThe keypad gives a "ding", and you hear the doors click.\n')
			current_room.allowed_movements.append(current_room.new_direction)
			del current_room.obstacle
		else:
			print('''\nThe keypad gives an angry "beep". You try the doors, but they still won't budge.\n''')

class END(Room):
	def __init__(self):
		pass
	def conclusion(self):
		print("\n\nYou step outside onto the grass and feel the Sun's warm rays hit your face. The doors slam shut behind you, and you walk home.\n\nCongrats! You made it out!")
		quit()


	
#************************ room code
mathClass = Room()
mathClass.initial_text = "Your eyelids flutter open, and you wake up from a dream about brown sugar boba and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log."
mathClass.after_text = "You are back in math class. You take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. You vaguely remember a dream about your favorite bubbly drink."
mathClass.allowed_movements.append("south")
mathClass.count = -1

desolateHallway = Room()
desolateHallway.allowed_movements.extend(["east","west","north"])
desolateHallway.initial_text = "You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. The hallway continues to the west, and music plays behind a set of double doors to the east. Someone stands in front of the doors."
desolateHallway.after_text = "You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. The hallway continues to the west, and music plays behind a set of double doors to the east. Someone stands in front of the doors."

goldfishKid = ObstacleRoom()
goldfishKid.allowed_movements.extend(["east","west"])
goldfishKid.allowed_commands.append("use")
goldfishKid.usable_item = "goldfish"
goldfishKid.obstacle = "hungryKid"
goldfishKid.item_received = "dollar"
goldfishKid.room_text["hungryKid"] = "You walk down the hallway. You see a boy sitting against a wall, patting his stomach. You can hear his stomach growling."
goldfishKid.room_text['none'] = "You walk down the hallway. You can see the boy you gave your Goldfish to munching happily. The floor around him is littered with crumbs."


hallwayEnglish = Room()
hallwayEnglish.allowed_movements.extend(["east","west","north"])
hallwayEnglish.initial_text = "As you walk down the hallway, a door appears to the north. The hallway continues both to the west and east."
hallwayEnglish.after_text = "You are in the hallway. A door to the north leads to english class. The hallway continues both to the west and east."

vendingMachine = ObstacleRoom()
vendingMachine.allowed_movements.extend(["east","west"])
vendingMachine.allowed_commands.append("use")
vendingMachine.item_received = "energy drink"
vendingMachine.obstacle = "vendingMachine"
vendingMachine.usable_item = "dollar" 
vendingMachine.room_text["none"] = "You walk down the hallway. You stand next to a vending machine, a big metal box pressed up against the cold brick wall of the hallway. It's filled with candy, chip bags, and drinks with concerning amounts of caffeine. There's an empty spot where the last energry drink was. Loud, overlapping conversations echo in the hallway from the west, the cafeteria. The hallway continues to the east."
vendingMachine.room_text["vendingMachine"] = "You walk down the hallway. You stand next to a vending machine, a big metal box up against the cold brick wall of the hallway. It's filled with candy, chip bags, and drinks with concerning amounts of caffeine. Loud, overlapping conversations echo in the hallway from the west, the cafeteria. The hallway continues to the east. "


cafEntrance = Room()
cafEntrance.allowed_movements.extend(["east","west"])
cafEntrance.after_text = "You are in very large, very noisy lunchroom. Groups of circular tables crowd the place, each packed with kids eating, talking, and laughing. To the west you can see a set of double doors leading outside, a blessed exit."
cafEntrance.initial_text = "You are in very large, very noisy lunchroom. Groups of circular tables crowd the place, each packed with kids eating, talking, and laughing. To the west you can see a set of double doors leading outside, a blessed exit."
#EXIT = pass #we'll deal with that later

laptopKid = ObstacleRoom() # figure the mechanics of this out
laptopKid.room_text["none"] = "You are next to the boy with the laptop. South is the locked set of doors that lead to the glorious outside. To the east, you see an especially judgmental-looking group of teenagers surrounding a table, sporting name-brand shoes, backpacks, and... pencils? I didn't even know they sold those."
laptopKid.room_text["laptopKid"] = "You walk towards the boy with the laptop, and with a closer view, you can see a pale, sickly skinned boy. His bloodshot eyes are lit up by the screen of his laptop. To the east, you see an especially judgmental-looking group of teenagers surrounding a table, sporting name-brand shoes, backpacks, and... pencils? I didn't even know they sold those."
laptopKid.usable_item = "energy drink"
laptopKid.allowed_commands.extend(["use","talk"])
laptopKid.allowed_movements.extend(["east","south"])
laptopKid.obstacle = "laptopKid"
laptopKid.speech["laptopKid"] = '''You try to ask him about the locked door, but he interrupts you. "I'm running on sleep hours of 3 from night last" he says, delirious. "But I have to stay awake until the semifinals end. I need a pick me up. Find me something, then we'll talk."'''
laptopKid.speech["none"] = '''You ask again about the locked door. "Oh, yeah, that's totally normal." He says, eyes never leaving the screen. "They lock them all the time. WHAT? That's a total foul!" He shouts at the laptop, then recomposes himself. "You can try to guess the access code, but it's always some really obscure phras- ARE YOU KIDDING ME? Where did they get this ref? Oh, but I think I did see one of the teachers, Mr. Perison, drop some piece of paper or something after he walked away from the door. It fell under the popular kids' table, so there's pretty much no hope for that. Maybe you can tell them please," he laughs.'''

kidsTable = ObjectRoom()
kidsTable.allowed_movements.append("west")
kidsTable.allowed_commands.append("talk")
kidsTable.room_item = "note"
kidsTable.room_text["note"] = "You are right next to the group of kids. Being so close to them makes you feel incredibly nervous. Your legs stiffen. You realize your shoes are untied, and that your socks are mismatched. The room starts to feel hotter, and one of the kids glances your way. You quickly look down at the floor, and see something under their table."
kidsTable.room_text["none"] = "You are right next to the group of kids. Being so close to them makes you feel incredibly nervous. Your legs stiffen. You realize your shoes are untied, and that your socks are mismatched. The room starts to feel hotter, and one of the kids glances your way. You quickly look down at the floor."
kidsTable.new_action = "grab"

englishClass = ObjectRoom()
englishClass.allowed_movements.append("south")
englishClass.allowed_commands.append("grab")
englishClass.room_item = "hamlet"
englishClass.room_text["hamlet"] = "You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."
englishClass.room_text["none"] = "You are in classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them."

hallwayTheater = ObstacleRoom()
hallwayTheater.allowed_movements.append("west")
hallwayTheater.allowed_commands.append("use")
hallwayTheater.new_direction = "east" #FIGURE THE MECHANICS OF THIS OUT
hallwayTheater.usable_item = "hamlet"
hallwayTheater.obstacle = "theaterKid"
hallwayTheater.room_text["theaterKid"] = '''You are next to a set of double doors. You can hear instruments playing from behind the door. \nA boy in bizarre clothing blocks your way to the entrance. \nHe exclaims: "To be, or not to be, that is the question." \nYou stare at him blankly. \n"It's Shakespeare," he says, exasperated. "You have to finish the line."'''
hallwayTheater.room_text["none"] = "You are in the hallway. To the east there is a set of double doors. You can hear instruments playing from behind the door. The boy in strange clothing paces around the hallway, practicing lines for an obscure play."

theaterRoom = Room()
theaterRoom.allowed_movements.extend(["west","north"])
theaterRoom.initial_text = "You enter a large room full of students. On your side of the room, music is playing loudly, and people are singing along, standing in rows. Music sheets litter the floor under the stands that should be holding them. A few people glance your way, but continue their rehearsal. To the north, you can see chairs, and people playing instruments on the other side. You can see a box of snacks on the other side of the room as well."
theaterRoom.after_text = "You are in the entrance of the theater room. On your side of the room, music is playing loudly, and people are singing along, standing in rows. Music sheets litter the floor under the stands that should be holding them. A few people glance your way, but continue their rehearsal. To the north, you can see chairs, and people playing instruments on the other side. You can see a box of snacks on the other side of the room as well."

goldfishBox = ObjectRoom()
goldfishBox.allowed_movements.append("south")
goldfishBox.allowed_commands.append("grab")
goldfishBox.room_item = "goldfish"
goldfishBox.room_text["goldfish"] = 'You make you way to the back of the rows through the rehearsing singers, trying not to bump into anyone. A couple of them give you dirty looks for disturbing their performance, and you immediately remember why dropped theater in the 7th grade. The chairs, instruments and box of snacks are now right next to you. The box lays on top of a table. A handwritten note on the box reads "Congrats on opening night!"'
goldfishBox.room_text["none"] = 'You are in the back of the room, after weaving through the rehearsing singers and trying not to bump into anyone. The ones that gave you dirty looks for disturbing their performance glare back at you occasionally. The chairs and instruments are now right next to you. The box of snacks you rummaged through for the Goldfish lays on top of a table. Despite the temptation, you decide it would be best to refrain from taking another.'

lockedDoors = Exit()
lockedDoors.room_text["passcode"] = "You are next to the doors. You try to open them, but they don't budge. Locked. A closer look and you see a keypad next to the handle. The keypad has every letter of the alphabet. You mutter under your breath. Looking around, you spot to the north someone sitting alone in the corner of the cafeteria, eyes glued to the screen of the laptop sitting on his legs. Maybe he can help."
lockedDoors.room_text["none"] = "You are next to the unlocked doors."
lockedDoors.obstacle = "passcode"
lockedDoors.password = "brown sugar boba"
lockedDoors.allowed_movements.extend({"north","east"})
lockedDoors.allowed_commands.append("use")
lockedDoors.new_direction = "west"

ENDING = END()
#ENDING.text = "You step outside onto the grass and feel the Sun's warm rays hit your face.\n\nCongrats! You made it out!"


#******************** relevant dictionaries/functions

#calls the text for when an object is taken
object_taken_text = {"hamlet": "You grab the book. The cover reads Hamlet.",
					"dollar": "You take the dollar, fold it up, and place it in your pocket.",
					"goldfish": "You dig your hand into the box of snacks and pull out a bag of Special Edition Disney Princess Goldfish. Your favorite.",
					"note": "You climb under the table and find a sticky note with some writing on it."}
#calls the text for when an object is used
object_used_text = {"hamlet": "You pull out Hamlet, open the book, and read:\n'To be, or not to be, that is the question:\nWhether 'tis nobler in the mind to suffer\nThe slings and arrows of outrageous fortune,\nOr to take arms against a sea of troubles\nAnd by opposing end them.'\nThe boy's eyes well with tears, he nods, and steps aside from the door.",
					"dollar": "You pull out the dollar bill and put it into the vending machine. It whirs, then drops out an energy drink can. You take it.",
					"goldfish": "You pull out a the bag of Disney Princess Edition Goldfish and hand it to the boy. A sigh escapes your lips. The boy gratefully accepts the goldfish, and gives you a dollar bill as a token of appreciation.",
					"energy drink": "You offer the energy drink, and the boy gratefully takes the can. He pops it open and chugs it down within seconds. He looks ready to talk."}

note_contents = '''You look at what's on the note, and realize it's a poem:

	a delicious drink
	color of earth
	taste of its bounty
	sugarcane, tapioca, tea leaves
	work in harmony
	and strike a balance
	unrivaled.

	three is key:
	color is first
	sweetness is second
	bubbly component last
	(if you can't remember, go to the beginning)'''

#initalizes player position (x,y,z)/(-north/+south,-west/+east,-down/+up) at the origin, math class
playerPosition = [0,0,0]
inventory = []

potential_inputs = ["save", "load", "grab", "use", "talk", "look", "examine", "help", "inventory", "north", "south", "west", "east"]
potential_movements = ["north","south", "west", "east"]
potential_commands = ["grab", "use", "talk", "look", "examine", "help", "inventory"]
help_text = "Potential movements: north, south, west, east. Potential commands:\ngrab - take an object \nuse - use an item in your inventory\ntalk - speak with people in the room you are in\nlook - room description is displayed again\nexamine - take a closer look at a special object\nhelp - displays this text again\ninventory - displays current inventory\n\nType 'quit' to end the game. Type the direction you want to move or action you want to perform, and nothing else. For example, if you see something that you want to take, simply type 'grab'. In any given room, you will be given a set of potential directions you can go."



print(help_text)
print("Press 'Enter' to continue.")


def save():
	with open('game.dat','wb') as f:
		pickle.dump(Room,f)
	print("\nGame saved!\n")

def load():
	global Room
	try:
		with open("game.dat",'rb') as f:
			Room = pickle.load(f)
		print("\nGame loaded!\n")
	except FileNotFoundError:
		print("\nGame file not found!\n")


def move(direction): #this function doesn't need further restrictions, because the only time it is called is after it passes certain resrictions
	if direction == "west":
		playerPosition[1] += -1
	elif direction == "east":
		playerPosition[1] += 1
	elif direction == "north":
		playerPosition[0] += -1
	elif direction == "south":
		playerPosition[0] += 1
	elif direction == "down":
		playerPosition[2] += -1
	elif direction == "up":
		playerPosition[2] += 1
	else:
		print("I'm not sure how you managed to put that argurment into my movement function, but you totally broke my code.")
	return playerPosition


def command(action): #this fucntion doesn't need further restrictions, because the only time it is called is after it passes certain resrictions
	if action == "grab":
		if current_room.room_item:
			inventory.append(str(current_room.room_item))
			print(f"\n{object_taken_text[current_room.room_item]}\n")
			del current_room.room_item
		else:
			print("\nYou can't do that right now.\n")
		
		
	elif action == "use":
		if current_room.__class__.__name__ == "Exit":
				guess = input("You take a look at the keypad, and punch in the passcode:\n").lower()
				current_room.unlock_attempt(guess)
		elif current_room.__class__.__name__ == "ObstacleRoom": 
			try:
				if current_room.usable_item in inventory:
					print(f"\n{object_used_text[current_room.usable_item]}\n")
					inventory.remove(current_room.usable_item)
					del current_room.usable_item
					if current_room.new_direction:
						current_room.allowed_movements.append(current_room.new_direction)
					if current_room.item_received:
						inventory.append(str(current_room.item_received))
						del current_room.item_received
					del current_room.obstacle
				else:
					print("\nYou can't do that right now.\n")

			except AttributeError:
				print("\nYou can't do that right now.\n")

		else:
			print("You don't have anything you can use here.")
	
	elif action == "talk":
		if tuple(playerPosition) == (0,-4,0):
			current_room.convo()
		elif tuple(playerPosition) == (0,-5,0):
			try:
				print(f"\n{current_room.speech[current_room.obstacle]}\n")
			except KeyError and AttributeError:
				print(f"\n{current_room.speech['none']}\n")
		else:
			print("You can't do that right now.")

callRoom = {(0,0,0): mathClass,
			(1,0,0): desolateHallway,
			(1,-1,0): goldfishKid,
			(1,-2,0): hallwayEnglish,
			(0,-2,0): englishClass,
			(1,-3,0): vendingMachine,
			(1,-4,0): cafEntrance,
			(0,-4,0): kidsTable,
			(1,-5,0): lockedDoors,
			(1,-6,0): ENDING,
			(0,-5,0): laptopKid,
			(1,1,0): hallwayTheater,
			(1,2,0): theaterRoom,
			(0,2,0): goldfishBox
			}

#**************************** the main game loop
quitGame = False
last_direction = None
response = input()
while quitGame == False: #could be a quit variable
	#get current position variables
	current_room = callRoom[tuple(playerPosition)]
	current_room_check = current_room
	
	if current_room.__class__.__name__ == "Room":
		current_room.count += 1
		current_room.text_decision()
	elif current_room.__class__.__name__ == "END":
		current_room.conclusion()
	else:
		current_room.text_decision()
	
	while current_room_check == current_room:
		response = input().lower().strip()
		if response in potential_inputs:
			if response in potential_movements:
				if response in current_room.allowed_movements:
					move(response)
					break
				else:
					print("\nYou can't go that way, you silly goose.\n")
				
			
			if response in potential_commands:
				if response in current_room.allowed_commands:
					command(response)
				elif response == "inventory":
					print(f"\n{inventory}\n")
				elif response == "help":
					print(f"\n{help_text}\n")
				elif response == "look":
					current_room.text_decision()
				elif response == "examine":
					if 'note' in inventory:
						print(note_contents)
					else:
						print("\nYou can't do that right now.\n")
				
				else:
					print("\nYou can't do that right now.\n")

			elif response == "save":
				save()
								
			elif response == "load":
				load()

			elif response == "quit":
				confirmation = input("Are you sure you want to quit the game? You'll have to restart. (yes/no):\n")
				if confirmation.lower() == "yes":
					quitGame = 1
					quit()
		else:
			print("\nI don't know what you mean. Type 'help' to see what you can do.\n")
	
			
		
