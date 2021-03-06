import unittest
import heap as h

class HeapTests(unittest.TestCase):
    def testInsert(self):
        testHeap = h.Heap()
        testHeap.insert(3)
        testHeap.insert(5)
        testHeap.insert(4)
        testHeap.insert(2)
        testHeap.insert(1)
        testHeap.insert(1)
        testHeap.insert(14)
        testHeap.insert(12)
        testHeap.insert(11)
        self.assertEqual(testHeap.items[1], 1)
    def testGetHeight(self):
        testHeap = h.Heap()
        testHeap.insert(3)
        testHeap.insert(5)
        testHeap.insert(4)
        testHeap.insert(2)
        testHeap.insert(1)
        testHeap.insert(1)
        testHeap.insert(14)
        testHeap.insert(12)
        testHeap.insert(11)
        self.assertEqual(testHeap.getHeight(), 4)
    def testPeek(self):
        testHeap = h.Heap()
        testHeap.insert(3)
        testHeap.insert(5)
        testHeap.insert(4)
        testHeap.insert(2)
        testHeap.insert(14)
        testHeap.insert(12)
        testHeap.insert(11)
        self.assertEqual(testHeap.peek(), 2)
    # def testPop(self):
    #     testHeap = h.Heap()
    #     testHeap.insert(3)
    #     testHeap.insert(5)
    #     testHeap.insert(4)
    #     self.assertEqual(testHeap.pop(), 3)
    #     self.assertEqual(testHeap.pop(), 4)
    #     self.assertEqual(testHeap.pop(), 5)
    def testPop2(self):
        testHeap = h.Heap()
        testHeap.insert(3)
        testHeap.insert(5)
        testHeap.insert(4)
        testHeap.insert(3)
        testHeap.insert(14)
        testHeap.insert(12)
        testHeap.insert(11)
        self.assertEqual(testHeap.pop(), 3)
        self.assertEqual(testHeap.pop(), 3)
        self.assertEqual(testHeap.pop(), 4)
        self.assertEqual(testHeap.pop(), 5)
        self.assertEqual(testHeap.pop(), 11)
        self.assertEqual(testHeap.pop(), 12)
        self.assertEqual(testHeap.pop(), 14)
        testHeap.insert(11)
        self.assertEqual(testHeap.pop(), 11)

if __name__ == '__main__':
    unittest.main()