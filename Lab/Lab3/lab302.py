def common(lsta,lstb):
    a = 0
    b = 0
    common_lst = []
    while a < len(lsta) and b < len(lstb):
        if lsta[a] > lstb[b]:
            b += 1
        elif lsta[a] < lstb[b]:
            a += 1
        else:
            common_lst.append(lsta[a])
            a += 1
            b += 1
    return common_lst
lst1 = [1,6,14,15]
lst2 = [2,6,14,19]
print(common(lst1,lst2))