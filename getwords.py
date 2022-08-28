#all words from dataset
g = open("phonemes.txt","r")
lines = g.readlines()

# function that filters vowels
def fun(line):
    if (ord(line[0]) >= 65 and ord(line[0]) <= 90):
        return True
    else:
        return False
  
# using filter function
datawords = list(filter(fun, lines))
  
# for i in range(len(datawords)):
#     datawords[i] = datawords[i].replace("\n", "").split(" ", 1)

# fdict = dict(datawords)
# print('done')

#legal words
w = open("legalwords.txt","r")
words = w.readlines()

for i in range(len(words)):
    words[i] = words[i].replace("\n", "")


def fun2(line):
    if (line[0] in words):
        return True
    else:
        return False

def iterator(line):
    return True if line.split(" ", 1)[0] in words else False

legalwords = list(filter(iterator, lines))

#add lines
f = open("dictionary.txt", "w")
f.writelines(legalwords)
f.close()