'''
Write your Functions below
'''

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # less than root
    if l < n and arr[i] > arr[l]:
        smallest = l

    # See if right child of root exists and is
    # less than root
    if r < n and arr[smallest] > arr[r]:
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, smallest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Driver code to test above
# arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
arr = [10, 4, 16, 8, 7, 9, 3, 2, 14, 1]
print("Input array is")
print(arr)
heapSort(arr)
n = len(arr)
print ("Sorted array is")
print(arr)
