import sys

uniqList = []   # To compute count in the second column
posDict = {}    # The frequency of tags 
pairDict = {}   # The frequency of [form,tag]
formDict = {}   # The frequency of tokens on condition of being put into the first colomn (1/frequency)

base = open('wiki.conllu', 'r')

for line in base.readlines():
    line = line.strip('\n')
    if '\t' not in line:
            continue
    row = line.split('\t')
    form = row[1]
    tag = row[3]
    uniqList.append((form,tag))

for item in uniqList:
    if item not in posDict:
        pairDict[item] = 0
    pairDict[item] = pairDict[item] + 1

counter = 0
for (form,tag) in uniqList:
    if tag not in posDict:
        posDict[tag] = 0
    posDict[tag] = posDict[tag] + 1
    if form not in formDict:
        formDict[form] = 0
    formDict[form] = formDict[form] + 1

print("{}\t{}\t{}\t{}\n".format("# P","count", "tag","form"))  # Create headings

for key, value in posDict.items():
    print("{:.2f}\t{}\t{}\t{}".format(value/sum(posDict.values()), value, key, '_'))

for key, value in pairDict.items():
    form = key[0]
    tokenFreq = formDict[form]      
    print("{:.2f}\t{}\t{}\t{}".format(value/tokenFreq, value , key[1], key[0]))
