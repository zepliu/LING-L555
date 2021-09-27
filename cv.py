import sys

counterC = 0
counterV = 0

token = sys.stdin.read()

for c in token:
	if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
		counterC = counterC + 1
	if c in 'aeiouAEIOU':
		counterV = counterV + 1

print("The number of consonants is", counterC)
print("The number of vowels is", counterV)
