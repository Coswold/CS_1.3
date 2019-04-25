#!python

from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        s = CircularBuffer()
        assert s.max_size == 8
        assert s.size == 0
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert s.max_size == 3
        assert s.size == 3
        assert s.list == ['A', 'B', 'C']
        s = CircularBuffer(3, ['A', 'B', 'C', 'D'])
        assert s.max_size == 3
        assert s.size == 3
        assert s.list == ['B', 'C', 'D']

    def test_is_empty(self):
        s = CircularBuffer()
        assert s.max_size == 8
        assert s.size == 0
        assert s.is_empty() == True
        s = CircularBuffer(3, ['A', 'B', 'C'])
        s.dequeue()
        s.dequeue()
        s.dequeue()
        assert s.is_empty() == True

    def test_is_full(self):
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert s.is_full() == True
        assert s.size == 3
        s = CircularBuffer(3, ['A', 'B', 'C', 'D'])
        assert s.is_full() == True
        assert s.size == 3
        s = CircularBuffer(['A', 'B', 'C'])
        print(s.list)
        assert s.is_full() == False
        assert s.size == 3
