from Lecture.ArrayMinHeap import ArrayMinHeap

class FIFOQueue:
    def __init__(self):
        self.heap = ArrayMinHeap()
        self.count = 0

    def enqueue(self,elem):
        self.heap.insert(self.count,elem)
        self.count = len(self)

    def dequeue(self):
        min = self.heap.min()
        self.heap.delete_min()
        self.count = len(self)
        return min[1]

    def first(self):
        self.count -= 1
        return self.heap.min()

    def __len__(self):
        return len(self.heap.data)

    def is_empty(self):
        return len(self) == 0

heap = FIFOQueue()
heap.enqueue(1)
heap.enqueue(2)
heap.enqueue(3)
print(heap.dequeue())
print(heap.dequeue())
print(heap.dequeue())

from Lecture.LinkedBinaryTree import LinkedBinaryTree
class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority

    def __init__(self, priorities_lst=None, values_lst = None):
        self.data = [None]

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0

    def left(self, j):
        return 2*j

    def right(self, j):
        return 2*j+1

    def parent(self, j):
        return j // 2

    def has_left(self, j):
        return self.left(j) <= len(self.data) - 1

    def has_right(self, j):
        return self.right(j) <= len(self.data) - 1

    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        item = self.data[1]
        return (item.priority, item.value)

    def insert(self, priority, value=None):
        self.data.append(ArrayMinHeap.Item(priority, value))
        self.fix_up(len(self.data) - 1)

    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        if (not self.is_empty()):
            self.fix_down(1)
        return (item.priority, item.value)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def fix_up(self, j):
        if(j == 1):
            return
        else:
            parent_ind = self.parent(j)
            if (self.data[j] < self.data[parent_ind]):
                self.swap(j, parent_ind)
                self.fix_up(parent_ind)

    def fix_down(self, j):
        if (self.has_left(j)):
            left = self.left(j)
            small_child = left
            if (self.has_right(j)):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.fix_down(small_child)

    def find_less_than_or_equal_to(self,k):
        lst = []
        copy = []
        for i in range(k):
            if k >= self.min()[0]:
                copy.append(self.min())
                lst.append(self.min()[0])
                self.delete_min()
        for i in copy:
            self.insert(i[0],i[1])

        return lst
# h = ArrayMinHeap()
# h.insert(1,1)
# h.insert(2,2)
# h.insert(3,3)
# h.insert(4,4)
# h.insert(10,10)
# h.insert(20,20)
# h.insert(5,5)
# h.insert(6,6)
# print(h.find_less_than_or_equal_to(4))
# for i in range(len(h.data)-1):
#     print(h.delete_min())

class Heap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority

    def __init__(self, priorities_lst=None, values_lst = None):
        self.data = [None]

    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0

    def left(self, j):
        return 2*j

    def right(self, j):
        return 2*j+1

    def parent(self, j):
        return j // 2

    def has_left(self, j):
        return self.left(j) <= len(self.data) - 1

    def has_right(self, j):
        return self.right(j) <= len(self.data) - 1

    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        item = self.data[1]
        return (item.priority, item.value)

    def insert(self, priority, value=None):
        self.data.append(ArrayMinHeap.Item(priority, value))
        self.fix_up(len(self.data) - 1)

    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        if (not self.is_empty()):
            self.fix_down(1)
        return (item.priority, item.value)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def fix_up(self, j):
        if(j == 1):
            return
        else:
            parent_ind = self.parent(j)
            if (self.data[j] < self.data[parent_ind]):
                self.swap(j, parent_ind)
                self.fix_up(parent_ind)

    def fix_down(self, j):
        if (self.has_left(j)):
            left = self.left(j)
            small_child = left
            if (self.has_right(j)):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.fix_down(small_child)
