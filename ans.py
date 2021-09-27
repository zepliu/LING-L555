import sys

counterV = 0
counterT = 0

token = sys.stdin.read()

for c in token:
	if(c.isspace()):
		counterT = counterT + 1
	if c in 'aeiouAEIOU':
		counterV = counterV + 1

print("The average number of syllables per word is", counterV/counterT)
