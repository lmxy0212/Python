def flat_list(nested_lst,low,high):
    if low > high:
        return []
    else:
        new_lst = flat_list(nested_lst,low,high-1)
        if isinstance(nested_lst[high],list):
            return new_lst+flat_list(nested_lst[high],0,len(nested_lst[high])-1)
        else:
            new_lst.append(nested_lst[high])
            return new_lst