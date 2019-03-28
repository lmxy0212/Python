def appearances(s,low,high):
    if low > high:
        return {}
    else:
        dict = appearances(s,low+1,high)
        if s[low] in dict.keys():
            dict[s[low]] += 1
        else:
            dict[s[low]] = 1
        return dict


def appearances2(s,low,high):
    if low > high:
        return {}
    else:
        dict = appearances(s,low+1,high)
        if s[low] not in dict:
            dict[s[low]] = s.count(s[low])
        return dict