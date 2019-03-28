import ctypes
def powers_of_two(num):
    for i in range(1,num+1):
        yield 2**i
# for curr_value in powers_of_two(6):
#             print(curr_value)
# print()


def sum_lst(lst,low):
    if low == len(lst):
        return 0
    else:
        if isinstance(lst[low],list):
            return sum_lst(lst,low+1) + sum_lst(lst[low],0)
        else:
            return lst[low]+ sum_lst(lst,low+1)


def sum_nested_lst(lst):
    sum = 0
    for elem in lst:
        if isinstance(elem,list):
            sum += sum_nested_lst(elem)
        else:
            sum += elem
    return sum


lst = [[1, 2], [3, [[4], 5]], 6]
print(sum_lst(lst,0))
print(sum_nested_lst(lst))
print()


def sort_first(lst,count,high,ind):
    if count==len(lst):
        return
    else:
        if lst[high]<lst[ind]:
            temp = lst[high]
            lst.pop(high)
            lst.insert(ind,temp)
            sort_first(lst,count+1,high,ind+1)
        else:
            sort_first(lst, count + 1,high-1, ind)

# lst  =   [ 54 ,26 ,93 ,  17 ,  77 ,  31 ,  44 ,  55, 20]
# sort_first ( lst,0,8,0)
# print(lst)
# print()


def sort(lst):
    pivot = lst[0]
    big = 1
    small= len(lst)-1
    while big< small:
        if lst[big]<pivot:
            big += 1
        if lst[small]>pivot:
            small -= 1
        if lst[big] > pivot and lst[small] < pivot:
            lst[big],lst[small]=lst[small],lst[big]
    lst[small-1],lst[0]=lst[0],lst[small-1]
lst  =   [54,26,93,17,77,56,44,55,20]
sort( lst)
print(lst)
print()


# def string(n):
#     return (n * ctypes.py_object)()
# class MyString:
#     def __init__(self,s=string(0)):
#         self.string=s
#
#     def __len__(self):
#         return len(self.string)
#
#     def __iter__(self):
#         for i in range(len(self.string)):
#             yield self.string[i]
#
#     def __str__(self):
#         return str(self.string)
#
#     def __repr__(self):
#         return str(self)
#
#     def __getitem__(self, item):
#         return self.string[item]
#
#     def __add__(self,other):
#         result = MyString()
#         result.string = self.string + other
#         return result
#
#     def __radd__(self, other):
#         result = MyString()
#         result.string = other + self.string
#         return result
#
#     def upper(self):
#         return self.string.upper()
#
#     def __iadd__(self, other):
#         self.string = self.string + other.string
#         return self
# st1  =   MyString ()
# print(st1)
# st1  =  st1  + "hi"
# print(st1)
# st2  =   "hello"
# print(st2  + st1)
# print(st1 . upper ())
# print()


def decimal_to_binary(int):
    if int == 1:
        return "1"
    else:
        bin = 0
        if int%2==1:
            bin = 1
        return decimal_to_binary(int//2) + str(bin)
# print(decimal_to_binary(30))
# print()


def solve_hanoi(n,start,dest,spare):
    if n == 1:
        print("move disk from %s to %s" % (start, dest))
        # move the biggest to dest
    else:
        solve_hanoi(n-1,start,spare,dest)
        # move all from start to spare except for the biggest one
        print("move disk from %s to %s"%(start,dest))
        solve_hanoi(n-1, spare, dest,start)
        # move the rest from spare to dest
# solve_hanoi(3,"a","c","b")


# def board_game(lst):
#



