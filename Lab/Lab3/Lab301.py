def reverse_vowels(input_str):
    lst = list(input_str)
    print(lst)
    vowel = []
    count = []
    for i in range(len(input_str)):
        if lst[i] == "a" or lst[i] == "e" or lst[i] == "i" or lst[i] == "o" or lst[i] == "u":
            vowel.append(lst[i])
            count.append(i)
            # print(lst[i])
    for j in range(len(count)):
        lst[count[j]] = vowel[len(vowel)-1-j]
        # print(new)
        # print(vowel[len(vowel)-1-j])
    return "".join(lst)

print(reverse_vowels("tanedn"))

def vowel(str):
    lst = list(str)
    low = 0
    high = len(str)-1
    while low<high:
        if (lst[low] == "a" or lst[low] == "e" or lst[low] == "i" or lst[low] == "o" or lst[low] == "u"):
            if lst[high] == "a" or lst[high] == "e" or lst[high] == "i" or lst[high] == "o" or lst[high] == "u":
                lst[low],lst[high]= lst[high],lst[low]
                low+=1
                high-=1
            else:
                high-=1
        else:
            if lst[high] == "a" or lst[high] == "e" or lst[high] == "i" or lst[high] == "o" or lst[high] == "u":
                low+=1
            else:
                low += 1
                high -= 1
    return "".join(lst)
# print(vowel("tandone"))