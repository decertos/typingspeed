from base_words import words
from random import choice

words_coincidences = {}
lw = len(words) - 2

for i in range(len(words)):
    if i != lw and words[i] not in ",./;':!?-+()":
        if words[i + 1] not in ",./;':!?-+()":
            to_coincidence = words[i + 1]
        else:
            to_coincidence = words[i + 2]

        if words[i] in words_coincidences:
            words_coincidences[words[i]].append(to_coincidence)
        else:
            words_coincidences[words[i]] = [to_coincidence]
    elif i == lw:
        break


def generate_sentence(length):
    text = ""
    now_word = choice(words[:-1])

    for i in range(length):
        while True:
            if now_word in words_coincidences:
                random_word = choice(words_coincidences[now_word])
                text += random_word + " "
                now_word = random_word
                break
            else:
                now_word = choice(words[:-1])

    text = text[0].upper() + text[1:].lower()
    return text