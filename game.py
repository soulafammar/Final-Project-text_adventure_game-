print("hello")
print("this is where the intro text will go")
inventory = []
def commandMenu():
	print("grab/take\nuse\nhint?\ntalk\nlook closer?")
def directions():
	print("up\ndown\nnorth\nsouth\nwest\neast")

#initalizes player position (x,y,z)/(+north/-south,east/west,up) at the origin, math class
playerPosition = [0,0,0]
standInVar = 0
commandMenu()
print("...")
print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
while standInVar == 0:
	if playerPosition == [0,0,0]:
		print("Your eyelids flutter open, and you wake up from a dream about brown sugar boba (dream is important later) and find yourself in your math class. Forgetting the pleasures of your dream, you take in your surroundings: exhausted 17 year-olds, graphing calculators, papers spread out on uneven desks. Your teacher is droning on about logarithms and their properties. The buzz of the fluorescent ceiling lights is ceaseless. You look towards the door longingly. Your friend sitting besides you catches your glance, and gives you a sympathetic smile. You look back at your teacher and ask to use the restroom. She nods, continuing to describe the change of base properties of both natural and common log.")
	elif playerPosition == [1,0,0]:
		print("You find yourself in a desolate hallway. The overhead lights make the same buzzing sound you've become so accustomed to in math class. There's a faint sound of people conversing to the west, and music playing to the east.")
	elif playerPosition == [1,-1,0]:
		print("You walk down the hallway. The sound of voices overlapping each other gets louder and louder. i think this is where the hungry kid is.")