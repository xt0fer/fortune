import random

fin = open("../fortunedat.txt", 'r')

quotes = []
linez = ""

for line in fin:
    if line != "%\n":
        linez = linez + line
    elif line == "%\n":
        quotes.append(linez)
        linez = ""

number_of_quotes = len(quotes)
# print("debug>", len(linez), number_of_quotes, len(quotes))
qn = random.randint(0, number_of_quotes)
print("\n"+quotes[qn])
