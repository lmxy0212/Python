def permutations(lst,low,high):
    if low == high:
        return [[i for i in lst]]
    else:
        result = []
        for i in range(low,high+1):
            lst[low], lst[i] = lst[i],lst[low]
            result += permutations(lst, low + 1, high)
            lst[low], lst[i] = lst[i], lst[low]

        return result
print(permutations([1,2,3,4],0,3))


# def permutations(lst):
#     stack = ArrayStack()
#     stack.push(lst[:])
#     temp = [0] * len(lst)
#     q = ArrayQueue()
#     i = 1
#     while i < len(lst):
#         print(i)
#         if temp[i] < i:
#             j = temp[i] if i % 2 else 0
#             lst[j], lst[i] = lst[i], lst[j]
#             stack.push(lst[:])
#             temp[i] += 1
#             i = 1
#             print(temp)
#         else:
#             print(temp)
#             temp[i] = 0
#             i += 1
#         print(stack.data)
#     return stack.data
#
# l = [1,2,3]
# print(permutations(l))