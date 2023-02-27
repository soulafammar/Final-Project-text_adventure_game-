print("hello")
print("this is where the intro text will go")
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


#location of room -> [[items],(allowed_movements),"description"]
#dictionary of all the rooms
rooms = {[0,0,0]:[[],("south"), "math class text"]
		[0,-2,0]:[["hamlet"],("south"),"You enter a classroom full of chattering students. Each student has a laptop open and a copy of the same pale yellow book in hand, discussing it with the others next to them. An abandoned copy lies on a desk in front of you."],
		"hiddenRoom":[["key"],("west"), "hidden room text"]
		[1,0,0]:[[],("north","west","east"), "You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east."]
		[1,-1,0]:[[],("west","east"),"You walk down the hallway. The sound of voices overlapping each other gets louder and louder. goldfish kid here."]
		[1,-2,0]:[[],("west","east","north"),"suddenly you here noise from ANOTHER direction, north, see a door way to english class,"]
		[1,-3,0]:[["vending machine soda"],("west","east"), "here is the vending machine spot"]
		[1,-4,0]:[["escape door"],("north","east"),"south side of cafeteria"]
		[0,-4,0]:[["fairy tales book"],("south"),"were are in the cafeteria, theres popular kids table, and a kid playing video games"]}
#should i add an obstacles element to the list?

	
while standInVar == 0:
	#get current position variables
	items, allowed_movements, description = [tuple(playerPosition)]:
	print(description)
	if input() in allowed_movements:
		move() CREATE THIS FUNCTION
	#get player input
	#if player input in allowed_move
		#move())))))))))))))))))))))))
	#elif player input in allowed command
		#action()
	#else
		#doesn't work in this room
	
	
	
	
	if playerPosition == [0,0,0]:
		print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
	elif playerPosition == [1,0,0]:
		print("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")
	elif playerPosition == [1,-1,0]:
		print("You walk down the hallway. The sound of voices overlapping each other gets louder and louder. i think this is where the hungry kid is.")

