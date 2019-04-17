#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        d = Deque()
        assert q.front() is None
        assert d.length() == 0
        assert d.is_empty() is True

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        assert d.front() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_length(self):
        d = Deque()
        assert d.length() == 0
        d.enqueue('A')
        assert d.length() == 1
        d.enqueue('B')
        assert d.length() == 2
        d.dequeue()
        assert d.length() == 1
        d.dequeue()
        assert d.length() == 0

    def test_push_front(self):
        d = Deque()
        d.enqueue('A')
        assert d.front() == 'A'
        assert d.length() == 1
        d.enqueue('B')
        assert d.front() == 'A'
        assert d.length() == 2
        d.enqueue('C')
        assert d.front() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_front(self):
        d = Deque()
        assert d.front() is None
        d.enqueue('A')
        assert d.front() == 'A'
        d.enqueue('B')
        assert d.front() == 'A'
        d.dequeue()
        assert d.front() == 'B'
        d.dequeue()
        assert d.front() is None

if __name__ == '__main__':
    unittest.main()
