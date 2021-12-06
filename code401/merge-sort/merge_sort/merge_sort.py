def merge_sort(arr):

    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right,arr)
    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while k < len(arr):
            arr[k] = right [j]
            k += 1
            j += 1
    else:
       while k < len(arr):
            arr[k] = left [i]
            k += 1
            i += 1

arr = [8,4,23,42,16,15]
merge_sort(arr)
print (arr)