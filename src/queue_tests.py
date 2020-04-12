import unittest
import __queue as q

class QueueTests(unittest.TestCase):
    def test_Enqueue(self):
        testQueue = q.Queue()
        testQueue.enqueue(0)
        self.assertEqual(testQueue.endIndex, 1)
        self.assertEqual(testQueue.startIndex, 0)
    def test_Enqueue2(self):
        testQueue = q.Queue()
        testQueue.enqueue(0)
        testQueue.enqueue(0)
        self.assertEqual(testQueue.endIndex, 2)
        self.assertEqual(testQueue.startIndex, 0)
    def test_Peek(self):
        testQueue = q.Queue()
        testQueue.enqueue(5)
        self.assertEqual(testQueue.peek(), 5)
    def test_Dequeue(self):
        testQueue = q.Queue()
        testQueue.enqueue(1)
        self.assertEqual(testQueue.dequeue(), 1)
    def test_Dequeue2(self):
        testQueue = q.Queue()
        self.assertEqual(testQueue.dequeue(), None)
    def test_Dequeue3(self):
        testQueue = q.Queue()
        testQueue.enqueue(0)
        testQueue.enqueue(1)
        self.assertEqual(testQueue.dequeue(), 0)
    def test_Dequeue4(self):
        testQueue = q.Queue()
        testQueue.enqueue(0)
        testQueue.dequeue()
        testQueue.enqueue(1)
        self.assertEqual(testQueue.startIndex, 1)
        self.assertEqual(testQueue.endIndex, 2)

if __name__ == '__main__':
    unittest.main()