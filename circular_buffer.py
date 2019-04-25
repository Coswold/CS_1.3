#!python

"""Circular buffer implemented with a list"""
class CircularBuffer(object):

    def __init__(self, max_size=8, items=None):
        self.list = [None] * max_size
        self.size = 0
        self.current_index = 0

        if items is not None:
            for item in items:
                if self.current_index > len(self.list) - 1:
                    self.current_index = 0
                self.list[self.current_index] = item
                self.current_index += 1
                if self.size < len(self.list):
                    self.size += 1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.list)

    def enqueue(self, item):
        if self.current_index > len(self.list) - 1:
            self.current_index = 0
        self.list[self.current_index] = item
        if self.size < len(self.list):
            self.size += 1

    def front(self):
        i = 0
        while i < self.size:
            i += 1
        return self.list[i]

    def dequeue(self):
        i = 0
        while i < self.size:
            i += 1
        item = self.list[i]
        self.list[i] = None
        return item
