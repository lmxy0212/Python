def remove_all_evens(lst):
    n = len(lst)
    for i in range(n-1,-1,-1):
        if lst[-1]%2==0:
            lst.pop()
        elif lst[i] %2 == 0:
            lst[-1],lst[i] = lst[i],lst[-1]
            lst.pop()
# lst = [2,3,5,2,16,13]
# remove_all_evens(lst)
# print(lst)

def remove_all(lst,val):
    n = len(lst)
    for i in range(n-1,-1,-1):
        if lst[-1]==val:
            lst.pop()
        elif lst[i] == val:
            lst[-1],lst[i] = lst[i],lst[-1]
            lst.pop()
# lst = [2,3,5,2,4,2,5,6]
# remove_all(lst,2)
# print(lst)

def remove_evens(lst):
    low = 0
    high = len(lst)-1
    while low<=high:
        if lst[high]%2==0:
            lst.pop()
            high -= 1
        else:
            if lst[low]%2==0:
                lst[low],lst[high]=lst[high],lst[low]
                lst.pop()
                high-=1
            low+=1
# lst = [2,3,5,2,16,13]
# remove_evens(lst)
# print(lst)

def is_sorted(lst,low,high):
    if low == high-1:
        return lst[low] <= lst[high]
    else:
        if lst[low] <= lst[low+1]:
            return is_sorted(lst,low+1,high)
        else:
            return False
# lst = [1,3,6,18,8,12,25]
# print(is_sorted(lst,0,6))

def positive_prefix_sum(lst):
    return [i for i in range(len(lst)) if sum(lst[:i+1])>0]
# lst = [-1,1,4,-2,-3]
# print(positive_prefix_sum(lst))

def reverse(lst):
    for i in range(1,len(lst)//2+1):
        lst[i-1],lst[-i]= lst[-i],lst[i-1]
# lst = [1,3,6,18,0,8,12,25]
# reverse(lst)
# print(lst)
