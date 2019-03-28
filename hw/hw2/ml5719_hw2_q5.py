def split_parity(lst):
    index = 0
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            temp = lst[i]
            lst[i] = lst[index]
            lst[index] = temp
            index += 1
lst = [2,1,4,4,5,4,3,5]
print(lst)
split_parity(lst)
print(lst)

def split(lst,low,high):
    if low >= high:
        return
    else:
        if lst[low]%2 == 0:
            if lst[high]%2!=0:
                lst[low],lst[high]= lst[high],lst[low]
                low += 1
            high -=1
        else:
            low += 1

        split(lst,low,high)

split(lst,0,7)
print(lst)