import random


class Dictogram(dict):
    def __init__(self, iterable=None):
        super(Dictogram, self).__init__()
        if iterable:
            self.update(iterable, )

    def update(self, iterable, **kwargs):
        for word in iterable:
            if word:
                if word in self:
                    self[word] += 1
                else:
                    self[word] = 1

    def count(self, word):
        return self.get(word, 0)

    def get_word(self):
        keys = self.keys()
        if len(keys) < 1:
            return '.'
        else:
            return random.sample(self.keys(), 1)[0]
