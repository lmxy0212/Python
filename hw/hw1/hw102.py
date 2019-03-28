def shift(lst,k):
    for i in range(k):
        lst.append(lst.pop(0))
    return lst

def shift2(lst,k,direction = "left"):
    for i in range(k):
        if direction == "right":
            lst.insert(0,lst.pop())
        else:
            lst.append(lst.pop(0))
    return lst