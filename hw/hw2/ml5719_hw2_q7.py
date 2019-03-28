def findChange(lst01):
    high = len(lst01) - 1
    low = 0
    while high >= low:
        mid = (high + low)//2
        if lst01[mid] == 0:
            if lst01[mid+1]==1:
                return mid+1
            else:
                low = mid + 1
        else:
            if lst01[mid-1]==0:
                return mid
            else:
                high = mid - 1