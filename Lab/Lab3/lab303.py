def square_root(num):
    sq_possible = 0.01
    found = False
    while not found:
        check = round(sq_possible**2,2)
        if check == num:
            found = True
        else:
            sq_possible += 0.01
    return sq_possible
print(square_root(100))


def improved_square_root_func(num):
    start = 0.01
    end = num/2
    mid = (start + end)/2
    sq = mid ** 2
    while round(sq,2) != num:
        if sq < num:
            start = mid + 0.01
        else:
            end = mid - 0.01
        mid = (start + end) / 2
        sq = mid ** 2
    return mid
print(improved_square_root_func(100))