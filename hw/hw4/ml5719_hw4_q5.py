def count_lowercase(s,low,high):
    if low > high:
        return 0
    else:
        if s[low].islower():
            return 1+count_lowercase(s,low+1,high)
        else:
            return count_lowercase(s, low + 1, high)


def is_number_of_lowercase_even(s,low,high):
    if low > high:
        return True
    else:
        if s[low].islower():
            return (1+is_number_of_lowercase_even(s,low+1,high))==1
        else:
            return (is_number_of_lowercase_even(s, low + 1, high))==1
