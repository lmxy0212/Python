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


class Integer:
    def __init__(self, num_str):
        self.dlst = DoublyLinkedList()
        for i in range(len(num_str)):
            if i == 0:
                if num_str[0] != "0":
                    self.dlst.add_last(num_str[i])
            else:
                self.dlst.add_last(num_str[i])

    def __add__(self, other):
        if len(self.dlst) > len(other.dlst):
            this = self.dlst.last_node()
            that = other.dlst.last_node()
            small_len = len(other.dlst)
            long_long = len(self.dlst)
        else:
            this = other.dlst.last_node()
            that = self.dlst.last_node()
            small_len = len(self.dlst)
            long_long = len(other.dlst)

        result = Integer("")
        digit = 0
        for i in range(small_len):
            digit += self.check_digit(this.data) + self.check_digit(that.data)
            result.dlst.add_first(str(digit%10))
            if digit >= 10:
                digit = 1
            else:
                digit = 0
            this = this.prev
            that = that.prev

        for j in range(small_len,long_long):
            digit += self.check_digit(this.data)
            result.dlst.add_first(str(digit%10))
            if digit >= 10:
                digit = 1
            else:
                digit = 0
            this = this.prev
        if digit != 0:
            result.dlst.add_first(str(digit))

        return result

    def check_digit(self,a):
        if a == "0":
            return 0
        elif a == "1":
            return 1
        elif a == "2":
            return 2
        elif a == "3":
            return 3
        elif a == "4":
            return 4
        elif a == "5":
            return 5
        elif a == "6":
            return 6
        elif a == "7":
            return 7
        elif a == "8":
            return 8
        elif a == "9":
            return 9

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "".join([i for i in self.dlst])

    def __mul__(self, other):
        result = Integer('0')
        this = self.dlst.last_node()
        that = other.dlst.last_node()
        temp = 0
        count = 0
        while that is not None:
            current = Integer('0' * count)
            for i in range(len(self.dlst)):
                if this.prev is self.dlst.header:
                    digit = (self.check_digit(that.data) * self.check_digit(this.data) + temp) % 10
                    current.dlst.add_first(digit)
                    temp = (self.check_digit(that.data) * self.check_digit(this.data) + temp) // 10
                    if temp != 0:
                        current.dlst.add_first(temp)
                else:
                    digit = (self.check_digit(that.data) * self.check_digit(this.data) + temp) % 10
                    temp = (self.check_digit(that.data) * self.check_digit(this.data) + temp) // 10
                    current.dlst.add_first(digit)
                    this = this.prev
            this = self.dlst.last_node()
            that = that.prev
            result = result + current
            temp = 0
            count += 1
        return result
s1 = Integer("10")
s2 = Integer("9")
print(s1*s2)
