from Lecture.DoublyLinkedList import DoublyLinkedList
from Lecture.ArrayStack import ArrayStack
from Lecture.LinkedBinaryTree import LinkedBinaryTree
def is_sum_balanced(subtree_root):
    if subtree_root == None:
        return True, 0
    else:
        l = is_sum_balanced(subtree_root.left)
        r = is_sum_balanced(subtree_root.right)
        print(l[1]+r[1]+subtree_root.data)
        if abs(l[1]-r[1])<= 1 and l[0] == True and r[0] == True:
            return True, (l[1]+r[1]+subtree_root.data)
        else:
            return False, (l[1]+r[1]+subtree_root.data)
p1 = LinkedBinaryTree.Node(4)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(3, p1, p2)
p8 = LinkedBinaryTree.Node(1)
# p7 = LinkedBinaryTree.Node(4)
# p6 = LinkedBinaryTree.Node(7, p8, p7)
p6 = LinkedBinaryTree.Node(6, p8)
# p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(4, p3, p6)
bt = LinkedBinaryTree(p5)
print(is_sum_balanced(bt.root))

def insert_sort(lnk_lst,elem):
    if elem > lnk_lst.last_node().data:
        lnk_lst.add_last(elem)
    elif elem < lnk_lst.first_node().data:
        lnk_lst.add_first(elem)
    else:
        curr = lnk_lst.first_node()
        while curr.data < elem and curr.next.data < elem:
            curr = curr.next
        temp = curr.next
        new = DoublyLinkedList.Node(elem,curr,temp)
        curr.next = new
        temp.prev = new

dl = DoublyLinkedList()
for i in range(6):
    dl.add_last(i)
print(dl)
insert_sort(dl,12)
print(dl)


class DupStack:
    def __init__(self):
        self.data = ArrayStack()
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0

    def push(self,e):#(element, number_of_dup_on_top)
        if self.is_empty():
            self.data.push((e, 1))
        else:
            if self.data.top()[0] == e:
                num = self.data.top()[1]
                num += 1
                self.data.pop()#touple not mutatable->pop and mutate->push back
                self.data.push((e,num))
            else:
                self.data.push((e,1))
        self.length += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def top_dups_count(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        temp = self.data.top()[0]
        num = self.data.top()[1]
        self.data.pop()
        if num > 1:
            num -= 1
            self.data.push((temp, num))
        return temp

    def pop_dups(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        temp = self.data.top()[0]
        self.length -= self.data.top()[1]
        self.data.pop()
        return temp

s = DupStack()
s.push(4)
s.push(5)
s.push(5)
s.push(5)
s.push(4)
s.push(4)
print(s.data.data)
# print(len(s))
# print(s.top_dups_count())
# print(s.top())
# print(s.top_dups_count())
print(s.pop())
print(s.data.data)
print(s.pop())
print(s.data.data)
# print(s.top())
# print(s.top_dups_count())
print(s.pop_dups())
print(s.data.data)
# print(s.top())