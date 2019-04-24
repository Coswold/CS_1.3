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
        s.add('A')
        assert s.size == 1
        s.add('B')
        s.add('B')
        assert s.size == 2
        assert s.list == ['A', 'B']

    def test_remove(self):
        s = Set(['A', 'B'])
        assert s.size == 2
        s.remove('A')
        assert s.contains('B')
        assert s.size == 1

    def test_intersection(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        intersection = s.intersection(other_set)
        assert intersection.contains('A') == True
        other_set = Set(['D'])
        intersection = s.intersection(other_set)
        assert intersection.contains('D') == False
        assert intersection.size == 0

    def test_union(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        union = s.union(other_set)
        assert union.list == ['A', 'B', 'C']
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D', 'E'])
        union = s.union(other_set)
        assert union.list == ['A', 'B', 'C', 'D', 'E']

    def test_difference(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'D'])
        difference = s.difference(other_set)
        assert difference.list == ['D', 'B', 'C']
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D', 'E', 'F'])
        difference = s.difference(other_set)
        assert difference.list == ['D', 'E', 'F', 'A', 'B', 'C']
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C'])
        difference = s.difference(other_set)
        assert difference.list == []

    def test_is_subset(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A'])
        assert s.is_subset(other_set) == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C'])
        assert s.is_subset(other_set) == True
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'B', 'C', 'D'])
        assert s.is_subset(other_set) == False
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D'])
        assert s.is_subset(other_set) == False
