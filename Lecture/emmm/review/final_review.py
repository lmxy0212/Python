from Lecture.ChainingHashTableMap import ChainingHashTableMap
from Lecture.DoublyLinkedList import DoublyLinkedList
class PlayList:
    def __init__(self):
        self.hashtable = ChainingHashTableMap()
        self.dll = DoublyLinkedList()

    def add_song(self,new_song_name):
        self.dll.add_last(new_song_name)
        self.hashtable[new_song_name] = self.dll.last_node()

    def add_song_after(self,song_name,new_song_name):
        node = self.hashtable[song_name]
        self.dll.add_after(node,new_song_name)
        self.hashtable[new_song_name] = node.next

    def play_song(self,song_name):
        try:
            self.hashtable[song_name] is not None
        except:
            KeyError("key not found")
        else:
            print(song_name)

    def play_list(self):
        curr = self.dll.first_node()
        while curr.next is not None:
            print(curr.data)
            curr = curr.next
# pl = PlayList()
# pl.add_song("fell it still")
# pl.add_song("perfect")
# pl.add_song("havana")
# pl.add_song_after("perfect","thunder")
# pl.add_song_after("fell it still","something just like this")
# pl.play_list()

from Lecture.LinkedBinaryTree import LinkedBinaryTree
def level_list(root,level):
    if root == None:
        return []
    if level == 0:
        return [root.data]
    else:
        l = level_list(root.left,level-1)
        print("l",l)
        r = level_list(root.right,level-1)
        print("r",r)
        l.extend(r)
        return l

p1 = LinkedBinaryTree.Node(4)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(6, p1, p2)
p4 = LinkedBinaryTree.Node(7)
p6 = LinkedBinaryTree.Node(4, p3, p4)
p5 = LinkedBinaryTree.Node(10)
p7 = LinkedBinaryTree.Node(5, p5)
p8 = LinkedBinaryTree.Node(2, p6, p7)
p9 = LinkedBinaryTree.Node(19)
p10 = LinkedBinaryTree.Node(13)
p11 = LinkedBinaryTree.Node(9,p9,p10)
p12 = LinkedBinaryTree.Node(5,p11)
p0 = LinkedBinaryTree.Node(1,p8,p12)
bin_tree = LinkedBinaryTree(p0)
for i in bin_tree.preorder():
    print(i.data, end=' ')
print()
print(level_list(bin_tree.root,0))

from Lecture.ArrayMinHeap import ArrayMinHeap


def k_largest_elem(lst,k):
    h = ArrayMinHeap()
    for i in lst:
        print(i)
        h.insert(i)
        if len(h) > k:
            h.delete_min()
    return [h.data[i].priority for i in range(1,len(h.data))]

print("k max",k_largest_elem([3,9,2,7,1,8,1,3], 3))