import unittest
import hashtable as h

class HashTableTests(unittest.TestCase):
    def test_insert(self):
        testHashTable = h.HashTable()
        testHashTable.insert("abc")
        self.assertEqual(testHashTable.items[hash("abc")%1024], "abc")
    def test_search(self):
        testHashTable = h.HashTable()
        testHashTable.insert("banan")
        res = testHashTable.search("banan")
        self.assertTrue(res)
    def test_search2(self):
        testHashTable = h.HashTable()
        testHashTable.insert("banan")
        res = testHashTable.search("baba")
        self.assertFalse(res)
    def test_delete(self):
        testHashTable = h.HashTable()
        testHashTable.insert("troll")
        testHashTable.delete("troll")
        self.assertFalse(testHashTable.search("troll"))
    def test_delete2(self):
        testHashTable = h.HashTable()
        testHashTable.insert("troll2")
        testHashTable.delete("troll3")
        self.assertTrue(testHashTable.search("troll2"))

if __name__ == '__main__':
    unittest.main()