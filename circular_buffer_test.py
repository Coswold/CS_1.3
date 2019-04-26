#!python

from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        s = CircularBuffer()
        assert len(s.list) == 8
        assert s.size == 0
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert len(s.list) == 3
        assert s.size == 3
        s = CircularBuffer(3, ['A', 'B', 'C', 'D'])
        assert len(s.list) == 3
        assert s.size == 3
        assert s.is_full() == True
        assert s.return_front() == 'D'
        assert s.list[s.back] == 'B'

    def test_is_empty(self):
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert s.is_empty() == False
        s.dequeue()
        assert s.is_empty() == False
        s.dequeue()
        assert s.is_empty() == False
        s.dequeue()
        assert s.is_empty() == True
        assert len(s.list) == 3
        assert s.size == 0

    def test_is_full(self):
        s = CircularBuffer(8, ['A', 'B', 'C'])
        assert s.is_full() == False
        s = CircularBuffer(4, ['A', 'B', 'C'])
        assert s.is_full() == False
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert s.is_full() == True
        s.enqueue('D')
        assert s.is_full() == True
        s.dequeue()
        assert s.is_full() == False

    def test_enqueue(self):
        s = CircularBuffer(3, ['A', 'B', 'C'])
        s.enqueue('D')
        assert s.return_front() == 'D'
        s.enqueue('E')
        assert s.return_front() == 'E'
        s.enqueue('F')
        assert s.return_front() == 'F'
        s.enqueue('G')
        assert s.return_front() == 'G'
        s.enqueue('H')
        assert s.return_front() == 'H'
        assert s.size == 3
        assert len(s.list) == 3

    def test_dequeue(self):
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert s.dequeue() == 'A'
        assert s.dequeue() == 'B'
        assert s.dequeue() == 'C'
        s.enqueue('D')
        s.enqueue('E')
        s.enqueue('F')
        s.enqueue('G')
        assert s.dequeue() == 'E'
        assert s.dequeue() == 'F'
        assert s.dequeue() == 'G'

    def text_complex_patterns(self):
        s = CircularBuffer(4)
        s.enqueue('D')
        assert s.dequeue() == 'D'
        assert s.return_front() == None
        s.enqueue('E')
        s.enqueue('F')
        s.enqueue('G')
        s.enqueue('H')
        s.enqueue('I')
        s.enqueue('J')
        s.enqueue('K')
        assert s.return_front() == 'K'
        assert s.list[s.back] == 'H'
        assert s.dequeue() == 'H'
        assert s.dequeue() == 'I'
        assert s.dequeue() == 'J'
        s.enqueue('L')
        s.enqueue('M')
        assert s.return_front() == 'M'
        assert s.list[s.back] == 'K'
        assert s.is_full() == False
        assert s.is_empty() == False
        assert s.size == 3
