from collections import namedtuple

class Vocab:
    def __init__(self):
        self.w2i = {}
        self.i2w = {}
        self.counter = 0
        self.frozen = False

        self.set_specials()


    def set_specials(self):
        Special = namedtuple('Special', 'pad bos eos unk')
        self.special = Special(pad='<pad>', bos='<s>', eos='</s>', unk='<unk>')
        for key, value in self.special._asdict().items():
            self.add(value)

    def add(self, key):
        assert(not self.frozen)
        if key not in self.w2i:
            self.counter += 1
            self.w2i[key] = self.counter
            self.i2w[self.counter] = key

    def freeze(self):
        self.frozen = True

    def __len__(self):
        return self.counter

    def __getitem__(self, key):
        if key not in self.w2i:
            return self.w2i['<unk>']
        return self.w2i[key]

