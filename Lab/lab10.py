from Lecture.DoublyLinkedList import DoublyLinkedList
from Lecture.ArrayQueue import ArrayQueue
from Lecture.ArrayStack import ArrayStack

def prime_factorization ( num ):
    res = DoublyLinkedList()
    q = ArrayQueue()
    q.enqueue(num)
    while not q.is_empty():
        test = q.dequeue()
        i = 2
        isprime = True
        while i*i <= test and isprime is True:
            if test % i == 0:
                q.enqueue(test // i)
                res.add_last(i)
                isprime = False
            i += 1
        if isprime:
            res.add_last(test)
    return res
print(prime_factorization(26))

class BoostQueue:
    def __init__(self):
        self.dl = DoublyLinkedList()

    def __len__(self):
        return len(self.dl)

    def is_empty(self):
        return self.dl.is_empty()

    def enqueue(self,e):
        self.dl.add_last(e)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        result = self.dl.first_node().data
        self.dl.delete_first()
        return result

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.dl.first_node()

    def boost(self,k):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        if k >= len(self):
            k = len(self)
        curr = self.dl.last_node()
        for i in range(k):
            curr = curr.prev
        this = self.dl.last_node()
        self.dl.add_before(curr,this.data)
        self.dl.delete_last()

# boost_q = BoostQueue()
# boost_q.enqueue( 1 )
# boost_q.enqueue( 2 )
# boost_q.enqueue( 3 )
# boost_q.enqueue( 4 )
# print(boost_q.dl)
# boost_q.boost( 2 )
# print(boost_q.dl)
# print(boost_q.dequeue())
# print(boost_q.dequeue())
# print(boost_q.dequeue())
# print(boost_q.dequeue())

def flatten(lnk_lst):
    new = DoublyLinkedList()
    helper(lnk_lst.first_node(),new)
    return new

def helper(node,lnk_lst):
    while node.data is not None:
        if not isinstance(node.data,int):
            helper(node.data.first_node(),lnk_lst)
        else:
            lnk_lst.add_last(node.data)
        node = node.next


lst = [[2, 1], [3, [[4], 5]], 7, [6, 8], [[[[9], [10, 11]]]]]

def flatten_lst(lst):
    s = ArrayStack()
    while len(lst) != 0:
        val = lst.pop()
        if isinstance(val, list):
            lst.extend(val)
        else:
            s.push(val)
    while not s.is_empty():
        lst.append(s.pop())
# flatten_lst(lst)
# print(lst)

def flatten_lnk_lst(lnk_lst):
    s = ArrayStack()
    while len(lnk_lst) != 0:
        this = lnk_lst.last_node()
        if isinstance(this.data,int):
            s.push(this.data)
            lnk_lst.delete_last()
        else:
            for i in this.data:
                lnk_lst.add_after(this.prev,i)
            lnk_lst.delete_last()
    while not s.is_empty():
        lnk_lst.add_last(s.pop())

dl = DoublyLinkedList()
dl.add_first(1)
dl.add_first(2)
dl.add_first(3)
dl2 = DoublyLinkedList()
dl2.add_first(4)
dl2.add_first(5)
dl2.add_first(6)
dl2.add_last(dl)
dl1 = DoublyLinkedList()
dl1.add_first(dl)
dl1.add_first(7)
dl1.add_first(8)
dl1.add_first(9)
dl1.add_first(dl2)
print(dl1)
print(flatten(dl1))
# print(dl1)


class Playlist:
    INITIAL_CAPACITY = 3
    def __init__(self):
        self.data = [None] * Playlist.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (self.number_of_elems == 0)

    def add_to_playlist(self,str_tittle):
        if (self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = str_tittle
        self.number_of_elems += 1

    def print_playlist(self):
        for i in range(len(self)):
            ind = (self.front_ind + i)%len(self.data)
            print("Track %d: %s" %(i+1,self.data[ind]))

    def play(self,n):
        return self.data[(self.front_ind+n-1)%len(self.data)]

    def move_up(self,n):
        this = (self.front_ind+n-1)%len(self.data)
        if this == self.front_ind:
            raise Exception("Already first song!")
        prev = (this - 1)%len(self.data)
        self.data[this],self.data[prev] = self.data[prev],self.data[this]

    def move_down(self,n):
        this = (self.front_ind + n - 1) % len(self.data)
        if this == self.front_ind + len(self):
            raise Exception("Already first song!")
        next = (this + 1) % len(self.data)
        self.data[this], self.data[next] = self.data[next], self.data[this]

    def remove_song(self,n):
        for i in range(n,len(self)+1):
            this = (self.front_ind + i - 1)%(len(self))
            print(this)
            next = (this + 1)%len(self)
            self.data[this] = self.data[next]
            if i == len(self):
                self.data[this] = None
                self.number_of_elems -= 1

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind  = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0
# lst1 = Playlist()
# lst1.add_to_playlist("Stairway to Heaven")
# lst1.add_to_playlist("Help")
# lst1.add_to_playlist("I Will Survive")
# lst1.add_to_playlist("Lean On Me")
# lst1.add_to_playlist("Living on A prayer")
# # lst1.print_playlist()
# # print(lst1.play(1))
# # lst1.move_up(5)
# # lst1.print_playlist()
# lst1.remove_song(4)
# lst1.print_playlist()





