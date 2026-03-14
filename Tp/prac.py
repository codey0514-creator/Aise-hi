def bubble_sort(l):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            continue
        else :
            a = l[i]
            l[i] = l[i+1]
            l[i+1] = a
    return l
print(bubble_sort([1,2,3,4]))