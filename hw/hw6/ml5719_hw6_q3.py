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


class CompactString:
    def __init__(self, orig_str=""):
        self.data = DoublyLinkedList()
        count = 0
        self.n = len(orig_str)
        if orig_str:
            for i in range(len(orig_str)):
                if orig_str[i] != orig_str[i-1] and i != 0:
                    self.data.add_last((orig_str[i-1],count))
                    count = 1
                else:
                    count += 1
                if i == len(orig_str)-1:
                    self.data.add_last((orig_str[i], count))

    def __add__(self, other):
        if self.data.is_empty() and other.data.is_empty():
            result = CompactString("")
            return result
        elif self.data.is_empty():
            result = CompactString(str(other))
            return result
        elif other.data.is_empty():
            result = CompactString(str(self))
            return result

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
        if self.data.is_empty() and other.data.is_empty():
            return False
        elif self.data.is_empty():
            return True
        elif other.data.is_empty():
            return False
        this = self.data.first_node()
        that = other.data.first_node()
        n1 = self.n
        n2 = other.n
        n = min(n1,n2)
        count1 = 0
        count2 = 0
        i = 0
        while i < n:
            char1 = this.data[0]
            char2 = that.data[0]
            num1 = this.data[1]
            num2 = that.data[1]
            i += 1
            count1 += 1
            count2 += 1
            if count1 == num1:
                this = this.next
                count1 = 0
            if count2 == num2:
                that = that.next
                count2 = 0
            if char1 > char2:
                return False
            if char2 > char1:
                return True
        return n1 <= n

    def __le__(self, other):
        return not self > other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __repr__(self):
        return str(self)

    def __str__(self):
        str_self = ""
        for i in self.data:
            str_self += i[0]*i[1]
        return str_self

str1 = 'aaaab'
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