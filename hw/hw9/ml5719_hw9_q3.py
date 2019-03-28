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


class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
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
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        if isinstance(self.table[i],UnsortedArrayMap.Item):
            return self.table[i].value
        return curr_bucket[key]

    def __setitem__(self, key, value):
        add = False
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnsortedArrayMap.Item(key,value)
            add = True
        elif isinstance(self.table[i],UnsortedArrayMap.Item):
            curr_key = self.table[i].key
            curr_val = self.table[i].value
            if curr_key == key:
                self.table[i].value = value
            else:
                self.table[i] = UnsortedArrayMap()
                self.table[i][curr_key] = curr_val
                add = True
        else:
            old_size = len(self.table[i])
            self.table[i][key] = value
            new_size = len(self.table[i])
            if (new_size > old_size):
                add = True
        if add:
            self.n += 1

        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        elif isinstance(curr_bucket,UnsortedArrayMap.Item):
            self.table[i] = None
            self.n -= 1
        else:
            del curr_bucket[key]
            self.n -= 1
            if (curr_bucket.is_empty()):
                self.table[i] = None
            elif len(curr_bucket) == 1:
                curr_key = curr_bucket[0].key
                curr_value = curr_bucket[0].value
                self.table[i] = UnsortedArrayMap.Item(curr_key,curr_value)
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                if isinstance(curr_bucket,UnsortedArrayMap.Item):
                    yield curr_bucket.key
                else:
                    for key in curr_bucket:
                        yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            print(value)
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value
def test():
    map = ChainingHashTableMap()
    map[1] = 1
    # print(map[1])
    print("size",map.n)
    map[10] = 10
    print("size", map.n)
    map[5] = 5
    map[99] = 99
    print("size", map.n)
    map[1] = 3
    print("size", map.n)
    print(map[1])
    print(map[5])
    print(map[99])
    print(map[10])
    # n = del map[5]
    # m = del map[10]
    # print("del",n)
    # print("del",m)
    print(len(map))
    # print(map[5])
    for i in map:
        print(1,i)
# test()