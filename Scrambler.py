import random

class Scrambler:
	
	def __init__(self):
		self.moves = "F","R","U","B","L","D","F'","R'","U'","B'","L'","D'","F2","R2","U2","B2","L2","D2","Fw","Rw","Uw","Bw","Lw","Dw","Fw'","Rw'","Uw'","Bw'","Lw'","Dw'","Fw2","Rw2","Uw2","Bw2","Lw2","Dw2"
	
	# cubeType refers to the size of the cube
	def scramble(self, cubeType):
		if cubeType == 2:
			len = random.randrange(8, 13)
			moveTypes = 18
		elif cubeType == 3:
			len = random.randrange(17, 23)
			moveTypes = 18
		elif cubeType == 4:
			len = random.randrange(25, 32)
			moveTypes = 36
		elif cubeType == 5:
			len = random.randrange(33, 37)
			moveTypes = 36
		lst = []
		lastMove = random.randrange(moveTypes)
		lst.append(lastMove)
		for i in range(len-1):
			newMove = random.randrange(moveTypes)
			while ((bool(newMove >= 18) == bool(lastMove >= 18)) & (lastMove % 6 == newMove % 6)):
				newMove = random.randrange(moveTypes)
			lst.append(newMove)
			lastMove = newMove
		lst = [self.moves[i] for i in lst]
		return (lst)

		
Scrambler = Scrambler()

def main():
	while True:
		response = int(input("Enter a scramble: "))
		lst = Scrambler.scramble(response)
		lst2 = [print(i, end=' ') for i in lst]
		print()
	
if __name__ == '__main__':
	main()

	
	
