import unittest
import stack as s

class StackTests(unittest.TestCase):
    def test_Push(self):
        testStack = s.Stack()
        testStack.push(0)
        testStack.push(1)
        self.assertEqual(testStack.topIndex, 2)
    def test_Push2(self):
        testStack = s.Stack()
        testStack.push(0)
        self.assertEqual(testStack.topIndex, 1)
    def test_Peek(self):
        testStack = s.Stack()
        testStack.push(0)
        self.assertEqual(testStack.peek(), 0)
    def test_Pop(self):
        testStack = s.Stack()
        testStack.push(3)
        self.assertEqual(testStack.pop(), 3)
    def test_Pop2(self):
        testStack = s.Stack()
        result = testStack.pop()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()