from random import *

def in_range(v, a, b):
	if a <= v < b:
		return True
	else:
		return False

def roller(r, d, s):
	c = 0
	thingy = d * s
	thingymabobber = thingy / 2
	thingything = s**d
	dieSumCount = [0 for j in range(thingy - 1)]
	dieRollProbs = [0 for j in range(thingy - 1)]
	
	for j in range(thingy - 1):
		if j < thingymabobber:
			qwert = j + 1
			dieRollProbs[j] = qwert / thingything
		elif j >= thingymabobber:
			qwert = qwert - 1
			dieRollProbs[j] = qwert / thingything
	
	while (c < r):
		dc = 0
		rolled = []
		while (dc < d):
			rand = random()
			for i in range(0, s):
				j = i + 1
				res = in_range(rand, i/s, j/s)
				if res:
					rolled.append(j)
				else:
					continue
			dc += 1
		c += 1
		dieSumCount[sum(rolled) - d] += 1
		print(c)
		print("Rolled:", rolled, " |  Total of all dice:", sum(rolled))
	dieSumProbs = [(p / r) for p in dieSumCount]
	diffs = [(dieSumProbs[j] - dieRollProbs[j]) for j in range(len(dieSumProbs))]
	absdidds = [abs(h) for h in diffs]
	totalEB = sum(absdidds)
	print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("Experiment Results")     
	print("Experimental Die Sum Probabilities =", dieSumProbs)
	print(d, s, "Sided sum Probabilities =", dieRollProbs)
	print("\nError Analysis\nProbability Differences =", diffs)
	print("Total Error Bound", totalEB)

numRollsIn = input("Number of rolls: ")
numRolls = int(numRollsIn)
numDiceIn = input("Number of dice to use: ")
numDice = int(numDiceIn)
numSidesIn = input("Number of sides a die has: ")
numSides = int(numSidesIn)
roller(numRolls, numDice, numSides)