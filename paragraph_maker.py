# for making nonsense paragraphs

import random

lower = ["abcdefghijklmnoqrstuwxyz"]
symbols = ["? ", "! ", ". "]



def create_paragraph(sentences):
    p = []
    for i in range(1, sentences): # makes a sentence
        s = []
        w = random.randint(1, 9)

        for _ in range(1, w): # makes a word
            word = []
            l = random.randint(1, 11)

            for _ in range(1, l):
                char = lower[random.randint(1, l)]
                word.append(char)
            word.append(random.choice(symbols))
            "".join(word)
            print(word)

        s.append(word)
        print(s)

create_paragraph(4)
        

