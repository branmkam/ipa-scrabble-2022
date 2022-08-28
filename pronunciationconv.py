import codecs
with codecs.open("arpabetconv.txt","r", encoding='utf-8') as h:
    phones = list(h.readlines())

for p in range(len(phones)):
    phones[p] = phones[p].replace('\n', '').replace('\r', '').split("\t")[:2]

#print(dict(phones))

g = open("dictionary.txt","r")
words = g.readlines()

test = words[120:130]
for t in range(len(test)):
    test[t] = test[t].replace(r'[0-9]', '').split(" ", 1)
    print(test[t])