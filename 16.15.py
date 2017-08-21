'''
Master Mind: The Game of Master Mind is played as follows:

The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (G), or blue (B). 
For example, the computer might have RGGB (slot #1 is red, slots #2 and #3 are green, Slot #4 is blue).

You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit." If you guess a color that exists, but is in the
wrong slot, you get a "pseudo-hit". Note that a slot that is a hit can never count as a pseudo-hint.

For example, if the actual solutoin is RGBY and you guess GGRR, you have one hit and one pseudo-hit. 
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits. 
'''

def calculate_hits(guess, actual):
	guess = list(guess)
	actual = list(actual)
	hit = 0
	for i in range(len(guess)):
		if guess[i] == actual[i]:
			hit += 1
			actual[i], guess[i] = "-", "-" #avoid double counting

	pseudohit = 0
	for i in range(len(actual)):
		if actual[i] != "-" and actual[i] in guess:
			pseudohit += 1
			guess[guess.index(actual[i])] = "-"
			actual[i] = "-"


	return (hit, pseudohit)

actual = "RGBY"
guess = "GGRR"
print(calculate_hits(guess, actual))
