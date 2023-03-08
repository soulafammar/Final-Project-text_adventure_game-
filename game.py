print("hello")
print("this is where the intro text will go. You can grab, talk, use, examine. if you forget type 'help' ")
inventory = []
def commandMenu():
	print("grab/take\nuse\nhint?\ntalk\nlook closer?")
def directions():
	print("up\ndown\nnorth\nsouth\nwest\neast")

#initalizes player position (x,y,z)/(-north/+south,-west/+east,-down/+up) at the origin, math class
playerPosition = [0,0,0]

movement = input("Pick the direction to move")
#this if statement checks which direction the player types and moves position accordingly
#DOES NOT CHECK IF MOVEMENT IN DIRECTION IS POSSIBLE IN GAME: needs solution
if movement == "west":
	playerPosition[1] += -1
elif movement == "east":
	playerPosition[1] += 1
elif movement == "north":
	playerPosition[0] += -1
elif movement == "south":
	playerPosition[0] += 1
elif movement == "down":
	playerPosition[2] += -1
elif movement == "up":
	playerPosition[2] += 1

potential_movements = ["up","down","north","south", "east"]
potential_commands = ["grab", "use", "talk", "examine", "help"]

standInVar = 0
commandMenu()
print("...")
print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
#checks playerPosition and displays flavor text accordingly
#should i do it like this:
#if playerPosition == [x,y,z]:
	#roomLocation == Math Class (math class will be a list with items in it)
#OR like this:
#if playerPosition == [x,y,z]:
	#specificRoomFunction(): ---> this room function will display the flavor text, include items, determine which movement directions are possible


#location of room -> ["name of room",[items],[obstacles],(allowed_movements),(allowed_commands),"flavor text"]
#dictionary of all the rooms
rooms = {[0,0,0]:["Math Class",[],[], ("south"), (), "math class text"]
		[0,-2,0]:["English Class",["hamlet"], [], ("grab"), ("south"), "You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."],
		"hiddenRoom":["Hidden Room",["key"], [], ("grab"), ("west"), "hidden room text"]
		[1,0,0]:["Hallway outside math class",[], [], ("north","west","east"), "You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east."]
		[1,-1,0]:["Goldfish Kid",[], ["goldfish kid"]("west","east"), ("use"), "You walk down the hallway. The sound of voices overlapping each other gets louder and louder. goldfish kid here."]
		[1,-2,0]:[[],("west","east","north"),"suddenly you here noise from ANOTHER direction, north, see a door way to english class,"]
		[1,-3,0]:[["vending machine soda"],("west","east"), "here is the vending machine spot"]
		[1,-4,0]:[["escape door"],("north","east"),"south side of cafeteria"]
		[0,-4,0]:[["fairy tales book"],("south"),"were are in the cafeteria, theres popular kids table, and a kid playing video games"]}
#should i add an obstacles element to the list?

def move(direction):
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
		inventory.append(rooms[playerPosition][2])
		#delete from room list
	elif action == "use":
		#get rid of obstacle, display flavor text
		#delete from inventory
	elif action == "look":
		#display flavor text
	elif action == "examine":
		#display hidden flavor text
	elif action == "help":
		#display list of commands and movements/possible exits?
	elif action == "talk":
		#display hidden dialogue text for certain character
#THIS IS THE MAIN WHILE LOOP THAT DECIDES WHAT TO DO WITH PLAYER RESPONSES
response = input()
while standInVar == 0: #could be a quit variable
	#get current position variables
	location_name, items, obstacles, allowed_movements, description = [tuple(playerPosition)]:
	print(description)
	if response.lower() in potential_movements:
		if response.lower() in allowed_movements:
		move(response.lower())
		else:
			print("You can't go that way, you silly goose.")
	elif response.lower() in potential_commands:
		if response.lower() in allowed_commands: #MAKE AN ALLOWED COMMANDS LIST IN MASTER DICTONARY
			command(response.lower())
		else:
			print("You can't do that right now.")
	else:
		print("You can't do that right now.")
	#get player input
	#if player input in allowed_move
		#move())))))))))))))))))))))))
	#elif player input in allowed command
		#action()
	#else
		#doesn't work in this room

#scrap code - keep in case
if playerPosition == [0,0,0]:
	print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
elif playerPosition == [1,0,0]:
	print("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")
elif playerPosition == [1,-1,0]:
	print("You walk down the hallway. The sound of voices overlapping each other gets louder and louder. i think this is where the hungry kid is.")

