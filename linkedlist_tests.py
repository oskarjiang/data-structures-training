import unittest
import linkedlist as ll

class LinkedListTests(unittest.TestCase):
    def test_Add(self):
        testList = ll.SinglyLinkedList()
        testList.add(ll.Node(5))
        self.assertEqual(testList.head.data, 5)
    def test_AddAtIndex(self):
        testList = ll.SinglyLinkedList()
        testList.add(ll.Node(1))
        testList.add(ll.Node(3))
        testList.addAtIndex(ll.Node(2), 0)
        self.assertEqual(testList.head.data, 2)
    def test_AddAtIndex2(self):
        testList = ll.SinglyLinkedList()
        testList.add(ll.Node(1))
        testList.add(ll.Node(3))
        testList.addAtIndex(ll.Node(2), 1)
        self.assertEqual(testList.head.next.data, 2)

if __name__ == '__main__':
    unittest.main()