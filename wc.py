import sys

counterL = 0
counterT = 0
counterC = 0

token = sys.stdin.read()

for c in token:
	if c == '\n':
		counterL = counterL + 1 
	if(c.isspace()):
		counterT = counterT + 1
	if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
		counterC = counterC + 1

print("The number of lines is", counterL)
print("The number of tokens is", counterT)
print("The number of characters is", counterC)	
