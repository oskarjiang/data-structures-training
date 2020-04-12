class Queue:
    startIndex = 0
    endIndex = 0
    items = [None] * 64
    def enqueue(self, item):
        self.items[self.endIndex] = item
        self.endIndex += 1
    def dequeue(self):
        if self.startIndex == self.endIndex:
            return None
        else:
            itemToReturn = self.items[self.startIndex]
            self.startIndex += 1
        return itemToReturn
    def peek(self):
        if self.startIndex == self.endIndex:
            return None
        else:
            return self.items[self.startIndex]