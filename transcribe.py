import sys

IPA = {}
base = open('IPA.txt', 'r')

for line in base.readlines():
	line = line.strip('\n')
	(l,i) = line.split('\t')
	IPA[l] = i

transcription = ''

for line in sys.stdin.readlines():
	if '\t' not in line:
		print(line)	   # Skip the line without tab
	elif '\t' in line:
		row = line.split('\t')
		word = row[1]     # To get the token in each line
		transcription = word
		for k in word:
			if k in IPA:
				transcription = transcription.replace(k, IPA[k])      # Replace the token with the IPA form
		row[9] = 'IPA=' + transcription
		print('\t'.join(row))      # Print all lines

