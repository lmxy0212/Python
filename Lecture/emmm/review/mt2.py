from Lecture.DoublyLinkedList import DoublyLinkedList
from Lecture.ArrayStack import ArrayStack
from Lecture.ArrayDeque import ArrayDeque
def reverse(n):
    if n is None:
        return
    else:
        reverse(n.next)
        print(n.data)

# head1 = Node()
# head1.data = "1"
# head1.next = Node()
# head1.next.data = "2"
# head1.next.next = Node()
# head1.next.next.data = "3"
# reverse(head1)

def isBalance(str):
    stack = ArrayStack()
    for i in str:
        if i == "[" or i == "(":
            print(1,i)
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            if i == "]" and stack.top() == "[":
                print(2,i)
                stack.pop()
            elif i == ")" and stack.top() == "(":
                print(2,i)
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

# print(isBalance("[()]"))

def palindrome(q):
    n = len(q)
    for i in range(n//2):
        print(q.first(),q.last())
        if q.delete_first() != q.delete_last():
            return False
    return True

# boost_q = ArrayDeque()
# boost_q.add_first("r")
# boost_q.add_first("a")
# boost_q.add_first( "c" )
# boost_q.add_first( "c" )
# boost_q.add_first( "a" )
# # boost_q.add_first("a")
# boost_q.add_first("r")
# print(palindrome(boost_q))

def remove(node, ele):
    this = node
    while this is not None and this.next is not None:
        if this.next.data == ele:
            this.next = this.next.next
        this = this.next
    if node.data == ele:
        node = node.next
    return node


head1 = DoublyLinkedList().Node()
head1.data = "1"
head1.next = DoublyLinkedList().Node()
head1.next.data = "2"
head1.next.next = DoublyLinkedList().Node()
head1.next.next.data = "3"
new = remove(head1,"2")
this = new
for i in range(2):
    print("hhh",this.data)
    this = this.next


def eval_postfix_boolean_exp(boolean_exp_str):
    operators = '<>=&|'
    exp = boolean_exp_str.split()
    S = ArrayStack()
    for token in exp:
        if token in operators:
            arg1 = S.pop()
            arg2 = S.pop()
            if (token == '<'):
                res = arg2 < arg1
            elif (token == '>'):
                res = arg2 > arg1
            elif (token == '='):
                res = (arg2 == arg1)
            elif token == '|':
                res = arg2 or arg1
            elif token == '&':
                res = arg2 and arg1
            else:
                return "Error"
            S.push(res)
        else:
            S.push(int(token))
    return S.pop()


def infix(str):
    num = ArrayStack()
    op = ArrayStack()
    symbols = "+-*/"
    lst = str.split()
    for i in lst:
        if i.isdigit():
            num.push(int(i))
        elif i in symbols:
            op.push(i)
        elif i == ")":
            second = num.pop()
            first = num.pop()
            operation = op.pop()
            if operation == "+":
                result = first + second
            elif operation == "-":
                result = first - second
            elif operation == "*":
                result = first * second
            elif operation == "/":
                result = first // second
            else:
                return "Error"
            print(result)
            num.push(result)
    return num.pop()
print(infix("( ( ( 60 + 40 ) / 50 ) * ( 16 - 4 ) )"))






