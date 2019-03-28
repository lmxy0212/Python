def remove_all(lst, value):
    n = len(lst)-1
    i = 0

    while i<=n:
        if lst[i] == value:
            temp = lst[n]
            lst[n] = lst[i]
            lst[i] = temp
            n -= 1
            lst.pop()
        else:
            i += 1
lst = [1,2,3,1,1,4,1,6]
remove_all(lst,1)
print(lst)
