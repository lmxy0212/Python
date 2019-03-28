import random
class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

class EmptyCollection(Exception):
    pass


class DLL:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DLL.Node()
        self.trailer = DLL.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DLL.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.dll = DLL()
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key].data[1]

    def __setitem__(self, key, value):
        # j = self.hash_function(key)
        # self.dll.add_last([key, value])
        # if self.table[j] is None:
        #     self.table[j] = UnsortedArrayMap()
        # old_size = len(self.table[j])
        # self.table[j][key] = value
        # self.table[j][key] = self.dll.last_node()
        # new_size = len(self.table[j])
        # if (new_size > old_size):
        #     self.n += 1
        # if (self.n > self.N):
        #     self.rehash(2 * self.N)
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
            self.dll.add_last([key, value])
            self.table[j][key] = self.dll.last_node()
            self.n += 1
        else:
            self.table[j][key].data = [key,value]
        # self.table[j][key] = value
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        self.dll.delete(curr_bucket[key])
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for i in self.dll:
            yield i[0]

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        self.dll = DLL()
        for (key, value) in old:
            self[key] = value


def test():
    map = ChainingHashTableMap()
    map[1] = 1
    # print(map[1])
    map[10] = 1
    # for i in map.dll:
    #     print(i)
    map[5] = 1
    map[2345] = 5
    # for i in map.dll:
    #     print(i)
    map[99] = 1
    map[1] = 3
    # for i in map:
    #     print(1,i,map[i])
    print(1,map[1])
    print(10,map[10])
    print(5,map[5])
    print(99,map[99])
    # del map[5]
    del map[5]
    print(len(map))
    # print(map[5])
    # for i in map.dll:
    #     print(i)
    # for i in map:
    #     print("map",i)
    for i in map:
        print(1,i,map[i])
test()