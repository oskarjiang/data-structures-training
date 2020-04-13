class HashTable:
    items = [None] * 1024
    def insert(self, item):
        key = hash(item)
        index = key % 1024
        self.items[index] = item
    def search(self, item):
        key = hash(item)
        index = key % 1024
        if (self.items[index] is None):
            return False
        else:
            return True
    def delete(self, item):
        key = hash(item)
        index = key % 1024
        self.items[index] = None