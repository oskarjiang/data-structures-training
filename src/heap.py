import math

class Heap:
    items = [None] * 64
    def __init__ (self):
        self.items = [None] * 64
    def insert(self, item):
        for i in range(1, 64):
            if (self.items[i] is None):
                self.items[i] = item
                indexOfitemToSift = i
                if i == 1:
                    return
                while self.items[indexOfitemToSift] < self.items[self.getParentIndex(indexOfitemToSift)]:
                    temp = self.items[indexOfitemToSift]
                    self.items[indexOfitemToSift] = self.items[self.getParentIndex(indexOfitemToSift)]
                    self.items[self.getParentIndex(indexOfitemToSift)] = temp

                    if self.getParentIndex(indexOfitemToSift) == 1:
                        return
                    indexOfitemToSift = self.getParentIndex(indexOfitemToSift)
                return
        return
    def pop(self):
        itemToReturn = self.items[1]
        self.heapify(1)
        return itemToReturn
    def heapify(self, i):
        left = self.items[self.getLeftChildIndex(i)]
        right = self.items[self.getRightChildIndex(i)]
        if left is None and right is None:
            return
        elif left is None:
            self.items[i] = right
            self.items[self.getRightChildIndex(i)] = None
            self.heapify(self.getRightChildIndex(i))
        elif right is None:
            self.items[i] = left
            self.items[self.getLeftChildIndex(i)] = None
            self.heapify(self.getLeftChildIndex(i))
        elif left <= right:
            self.items[i] = left
            self.items[self.getLeftChildIndex(i)] = None
            self.heapify(self.getLeftChildIndex(i))
        else:
            self.items[i] = right
            self.items[self.getRightChildIndex(i)] = None
            self.heapify(self.getRightChildIndex(i))

    def peek(self):
        return self.items[1]
    def getParentIndex(self, index):
        return math.floor(index/2)
    def getLeftChildIndex(self, index):
        return index*2
    def getRightChildIndex(self, index):
        return index*2+1
    def printHeap(self):
        print(self.items)
    def getHeight(self):
        currentIndex = 1
        height = 0
        while self.items[currentIndex] is not None:
            currentIndex *= 2
            height += 1
        return height