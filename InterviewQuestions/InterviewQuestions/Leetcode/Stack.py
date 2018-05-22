class Stack:
    def __init__(self):
        self.storage = []

    def isEmpty(self):
        return len(self.storage) == 0

    def push(self, p):
        self.storage.append(p)

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[len(self.storage) - 1]

    def length(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)


if __name__ == '__main__':
    stack = Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)

    print(stack.pop())
    print(stack)
