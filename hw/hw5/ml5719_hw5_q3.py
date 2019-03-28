class Empty(Exception):
    pass


class ArrayDeque:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.front_ind = 0
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def add_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1

    def add_last(self, e):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = e
        self.num_of_elems += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[(self.front_ind + self.num_of_elems - 1) % (len(self.data))]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

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


class MidStack():
    def __init__(self):
        self.first_half = ArrayStack()
        self.second_half = ArrayDeque()

    def __len__(self):
        return len(self.first_half) + len(self.second_half)

    def is_empty(self):
        return len(self) == 0

    def push(self,e):
        if self.is_empty():
            self.first_half.push(e)
        else:
            self.second_half.add_last(e)
            if len(self)%2 != 0:
                self.first_half.push(self.second_half.delete_first())

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        if (len(self) == 1):
            return self.first_half.top()
        return self.second_half.last()

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")

        if len(self)==1:
            num = self.first_half.pop()
        else:
            if len(self)%2 != 0:
                self.second_half.add_first(self.first_half.pop())
            num = self.second_half.delete_last()

        return num

    def mid_push(self,e):
        if len(self)%2 == 0:
            self.first_half.push(e)
        else:
            self.second_half.add_first(e)

n = MidStack()
n.push(1)
n.push(2)
n.push(3)
n.push(2)
n.push(5)
n.push(1)
for i in range(len(n)):
    print(n.pop())





