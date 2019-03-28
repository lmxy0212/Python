class Empty(Exception):
    pass


class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum


    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if ((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif ((subtree_root.left is not None) and (subtree_root.right is None)):
            return 1 + self.subtree_height(subtree_root.left)
        elif ((subtree_root.left is None) and (subtree_root.right is not None)):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.postorder():
            yield node.data

def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split()
    bin_root = create_expression_tree_helper(lst,0)[0]
    return LinkedBinaryTree(bin_root)

def create_expression_tree_helper(prefix_exp, start_pos):
    if prefix_exp[start_pos] in "+-*/":
        l = create_expression_tree_helper(prefix_exp,start_pos+1)
        r = create_expression_tree_helper(prefix_exp, start_pos+1+l[1])
        size = l[1] + r[1] + 1
        print(size)
        return LinkedBinaryTree.Node(prefix_exp[start_pos],l[0],r[0]),size
    else:
        return LinkedBinaryTree.Node(int(prefix_exp[start_pos])),1

def prefix_to_postfix(prefix_exp_str):
    return " ".join([str(i.data) for i in create_expression_tree(prefix_exp_str).postorder()])

binary_tree1 = create_expression_tree('* 2 + - 15 6 4')
for i in binary_tree1:
    print(i, type(i), end=' ')
print()
print(prefix_to_postfix('* 2 + - 15 6 4'))


# def create_expression_tree(prefix_exp_str):
#     prefix_exp = prefix_exp_str.split(" ")
#     prefix_exp.reverse()
#
#     for i in range(len(prefix_exp)):
#         if prefix_exp[i] not in "+-*/":
#             prefix_exp[i] = int(prefix_exp[i])
#
#     node = LinkedBinaryTree.Node(prefix_exp.pop())
#     tree = LinkedBinaryTree(node)
#
#     while prefix_exp:
#         value = prefix_exp.pop()
#         next_node = LinkedBinaryTree.Node(value)
#         if node.left is None:
#             node.left = next_node
#             next_node.parent = node
#         elif node.right is None:
#             node.right = next_node
#             next_node.parent = node
#         else:
#             node = node.parent
#             while node.left is not None and node.right is not None:
#                 node = node.parent
#             if node.left is None:
#                 node.left = next_node
#                 next_node.parent = node
#             elif node.right is None:
#                 node.right = next_node
#                 next_node.parent = node
#         if value == "+" or value == "-" or value == "*" or value == "/":
#             node = next_node
#     return tree