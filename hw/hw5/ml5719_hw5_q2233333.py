class MaxStack(): # L I F O
    def __init__(self):
        self.data = []
        self.maximum = []

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.data)

    def push(self,e):
        if len(self.maximum) == 0:
            self.maximum.append(e)
        elif e > self.maximum[-1]:
            self.maximum.append(e)
        self.data.append(e)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        num = self.data.pop()
        if (self.is_empty()):
            raise Exception("Stack is empty")
        if num == self.maximum[-1]:
            self.maximum.pop()
        return num

    def max(self):
        return self.maximum[-1]


maxS = MaxStack()
maxS.push(1)
maxS.push(3)
maxS.push(6)
maxS.push(4)
print(maxS.data)
print(maxS.max())
print("max",maxS.maximum)
print(maxS.pop())
print(maxS.data)
print(maxS.pop())
print("max",maxS.maximum)
print(maxS.maximum)
print(maxS.pop())
print(maxS.max())
print("max",maxS.maximum)




