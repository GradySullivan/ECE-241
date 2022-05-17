def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf):
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf):
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1
    return comparison

def mergeSort_3_way(alist):

    comparison = 0

    if len(alist) == 2:
        comparison = comparison + 1
        if alist[1] > alist[0]:
            temp = alist[1]
            alist[1] = alist[0]
            alist[0] = temp

    if len(alist) > 2:
        third1 = len(alist) // 3  # split list into thirds
        third2 = 2 * len(alist) // 3
        group1 = alist[:third1]
        group2 = alist[third1:third2]
        group3 = alist[third2:]
        comparison = comparison + mergeSort_3_way(group1) + mergeSort_3_way(group2) + mergeSort_3_way(group3)

        a, b, c, = 0, 0, 0 # indexing variables for each third
        order = 0 # final list position

        while a < len(group1) and b < len(group2) and c < len(group3): #checks which one is greatest
            if group2[b] < group1[a] and group3[c] < group1[a]:
                alist[order] = group1[a]
                a = a + 1
            elif group1[a] < group2[b] and group3[c] < group2[b]:
                alist[order] = group2[b]
                b = b + 1
            else:
                alist[order] = group3[c]
                c = c + 1

            order = order + 1 # changes to sort next greatest value in next spot
            comparison = comparison + 2

        if a == len(group1): #calculate comparisons with recursion
            comparison = comparison + merge2List(alist, group2, group3, b, c, order)
        if b == len(group2):
            comparison = comparison + merge2List(alist, group1, group3, a, c, order)
        if c == len(group3):
            comparison = comparison + merge2List(alist, group1, group2, a, b, order)

    return comparison

arr = [5, 10, 9, 6, 8, 3, 1, 4, 2, 7]
mergeSort_3_way(arr)
print(arr)
comp = mergeSort_3_way(arr)
print("Total comparisons: " + str(comp))