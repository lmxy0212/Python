from Lecture.binary_search_tree import BinarySearchTreeMap
import csv
from Lecture.LinkedBinaryTree import LinkedBinaryTree
import math
def create_csv(sizes_lst, heights_lst):
    file = open("height.csv", "w")
    if len(sizes_lst) != len(heights_lst):
        raise Exception("list given must be of equal sizes")
    for i in range(len(sizes_lst)):
        file.write(str(sizes_lst[i]) + "," + str(heights_lst[i]) + "\n")
    file.close()


def is_bst(binary_tree):#(max,min,bool)
    return is_bst_helper(binary_tree.root)[2]


def is_bst_helper(curr_root):
    if curr_root is None:
        return (-math.inf,math.inf,True)
    else:
        left = is_bst_helper(curr_root.left)
        right = is_bst_helper(curr_root.right)
        if (left[2]== False or right[2]== False) :
            return (-math.inf,math.inf,False)
        else:
            # (left[2] and right[2]) == True:
            boolean = True
            max_val = max(left[0], right[0])
            min_val = min(left[1], right[1])

            if right[1] > curr_root.data and left[0] < curr_root.data and boolean == True:
                boolean = True
            else:
                boolean = False

            if curr_root.data < min_val:
                min_val = curr_root.data
            if curr_root.data > max_val:
                max_val = curr_root.data
            return (max_val, min_val, boolean)

# p1 = LinkedBinaryTree.Node(1)
# p2 = LinkedBinaryTree.Node(11)
# p3 = LinkedBinaryTree.Node(10, p1, p2)
# p4 = LinkedBinaryTree.Node(16)
# p5 = LinkedBinaryTree.Node(15, p3, p4)
# binary_tree1 = LinkedBinaryTree(p5)

# print(is_bst(binary_tree1))

def same_elem(bst1,bst2):
    lst1 = [i.item.key for i in bst1.inorder()]
    lst2 = [i.item.key for i in bst2.inorder()]
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False

b1 = BinarySearchTreeMap()
b2 = BinarySearchTreeMap()
b1[1] = None
b1[2] = None
b1[5] = None
b1[20] = None
b2[1] = None
b2[2] = None
b2[5] = None
b2[20] = None
print(same_elem(b1,b2))

def gresteat_le_n(bst,n):
    lst = [i.item.key for i in bst.inorder()]
    num = -1
    for i in range(len(lst)-1):
        if lst[i] < n and lst[i+1] >= n:
            num = lst[i]
    return num

b = BinarySearchTreeMap()
b[1] = None
b[2] = None
b[3] = None
b[5] = None
b[12] = None
print(gresteat_le_n(b,6))



