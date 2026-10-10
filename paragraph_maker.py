# for making nonsense paragraphs

# DOESNT WORK

import random
import string

symbols=["?!."]

def create_paragraph(sentences):
    paragraph = []
    for _ in range(sentences):
        s = []
        length = random.randint(3,10)
        word_amount = random.randint(4, 10)
        word = "".join(random.choices(string.ascii_letters + string.digits, k=length))
        for _ in range(word_amount):
            s.append(word + " ")

        ending = random.choice(symbols) # TODO Fix this
        s.append(ending)
        x = "".join(s)
        paragraph.append(x)

    p = ' '.join(paragraph)
    return p

print(create_paragraph(9))

