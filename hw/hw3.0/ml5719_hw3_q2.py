import ctypes


def make_array(n):
    return (n * ctypes.py_object)()


class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]


    def __len__(self):
        return self.n

    def resize(self):
        if self.n == self.capacity:
            new_array = make_array(self.capacity*2)
            for i in range(self.n):
                new_array[i] = self.data[i]
            self.data = new_array
            self.capacity = self.capacity*2
        if self.n < self.capacity//4:
            new_array = make_array(self.capacity//2)
            for i in range(self.n):
                new_array[i] = self.data[i]
            self.data = new_array
            self.capacity = self.capacity // 2

    def append(self, val):
        self.resize()
        self.data[self.n] = val
        self.n += 1

    def insert(self,index,val):
        if index < 0 or index > self.n:
            raise IndexError("Index out of range")
        self.resize()

        for i in range(self.n,index,-1):
            self.data[i] = self.data[i-1]
        self.n += 1
        self.data[index] = val

    def pop(self,ind=None):
        if self.n == 0:
            raise IndexError()
        elif ind or ind == 0:
            num = self.data[ind]
            for i in range(ind, self.n-1):
                self.data[i] = self.data[i + 1]
        else:
            num = self.data[self.n - 1]
            self.data[self.n-1] = None
        self.n -=1
        self.resize()
        return num

    def __str__(self):
        return str([self.data[i] for i in range(self.n)])


    def __repr__(self):
        return str(self)


