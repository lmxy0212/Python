def  inslst ( lst ):
    length  =  0
    origlen  =  len ( lst )
    while length  <   ( origlen  *   2 ):
        square  =  lst [ length ]** 2
        length  +=   1
        print ( length ,  square)
        lst.insert ( length ,  square)
        length  +=   1
lst = [1,2,3]
inslst(lst)
print(lst)

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __str__(self):
        return str([self.data[i] for i in range(self.n)])


    def __repr__(self):
        return str(self)


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)



    def __getitem__(self,ind):
        result = MyList()
        if isinstance(ind,slice):
            if ind.step==None:
                ind.step = 1
            for i in range(ind.start,ind.stop,ind.step):
                result.append(self.data[i])
            return result
        else:
            if (not (0 <= ind <= self.n - 1)):
                raise IndexError('invalid index')
            else:
                return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]
            # alternatively, could say yield self[i], which will call __getitme__()

    def __add__(self,other):
        result = MyList()
        for i in range(self.n):
            result.append(self.data[i])
        for i in range(other.n):
            result.append(other.data[i])
        return result

    def __iadd__(self, other):
        for i in range(other.n):
            self.append(other.data[i])
        return self

    def __mul__(self,var):
        result = MyList()
        count = 0
        for i in range(var*self.n):
            if count == self.n:
                count = 0
            result.append(self.data[count])
            count += 1
        return result

    def __rmul__(self,var):
        result = MyList()
        count = 0
        for i in range(var * self.n):
            if count == self.n:
                count = 0
            result.append(self.data[count])
            count += 1
        return result


lst1 = MyList()
for i in range(1,6):
    lst1.append(i)     #lst1 [1,2,3,4,5]

lst2 = MyList()        #lst2 [3,4,5]
for i in range(3,6):
    lst2.append(i)

print("+",lst1+lst2)
lst1 += lst1            #lst1 [1,2,3,4,5,1,2,3,4,5]
print("+=",lst1)
print("*3",lst2*3)
print("*3",3*lst2)
print("slice",lst1[2:8:2])


