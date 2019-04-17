#!python
# -*- coding: utf-8 -*-

class Deque(object):

    def __init__(self, iterable=None):
        """Initialize this deque and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this deque."""
        return 'Deque({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this deque is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this deque."""
        return len(self.list)

    def push_front(self, item):
        """Insert the given item at the front of this deque.
        Running time: O(???) – Why? [TODO]"""
        self.list.append(item)

    def push_back(self, item):
        """Insert the given item at the back of this deque.
        Running time: O(???) – Why? [TODO]"""
        [item] + self.list

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this queue is empty."""
        if self.is_empty() == True:
            return None
        return self.list[0]

    def back(self):
        """Return the item at the back of this deque without removing it,
        or None if this queue is empty."""
        if self.is_empty() == True:
            return None
        return self.list[-1]

    def pop_front(self):
        """Remove and return the item at the front of this deque,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty() == True:
            raise ValueError('Deque is empty.')
        return self.list.pop(0)

    def pop_back(self):
        """Remove and return the item at the front of this deque,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty() == True:
            raise ValueError('Deque is empty.')
        return self.list.pop()
