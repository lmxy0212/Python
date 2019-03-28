'''It would be better to put ArrayStack  definition in a separate file and import it'''

class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

###########################
# Examples of using stack #
###########################

# Reversing a string

def print_in_reverse(str):
    S = ArrayStack()

    for ch in str:
        S.push(ch)

    while (S.is_empty() == False):
        ch = S.pop()
        print(ch, end='')
    print()

# checking whether different kinds of parentheses are nested correctly:

def is_matched(expr):
    lefty = '({['
    righty = ')}]'

    S = ArrayStack()

    for token in expr:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty( ):
                return False
            from_S = S.top()
            if (righty.index(token) == lefty.index(from_S)):
                S.pop()
            else:
                return False
        else:
            raise ValueError

    return S.is_empty()

# evaluate postfix expression

def eval_postfix_exp(exp_str):
    operators = '+-*/'
    exp = exp_str.split()
    S = ArrayStack()
    for token in exp:
        if token in operators:
            arg1 = S.pop()
            arg2 = S.pop()
            if (token == '+'):
                res = arg2 + arg1
            elif (token == '-'):
                res = arg2 - arg1
            elif (token == '*'):
                res = arg2 * arg1
            else: # token == '/'
                res = arg2 / arg1

            S.push(res)
        else:
            S.push(float(token))
    return S.pop()


#evaluate infix expression (including tokenization of input with positive integers):

def get_token(line):
    '''generator returns next token from line (a string)
    Each token is a string representing a positive integer or
    one of the following: (, ), +, -, *, /, end '''

    n = len(line)
    i = 0

    while i < n:
        while i < n and line[i] == ' ':
            # skip white space
            i += 1
        if i >= n:
            return
        elif line[i] in '()+-*/':
            yield line[i]
            i += 1
        else:
            # next token is a number;
            dig_list = []
            while i < n and line[i].isdigit():
                dig_list.append(line[i])
                i += 1
            num_str = ''.join(dig_list)
            yield (num_str)


def eval_infix(expression):
    ''' expression is a string representing a fully parenthesized
    infix expression with positive integer operands and with operators: +, -, *, / '''
    num_stack = ArrayStack()
    operator_stack = ArrayStack()

    for token in get_token(expression):
        if token.isdigit():
            num_stack.push(int(token))
        elif token == '(':
            pass
        elif token in '+-*/':
            operator_stack.push(token)
        else:
            # token is ')'. Evaluate sub-expression and push result
            # should raise MalformedInfix if stack empty before popping
            operand2 = num_stack.pop()
            operand1 = num_stack.pop()
            operator = operator_stack.pop()
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            else:
                if operand2 == 0:
                    raise ValueError
                else:
                    result = operand1 / operand2
            num_stack.push(result)
            #operator = operator_stack.pop()

    ''' End of infix expression there should be one element left on num_stack'''
    result = num_stack.pop()
    return (result)
