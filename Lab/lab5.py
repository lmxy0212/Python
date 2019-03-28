import os.path
def find_lst_max(lst):
    if(len(lst)==1):
        return lst[0]
    else:
        if lst[0]>lst[1]:
            lst[1]=lst[0]
        return find_lst_max(lst[1:])
lst = [1,2,3,4,100,12,2]
print(find_lst_max(lst))

def product_evens(lst,ind):
    if ind == len(lst):
        return 1
    else:
        if lst[ind]%2==0 and lst[ind] <= len(lst):
            return(lst[ind]*product_evens(lst,ind+1))
        else:
            return(product_evens(lst,ind+1))
print(product_evens(lst,0))

def is_palindrome(str,low,high):
    if low >= high:
        return True
    else:
        if str[low]!=str[high]:
            return False
        else:
            return is_palindrome(str,low+1,high-1)
str = "kaak"
print(is_palindrome(str,0,3))

def binary_search(lst,val,low,high):
    if low == high:
        if lst[high]==val:
            return high
        else:
            return None
    else:
        if lst[(low+high)//2]==val:
            return (low+high)//2
        elif lst[(low+high)//2]>val:
            return binary_search(lst,val,low,(low+high)//2-1)
        else:
            return binary_search(lst,val,(low+high)//2+1,high)
binary = [1,2,3,4,5]
print(binary_search(binary,5,0,4))

def disk_uage(path):
    if not(os.path.isdir(path)):
        return os.path.getsize(path)
    else:
        for i in os.listdir(path):
            path = os.path.join(path,i)
            if os.path.isdir(path):
                return os.path.getsize(path)+disk_uage(path)
            else:
                return os.path.getsize(path)
print(disk_uage("/Users/ene/Documents/PycharmProjects/CS 1134"))


