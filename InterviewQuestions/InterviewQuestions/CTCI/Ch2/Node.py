class Node:
    next = None
    data = None

    def __init__(self, data):
        self.data = data

    def appendToHead(self, data):
        newNode = Node(data)
        newNode.next = self
        return newNode

    def appendToTail(self, data):
        if not self:
            return

        currentNode = self

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = Node(data)

    def getSize(self):
        currentNode = self
        size = 0

        while currentNode:
            size += 1
            currentNode = currentNode.next

        return size

    def printNodes(self):
        currentNode = self
        string = ''

        while currentNode:
            string += '{}{}{}'.format("[", currentNode.data, "] => ")
            currentNode = currentNode.next
        print(string)


if __name__ == '__main__':
    linkedList = Node(10)

    linkedList = linkedList.appendToHead(3)
    linkedList.appendToTail(0)

    linkedList.printNodes()
