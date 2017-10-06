from Scrambler import Scrambler

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 25)
ORANGE = (255, 128, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
# colorsCharToRGB = {
			# 'W': WHITE,
			# 'R': RED,
			# 'B': BLUE,
			# 'Y': YELLOW,
			# 'O': ORANGE,
			# 'G': GREEN,
			# }
# colorsRGBToChar = {
			# WHITE: 'W',
			# RED: 'R',
			# BLUE: 'B',
			# YELLOW: 'Y',
			# ORANGE: 'O',
			# GREEN: 'G',
			# }
			
class Cube2x2():
	''' 
		Represent a 2x2 Rubiks Cube
	'''
	
	# initalize the cube with the provided scramble
	def __init__(self, colorOptions={"F": "W","R": "R","U": "B","B": "Y","L": "O","D": "G"}, scramble=[]):
		'''	Intialize a new cube
			
			- colorOptions: allows you to set a starting color for each face
			- scramble: allows you to specify a starting scramble for the cube
		'''

		self.colorOptions = colorOptions
		self.scramble = scramble
		self.faces = "F","R","U","B","L","D"
		self.oppositeFaces = {
			"F":"B",
			"R":"L",
			"U":"D",
			"B":"F",
			"L":"R",
			"D":"U"
		}
		self.colors = [colorOptions[i] for i in self.faces]
		self.oppositeColors = dict(((self.colorOptions[i],colorOptions[self.oppositeFaces[i]])  for i in self.faces))
		self.currentMoveSet = []
		# self.relative = dict(((n,[self.colorOptions[j] for i,j in enumerate(self.faces) if (i>0)]) for n in self.colors))
		# self.relative = {
			# "B": ["B","W","O","G","Y","R"],
			# "W": ["W","O","G","Y","R","B"],
			# "O": ["O","G","Y","R","B","W"],
			# "G": ["G","Y","R","B","W","O"],
			# "Y": ["Y","R","B","W","O","G"],
			# "R": ["R","B","W","O","G","Y"]
		# }
		self.calculateRight = {
			"B": ["W","O","Y","R","W"],
			"G": ["W","R","Y","O","W"],
			"O": ["W","G","Y","B","W"],
			"R": ["W","B","Y","G","W"],
			"W": ["B","R","G","O","B"],
			"Y": ["B","O","G","R","B"],
		}
		self.data = dict([[i, [self.colorOptions[i] for n in range(4)]] for i in self.faces])
		
		# Scramble the cube
		for i in self.scramble:
			self.move(i)
	
	#rotates a side of a cube in the dircetion 	
	def move(self, moves):
		'''	Rotates a side of the cube in the direction
			
			- moves: a list of moves to make
		'''
		for move in moves:
			self.currentMoveSet.append(move)
			face = move[0]
			if(len(move) == 2):
				if(move[1] == "2"):
					rotations = 2
				elif(move[1] == "'"):
					rotations = 3
			else:
				rotations = 1
				
			
			for i in range(rotations):
				# rotate face
				temp = [n for n in self.data[face]]
				self.data[face][0] = temp[3]
				self.data[face][1] = temp[0]
				self.data[face][2] = temp[1]
				self.data[face][3] = temp[2]
				
				# rotate edges
				# relativeLocations = self.relativeFaceLocations[face]
				temp = []
				
				if (face == "F"):
					# record current state in a list
					temp.append(self.data["U"][3])
					temp.append(self.data["U"][2])
					temp.append(self.data["R"][0])
					temp.append(self.data["R"][3])
					temp.append(self.data["D"][1])
					temp.append(self.data["D"][0])
					temp.append(self.data["L"][2])
					temp.append(self.data["L"][1])
					
					# use that to set the new positions
					self.data["U"][3] = temp[6]
					self.data["U"][2] = temp[7]
					self.data["R"][0] = temp[0]
					self.data["R"][3] = temp[1]
					self.data["D"][1] = temp[2]
					self.data["D"][0] = temp[3]
					self.data["L"][2] = temp[4]
					self.data["L"][1] = temp[5]
				elif (face == "R"):
					# record current state in a list
					temp.append(self.data["U"][2])
					temp.append(self.data["U"][1])
					temp.append(self.data["B"][0])
					temp.append(self.data["B"][3])
					temp.append(self.data["D"][2])
					temp.append(self.data["D"][1])
					temp.append(self.data["F"][2])
					temp.append(self.data["F"][1])
					
					# use that to set the new positions
					self.data["U"][2] = temp[6]
					self.data["U"][1] = temp[7]
					self.data["B"][0] = temp[0]
					self.data["B"][3] = temp[1]
					self.data["D"][2] = temp[2]
					self.data["D"][1] = temp[3]
					self.data["F"][2] = temp[4]
					self.data["F"][1] = temp[5]
				elif (face == "U"):
					# record current state in a list
					temp.append(self.data["B"][1])
					temp.append(self.data["B"][0])
					temp.append(self.data["R"][1])
					temp.append(self.data["R"][0])
					temp.append(self.data["F"][1])
					temp.append(self.data["F"][0])
					temp.append(self.data["L"][1])
					temp.append(self.data["L"][0])
					
					# use that to set the new positions
					self.data["B"][1] = temp[6]
					self.data["B"][0] = temp[7]
					self.data["R"][1] = temp[0]
					self.data["R"][0] = temp[1]
					self.data["F"][1] = temp[2]
					self.data["F"][0] = temp[3]
					self.data["L"][1] = temp[4]
					self.data["L"][0] = temp[5]
				elif (face == "B"):
					# record current state in a list
					temp.append(self.data["U"][1])
					temp.append(self.data["U"][0])
					temp.append(self.data["L"][0])
					temp.append(self.data["L"][3])
					temp.append(self.data["D"][3])
					temp.append(self.data["D"][2])
					temp.append(self.data["R"][2])
					temp.append(self.data["R"][1])
					
					# use that to set the new positions
					self.data["U"][1] = temp[6]
					self.data["U"][0] = temp[7]
					self.data["L"][0] = temp[0]
					self.data["L"][3] = temp[1]
					self.data["D"][3] = temp[2]
					self.data["D"][2] = temp[3]
					self.data["R"][2] = temp[4]
					self.data["R"][1] = temp[5]
				elif (face == "L"):
					# record current state in a list
					temp.append(self.data["U"][0])
					temp.append(self.data["U"][3])
					temp.append(self.data["F"][0])
					temp.append(self.data["F"][3])
					temp.append(self.data["D"][0])
					temp.append(self.data["D"][3])
					temp.append(self.data["B"][2])
					temp.append(self.data["B"][1])
					
					# use that to set the new positions
					self.data["U"][0] = temp[6]
					self.data["U"][3] = temp[7]
					self.data["F"][0] = temp[0]
					self.data["F"][3] = temp[1]
					self.data["D"][0] = temp[2]
					self.data["D"][3] = temp[3]
					self.data["B"][2] = temp[4]
					self.data["B"][1] = temp[5]
				elif (face == "D"):
					# record current state in a list
					temp.append(self.data["B"][3])
					temp.append(self.data["B"][2])
					temp.append(self.data["L"][3])
					temp.append(self.data["L"][2])
					temp.append(self.data["F"][3])
					temp.append(self.data["F"][2])
					temp.append(self.data["R"][3])
					temp.append(self.data["R"][2])
					
					# use that to set the new positions
					self.data["B"][3] = temp[6]
					self.data["B"][2] = temp[7]
					self.data["L"][3] = temp[0]
					self.data["L"][2] = temp[1]
					self.data["F"][3] = temp[2]
					self.data["F"][2] = temp[3]
					self.data["R"][3] = temp[4]
					self.data["R"][2] = temp[5]
			
	# Prints the cube to the console
	def __str__(self):
		return("  |" + self.data['U'][0] + self.data['U'][1] + '\n' +
		"  |" + self.data['U'][3] + self.data['U'][2] + '\n' +
		self.data['L'][0] + self.data['L'][1]+"|"+
		self.data['F'][0] + self.data['F'][1] + "|" +
		self.data['R'][0] + self.data['R'][1] + "|" +
		self.data['B'][0] + self.data['B'][1]  + '\n' +
		self.data['L'][3] + self.data['L'][2]+"|"+
		self.data['F'][3] + self.data['F'][2] + "|" +
		self.data['R'][3] + self.data['R'][2] + "|" +
		self.data['B'][3] + self.data['B'][2]  + '\n' +
		"  |" + self.data['D'][0] + self.data['D'][1] + '\n' +
		"  |" + self.data['D'][3] + self.data['D'][2] + '\n')
	
	def __eq__(self, other):
		for side in self.data.keys():
			if self.data[side] != other.data[side]:
				break
		else:
			return True

		return False

	# returns a sorted list (in the form of a string) of the positions with each element as (side, position)
	def colorPositions(self, color):
		lst = []
		for side in self.data:
			for position in range(len(self.data[side])):
				if(self.data[side][position] == color):
					lst.append((side, position))
		lst.sort()
		output = ""
		for i in lst:
			for n in i:
				output += str(n)
		return(output)
		
	# returns a tuple that in the form (side, color, number solved)
	def colorWithMostSolved(self):
		maxList = []
		maxColors = []
		for side in self.faces:
			colorsMaxList = [0 for i in range(len(self.colors))]
			for i,j in enumerate(self.colors):
				for n in self.data[side]:
					if(n == j):
						colorsMaxList[i] += 1
			max = 0
			maxIndex = 0
			for i,j in enumerate(colorsMaxList):
				if(j > max):
					max = j
					maxIndex = i
			maxList.append(max)
			maxColors.append(self.colors[maxIndex])
		max = 0
		maxIndex = 0
		for i,j in enumerate(maxList):
			if(j > max):
				max = j
				maxIndex = i
		return(self.faces[maxIndex], maxColors[maxIndex], max)

	# Returns N if none else returns the solved side
	# def firstFaceIsSolved(self):
		# solvedSide = "N"
		# for side in self.faces:
			# thisSide = True
			# sideColor = self.data[side][0]
			# for piece in self.data[side]:
				# if (piece != sideColor):
					# thisSide = False
					# break
					
			# if (thisSide == True):
				# solvedSide = side
				# break
		
		# return(solvedSide)
	
	# returns a sorted list (in the form of a string) of the cube
	# format: top0top1top2top3front0front1front2front3right0right1right2right3back0back1back2back3left0left1left2left3bottom0bottom1bottom2bottom3
	# each piece is represented by a relative number generated by self.relative
	def cubeState(self):
		bottomColor = self.data["D"][0]
		topColor = self.oppositeColors[bottomColor]
		frontColor = self.data["F"][3]
		backColor = self.oppositeColors[frontColor]
		tempIndex = self.calculateRight[bottomColor].index(frontColor)
		rightColor = self.calculateRight[bottomColor][tempIndex+1]
		leftColor = self.oppositeColors[rightColor]
		print(bottomColor)
		print(topColor)
		print(frontColor)
		print(backColor)
		print(rightColor)
		print(leftColor)
		output = ""
		# output += self.data["U"][0]
		
	# Returns true if the cube is solved
	def isSolved(self):
		output = True
		for i in self.data:
			color = self.data[i][0]
			for j in self.data[i]:
				if(color != j):
					output = False
					break
			if(output != True):
				break
		return (output)
		
def main():
	cube = Cube2x2()
	cube2 = Cube2x2()
	print(cube2 == cube)
	cube.move("R", "R'")
	print(cube2 == cube)
	cube.move("R'")
	print(cube2 == cube)
		

if __name__ == '__main__':
	main()
	
