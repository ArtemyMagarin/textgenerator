import sys
import re
import random

from .dictogram import Dictogram


def get_text(path):
    with open(path, 'r') as f:
        text = f.read()
    return re.findall(r'\w+|[.,!?]+', text)


def make_model(word_list, size=1):
    model = {}
    for i in range(0, len(word_list)-size):
        key = tuple(word_list[i:i+size])
        value = (word_list[i+size],)
        if key in model:
            model[key].update(value)
        else:
            model[key] = Dictogram(value)
    return model


def generate(model, count, start_word):
    dots_count = 0
    words = list(start_word)
    size = len(list(model.keys())[0])
    while dots_count < count:
        key = tuple(words[-size:])
        word = model.get(key, Dictogram()).get_word()
        if word == '.':
            dots_count += 1
        words.append(word)
    return re.sub(r'\s+([.,!?]+)', '\g<1>', ' '.join(words))


def main():
    try:
        path = sys.argv[1]
        size = int(sys.argv[2])
        count = int(sys.argv[3])
    except (IndexError, ValueError) as e:
        sys.exit('Usage: %s <input file> <window_size> <sentences_count>' % sys.argv[0])

    word_list = get_text(path)
    model = make_model(word_list, size)
    i = random.randint(0, len(word_list)-size)
    print(generate(model, count, tuple(word_list[i:i+size])))


if __name__ == '__main__':
    main()



