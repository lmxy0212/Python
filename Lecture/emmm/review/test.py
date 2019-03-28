import copy
lst=[1,[2,3],4]
lst1 = lst          #same reference
lst2 = lst[:]       #shallow copy
lst3 = lst*2        #shallow copy
lst4 = copy.deepcopy(lst)
lst[0]= 10
lst[1][0] = 20
# print(lst)
# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)

def iterative(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        a, b, c = b, c, a+b+c
        print(c)
    return c
# print(iterative(4))

def power(x,n):
    if n ==0:
        return 1
    else:
        part = power(x,n//2)
        result = part * part
        if n%2 != 0:
            result *= x
        return result
print(power(2,4))

def fun1(n):
     if (n == 0):
        return 1
     else:
         part1 = fun1(n-1)
         part2 = fun1(n-1)
         res = part1 + part2
         return res
# print(fun1(4))

def fun2(n):
    if (n == 0):
        return 1
    else:
        res = fun2(n//2)
        res += n
        return res
# print(fun2(8))

def fun3(n):
    if (n == 0):
        return 1
    else:
        res = fun3(n//2)
        for i in range(1, n+1):
            res += i
        return res
# print(fun3(6))

# print(pow(2,4))

def flat_list(nested_lst,low,high):
    if low > high:
        return []
    else:
        new_lst = flat_list(nested_lst,low,high-1)
        if isinstance(nested_lst[high],list):
            return new_lst+flat_list(nested_lst[high],0,len(nested_lst[high])-1)
        else:
            new_lst.append(nested_lst[high])
            return new_lst

def f_list(nested_lst):
    lst = []
    for i in nested_lst:
        if isinstance(i,list):
            lst.extend(f_list(i))
        else:
            lst.append(i)
    print(lst)
    return lst
# lst = [1,[2],[3,[4,5,6]]]
# print(f_list(lst))


def sum_nested_lst(lst):
    sum = 0
    for elem in lst:
        if isinstance(elem,list):
            sum += sum_nested_lst(elem)
        else:
            sum += elem
    return sum

def  f ( n ):
    if ( n  ==   1 ):
        print ( 1)
    else :
        f ( n - 1)
    for  i  in  range ( n ):
        print ( i ,   end   =   '   ')
    print ('')
# f(4)


def f(n):
    if (n == 1):
        print(1)
    else:
        f(n // 2)


    for i in range(n):
        print(i, end=' ')
    print('')
# f(4)

def make_palindrome_version(s):
    n = len(s)
    lst = [0]*n*2
    for i in range(n):
        lst[i] = s[i]
        lst[n*2-1-i] = s[i]
    return "".join([str(i) for i in lst])

# print(make_palindrome_version("abc"))