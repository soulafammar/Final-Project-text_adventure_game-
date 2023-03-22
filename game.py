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


class Rooms():
	def __init__(self):
		self.allowed_commands = []
		self.allowed_movements = []
		self.room_items = {}
		self.initial_text = []
		


#initalizes player position (x,y,z)/(-north/+south,-west/+east,-down/+up) at the origin, math class
playerPosition = [0,0,0]
inventory = []

potential_movements = ["up","down","north","south", "west", "east"]
potential_commands = ["grab", "use", "talk", "look", "examine", "help"]
help_text = "Potential commands: grab, use, talk, look, examine, help. Potential movements: up, down, north, south, west, east."

print("...")
print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
print(f"Possible exits: {rooms[tuple(playerPosition)][3]}")

#location of room -> ["name of room",[items],[obstacles],(allowed_movements),(allowed_commands),"flavor text"]
#dictionary of all the rooms


#should i do this?
#roomText = {(0,0,0): ["math class text"]
			#(0,-2,0): ["You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."]
			#}
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
		inventory.append(rooms[playerPosition][2])
		#delete from room list
	#elif action == "use":
		#inventory.delete()
		#get rid of obstacle, display flavor text
		#delete from inventory
	elif action == "look":
		print(rooms[playerPosition][5])
	#elif action == "examine":
	#	#display hidden flavor text
	elif action == "help":
		print(help_text)
	#elif action == "talk":
	#	#display hidden dialogue text for certain character




#PROBLEMS:
#the biggest situation currently is the fact that the flavor text of a room stays the same no matter what direction the player
#is coming from, or whether or not an object has already been taken, etc
#solutions?:
#1) create an adition to the dictionary for flavor text that sometimes appears
#2) create a flavor text dictionary within the dictionary for each room
	#have a last movement variable that can be used to choose what type of flavor text
#3) create a brand new flavor text dictionary for each room
	#have a last movement variable that can be used to choose what type of flavor text


quitGame = 0
#THIS IS THE MAIN WHILE LOOP THAT DECIDES WHAT TO DO WITH PLAYER RESPONSES
last_direction = None
response = input()
while quitGame == False: #could be a quit variable
	#get current position variables
	location_name, items, obstacles, allowed_movements, allowed_commands, description = rooms[tuple(playerPosition)]
	#print(description.get(playerPosition, "not valid"))
	try:
		print(description[last_direction]) #calls the specific text for the specific direction/ MUST TURN DIRECTIONS INTO ANOTHER DICTIONARY
	except TypeError:
		print(description)
	
	print(f"\nPossible exits: {allowed_movements}")
	response = input().lower()

	if response in potential_movements:
		if response in allowed_movements:
			move(response)
			last_direction = response
		else:
			print("You can't go that way, you silly goose.")
	
	if response in potential_commands:
		if response in allowed_commands: #MAKE AN ALLOWED COMMANDS LIST IN MASTER DICTONARY
			command(response)
		else:
			print("You can't do that right now.")
	
	if response == "quit":
		confirmation = input("Are you sure you want to quit the game? You'll have to restart. (yes/no)")
		if confirmation.lower == "yes":
			quitGame = 1
