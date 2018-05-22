import Node


# Find kth element from end
class ReturnKthToLast:
    def __init__(self):
        print ""

    @staticmethod
    def returnKthToLast(linkedList, k):
        runner = linkedList
        top = linkedList
        while runner.next:
            runner = runner.next
            if k > 0:
                k -= 1
            else:
                top = top.next

        return top.data


if __name__ == '__main__':
    linkedList1 = Node.Node(5)
    linkedList1.appendToTail(4)
    linkedList1.appendToTail(3)
    linkedList1.appendToTail(2)
    linkedList1.appendToTail(1)
    linkedList1.printNodes()

    print(ReturnKthToLast.returnKthToLast(linkedList1, 5))  # 5
    print(ReturnKthToLast.returnKthToLast(linkedList1, 4))  # 5
    print(ReturnKthToLast.returnKthToLast(linkedList1, 3))  # 4
    print(ReturnKthToLast.returnKthToLast(linkedList1, 2))  # 3
    print(ReturnKthToLast.returnKthToLast(linkedList1, 1))  # 2
    print(ReturnKthToLast.returnKthToLast(linkedList1, 0))  # 1
