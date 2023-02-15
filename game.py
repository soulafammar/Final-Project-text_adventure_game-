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
if movement = "west":
	playerPosition[1] += -1
elif movement = "east":
	playerPosition[1] += 1
elif movement = "north":
	playerPosition[0] += -1
elif movement = "south":
	playerPosition[0] += 1
elif movement = "down":
	playerPosition[2] += -1
elif movement = "up":
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


	
while standInVar == 0:
	if playerPosition == [0,0,0]:
		print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
	elif playerPosition == [1,0,0]:
		print("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")
	elif playerPosition == [1,-1,0]:
		print("You walk down the hallway. The sound of voices overlapping each other gets louder and louder. i think this is where the hungry kid is.")