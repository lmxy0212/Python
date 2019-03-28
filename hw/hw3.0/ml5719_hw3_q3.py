def find_duplicates(lst):
    duplicate = []
    for i in range(0,len(lst)):
        if lst[abs(lst[i])] >= 0:
            lst[abs(lst[i])] = -lst[abs(lst[i])]
        else:
            duplicate.append(abs(lst[i]))
    return duplicate