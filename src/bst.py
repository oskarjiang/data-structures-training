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
            self.items[index] = None
        else:
            if item < root:
                self.deleteItemAt(item, self.getLeftChildIndex(index))
            elif item > root:
                self.deleteItemAt(item, self.getRightChildIndex(index))

    def getParentIndex(self, index):
        return math.floor((index-1)/2)
    def getLeftChildIndex(self, index):
        return index*2+1
    def getRightChildIndex(self, index):
        return index*2+2