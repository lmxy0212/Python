def split_by_sign(lst,low,high):
    if low > high:
        return
    else:
        if lst[low]>0:
            if lst[high]<0:
                lst[low],lst[high]=lst[high],lst[low]
                split_by_sign(lst,low+1,high-1)
            else:
                split_by_sign(lst,low,high-1)
        else:
            split_by_sign(lst,low+1,high)

lst = [1,-1,2,3,-1,3,-5]
split_by_sign(lst,0,6)
print(lst)