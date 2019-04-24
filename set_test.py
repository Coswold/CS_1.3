#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('C') == True
        assert s.size == 3

    def test_length(self):
        s = Set()
        assert s.size == 0
        s.add('A')
        assert s.size == 1
        s.add('B')
        assert s.size == 2
        s.remove('A')
        assert s.size == 1
        s.remove('B')
        assert s.size == 0

    def test_add(self):
        s = Set()
        s.add('A')
        assert s.contains('A') == True
        # How can I test for KeyError?
        # s.add('A')
        # s.length() == 1

    def test_remove(self):
        s = Set(['A', 'B'])
        assert s.size == 2
        s.remove('A')
        assert s.contains('B')
        assert s.size == 1
