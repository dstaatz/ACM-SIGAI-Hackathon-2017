import json
from Scrambler import Scrambler
from Cube import Cube2x2
import time

creature = {}
for i in range(10):
	with open("C:\\Users\\Dylan Staatz\\Desktop\\Python\\Rubiks_Solver\\first_side\\PerfectMoveSet" + str(i) + ".json", "r") as f:
		stringThing = f.read()
		dct = json.loads(stringThing)
		for key, value in dct.items():
			creature[key] = value

				

start = time.time()
count = 0
total = 1
numberOfMoves = 0
for n in range(total):
	scramble = Scrambler.scramble(2)
	cube = Cube2x2(scramble=scramble)
	bestColor = cube.colorWithMostSolved()[1]
	positions = cube.colorPositions(bestColor)
	localCount = 0
	[print(i, end=' ') for i in scramble]
	print()
	for move in creature[positions]:
		cube.move(move)
		localCount += 1
		if(cube.colorWithMostSolved()[2] == 4 ):
			numberOfMoves += localCount
			count += 1
			break
	# if(cube.colorWithMostSolved()[1] != "G"):
		# [print(i, end=' ') for i in scramble]
		# print()
		# print(positions, "=", creature[positions])
		# print(cube.colorWithMostSolved())
		# cube.printCube()
		# print(count)
		# input()


end = time.time()
print("Successful:", count)
print("Total Tested:", total)
print("Avg number of moves:", numberOfMoves/total)
print("Total Time:", end-start)
print("Avg time:", (end-start)/total)

[print(i, end=' ') for i in cube.currentMoveSet]
print()