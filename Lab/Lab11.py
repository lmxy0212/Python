# from Lecture.LinkedBinaryTree import LinkedBinaryTree
def invert(tree):
    if tree.left is None and tree.right is None:
        return tree
    else:
        if tree.left is None:
            return LinkedBinaryTree.Node(tree.data,invert(tree.right))
        elif tree.right is None:
            return LinkedBinaryTree.Node(tree.data,None,invert(tree.left))
        else:
            this = LinkedBinaryTree.Node(tree.data,invert(tree.right),invert(tree.left))
            print(this.data)
            return this

# p1 = LinkedBinaryTree.Node(1)
# p2 = LinkedBinaryTree.Node(3)
# p3 = LinkedBinaryTree.Node(2, p1, p2)
# p6 = LinkedBinaryTree.Node(6)
# p7 = LinkedBinaryTree.Node(9)
# p4 = LinkedBinaryTree.Node(7,p6,p7)
# p5 = LinkedBinaryTree.Node(4, p3, p4)
# p8 = LinkedBinaryTree.Node(9,p5)
# binary_tree1 = LinkedBinaryTree(p8)
#
# for i in binary_tree1:
#     print(i, end=' ')
# print()

# tree1 = LinkedBinaryTree(invert(binary_tree1.root))
# for i in tree1:
#     print(i, end=' ')
# print()




from Lecture.ArrayQueue import ArrayQueue

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
        if (subtree_root.left is None and subtree_root.right is None):
            return 0
        elif (subtree_root.left is not None):
            return 1 + self.subtree_height(subtree_root.left)
        elif (subtree_root.right is not None):
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

    def subtree_children_dist(self,node):
        lst = [0,0,0]
        if node is None:
            return lst
        if node.left is not None:
            left = self.subtree_children_dist(node.left)
        else:
            left = [0,0,0]
        if node.right is not None:
            right = self.subtree_children_dist(node.right)
        else:
            right = [0,0,0]
        lst[0] = left[0] + right[0]
        lst[1] = left[1] + right[1]
        lst[2] = left[2] + right[2]
        if node.left is None and node.right is None:
            lst[0] += 1
        elif node.left is None or node.right is None:
                lst[1] += 1
        else:
                lst[2] += 1

        return lst

p1 = LinkedBinaryTree.Node(1)
p2 = LinkedBinaryTree.Node(3)
p3 = LinkedBinaryTree.Node(2, p1, p2)
p6 = LinkedBinaryTree.Node(6)
p7 = LinkedBinaryTree.Node(9)
p4 = LinkedBinaryTree.Node(7,p6,p7)
p5 = LinkedBinaryTree.Node(4, p3, p4)
p8 = LinkedBinaryTree.Node(9,p5)
binary_tree1 = LinkedBinaryTree(p8)

for i in binary_tree1:
    print(i, end=' ')
print()

new = binary_tree1.subtree_children_dist(p8)
print(new)


# def flatten(tree):
#     if tree.left is None and tree.right is None:
#         print(tree.data)
#         return tree
#     else:
#         if tree.left is None:
#             this = LinkedBinaryTree.Node(tree.data, None, invert(tree.right))
#             print(this.data)
#             return this
#         elif tree.right is None:
#             this = LinkedBinaryTree.Node(tree.data, None,invert(tree.left))
#             print(this.data)
#             return this
#         else:
#             left = flatten(tree.left)
#             right = flatten(tree.right)
#             print(left.data,right.data)
#             left = LinkedBinaryTree(left).Node(tree.data,None,right)
#             print((left.data))
#             return left

def flattennn(root):
    return flattenRecu(root, None)

def flattenRecu(root, list_head):
    if root != None:
        list_head = flattenRecu(root.right, list_head)
        list_head = flattenRecu(root.left, list_head)
        root.right = list_head
        root.left = None
        return root
    else:
        return list_head

# def flatten(self, root):
#     if root != None:
#         self.flatten(root.right)
#         self.flatten(root.left)
#         root.right = self.list_head
#         root.left = None
#         self.list_head = root
#         return root

p1 = LinkedBinaryTree.Node(4)
p2 = LinkedBinaryTree.Node(2,p1)
p3 = LinkedBinaryTree.Node(6)
p6 = LinkedBinaryTree.Node(5,p3)
p7 = LinkedBinaryTree.Node(1,p2,p6)
binary_tree1 = LinkedBinaryTree(p7)

for i in binary_tree1:
    print(i, end=' ')
print()

tree1 = LinkedBinaryTree(flattennn(binary_tree1.root))
for i in tree1.preorder():
    print(i.data, end=' ')
print()