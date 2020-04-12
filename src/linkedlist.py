class Node:
    def __init__ (self, data):
        self.data = data
    data = None
    next = None
    previous = None

class SinglyLinkedList:
    head = None;
    def add(self, node):
        if (self.head is None):
            self.head = node
        else:
            currentNode = self.head
            while (currentNode.next is not None):
                currentNode = currentNode.next
            currentNode.next = node
    def addAtIndex(self, node, index):
        if (self.head is None):
            self.head = node
        else:
            if (index == 0):
                node.next = self.head
                self.head = node
                return
            currentNode = self.head
            counter = 0
            while (currentNode.next is not None):
                if (counter == index - 1):
                    temp = currentNode.next
                    currentNode.next = node
                    node.next = temp
                    return
                currentNode = currentNode.next
                counter += 1
    def delete(self, nodeData):
        currentNode = self.head
        if (currentNode.data == nodeData):
            self.head = None
        while (currentNode.next is not None):
            if (currentNode.next.data == nodeData):
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

def printLinkedList(linkedList):
    if (not linkedList.head):
        print([])
    else:
        nodesToPrint = []
        currentNode = linkedList.head
        while (currentNode is not None):
            nodesToPrint.append(currentNode)
            currentNode = currentNode.next
        for nodeToPrint in nodesToPrint:
            print("Data: "+str(nodeToPrint.data))
            if (nodeToPrint.next is None):
                print("Next: ")
            else:
                print("Next: "+str(nodeToPrint.next.data))
            print()