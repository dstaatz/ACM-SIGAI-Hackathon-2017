
from Cube import Cube2x2
from Scrambler import Scrambler

class Solver :

	def __init__(self, cube):
		self.cube = cube
		self.OUTPUT_MOVESET = []
	
	# Return a list of moves that will solve a specific cube object
	def solve(self):
		temp = self.cube.colorWithMostSolved()
		sideMostSolved = temp[0]
		colorMostSolved = temp[1]
		numberMostSolved = temp[2]
		
		
		if(numberMostSolved == 1):
			self.solveTwo()
		# temp = cube.colorWithMostSolved()
		# sideMostSolved = temp[0]
		# colorMostSolved = temp[1]
		# numberMostSolved = temp[2]
		
		# if(numberMostSolved == 2):
			# self.solveThree()
		# temp = cube.colorWithMostSolved()
		# sideMostSolved = temp[0]
		# colorMostSolved = temp[1]
		# numberMostSolved = temp[2]
		
		# if(numberMostSolved == 3):
			# self.solveSide()
		
		# Move solved side to the bottom
		
		# self.OLL()
		
		# self.PLL()
		
		return(self.OUTPUT_MOVESET)
		
	def solveTwo(self):
		count = 0
		while (self.cube.colorWithMostSolved()[2] == 1):
			solveTwoMoveSet = ["U","F","R", "D", "B", "L"]
			self.OUTPUT_MOVESET.append(solveTwoMoveSet[count])
			self.cube.move(solveTwoMoveSet[count])
			count += 1
			if(count == 7):
				print("WARNING WARNING WARNING WARNING WARNING")
				quit()
		
	def solveThree(self):
		pass
		
	def solveSide(self):
		pass
	
	def OLL(self):
		pass
	
	def PLL(self):
		pass
		
		
def main():
	for i in range(1000):
		while True:
			scramble = Scrambler.scramble(2)
			cube = Cube2x2(scramble=scramble)
			if (cube.colorWithMostSolved()[2] == 1):
				break
		#[print(i, end=" ") for i in scramble]
		#print()
		#cube.printCube()
		s = Solver(cube)
		temp = s.solve()
		if (len(temp) == 6):
			print("Temp = ", temp)
			print(scramble)
		#cube.printCube()

def test():
	cube = Cube2x2(scramble=["L'", 'B', 'D2', 'R', 'L2', "R'", 'D2', 'U', 'D', "B'", 'D'])
	s = Solver(cube)
	temp = s.solve()
	s.cube.printCube()
	print(s.cube.colorWithMostSolved())
	if (len(temp) == 6):
		print("Temp = ", temp)
		print(["L'", 'B', 'D2', 'R', 'L2', "R'", 'D2', 'U', 'D', "B'", 'D'])

if __name__ == "__main__":
	main()