#!python

from hashtable import HashTable

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

    def contains(self, element):
        for i in self.list:
            if i == element:
                return True
        return False

    def add(self, element):
        if self.contains(element) == False:
            self.list.append(element)
            self.size += 1

    def remove(self, element):
        i = 0
        while i < len(self.list):
            if self.list[i] == element:
                self.list.pop(i)
                self.size -= 1
                return
        raise KeyError('Element not found in set.')

    def intersection(self, other_set):
        new_set = List_Set()
        i = 0
        while i < other_set.size:
            if self.contains(other_set.list[i]):
                new_set.add(other_set.list[i])
            i += 1
        return new_set

    def union(self, other_set):
        new_set = List_Set(self.list)
        i = 0
        while i < other_set.size:
            new_set.add(other_set.list[i])
            i += 1
        return new_set

    def difference(self, other_set):
        new_set = List_Set()
        i = 0
        while i < other_set.size:
            if self.contains(other_set.list[i]) != True:
                new_set.add(other_set.list[i])
            i += 1
        i = 0
        while i < self.size:
            if other_set.contains(self.list[i]) != True:
                new_set.add(self.list[i])
            i += 1
        return new_set

    def is_subset(self, other_set):
        i = 0
        while i < other_set.size:
            if self.contains(other_set.list[i]) != True:
                return False
            i += 1
        return True

"""Set implemented with a hashtable"""
class Hash_Set(object):

    def __init__(self, elements=None):
        self.list = HashTable()
        self.size = 0
        # Append the given items
        if elements is not None:
            for element in elements:
                self.list.set(element, element)
                self.size += 1

    def contains(self, element):
        return self.list.contains(element)

    def add(self, element):
        if self.contains(element) == False:
            self.list.set(element, element)
            self.size += 1

    def remove(self, element):
        if self.contains(element) == True:
            self.list.delete(element)
            self.size -= 1
        else:
            raise KeyError('Element not found in set.')

    def intersection(self, other_set):
        new_set = Hash_Set()
        items = other_set.list.values()
        for item in items:
            if self.list.contains(item):
                new_set.add(item)
        return new_set

    def union(self, other_set):
        new_set = Hash_Set(self.list.values())
        items = other_set.list.values()
        for item in items:
            new_set.add(item)
        return new_set

    def difference(self, other_set):
        new_set = Hash_Set()
        items = other_set.list.values()
        for item in items:
            if self.contains(item) == False:
                new_set.add(item)
        return new_set

    def symetric_difference(self, other_set):
        new_set = Hash_Set()
        items = other_set.list.values()
        for item in items:
            if self.contains(item) == False:
                new_set.add(item)
        items = self.list.values()
        for item in items:
            if other_set.contains(item) == False:
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        items = other_set.list.values()
        for item in items:
            if self.contains(item) == False:
                return False
        return True

# Set = List_Set
Set = Hash_Set

if __name__ == '__main__':
    s = Set(['A', 'B', 'C'])
