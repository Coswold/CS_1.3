#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.length() == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('C') == True
        assert s.length() == 3

    def test_length(self):
        s = Set()
        assert s.length() == 0
        s.add('A')
        assert s.length() == 1
        s.add('B')
        assert s.length() == 2
        s.remove('A')
        assert s.length() == 1
        s.remove('B')
        assert s.length() == 0
