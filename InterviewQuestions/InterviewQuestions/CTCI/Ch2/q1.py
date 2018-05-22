import Node


# Remove duplicates from linked list
class RemoveDuplicates:
    def __init__(self):
        print ""

    @staticmethod
    def removeDuplicates(linkedList):
        if not linkedList:
            return linkedList

        currentNode = linkedList.next
        prevNode = linkedList
        values = set()
        values.add(prevNode.data)

        while currentNode:
            if currentNode.data in values:
                # Remove node
                prevNode.next = currentNode.next
                currentNode = prevNode.next
            else:

                values.add(currentNode.data)
                prevNode = currentNode
                currentNode = currentNode.next

        return linkedList


if __name__ == '__main__':
    linkedList1 = Node.Node(1)
    linkedList1.appendToTail(2)
    linkedList1.appendToTail(2)
    linkedList1.appendToTail(3)
    linkedList1.appendToTail(1)

    # linkedList1.printNodes()
    # RemoveDuplicates.removeDuplicates(linkedList1).printNodes()  # 1, 2, 3

    linkedList2 = Node.Node(1)
    linkedList2.appendToTail(1)

    linkedList2.printNodes()
    RemoveDuplicates.removeDuplicates(linkedList2).printNodes()  # 1
