from Lab.ArrayStack import ArrayStack

def is_mached(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for token in expr:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty():
                return False
            from_S = S.top()
            if (righty.index(token) == lefty.index(from_S)):
                S.pop()
            else: return False
        else: raise ValueError
    return S.is_empty()


def get_tag(text):
    i = 0
    n = len(text)
    while i<n:
        while i<n and text[i] != '<':
            i+=1
        i+=1
        start=i
        while i<n and text[i]!= '>':
            i+=1
        end = i
        if start < end:
            yield text[start:end]


def is_matched_html(text):
    stack = ArrayStack()
    for tag in get_tag(text):
        if tag[0] == '/':
            if stack.is_empty():
                return False
            top_elem = stack.pop()
            if top_elem != tag[1:]:
                return False
        else:
            stack.push(tag)
    return stack.is_empty()

# file = open("html_file.html","r")
# text = file.read()
# print(is_matched_html(text))

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

            S.push(res)
        else:
            S.push(int(token))
    return S.pop()
print(eval_postfix_boolean_exp('1 2 < 6 3 < &'))


def convert_infix_exp_to_postfix(str):
    pass
