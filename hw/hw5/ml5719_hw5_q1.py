input_str = input("--> ")
var_lst = {}

while input_str != "done()":
    lst = input_str.split(" ")
    length = len(lst)
    i = 0

    for j in range(length):

        if str(lst[i]).isalpha():
            if str(lst[i]) in var_lst.keys():
                lst[i] = var_lst[lst[i]]

        if str(lst[i]) in "+-*/":
            expression = lst.pop(i)
            second = int(lst.pop(i - 1))
            first = int(lst.pop(i-2))
            i -= 2

            if expression == "+":
                result = first + second
            elif expression == "-":
                result = first - second
            elif expression == "*":
                result = first * second
            else:
                result = first / second
            lst.insert(i,result)

        if j == length-1:
            if "=" in lst:
                var_lst[lst[0]] = lst.pop()
                print(lst[0])
            else:
                print(lst.pop())

        i += 1
    input_str = input("--> ")