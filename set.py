#!python

"""Set implemented with a list"""
class Set(object):

    def __init__(self, elements=None):
        self.list = list()
        self.size = 0
        # Append the given items
        if elements is not None:
            for element in elements:
                if element not in self.list:
                    self.append(element)
                    self.size += 1

    def contains(self, element):
        for i in self.list:
            if i == element:
                return True
        return False

    def add(self, element):
        if self.contains() == False:
            self.list.append(element)
        else:
            raise KeyError('Element already exists in set.')

    def remove(self, element):
        i = 0
        while i < len(self.list):
            if self.list[i] == element:
                self.list.pop(i)
                return
        raise KeyError('Element not found in set.')

    def union(self, other_set):
        new_set = Set()
        i = 0
        while i < len(self.list) and i < len(other_set):
            if 
