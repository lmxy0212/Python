#1>

p1 = LinkedBinaryTree.Node(5)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(9, p1, p2)
p8 = LinkedBinaryTree.Node(8)
p7 = LinkedBinaryTree.Node(4)
p6 = LinkedBinaryTree.Node(7, p8, p7)
p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(3, p4, p6)

binary_tree1 = LinkedBinaryTree(p5)
for i in binary_tree1:
    print(i, end=' ')
print()
print(min_and_max(binary_tree1))

#2>
p1 = LinkedBinaryTree.Node(5)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(9, p1, p2)
p8 = LinkedBinaryTree.Node(8)
p7 = LinkedBinaryTree.Node(4)
p6 = LinkedBinaryTree.Node(7, p8, p7)
p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(3, p4, p6)

binary_tree1 = LinkedBinaryTree(p5)
for i in binary_tree1:
    print(i, end=' ')
print()
binary_tree1.leaves_list()
print(binary_tree1.leaves_list())

#3>
p1 = LinkedBinaryTree.Node(5)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(9)
p8 = LinkedBinaryTree.Node(8,p1,p2)
p7 = LinkedBinaryTree.Node(4)
p6 = LinkedBinaryTree.Node(7, p8, p7)
p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(3, p4, p6)

binary_tree1 = LinkedBinaryTree(p5)
for i in binary_tree1:
    print(i, end=' ')
print()
print(is_height_balanced(binary_tree1))

#4>
p1 = LinkedBinaryTree.Node(5)
p2 = LinkedBinaryTree.Node(1)
p3 = LinkedBinaryTree.Node(9, p1, p2)
p8 = LinkedBinaryTree.Node(8)
p7 = LinkedBinaryTree.Node(4)
p6 = LinkedBinaryTree.Node(7, p8, p7)
p4 = LinkedBinaryTree.Node(2, p3)
p5 = LinkedBinaryTree.Node(3, p4, p6)

binary_tree1 = LinkedBinaryTree(p5)
for i in binary_tree1:
    print(i, end=' ')
print()
for i in binary_tree1.iterative_inorder():
    print(i, end=' ')

#5>
binary_tree1 = create_expression_tree('* 2 + - 15 6 4')
for i in binary_tree1:
    print(i, type(i), end=' ')
print()
print(prefix_to_postfix('* 2 + - 15 6 4'))