import sys

pos = []   # Create a list to store form and tag

base = open('wiki.conllu', 'r')

for line in base.readlines():
    line = line.strip('\n')
    if '\t' not in line:
            continue
    row = line.split('\t')
    form = row[1]
    tag = row[3]
    pos.append((form,tag))       # Put form and tag together

uniqList = {}    # Create a dict to store count data

for item in pos:
    if item not in uniqList:
        uniqList[item] = 0
    uniqList[item] = uniqList[item] + 1

print("{}\t{}\t{}\t{}\n".format("# P","count", "tag","form"))  # Create headings

for key, value in uniqList.items():
    print("{:.2f}\t{}\t{}\t{}".format(value/sum(uniqList.values()), value,key[1],key[0]))
