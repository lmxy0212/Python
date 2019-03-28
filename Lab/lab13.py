def most_frequent(lst):
    pass

class OpenAddressingHashMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = [None]*self.N
        self.N = 64
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, k):
        i = hash(k)%self.N
        while self.table[i] != None:
            if self.table[i] != "used" and self.table[i].key == k:
                return self.table[i].value
            i = (i+1) % self.N
        raise KeyError("invalid key")

    def __setitem__(self, k, v):
        i = hash(k) % self.N
        if self.table[i] == None:
            self.helper_insert(k,v,i)
        else:
            found_key = False
            reuse_index = None
            while self.table[i] != None and found_key == False:
                if self.table[i].key == k:
                    self.table[i].value = found_key = True
                elif self.table[i] == "used":
                    reuse_index = i
                i = (i+1)%self.N
            if found_key == False:
                if reuse_index is not None:
                    self.helper_insert(k,v,reuse_index)
                else:
                    self.helper_insert(k, v, i)

    def helper_insert(self,k,v,i):
        new_elem = OpenAddressingHashMap.Item(k,v)
        self.table[i] = new_elem
        self.n += 1
        if self.n > self.N//2:
            self.rehash(self.N*2)

    def __delitem__(self, k):
        i = hash(k) % self.N
        while self.table[i] != None:
            if self.table[i] != "used" and self.table[i].key == "k":
                self.table[i] = "used"
                self.n -= 1
                if self.n < self.N //4:
                    self.rehash(self.N//2)
                return
            i = (i+1)% self.N
    def __iter__(self):
        for item in self.table:
            if item is not None:
                yield item.key

    def rehash(self,new_size):
        pass