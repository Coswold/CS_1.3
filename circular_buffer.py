#!python

"""Circular buffer implemented with a list"""
class CircularBuffer(object):

    def __init__(self, max_size=8, items=None):
        self.list = []
        self.max_size = max_size
        self.size = 0

        if items is not None:
            for item in items:
                if self.size > self.max_size - 1:
                    self.list.pop(0)
                    self.size -= 1
                self.list.append(item)
                self.size += 1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.size > self.max_size:
            self.list.pop(0)
            self.size -= 1
        self.list.append(item)
        self.size += 1

    def front(self):
        return self.list[self.size - 1]

    def dequeue(self):
        if self.size > 0:
            self.list.pop(0)
            self.size -= 1
