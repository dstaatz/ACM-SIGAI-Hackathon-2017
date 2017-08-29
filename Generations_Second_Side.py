import json
from Scrambler import Scrambler
from Cube import Cube2x2
import time

start = time.time()
# Load Creature into dictionary creature_1
creature_1 = {}
for i in range(10):
	with open("C:\\Users\\Dylan Staatz\\Desktop\\Python\\Rubiks_Solver\\first_side\\PerfectMoveSet" + str(i) + ".json", "r") as f:
		stringThing = f.read()
		dct = json.loads(stringThing)
		for key, value in dct.items():
			creature_1[key] = value

			

runs = 9999
allPositions = {}
for i in range(runs):
	scramble = Scrambler.scramble(2)
	cube = Cube2x2(scramble=scramble)
	positions = cube.colorPositions(cube.colorWithMostSolved()[1])
	for move in creature_1[positions]:
		cube.move(move)
		if(cube.colorWithMostSolved()[2] == 4 ):
			firstSide = cube.colorWithMostSolved()[0]
			firstColor = cube.colorWithMostSolved()[1]
			break
	oppositeSide = cube.oppositeFaces[firstSide]
	oppositeColor = cube.oppositeColors[firstColor]
	
	# move to bottom
	if(firstSide != "D"):
		if (firstSide == "U"):
			cube.move("R2")
			cube.move("L2")
		if (firstSide == "F"):
			cube.move("R'")
			cube.move("L")
		if (firstSide == "B"):
			cube.move("R")
			cube.move("L'")
		if (firstSide == "R"):
			cube.move("F")
			cube.move("B'")
		if (firstSide == "L"):
			cube.move("F'")
			cube.move("B")
	
	secondPositions = cube.colorPositions(oppositeColor)
	
	if (secondPositions not in allPositions):
		allPositions[secondPositions] = cube.currentMoveSet
	if(len(allPositions) == 27):
		break

		
		
print(len(allPositions))
time = time.time() - start
print(time)
	
	