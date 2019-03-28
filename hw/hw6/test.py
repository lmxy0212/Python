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
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2,srt_lnk_lst1.first_node(),srt_lnk_lst2.first_node())

def merge_sublists(srt_lnk_lst1, srt_lnk_lst2,curr1,curr2):
    # result = DoublyLinkedList()
    if curr1.data is None and curr2.data is None:
        return

    if curr1.data is None:
        result = curr2
        # print(result.last_node())
        # result.delete_last()
        while curr2 is not None:
            result.next = curr2
            curr2 = curr2.next
        print("curr2", curr2.data)
        # print("result", result.data)
        return result


    if curr2.data is None:
        result = curr1
        while curr1 is not None:
            result.next = curr1
            curr1 = curr1.next
        print(curr1.data)
        # print(result.data)
        return result


    if curr1.data <= curr2.data:
        result = curr1
        print(result.data)
        result.next = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, curr1.next, curr2)
        return result
    else:
        result = curr2
        print(result.data)
        result.next = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, curr1, curr2.next)
        return result

list1 = DoublyLinkedList()
list1.add_last(10)
list1.add_last(20)
list1.add_last(30)
list1.add_last(40)
list1.add_last(50)
list2 = DoublyLinkedList()
list2.add_last(5)
list2.add_last(15)
list2.add_last(18)
list2.add_last(35)
list2.add_last(60)
list2.add_last(60)

result = merge_linked_lists(list1,list2)
for i in result:
    print(i)
# print(result)

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
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
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


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        count = 0
        for i in range(len(orig_str)):
            if orig_str[i] != orig_str[i - 1] and i != 0:
                self.data.add_last((orig_str[i - 1], count))
                count = 1
            else:
                count += 1
            if i == len(orig_str) - 1:
                self.data.add_last((orig_str[i], count))

    def __add__(self, other):
        result = CompactString(str(self))
        this = other.data.first_node()
        length = len(other.data)
        if self.data.last_node().data[0] is other.data.first_node().data[0]:
            count = self.data.last_node().data[1] + other.data.first_node().data[1]
            result.data.last_node().data = (result.data.last_node().data[0], count)
            this = this.next
            length -= 1

        for i in range(length):
            result.data.add_last(this.data)
            this = this.next
        return result

    def __lt__(self, other):
        this = self.data.first_node()
        that = other.data.first_node()

        for i in range(len(self.data)):
            if this.data[0] > that.data[0]:
                return False
            count = 1
            for j in range(this.data[1]):
                if this.data[0] < that.data[0]:
                    return True
                if this.data[0] > that.data[0]:
                    return False
                if that is other.data.last_node():
                    if this.data[1] < that.data[1]:
                        return True
                    return False
                if count == that.data[1]:
                    that = that.next
                    count = 1
                count += 1
            this = this.next
        return True

    def __le__(self, other):
        this = self.data.first_node()
        that = other.data.first_node()
        for i in range(len(self.data)):
            if this.data[0] > that.data[0]:
                return False
            count = 1
            for j in range(this.data[1]):
                if this.data[0] < that.data[0]:
                    return True
                if this.data[0] > that.data[0]:
                    return False
                if that is other.data.last_node():
                    if this.data[1] <= that.data[1]:
                        return True
                    return False
                if count == that.data[1]:
                    that = that.next
                    count = 1
                count += 1
            this = this.next
        return True

    def __gt__(self, other):
        this = self.data.first_node()
        that = other.data.first_node()
        for i in range(len(self.data)):
            print("i", i)
            if this.data[0] < that.data[0]:
                return False
            count = 1
            for j in range(this.data[1]):
                print("j", j)
                if this.data[0] > that.data[0]:
                    return True
                if this.data[0] < that.data[0]:
                    return False
                if that is other.data.last_node():
                    if this.data[1] > that.data[1]:
                        return True
                    return False
                if count == that.data[1]:
                    that = that.next
                    count = 1
                count += 1
            this = this.next
        return True

    def __ge__(self, other):
        this = self.data.first_node()
        that = other.data.first_node()
        for i in range(len(self.data)):
            print("i", i)
            if this.data[0] < that.data[0]:
                return False
            count = 1
            for j in range(this.data[1]):
                print("j", j)
                if this.data[0] > that.data[0]:
                    return True
                if this.data[0] < that.data[0]:
                    return False
                if that is other.data.last_node():
                    if this.data[1] >= that.data[1]:
                        return True
                    return False
                if count == that.data[1]:
                    that = that.next
                    count = 1
                count += 1
            this = this.next
        return True

    def __repr__(self):
        return str(self)

    def __str__(self):
        str_self = ""

        for i in self.data:
            str_self += i[0] * i[1]
        return str_self


str1 = 'aaaa'
str2 = 'aaaaaaacccaaaa'
s1 = CompactString(str1)
s2 = CompactString(str2)
s3 = s2 + s1
print(s3)
print(s1 < s2, str1 < str2)
print(s2 < s1, str1 > str2)
print(s1 <= s2, str1 <= str2)
print(s2 <= s1, str1 >= str2)
print(s1 > s2, str1 > str2)  #
print(s2 > s1, str1 < str2)
print(s1 >= s2, str1 >= str2)  #
print(s2 >= s1, str1 <= str2)







