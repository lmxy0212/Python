import LinkedBinaryTree

p1 = LinkedBinaryTree.Node(1)
p2 = LinkedBinaryTree.Node(6)
p3 = LinkedBinaryTree.Node(2, p1, p2)
p4 = LinkedBinaryTree.Node(4)
p5 = LinkedBinaryTree.Node(5, p3, p4)

binary_tree1 = LinkedBinaryTree.LinkedBinaryTree(p5)

for i in binary_tree1:
    print(i, end=' ')
print()


def seq1():
    yield 1
    yield 2

def seq2():
    yield 'a'
    yield 'b'
    yield from seq1()