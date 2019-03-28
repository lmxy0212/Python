class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

class Queue:
    def __init__(self):
        self.inn = ArrayStack()
        self.out = ArrayStack()

    def __len__(self):
        return len(self.inn)+len(self.out)

    def is_empty(self):
        return self.inn.is_empty()

    def enqueue(self, elem):
        self.inn.push(elem)

    def dequeue(self):
        if self.out.is_empty():
            while not self.inn.is_empty():
                self.out.push(self.inn.pop())
        return self.out.pop()

    def first(self):
        return self.out.top()