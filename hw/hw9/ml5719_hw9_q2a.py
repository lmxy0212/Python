#best worse case -> worse case theta(nlogn)
def intersection_list(lst1,lst2):
    all = [i for i in lst1]   # theta(n)
    all.extend([i for i in lst2])  # theta(n)
    all.sort()  # theta(nlogn)
    common = []
    for i in range(len(all)-1):  # theta(n)
        if all[i] == all[i+1]:
            common.append(all[i])
    return common



def test():
    print(intersection_list([3,9,2,7,1],[1,3,4,5,2]))
# test()