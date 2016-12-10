import time
import random


class SemiRandomData(object):

    def __init__(self, dim, rest, val, noise=0, include_neg=True):
        self.axes = int(dim)
        self.rest = rest
        self.val = val
        self.noise = noise
        if include_neg:
            self.inc_neg = 2
        else:
            self.inc_neg = 1
        self.divisor = self.axes * self.inc_neg
        self.t0 = time.time()
        self.get_value()

    def get_value(self):
        t1 = time.time()
        div1 = int((t1 - self.t0) // self.rest)
        div2 = int(div1 % self.divisor)
        tup_pos = int(div2 // self.inc_neg)
        tup_val = (1 - 2 * (div2 % self.inc_neg)) * self.val
        output = random_list(3, self.noise)
        output[tup_pos] += tup_val + tup_pos
        return tuple(output)


def random_list(dim, span):
    randall = []
    for i in range(dim):
        randall.append(span * (1 - 2 * random.random()))
    return randall


class bt(object):

    class BThandler(object):

        def __init__(self, activity):
            self.name = None
            self.exists = True
            self.ready = False
            self.enabled = False
            self.paired_device_list = ['1', '2', '3']

        def get_device_by_name(self, name):
            self.name = name
            self.ready = True

        def get_adapter(self):
            self.exists = True
            self.enabled = True

        def get_paired_device_list(self):
            return ['1', '2', '3']
