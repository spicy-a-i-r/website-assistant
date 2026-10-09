# for making nonsense paragraphs

# DOESNT WORK

import random
import string

symbols=["?!."]

def create_paragraph(sentences):
    paragraph = []
    for _ in range(sentences):
        sentence = []
        length = random.randint(0,10)
        word_amount = random.randint(0, 7)
        word = "".join(random.choices(string.ascii_letters + string.digits, k=length))
        for _ in range(word_amount):
            sentence.append(word + " ")

        ending = random.choice(symbols)
        sentence.append(ending)

        paragraph.append(sentence)
        
    return paragraph

print(create_paragraph(9))

