import random

NOUNS = ["автомобиль", "лес", "огонь", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat_words=False):


    jokes=[]
    if not repeat_words:
        nouns_copy= NOUNS.copy()
        random.shuffle(nouns_copy)
        adverbs_copy=ADVERBS.copy()
        random.shuffle(adverbs_copy)
        adjectives_copy=ADJECTIVES.copy()
        random.shuffle(adjectives_copy)
        for num, (noun, adverb, adjective) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy)):
            jokes.append(f'{noun} {adjective} {adverb}')
            if num == n:
                break
    else:
        for _ in range(n):
            jokes.append(f'{random.choice(NOUNS)} {random.choice(ADVERBS)} {random.choice(ADJECTIVES)}')
    return jokes

print(get_jokes(1))