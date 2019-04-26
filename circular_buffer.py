#!python

"""Circular buffer implemented with a list"""
class CircularBuffer(object):

    def __init__(self, max_size=8, items=None):
        self.list = [None] * max_size
        self.size = 0
        self.front = 0
        self.back = 0

        if items is not None:
            for item in items:
                self.enqueue(item)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.list)

    def enqueue(self, item):
        self.front += 1
        if self.front  > len(self.list) - 1:
            self.front = 0
            self.back += 1
        if self.back > len(self.list) - 1:
            self.back = 0
        self.list[self.front] = item
        if self.is_full() == True:
            self.back += 1
        if self.size < len(self.list):
            self.size += 1

    def return_front(self):
        return self.list[self.front]

    def dequeue(self):
        if self.back > len(self.list) - 1:
            self.back = 0
        item = self.list[self.back]
        if self.list[self.back] != None:
            self.list[self.back] = None
            self.size -= 1
            self.back += 1
        return item
