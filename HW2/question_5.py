def findLeftMost(arr, i, n):
    l = 2 * i + 1 # left child node equation
    if l < n:
        return findLeftMost(arr, l, n) # recursion if left value is less than array length
    else:
        return i

def findRightMost(arr,i,n):
    r = 2 * i + 2 # right child node equation
    if r < n:
        return findRightMost(arr, r, n) # recursion if right value is less than array length
    else:
        return i

arr = [5, 10, 9, 6, 8, 3, 1, 4, 2, 7]
n = len(arr)
i = findLeftMost(arr, 0, n)
r = findRightMost(arr, 0, n)
print("Leftmost node - index: ", i, " value: ", arr[i])
print("Rightmost node - index: ", r, " value: ", arr[r])