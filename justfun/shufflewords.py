import random


def scramble(sentence: str):
    words = []
    for word in sentence.split():
        if len(word) > 1:
            words.append(word[0] + ''.join(random.sample([char for char in word[1:-1]], len(word) - 2)) + word[-1])
        else:
            words.append(word)
    return ' '.join(words)


text = '''
   shuffle words in this sentence . python has many packages
'''

new = scramble(text)
print(new)
