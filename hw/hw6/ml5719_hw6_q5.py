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


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    if srt_lnk_lst2.is_empty() and srt_lnk_lst1.is_empty():
        return DoublyLinkedList()
    elif srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    elif srt_lnk_lst2.is_empty():
        return srt_lnk_lst1
    else:
        return merge_sublists(srt_lnk_lst1.first_node(),srt_lnk_lst2.first_node())

def merge_sublists(curr1,curr2):
    result = DoublyLinkedList()
    if curr1.data is None and curr2.data is None:
        return
    elif curr1.data is None or curr2.data is None:
        if curr1.data is None:
            this = curr2
        else:
            this = curr1
        while this.data is not None:
            result.add_last(this.data)
            this = this.next
    else:
        if curr1.data <= curr2.data:
            result = merge_sublists(curr1.next, curr2)
            result.add_first(curr1.data)
        else:
            result = merge_sublists(curr1, curr2.next)
            result.add_first(curr2.data)
    return result