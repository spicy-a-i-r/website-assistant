# for making nonsense paragraphs

import random

lower = "abcdefghijklmnoqrstuwxyz"
symbols = ["? ", "! ", ". "]

p = []

def create(s):
    low = list(lower)
    random.shuffle(low)

    

    for _ in range(s):
        sen = []
        l = random.randint(3, 11)
        a = random.choices(low, k=l)
        sentence = "".join("".join(a) for a in sen)
        print(sentence)
        sym = random.choice(symbols)
        sen.append(sym + " ")
        p.append(sen)



create(9)


        

