def e_approx(n):
    lst1 = [1]
    lst2 = [1]
    for i in range(1,n+1):
        lst2.append(lst2[i-1]*i)
        lst1.append(1/lst2[i] + lst1[i-1])
    return lst1[n]

