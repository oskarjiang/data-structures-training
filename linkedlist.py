class Node:
    def __init__ (self, data):
        self.data = data
    data = None
    next = None

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
            print("HasNext: "+str(nodeToPrint.next is not None))
            print()

myLinkedList = SinglyLinkedList()
myLinkedList.add(Node(1))
myLinkedList.add(Node(2))
myLinkedList.add(Node(3))
myLinkedList.add(Node(4))
myLinkedList.add(Node(5))
myLinkedList.delete(5)
printLinkedList(myLinkedList)