class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"


class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def push(self, e):
        self.data.add_last(e)

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        temp = self.data.last_node()
        self.data.delete_last()
        return temp

    def top ( self ):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.last_node()

    def is_empty ( self ):
        return len(self.data) == 0

    def  __len__ ( self ):
        return len(self.data)

class LeakyStack:
    def __init__(self,size):
        self.data = DoublyLinkedList()
        self.size = 0
        self.fix_size = size

    def push(self, e):
        if self.size < self.fix_size:
            self.data.add_last(e)
            self.size += 1
        else:
            self.data.delete_first()
            self.data.add_last(e)

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        self.data.delete_last()
        self.size -= 1
        return self.data.last_node()


    def  top ( self ):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.last_node()

    def  is_empty ( self ):
        return len(self.data) == 0

    def  __len__ ( self ):
        return len(self.data)

# S  =  LeakyStack(5)
# S.push ( 2)
# S.push ( 13)
# S.push ( 3)
# S.push ( 8)
# S.push ( 5)
# S.push(12)
# for i in S.data:
#     print(i)


def sum_lnk_lst(lnk_lst):
    curr = lnk_lst.first_node()
    return sum_helper(curr,lnk_lst)

def sum_helper(curr,lnk_lst):
    if curr is lnk_lst.last_node():
        return curr.data
    else:
        return curr.data + sum_helper(curr.next,lnk_lst)

lst = DoublyLinkedList()
lst.add_last(3)
lst.add_last(7)
lst.add_last(5)
lst.add_last(4)
# print(sum_lnk_lst(lst))

def reverse_list_change_elements_order_data(lnk_lst):
    data = []
    for i in lnk_lst:
        data.append(i)
    curr = lnk_lst.first_node()
    count = 0
    while curr is not lnk_lst.last_node():
        curr.data = data[len(data)-count-1]
        count += 1
        curr = curr.next
    curr.data = data[0]

def reverse_list_change_elements_order_node(lnk_lst):
    current = lnk_lst.last_node().prev
    while current is not lnk_lst.header:
        curr = current.prev

        pre = current.prev #disconnect current node
        next = current.next
        pre.next = next
        next.prev = pre

        lnk_lst.last_node().next = current #add current node to the last
        current.prev = lnk_lst.last_node()
        current.next = lnk_lst.trailer
        lnk_lst.trailer.prev = current
        current = curr
        # print(lnk_lst)

# def reverse1(lst): #change node
#     first_node = lst.header.next
#     cursor = first_node
#     lst.header.next = lst.trailer.prev
#     while cursor is not None:
#         cursor.next, cursor.prev = cursor.prev, cursor.next
#         cursor.prev.prev = lst.header
#         first_node = cursor
#         cursor.prev = first_node
#     return lst

def reverse2(lst): #change data
    head = lst.header.next
    tail = lst.trailer.prev
    while head != tail:
        head.data, tail.data = tail.data, head.data
        head = head.next
        if head == tail:
            break
        tail = tail.prev

print(lst)
reverse2(lst)
reverse_list_change_elements_order_node(lst)
print(lst)






