class BST:
    items = [None] * 64
    def __init__(self):
        self.items = [None] * 64
    
    def find(self, item):
        return self.findItemAt(item, 0)
    
    def findItemAt(self, item, index):
        root = self.items[index]
        if root is None:
            return False
        elif root == item:
            return True
        else:
            if item < root:
                return self.findItemAt(item, self.getLeftChildIndex(index))
            elif item > root:
                return self.findItemAt(item, self.getRightChildIndex(index))

    def insert(self, item):
        self.insertItemAt(item, 0)

    def insertItemAt(self, item, index):
        root = self.items[index]
        if root is None:
            self.items[index] = item
        else:
            if item < root:
                self.insertItemAt(item, self.getLeftChildIndex(index))
            elif item > root:
                self.insertItemAt(item, self.getRightChildIndex(index))

    def delete(self, item):
        self.deleteItemAt(item, 0)

    def deleteItemAt(self, item, index):
        root = self.items[index]
        if root is None:
            return
        elif root == item:
            self.replaceWithChildFrom(index)
        else:
            if item < root:
                self.deleteItemAt(item, self.getLeftChildIndex(index))
            elif item > root:
                self.deleteItemAt(item, self.getRightChildIndex(index))

    def replaceWithChildFrom(self, index):
        self.replaceWithChild(index)

    def replaceWithChild(self, index):
        leftChild = self.items[self.getLeftChildIndex(index)]
        rightChild = self.items[self.getRightChildIndex(index)]
        if leftChild is not None:
            self.items[index] = leftChild
            self.replaceWithChild(self.getLeftChildIndex(index))
        elif rightChild is not None:
            self.items[index] = rightChild
            self.replaceWithChild(self.getRightChildIndex(index))
        else:
            self.items[index] = None
    def treeWithDFT(self):
        return self.treeWithDFTAt(0, '')

    def treeWithDFTAt(self, index, res):
        root = self.items[index]
        leftChild = self.items[self.getLeftChildIndex(index)]
        rightChild = self.items[self.getRightChildIndex(index)]
        res = res + str(root) + ','
        if leftChild is not None:
            res = self.treeWithDFTAt(self.getLeftChildIndex(index), res)
        if rightChild is not None:
            res = self.treeWithDFTAt(self.getRightChildIndex(index), res)
        return res

    def getParentIndex(self, index):
        return math.floor((index-1)/2)
    def getLeftChildIndex(self, index):
        return index*2+1
    def getRightChildIndex(self, index):
        return index*2+2