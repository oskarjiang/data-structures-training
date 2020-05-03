import unittest
import bst as b

class BSTTests(unittest.TestCase):
    def testInsert(self):
        testBST = b.BST()
        testBST.insert(3)
        testBST.insert(5)
        testBST.insert(4)
        testBST.insert(2)
        testBST.insert(1)
        testBST.insert(1)
        testBST.insert(14)
        testBST.insert(12)
        testBST.insert(11)
        self.assertEqual(testBST.items[0], 3)
    def testFind(self):
        testBST = b.BST()
        testBST.insert(3)
        testBST.insert(5)
        testBST.insert(4)
        testBST.insert(2)
        testBST.insert(1)
        testBST.insert(1)
        testBST.insert(14)
        testBST.insert(12)
        testBST.insert(11)
        self.assertTrue(testBST.find(3))
        self.assertTrue(testBST.find(5))
        self.assertTrue(testBST.find(4))
        self.assertFalse(testBST.find(1337))
        self.assertTrue(testBST.find(2))
    def testDelete(self):
        testBST = b.BST()
        testBST.insert(3)
        testBST.insert(5)
        testBST.insert(4)
        testBST.insert(2)
        testBST.insert(1)
        testBST.insert(1)
        testBST.insert(14)
        testBST.insert(12)
        testBST.insert(11)
        testBST.delete(3)
        testBST.delete(5)
        testBST.delete(4)
        self.assertFalse(testBST.find(3))
        self.assertFalse(testBST.find(5))
        self.assertFalse(testBST.find(4))
        self.assertFalse(testBST.find(1337))
        self.assertTrue(testBST.find(2))
    def testTreeWithDFT(self):
        testBST = b.BST()
        testBST.insert(3)
        testBST.insert(5)
        testBST.insert(4)
        testBST.insert(2)
        testBST.insert(1)
        testBST.insert(1)
        testBST.insert(14)
        testBST.insert(12)
        testBST.insert(11)
        res = testBST.treeWithDFT()
        self.assertEqual(res, "3,2,1,5,4,14,12,11,")
if __name__ == '__main__':
    unittest.main()