#!python

from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        s = CircularBuffer()
        assert len(s.list) == 8
        assert s.size == 0
        assert s.current_index == 0
        s = CircularBuffer(3, ['A', 'B', 'C'])
        assert len(s.list) == 3
        assert s.size == 3
        assert s.current_index == 3
        s = CircularBuffer(3, ['A', 'B', 'C', 'D'])
        assert len(s.list) == 3
        assert s.size == 3
        assert s.current_index == 1

    def test_is_empty(self):
        s = CircularBuffer()
        assert len(s.list) == 8
        assert s.size == 0
        assert s.current_index == 0
