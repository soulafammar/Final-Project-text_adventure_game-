rooms = {(0,0,0):["Math Class",[],[], ("south"), (), "math class text"],
		(0,-2,0):["English Class",["hamlet"], [], ("south"), ("grab"), "You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."],
		"hiddenRoom":["Hidden Room",["key"], [], ("west"), ("grab"), "hidden room text"],
		(1,0,0):["Hallway outside math class",[], [], ("north","west","east"), (), "You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east."],
		(1,-1,0):["Goldfish Kid",[], ["goldfish kid"],("west","east"), ("use"), "You walk down the hallway. The sound of voices overlapping each other gets louder and louder. goldfish kid here."],
		(1,-2,0):[[],("west","east","north"),"suddenly you here noise from ANOTHER direction, north, see a door way to english class,"],
		(1,-3,0):[["vending machine soda"],("west","east"), "here is the vending machine spot"],
		(1,-4,0):[["escape door"],("north","east"),"south side of cafeteria"],
		(0,-4,0):[["fairy tales book"],("south"),"were are in the cafeteria, theres popular kids table, and a kid playing video games"]}

print("this is where the intro text will go. Potential commands: grab, use, talk, look, examine, help. Potential movements: up, down, north, south, west, east. ")


class Room():
	def __init__(self):
		self.allowed_commands = []
		self.allowed_movements = []
		self.initial_text = []
		self.after_text = []
		self.count = 0

class ObjectRoom(Room):
	def __init__(self):
		super().__init__()
		self.room_text = {}
		self.usable_item = {}

	room_item = ""

	def text_decision(self):
		try:
			print(self.room_text[self.room_item])
			print(f"Possible exits: {self.allowed_movements}")
		except KeyError:
			print(self.room_text["none"])
			print(f"Possible exits: {self.allowed_movements}")

		#if len(self.room_items) == 0:
		#	print(self.room_text["none"])
		#else: #len(room_items) > 1:
		#	for i in range(len(self.room_items)):
		#		thing = ""
		#		thing += str(self.room_items[i])
		#		print(thing)
		#	print(self.room_text[thing])

	def new(attempt):
		pass

class ObstacleRoom(Room):
	def __init__(self):
		super().__init__()
		self.room_item = ""
		self.room_text = {}
		self.usable_item = {}
		self.obstacle = ""

	def text_decision(self):
		try:
			print(self.room_text[self.obstacle])
			print(f"Possible exits: {self.allowed_movements}")
		except KeyError:
			print(self.room_text["none"])
			print(f"Possible exits: {self.allowed_movements}")

	
#************************new code
mathClass = Room()
mathClass.initial_text.append("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
mathClass.after_text.append("You are back in math class. You take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. You vaguely remember a dream about your favorite bubbly drink.")
mathClass.allowed_movements.append("south")

desolateHallway = Room()
desolateHallway.allowed_movements.extend(["east","west","north"])
desolateHallway.initial_text.append("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")
desolateHallway.after_text.append("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")

goldfishKid = ObstacleRoom() #obstacle room - create new child class
goldfishKid.allowed_movements.extend(["east","west"])
goldfishKid.allowed_commands.append("use")
goldfishKid.usable_item["goldfish"] = "You pull out a the bag of Disney Princess Edition Goldfish and hand it to the boy. A sigh escapes your lips.The boy gratefully accepts the goldfish, and gives you a dollar bill as a token of appreciation."
goldfishKid.obstacle = "hungryKid"
goldfishKid.room_item = "dollar"
goldfishKid.room_text["hungryKid"] = "this is where the kid who wants a snack is"
goldfishKid.room_text['none'] = "no one here, just a hallway"


hallwayEnglish = Room()
hallwayEnglish.allowed_movements.extend(["east","west","north"])
hallwayEnglish.initial_text.append("suddenly you here noise from ANOTHER direction, north, see a door way to english class,")
hallwayEnglish.after_text.append("suddenly you here noise from ANOTHER direction, north, see a door way to english class,")

vendingMachine = ObstacleRoom() #obstacle room
vendingMachine.allowed_movements.extend(["east","west"])
vendingMachine.allowed_commands.append("use")
vendingMachine.room_item = "energy drink"
vendingMachine.usable_item["dollar"] = "You pull out the dollar bill and put it into the vending machine. It whirs, then drops out an energy drink can."

cafEntrance = Room()
cafEntrance.allowed_movements.extend(["north","east","west"])
cafEntrance.after_text.append("You are in very large, very noisy lunchroom. Groups of circular tables crowd the place, each packed with kids eating, talking, and laughing. To the north, you see an especially judgmental-looking group of teenagers surrounding a table, sporting name-brand shoes, backpacks, and... pencils? I didn't even know they sold those. To the west you can see a set of double doors leading outside, a blessed exit.")
cafEntrance.initial_text.append("You are in very large, very noisy lunchroom. Groups of circular tables crowd the place, each packed with kids eating, talking, and laughing. To the north, you see an especially judgmental-looking group of teenagers surrounding a table, sporting name-brand shoes, backpacks, and... pencils? I didn't even know they sold those. To the west you can see a set of double doors leading outside, a blessed exit.")
#EXIT = pass #we'll deal with that later

laptopKid = ObjectRoom()


englishClass = ObjectRoom()
englishClass.allowed_movements.append("south")
englishClass.allowed_commands.append("grab")
englishClass.room_item = "hamlet"
#englishClass.room_items["hamlet"] = "You grab the book. The cover reads Hamlet"
englishClass.room_text['hamlet'] = "You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."
englishClass.room_text["none"] = "You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them."

#theaterRoom =


#nevermind i don't need this
#hallwayTheater = ObjectRoom()
#hallwayTheater.allowed_movements.append("east","west") #add north/ up once the player has talked to the gamer or has the fairy tale book
#hallwayTheater.allowed_commands.append("use")
#hallwayTheater.room_text[theaterKid] = 


#********************
#CREATE A FUNCTION THAT TAKES PLAYER LOCATION AND GIVES ROOM NAME TO USE TO CALL DESCRIPTION, OBJECT , ETC
#calls the text for when an object is taken
object_taken_text = {"hamlet": "You grab the book. The cover reads Hamlet",
				"dollar": "You take the dollar, fold it up, and place it in your pocket."}




#initalizes player position (x,y,z)/(-north/+south,-west/+east,-down/+up) at the origin, math class
playerPosition = [0,0,0]
inventory = []

potential_inputs = ["grab", "use", "talk", "look", "examine", "help", "inventory", "up", "down", "north", "south", "west", "east"]
potential_movements = ["up","down","north","south", "west", "east"]
potential_commands = ["grab", "use", "talk", "look", "examine", "help", "inventory"]
help_text = "Potential commands: grab, use, talk, look, examine, help. Potential movements: up, down, north, south, west, east."

print("...")

def move(direction): #this fucntion doesn't need further restrictions, because the only time it is called is after it passes certain resrictions
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
		inventory.append(str(current_room.room_item))
		print(object_taken_text[current_room.room_item])
		del current_room.room_item
		
	elif action == "use":
		if current_room.usable_item in inventory:
			print(dict.values(current_room.usable_item))
			del current_room.usable_item
			inventory.remove(current_room.usable_item)
		else:
			print("You don't have anything you can use here.")

	elif action == "look":
		text_decision
		if current_room.__class__.__name__ == "Room":
			print(current_room.initial_text)
		else:
			print(current_room.room_text[room_item])
	#elif action == "examine":
	#	#display hidden flavor text
	elif action == "help":
		print(help_text)
	
	elif action == "inventory":
		print(inventory)
	#elif action == "talk":
	#	#display hidden dialogue text for certain character

callRoom = {(0,0,0): mathClass,
			(1,0,0): desolateHallway,
			(1,-1,0): goldfishKid,
			(1,-2,0): hallwayEnglish,
			(0,-2,0): englishClass,
			(1,-3,0): vendingMachine,
			(1,-4,0): cafEntrance,
			#[0,-4,0]: kidsTable,
			#[1,-5,0]: EXIT,
			#[0,-5,0]: laptopKid,
			#[1,1,0]: hallwayTheater,
			#[1,2,0]: theaterRoom,
			#[0,2,0]: goldfishBox
			}


quitGame = 0
#THIS IS THE MAIN WHILE LOOP THAT DECIDES WHAT TO DO WITH PLAYER RESPONSES
last_direction = None
response = input()
while quitGame == False: #could be a quit variable
	#get current position variables
	current_room = callRoom[tuple(playerPosition)]
	current_room_check = current_room
	if current_room.__class__.__name__ == "Room":
		if current_room.count < 1:
			print(current_room.initial_text)
			current_room.count += 1
		else:
			print(current_room.after_text)
		
	elif current_room.__class__.__name__ == "ObjectRoom":
		current_room.text_decision()

	#elif current_room.__class__.__name__ == "ObjectRoom":
		#print(current_room.room_text[current_room.room_item])
	elif current_room.__class__.__name__ == "ObstacleRoom":
		current_room.text_decision()
		
		#print(current_room.room_text[current_room.obstacle[0]])
	#else:
		#text_decision = 
	#	print(current_room.room_text[current_room.obstacle[0]])
	
	print(f"\nPossible exits: {current_room.allowed_movements}")
	while current_room_check == current_room:
		response = input().lower()
		if response in potential_inputs:
			if response in potential_movements:
				if response in current_room.allowed_movements:
					move(response)
					#last_direction = response
					break
				else:
					print("You can't go that way, you silly goose.")
				
			
			if response in potential_commands:
				if response in current_room.allowed_commands:
					command(response)
				elif response == "inventory":
					print(inventory)
				elif response == "help":
					print(help_text)
				elif response == "look":
						if current_room.__class__.__name__ == "Room":
							print(current_room.initial_text)
						elif current_room.__class__.__name__ == "ObstacleRoom":
							current_room.text_decision()
							#print(current_room.room_text[current_room.obstacle[0]])
						else:
							current_room.text_decision()
							#print(current_room.room_text[current_room.room_item])
						
				else:
					print("You can't do that right now.")
		else:
			print("I don't know what you mean. Type 'help' to see what you can do.")
	
			
		if response == "quit":
			confirmation = input("Are you sure you want to quit the game? You'll have to restart. (yes/no)")
			if confirmation.lower == "yes":
				quitGame = 1
