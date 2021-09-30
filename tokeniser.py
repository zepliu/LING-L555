import sys

lines = sys.stdin.readlines()

n = 0

for line in lines:
	n = n + 1
	print("\n# sent_id = ", n)
	sent = line.strip()
	print("# text = ", sent, "\n")
	word_id = 1
	sent = sent.replace("," , " , ")
	sent = sent.replace("." , " . ")
	sent = sent.replace(":" , " : ")
	sent = sent.replace("(" , " ( ")
	sent = sent.replace(")" , " ) ")
	sent = sent.split()
	for i in sent:
		print(word_id, i)
		word_id = word_id + 1
