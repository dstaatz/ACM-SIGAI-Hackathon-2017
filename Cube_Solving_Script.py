from Cube import Cube2x2
from Scrambler import Scrambler
import random
#from Algorithms import Algorithms

scramble = Scrambler.scramble(2)
cube = Cube2x2(scramble=['L', 'U2', 'F', 'R2', "U'", "D'", "B'", 'F', "B'", 'F2'])
print(['L', 'U2', 'F', 'R2', "U'", "D'", "B'", 'F', "B'", 'F2'])
cube.printCube()
print("-----------------------------------------")
solution = []

#solve one side to at least have two together
for i in cube.faces:
	cube.move(i)
	if(cube.colorWithMostSolved()[2] > 1):
		solution.append(i)
		break
	else:
		cube.move(i + "'")
print(solution)
while(cube.colorWithMostSolved()[2] ==  1):
	cube.move(cube.faces[random.randrange(6)])
cube.printCube()
print("-----------------------------------------")


# solve one side to have at least three on one side
info = cube.colorWithMostSolved()
print(info)
firstColor = info[1]

# rotates most solved side to the bottom
if(info[0] != "D"):
	if(info[0] == "U"):
		solution.append("R2")
		cube.move("R2")
		solution.append("L2")
		cube.move("L2")
	elif(info[0] == "R"):
		solution.append("F")
		cube.move("F")
		solution.append("B'")
		cube.move("B'")
	elif(info[0] == "L"):
		solution.append("F'")
		cube.move("F'")
		solution.append("B")
		cube.move("B")
	elif(info[0] == "F"):
		solution.append("R'")
		cube.move("R'")
		solution.append("L")
		cube.move("L")
	elif(info[0] == "B"):
		solution.append("R")
		cube.move("R")
		solution.append("L'")
		cube.move("L'")

print(solution)
cube.printCube()

# find the spots left open on the bottom
openSpots = [i for i,piece in enumerate(cube.data["D"]) if (piece != firstColor)]
for spot in openSpots:
	# find a piece in top layer
	breakNow = False
	for side in cube.faces:
		if(side != "U"):
			for i,piece in enumerate(cube.data[side][0:1]):
				if(piece == firstColor):
					position = (side, i)
					breakNow = True
					break
		else:
			for i,piece in enumerate(cube.data[side]):
				if(piece == firstColor):
					position = (side, i)
					breakNow = True
					break
		if(breakNow):
			break
	#rotate top layer to above a spot
	print(position)
	
	
				
				
				