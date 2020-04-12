class Stack:
    topIndex = 0
    items = [None] * 64
    def push(self, item):
        self.topIndex += 1
        self.items[self.topIndex] = item
    def pop(self):
        if self.topIndex == 0:
            return None
        else:
            itemToReturn = self.items[self.topIndex]
            self.topIndex -= 1
        return itemToReturn
    def peek(self):
        if self.topIndex == 0:
            return None
        else:
            return self.items[self.topIndex]