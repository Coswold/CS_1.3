#!python

"""Set implemented with a list"""
class List_Set(object):

    def __init__(self, elements=None):
        self.list = list()
        self.size = 0
        # Append the given items
        if elements is not None:
            for element in elements:
                if element not in self.list:
                    self.list.append(element)
                    self.size += 1

    def length(self):
        length = 0
        for element in self.list:
            length += 1
        return length

    def contains(self, element):
        for i in self.list:
            if i == element:
                return True
        return False

    def add(self, element):
        if self.contains(element) == False:
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

    def intersection(self, other_set):
        new_set = List_Set()
        i = 0
        while i < len(other_set):
            if self.contains(other_set[i]) == True:
                new_set.add(other_set[i])
            i += 1
        return new_set

    def union(self, other_set):
        new_set = self.list
        i = 0
        while i < len(other_set):
            new_set.add(other_set[i])
            i += 1
        return new_set

    def difference(self, other_set):
        new_set = List_Set()
        i = 0
        while i < len(other_set):
            if self.contains(other_set[i]) != True:
                new_set.add(other_set[i])
            i += 1
        i = 0
        while i < len(self.list):
            if other_set.contains(self.list[i]) != True:
                new_set.add(self.list[i])
            i += 1
        return new_set

    def is_subset(self, other_set):
        while i < len(other_set):
            if self.contains(other_set[i]) != True:
                return False
            i += 1
        return True

Set = List_Set
# Set = Hash_Set
