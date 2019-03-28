def two_sum(srt_lst, target):
    high = len(srt_lst)-1
    low = 0
    while high >= low:
        sum = srt_lst[low] + srt_lst[high]
        if sum == target:
            return (low,high)
        elif sum < target:
            low += 1
        elif sum > target:
            high -= 1
    return None
