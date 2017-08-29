import random
from Cube import Cube2x2
from Scrambler import Scrambler
import time
import json

timer = time.time()
random.seed(1)
POSSIBLE_NUMBER_OF_KEYS = 5670


############################################################################################################################
runs = 99999
scramble = Scrambler.scramble(2)
cube = Cube2x2(scramble=scramble)
dct = {cube.colorPositions("G") : scramble}
while True:
	scramble = Scrambler.scramble(2)
	cube = Cube2x2(scramble=scramble)
	colorThing = cube.colorPositions("G")
	if (colorThing not in dct):
		dct[colorThing] = scramble
	if(len(dct) >= POSSIBLE_NUMBER_OF_KEYS):
		break

print(time.time() - timer)
timer = time.time()
############################################################################################################################


moves = "F","R","U","B","L","D","F'","R'","U'","B'","L'","D'","F2","R2","U2","B2","L2","D2"
GENERATIONS = 1000
CREATURES_PER_GENERATION = 100
TEST_PER_CREATURE = 100
CREATURE_MOVESET_LENGTH = 5

			
moveSet = {}
for key in dct:
	moveSet[key] = [moves[random.randrange(18)] for n in range(10)]

for i in range(1,10):
	# test for one key to randomly get better
	output = {}
	start = i * 567
	overallCount = start
	for testKey in sorted(dct)[start:start + 567]:
		#CREATURE_MOVESET_LENGTH = 5
		testCount = 1
		while True:
			cube = Cube2x2(scramble=dct[testKey])
			count = 0
			for move in moveSet[testKey]:
				cube.move(move)
				temp = cube.colorWithMostSolved()
				if (temp[1] == "G"):
					if (temp[2] == 4):
						break
				count += 1
				if(count >= CREATURE_MOVESET_LENGTH):
					break
			currentScore = count

			cube = Cube2x2(scramble=dct[testKey])
			count = 0
			randomMoveSet = [moves[random.randrange(18)] for n in range(CREATURE_MOVESET_LENGTH)]
			for move in randomMoveSet:
				cube.move(move)
				temp = cube.colorWithMostSolved()
				if (temp[1] == "G"):
					if (temp[2] == 4):
						break
				count += 1
			newScore = count
			if(newScore < currentScore):
				moveSet[testKey] = randomMoveSet
				output[testKey] = randomMoveSet
				overallCount += 1
				print(i, testKey, testCount, (overallCount/POSSIBLE_NUMBER_OF_KEYS)*100, time.time() - timer, output[testKey])
				break
			testCount += 1
			if(testCount == 200000):
				works = False
				while True:
					print("Having trouble with this one")
					print("Scramble =", dct[testKey])
					print("Position =", testKey)
					userIn = input("Enter in a Solution: ")
					moveSet[testKey] = userIn.split(",")
					print(moveSet[testKey])
					cube = Cube2x2(scramble=dct[testKey])
					for move in moveSet[testKey]:
						cube.move(move)
						temp = cube.colorWithMostSolved()
						if (temp[1] == "G"):
							if (temp[2] == 4):
								works = True
								break
					if(works):
						print("That works!")
						output[testKey] = moveSet[testKey]
						overallCount += 1
						print(i, testKey, testCount, (overallCount/POSSIBLE_NUMBER_OF_KEYS)*100, time.time() - timer, output[testKey])
						break
				if(works):
					break
			elif(testCount == 100000):
				print("CREATURE_MOVESET_LENGTH has been changed to 10 for this creature")
				CREATURE_MOVESET_LENGTH = 10
			elif(testCount == 10000):
				print("CREATURE_MOVESET_LENGTH has been changed to 8 for this creature")
				CREATURE_MOVESET_LENGTH = 8
			elif(testCount == 2500):
				print("CREATURE_MOVESET_LENGTH has been changed to 7 for this creature")
				CREATURE_MOVESET_LENGTH = 7
			elif(testCount == 1000):
				print("CREATURE_MOVESET_LENGTH has been changed to 6 for this creature")
				CREATURE_MOVESET_LENGTH = 6
				

	with open("PerfectMoveSet" + str(i) + ".json", 'w') as f:
		f.write(json.dumps(output))
	print("Batch of 567 have been saved to a new .json file")
		
print(time.time() - timer)


