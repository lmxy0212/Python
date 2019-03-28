class Deque:
    CAPACITY = 5
    def __init__(self):
        self.capacity= Deque.CAPACITY
        self.data = [None]* self.capacity
        self.first_ind = 0
        self.num = 0

    def __len__(self):
        return self.num

    def is_empty(self):
        return len(self.data)==0

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.first_ind]

    def last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.num]

    def add_first(self, e):
        if (self.num == len(self.data)):
            self.resize(2 * self.num)
        self.first_ind = (self.first_ind - 1) % len(self.data)
        self.data[self.first_ind] = e
        self.num += 1

    def add_last(self, e):
        if (self.num == len(self.data)):
            self.resize(2 * len(self.data))
        end = (self.first_ind + self.num) % len(self.data)
        self.data[end]=e
        self.num+=1

    def delete_first(self):
        if (self.num == len(self.data)):
            self.resize(2 * len(self.data))
        first = self.data[self.first_ind]
        self.data[self.first_ind] = None
        self.first_ind+=1
        self.num -= 1
        return first

    def delete_last(self):
        if (self.num == len(self.data)):
            self.resize(2 * len(self.data))
        end = (self.first_ind + self.num)%len(self)
        end_num = self.data[end]
        self.data[end] = None
        self.num -= 1
        return end_num

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0

# de = Deque()
# de.add_first(1)
# de.add_first(2)
# de.add_first(3)
# de.add_last(10)
# print(de.data)
# print(de.delete_first())
# print(de.delete_last())
# print(de.data)

class BoostQueue:
    def __init__(self):
        self.data = [None] * 5
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0

    def boost(self,k):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        if k >= self.number_of_elems:
            k = self.number_of_elems
        for i in range(k):
            print(self.data)
            self.data[self.number_of_elems-i-1],self.data[self.number_of_elems-i-1-1]=self.data[self.number_of_elems-i-1-1],self.data[self.number_of_elems-i-1]

# boost_q = BoostQueue()
# boost_q.enqueue( 1 )
# boost_q.enqueue( 2 )
# boost_q.enqueue( 3 )
# boost_q.enqueue( 4 )
# boost_q.boost( 2 )
# print(boost_q.data)
# print(boost_q.number_of_elems)
# print(boost_q.dequeue())
# print(boost_q.dequeue())
# print(boost_q.dequeue())
# print(boost_q.dequeue())


class ArrayQueue:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0


from Lecture.ArrayStack import ArrayStack


def sum_lst(lst):
    s = ArrayStack()
    while len(lst) != 0:
        val = lst.pop()
        if isinstance(val, list):
            lst.extend(val)
        else:
            s.push(val)
    sum = 0
    while not s.is_empty():
        sum += s.pop()
    return sum


# lst = [[1, 2], [3, [[4], 5]], 6]
# print(sum_lst(lst))


q = ArrayQueue()
i = 2
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
i += q.first()
q.enqueue(i)
q.dequeue()
q.dequeue()
print(i)
print(q.first())



