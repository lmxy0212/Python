import math
class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


# def restore_bst(prefix_lst):
#     bst = BinarySearchTreeMap()
#     if len(prefix_lst) == 0:
#         return bst
#     bst.root = restore_bst_helper(prefix_lst,0,len(prefix_lst)-1,"l")[0]
#     return bst
#
# def restore_bst_helper(lst, low, high, dir):
#     curr = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[low]))
#     end = low
#     if low >= high:
#         return curr, end
#     else:
#         # print(0)
#         if lst[low] > lst[low+1]:
#             l_node, end = restore_bst_helper(lst,low+1,high,"l")
#             print((1,l_node.item.key,end))
#             l_node.parent = curr
#             curr.left = l_node
#         if end < high and lst[end+1]>lst[low]:
#             if dir == "l" and low != 0 and lst[end+1] < lst[low-1]:
#                 r_node, end = restore_bst_helper(lst,end+1,high,"l")
#                 print((2, r_node.item.key, end))
#                 r_node.parent = curr
#                 curr.right = r_node
#             elif dir == "r" or low == 0:
#                 r_node, end = restore_bst_helper(lst, end + 1, high, "r")
#                 print((3, r_node.item.key, end))
#                 r_node.parent = curr
#                 curr.right = r_node
#     return curr, end

from Lecture.ArrayStack import ArrayStack
def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if (len(prefix_lst)==0):
        return bst
    else:
        bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
        bst.size += 1
        stack = ArrayStack()
        stack.push(bst.root)
        for i in range(1,len(prefix_lst)):
            node_temp = None
            while(stack.is_empty() is False and prefix_lst[i] > stack.top().item.key):
                node_temp = stack.pop()
            if node_temp is not None:
                new_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[i]))
                node_temp.right = new_node
                new_node.parent = node_temp
                stack.push(node_temp.right)
                bst.size += 1
            else:
                node_temp = stack.top()
                new_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[i]))
                node_temp.left = new_node
                new_node.parent = node_temp
                stack.push(node_temp.left)
                bst.size += 1
    return bst



def main():
    bst = restore_bst([9,7,3,1,5,13,11,15])
    # print(bst)
    for i in bst.preorder():
        print("p",i.item.key, end=' ')
    print()
main()