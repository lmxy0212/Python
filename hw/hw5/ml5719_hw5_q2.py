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


class MaxStack():
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        if len(self.data)==0:
            self.maximum = e
        if e > self.maximum:
            self.maximum = e
        self.data.push((e,self.maximum))

    def top(self):
        return self.data.top()[0]

    def pop(self):
        number = self.data.pop()
        return number[0]

    def max(self):
        return self.data.top()[1]