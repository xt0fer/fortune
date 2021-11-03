import random
import json


def read_fortunetxt():
    quotes = []
    linez = ""
    fin = open("../fortunedat.txt", 'r')
    for line in fin:
        if line != "%\n":
            linez = linez + line
        elif line == "%\n":
            quotes.append(linez)
            linez = ""
    return quotes

def make_json(q):
    outdata = json.dumps(q)
    return outdata

def save_as_json(outdata):
    fout = open("../fortunedat.json", "w")
    fout.write(outdata)
    fout.close()

def load_from_json():
    fout = open("../fortunedat.json", "r")
    quotes = json.loads(fout.read())
    return quotes

def print_random_fortune(quotes):
    number_of_quotes = len(quotes)
    # print("debug>", len(linez), number_of_quotes, len(quotes))
    qn = random.randint(0, number_of_quotes)
    print("\n"+quotes[qn])

def run_text_fortune():
    q = read_fortunetxt()
    print_random_fortune(q)

def run_json_fortune():
    q = load_from_json()
    print_random_fortune(q)

if __name__ == '__main__':
    run_text_fortune()
    run_json_fortune()
